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
#include "SyncPreamble_impl.h"

namespace gr {
  namespace SatelliteModem {

    SyncPreamble::sptr
    SyncPreamble::make(unsigned w_PacketLength, unsigned w_overheadBytes)
    {
      return gnuradio::get_initial_sptr
        (new SyncPreamble_impl(w_PacketLength, w_overheadBytes));
    }

    /*
     * The private constructor
     */
    SyncPreamble_impl::SyncPreamble_impl(unsigned w_PacketLength, unsigned w_overheadBytes)
      : gr::block("SyncPreamble",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)))
    {
      if(w_PacketLength < 1)
      {
        std::cout<<"Invalid packet length: "<<w_PacketLength << std::endl;
        exit(-1);
      }

      if(w_overheadBytes > PREAMBLE_PATTERN_LENGTH)
      {
        std::cout<<"preamble overhead should be less than "<<PREAMBLE_PATTERN_LENGTH<<std::endl;
        exit(-1);
      }

      d_packetLength = w_PacketLength;
      d_overheadBytes = w_overheadBytes;
      d_bytesRequired = 0;

      set_output_multiple(d_packetLength + d_overheadBytes + 2);
    }

    /*
     * Our virtual destructor.
     */
    SyncPreamble_impl::~SyncPreamble_impl()
    {
    }

    void
    SyncPreamble_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = noutput_items;
    }

    int
    SyncPreamble_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const char *in = (const char *) input_items[0];
      char *out = (char *) output_items[0];

      int i=0,j=0;

      if(d_overheadBytes == 0)
      {
        while (i < noutput_items)
        {
          out[i++] = in[j++];
        }
      }
      else
      {

        while(1)
        {
          
          if((j+d_packetLength+d_overheadBytes+2) > noutput_items)
          {
            // Not enough space
            break;
          }

          // ADD Extra bytes (OPTIONAL)
          out[i++] = 0;
          out[i++] = 1;

          // PREAMBLE
          for (int k = 0; k < d_overheadBytes; ++k)
          {
            out[i++] = PREAMBLE_PATTERN__[k];
          }

          // PAYLOAD
          for (int k = 0; k < d_packetLength; ++k)
          {
            out[i++] = in[j++];
          }
        }
      }

      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (j);

      // Tell runtime system how many output items we produced.
      return i;
    }

  } /* namespace SatelliteModem */
} /* namespace gr */

