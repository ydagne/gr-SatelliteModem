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

#ifndef INCLUDED_SATELLITEMODEM_PREAMBLEDETECTOR_IMPL_H
#define INCLUDED_SATELLITEMODEM_PREAMBLEDETECTOR_IMPL_H

#include <SatelliteModem/PreambleDetector.h>

namespace gr {
  namespace SatelliteModem {


    static const int PREAMBLE_PATTERN_LENGTH = 8;
    static const float PREAMBLE_PATTERN__[64] = {1, 1, 1,-1,-1, 1,-1, 1, 1, 1, 1, 1,-1,-1, 1, 1,
                                                -1, 1,-1, 1, 1, 1, 1, 1, 1,-1,-1, 1, 1,-1, 1,-1,
                                                 1, 1, 1,-1,-1, 1,-1, 1,-1, 1,-1, 1, 1, 1, 1, 1,
                                                 1, 1, 1, 1,-1,-1, 1, 1, 1,-1,-1, 1, 1,-1, 1,-1};

    class PreambleDetector_impl : public PreambleDetector
    {
     private:
      unsigned d_packetLength;
      unsigned d_overheadBytes;
      int      d_correlationWindow;
      int      d_bitsRequired;

      // Correlation parameters
      float d_correlation;
      float d_peak;
      int   d_peakIndex;
      float d_riseThreshold;
      float d_fallThreshold;
      bool  d_riseEdgeFound;
      bool  d_fallEdgeFound;

      float correlate(const float *w_in);


     public:
      PreambleDetector_impl(unsigned w_PacketLength, unsigned w_overheadBytes);
      ~PreambleDetector_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace SatelliteModem
} // namespace gr

#endif /* INCLUDED_SATELLITEMODEM_PREAMBLEDETECTOR_IMPL_H */

