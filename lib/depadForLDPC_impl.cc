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

#include <gnuradio/io_signature.h>
#include "depadForLDPC_impl.h"

namespace gr {
  namespace SatelliteModem {

    depadForLDPC::sptr
    depadForLDPC::make(unsigned w_frameBits, unsigned w_blockSize)
    {
      return gnuradio::get_initial_sptr
        (new depadForLDPC_impl(w_frameBits, w_blockSize));
    }

    /*
     * The private constructor
     */
    depadForLDPC_impl::depadForLDPC_impl(unsigned w_frameBits, unsigned w_blockSize)
      : gr::block("depadForLDPC",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)))
    {  
        m_frameBits = w_frameBits;
        m_blockSize = w_blockSize;

        if(w_frameBits < 1)
        {
          std::cout << "Frame size should be larger than 0" << std::endl;
          exit(-1);
        }
        else if(w_blockSize < 1)
        {
          std::cout << "Block size should be larger than 0" << std::endl;
          exit(-1);
        }

        m_paddingBits = w_blockSize - (w_frameBits % w_blockSize);

        set_output_multiple(w_frameBits);
    }

    /*
     * Our virtual destructor.
     */
    depadForLDPC_impl::~depadForLDPC_impl()
    {
    }

    void
    depadForLDPC_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = (noutput_items /  m_frameBits) * (m_frameBits + m_paddingBits); 
    }

    int
    depadForLDPC_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const char *in = (const char *) input_items[0];
      char *out = (char *) output_items[0];

      // Do <+signal processing+>
      int i = 0, j = 0, k = 0;

      k = m_frameBits + m_paddingBits;

      while(true)
      {
          if((j + k) <= noutput_items)
          {
             memcpy(&out[j], &in[i], m_frameBits);
             i += m_frameBits;
             j += m_frameBits;
             // Drop padding bits
             i+= m_paddingBits;
          }
          else
          {
            break;
          }
      }

      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (i);

      // Tell runtime system how many output items we produced.
      return j;
    }

  } /* namespace SatelliteModem */
} /* namespace gr */

