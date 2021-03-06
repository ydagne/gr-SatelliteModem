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

#ifndef INCLUDED_SATELLITEMODEM_SYNCPREAMBLE_IMPL_H
#define INCLUDED_SATELLITEMODEM_SYNCPREAMBLE_IMPL_H

#include <SatelliteModem/SyncPreamble.h>

namespace gr {
  namespace SatelliteModem {

    static const int PREAMBLE_PATTERN_LENGTH         = 8;
    static const unsigned char PREAMBLE_PATTERN__[8] = {229,243,95,154,229,95,243,154};

    class SyncPreamble_impl : public SyncPreamble
    {
     private:
      unsigned d_packetLength;
      unsigned d_overheadBytes;
      unsigned d_bytesRequired;

     public:
      SyncPreamble_impl(unsigned w_PacketLength, unsigned w_overheadBytes);
      ~SyncPreamble_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace SatelliteModem
} // namespace gr

#endif /* INCLUDED_SATELLITEMODEM_SYNCPREAMBLE_IMPL_H */

