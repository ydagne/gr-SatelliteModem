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
#include "Framer_impl.h"
#include "CRC16.hpp"

namespace gr {
  namespace SatelliteModem {

    Framer::sptr
    Framer::make(msg_queue::sptr w_msgq, unsigned w_MTU, uint8_t w_nonBlocking)
    {
      return gnuradio::get_initial_sptr
        (new Framer_impl(w_msgq, w_MTU, w_nonBlocking));
    }

    /*
     * The private constructor
     */
    Framer_impl::Framer_impl(msg_queue::sptr w_msgq, unsigned w_MTU, uint8_t w_nonBlocking)
      : gr::sync_block("Framer",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(1, 1, sizeof(char))) //, m_msgq(msg_queue::make(100))
    {
        m_MTU          = w_MTU;
        m_nonBlocking  = w_nonBlocking;
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
    Framer_impl::~Framer_impl()
    {
      delete[] m_scramblingSeq;
    }

    int
    Framer_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      uint8_t *out = (uint8_t *) output_items[0];

      // Do <+signal processing+>
      int j = 0;

      if(m_msgq->empty_p() && m_nonBlocking)
      {
          // Send dummy data
          out[0] = '0' ^ m_scramblingSeq[0];
          out[1] = '0' ^ m_scramblingSeq[1];

          //uint16_t len = 0;
          out[2] = 0 ^ m_scramblingSeq[2];
          out[3] = 0 ^ m_scramblingSeq[3];

          char cc = ((m_packetNumber++ % 2) == 0)? 'A' : 'B';
          for (int i = 4; i < (m_MTU+6); ++i)
          {
             out[i] =   cc ^ m_scramblingSeq[i];
          }

          j = m_MTU + 6;
      }
      else
      {
          m_msg = m_msgq->delete_head();

          if(m_msg)
          {
            
            uint16_t len = m_msg->length() > m_MTU? m_MTU : m_msg->length();

            // CRC-16
            uint16_t crc = CRC16::compute(m_msg->msg(), len);
            out[0] = ((crc >> 8) & 0xFF) ^ m_scramblingSeq[0];
            out[1] = (crc        & 0xFF) ^ m_scramblingSeq[1];

            out[2] = ((len >> 8) & 0xFF) ^ m_scramblingSeq[2];
            out[3] = (len        & 0xFF) ^ m_scramblingSeq[3];

            out[4] = ((m_packetNumber >> 8) & 0xFF) ^ m_scramblingSeq[4];
            out[5] = (m_packetNumber        & 0xFF) ^ m_scramblingSeq[5];
            m_packetNumber++;

            uint8_t *buff = m_msg->msg();
            int k = 0;

            for (int i = 6; i < (len+6); ++i)
            {
               out[i] = buff[k++] ^ m_scramblingSeq[i];
            }

            for (int i = (len+6); i < (m_MTU+6); ++i)
            {
               out[i] = '0' ^ m_scramblingSeq[i];
            }

            j = m_MTU + 6;

            m_msg.reset();
          }
      }

      // Tell runtime system how many output items we produced.
      return j;
    }

  } /* namespace SatelliteModem */
} /* namespace gr */

