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


#ifndef INCLUDED_SATELLITEMODEM_DPSKDEMODULATOR_H
#define INCLUDED_SATELLITEMODEM_DPSKDEMODULATOR_H

#include <SatelliteModem/api.h>
#include <gnuradio/sync_interpolator.h>

namespace gr {
  namespace SatelliteModem {

    /*!
     * \brief DPSK Demodulator
     * \ingroup SatelliteModem
     *
     */
    class SATELLITEMODEM_API DPSKDemodulator : virtual public gr::sync_interpolator
    {
     public:
      typedef boost::shared_ptr<DPSKDemodulator> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of SatelliteModem::DPSKDemodulator.
       *
       * To avoid accidental use of raw pointers, SatelliteModem::DPSKDemodulator's
       * constructor is in a private implementation
       * class. SatelliteModem::DPSKDemodulator::make is the public interface for
       * creating new instances.
       */
      static sptr make(int w_arity);
    };

  } // namespace SatelliteModem
} // namespace gr

#endif /* INCLUDED_SATELLITEMODEM_DPSKDEMODULATOR_H */

