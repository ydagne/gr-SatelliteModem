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
#include "PreambleDetector_impl.h"

namespace gr {
  namespace SatelliteModem {

    PreambleDetector::sptr
    PreambleDetector::make(unsigned w_PacketLength, unsigned w_overheadBytes)
    {
      return gnuradio::get_initial_sptr
        (new PreambleDetector_impl(w_PacketLength, w_overheadBytes));
    }

    /*
     * The private constructor
     */
    PreambleDetector_impl::PreambleDetector_impl(unsigned w_PacketLength, unsigned w_overheadBytes)
      : gr::block("PreambleDetector",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
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

      d_packetLength      = w_PacketLength;
      d_overheadBytes     = w_overheadBytes;
      d_bitsRequired      = 0;
      d_correlationWindow = 8 * w_overheadBytes;


      d_correlation    = 0.0;
      d_peak           = 0.0;
      d_peakIndex      = d_correlationWindow;
      d_riseThreshold  = 0.5 * (float)d_correlationWindow;
      d_fallThreshold  = 0.0;
      d_riseEdgeFound  = false;
      d_fallEdgeFound  = false;


      //set_history(d_correlationWindow+1);
      //set_history((2*d_packetLength + w_overheadBytes + 4)*8+1);
      set_history((d_packetLength + w_overheadBytes + 4)*8+1);
      set_output_multiple(d_packetLength*8);

    }

    /*
     * Our virtual destructor.
     */
    PreambleDetector_impl::~PreambleDetector_impl()
    {
    }

    void
    PreambleDetector_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = noutput_items + (d_overheadBytes + 4)*8;
    }

    float
     PreambleDetector_impl::correlate(const float *w_in)
    {
      float corr = 0.0;

      for (int i = 0; i < d_correlationWindow; ++i)
      {
        corr += w_in[i] * PREAMBLE_PATTERN__[i];
      }

      return corr;
    }

    int
    PreambleDetector_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *oldIn = (const float *) input_items[0];
      const float *newIn = (const float *) &((const float*)input_items[0])[d_correlationWindow]; 

      float *out = (float *) output_items[0];

    
      if(d_overheadBytes == 0) // No preamble
      {
        for (int i = 0; i < noutput_items; ++i)
        {
          out[i] = oldIn[i];
        }

        consume_each(noutput_items);
        return noutput_items;
      }

      //-----------PREAMBLE SEARCH---------------------
      int i=0;
      int j=0;

      int bitsPerFrame = (d_packetLength + d_overheadBytes + 2) * 8;

      while(1)
      {
          if((i+bitsPerFrame) > ninput_items[0])
          {
            break;  // Not enough input
          }

          if((j+8*d_packetLength) > noutput_items)
          {
            break;  // Not enough space
          }

          // PREAMBLE SEARCH

          // Reset flags
          d_riseEdgeFound = false;
          d_fallEdgeFound = false;
          d_peak          = 0.0;
          d_correlation   = 0;

          float threshold = 0.0;

          // Estimate average magnitude
          float sum = 0.0;
          for (int k = i; k < (i+d_overheadBytes*8); ++k)
          {
            sum += oldIn[k] > 0? oldIn[k] : -oldIn[k];
          }

          threshold = sum*d_riseThreshold/(d_overheadBytes*8);

          /*for (int k = i; k < (i+bitsPerFrame); ++k)
          {
            d_correlation = this->correlate(&oldIn[k]);
            
            //if (d_correlation > d_riseThreshold)
            if (d_correlation > threshold)
            {
              // Peak rise-edge detected
              d_riseEdgeFound = true;
              d_peak = d_correlation;
              d_peakIndex = k;

              for (int k2 = k+1; k2 < k+8; ++k2)
              {
                  d_correlation = this->correlate(&oldIn[k2]);

                  if(d_correlation > d_peak)
                  {
                    d_peak      = d_correlation;
                    d_peakIndex = k2;
                  }
                  else if(d_correlation < d_fallThreshold)
                  {
                    break; 
                  }
              }

              // peak was found

              // Write one full packet
              for (int k2 = (d_peakIndex+d_correlationWindow); k2 < (d_peakIndex + d_correlationWindow + d_packetLength*8); ++k2)
              {
                out[j++] = oldIn[k2];
              }

              break;
            }
          }*/

          d_peakIndex = i;

          for (int k = i; k < (i+bitsPerFrame); ++k)
          {
            d_correlation = this->correlate(&oldIn[k]);
            
            if(d_correlation > d_peak)
            {
              d_peak      = d_correlation;
              d_peakIndex = k;
            }
          }

          if (d_peak > threshold)
          {
              // Peak rise-edge detected
              d_riseEdgeFound = true;

              // Write one full packet
              for (int k2 = (d_peakIndex+d_correlationWindow); k2 < (d_peakIndex + d_correlationWindow + d_packetLength*8); ++k2)
              {
                out[j++] = oldIn[k2];
              }
          }



          if(d_riseEdgeFound && 
             ((d_peakIndex + d_packetLength*8) < ninput_items[0]))
          {
            i = d_peakIndex + d_packetLength*8;
          }
          else
          {
            i += bitsPerFrame;
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

