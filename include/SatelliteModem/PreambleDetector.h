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


#ifndef INCLUDED_SATELLITEMODEM_PREAMBLEDETECTOR_H
#define INCLUDED_SATELLITEMODEM_PREAMBLEDETECTOR_H

#include <SatelliteModem/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace SatelliteModem {

    /*!
     * \brief Preambler detector
     * \ingroup SatelliteModem
     *
     */
    class SATELLITEMODEM_API PreambleDetector : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<PreambleDetector> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of SatelliteModem::PreambleDetector.
       *
       * To avoid accidental use of raw pointers, SatelliteModem::PreambleDetector's
       * constructor is in a private implementation
       * class. SatelliteModem::PreambleDetector::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned w_PacketLength, unsigned w_overheadBytes);
    };

  } // namespace SatelliteModem
} // namespace gr

#endif /* INCLUDED_SATELLITEMODEM_PREAMBLEDETECTOR_H */

