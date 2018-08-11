/* -*- c++ -*- */
/* 
 * Copyright 2017 Yihenew Beyene: yihenew.beyene@gmail.com
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <iostream>
#include <gnuradio/io_signature.h>
#include "Deframer_impl.h"
#include "CRC16.hpp"

namespace gr {
  namespace SatelliteModem {

    Deframer::sptr
    Deframer::make(msg_queue::sptr w_msgq, unsigned w_MTU)
    {
      return gnuradio::get_initial_sptr
        (new Deframer_impl(w_msgq, w_MTU));
    }

    /*
     * The private constructor
     */
    Deframer_impl::Deframer_impl(msg_queue::sptr w_msgq, unsigned w_MTU)
      : gr::sync_block("Deframer",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(0, 0, 0))
    {
        m_MTU          = w_MTU;
        m_msgq         = w_msgq;
        m_packetNumber = 0;

        if(w_MTU <= 0)
        {
            std::cout<<"MTU size should be larger than 0" << std::endl;
        }
        
        int bytesLeft  = w_MTU+6; 
        unsigned index = 0;

        m_scramblingSeq = new uint8_t[w_MTU + 6];

        for (int i = 0; i < (w_MTU+6); ++i)
        {
            m_scramblingSeq[i] = PR_SEQUENCE[i % PR_SEQUENCE_LENGTH];
        }

        set_output_multiple(w_MTU + 6); 
    }

    /*
     * Our virtual destructor.
     */
    Deframer_impl::~Deframer_impl()
    {
    }

    int
    Deframer_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      if(noutput_items < (m_MTU+6))
      {
          //std::cout<<"not enough data"<<std::endl;
          return 0;
      }

      const uint8_t *in = (const uint8_t *) input_items[0];
      unsigned packet_length = m_MTU + 6;


      uint16_t len = ((in[2] ^ m_scramblingSeq[2]) << 8) | 
                     ( in[3] ^ m_scramblingSeq[3]);

      if(len > 0 && len < m_MTU)
      {
          m_packetNumber = ((in[4] ^ m_scramblingSeq[4]) << 8) | 
                           ( in[5] ^ m_scramblingSeq[5]);

          message::sptr msg = message::make(0,                    // msg type
                                        sizeof(uint8_t),          // arg1 for other end
                                        len,                      // arg2 for other end (redundant)
                                        len * sizeof(uint8_t));   // len of msg

          uint8_t *buff = msg->msg();
          int j=0;

          for (int i = 6; i < (6+len); ++i)
          {
             buff[j] = in[i] ^ m_scramblingSeq[i];
             j++;
          }


          // CRC-16
          uint16_t crc_rx = ((in[0] ^ m_scramblingSeq[0]) << 8) | 
                            ( in[1] ^ m_scramblingSeq[1]);

          uint16_t crc = CRC16::compute(msg->msg(), len);

          if(crc == crc_rx)
          {
              m_msgq->handle(msg);    // send it
          }
          else
          {
              //std::cout<<"CRC test failed: "<<crc<<" vs  "<<crc_rx << std::endl;
          }
      }

      // Tell runtime system how many output items we produced.
      return packet_length;
    }

  } /* namespace SatelliteModem */
} /* namespace gr */

