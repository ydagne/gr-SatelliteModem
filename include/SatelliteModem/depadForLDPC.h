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


#ifndef INCLUDED_SATELLITEMODEM_DEPADFORLDPC_H
#define INCLUDED_SATELLITEMODEM_DEPADFORLDPC_H

#include <SatelliteModem/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace SatelliteModem {

    /*!
     * \brief Removes padding
     * \ingroup SatelliteModem
     *
     */
    class SATELLITEMODEM_API depadForLDPC : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<depadForLDPC> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of SatelliteModem::depadForLDPC.
       *
       * To avoid accidental use of raw pointers, SatelliteModem::depadForLDPC's
       * constructor is in a private implementation
       * class. SatelliteModem::depadForLDPC::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned w_frameBits, unsigned w_blockSize);
    };

  } // namespace SatelliteModem
} // namespace gr

#endif /* INCLUDED_SATELLITEMODEM_DEPADFORLDPC_H */

