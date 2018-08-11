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


#ifndef INCLUDED_SATELLITEMODEM_FRAMER_H
#define INCLUDED_SATELLITEMODEM_FRAMER_H

#include <SatelliteModem/api.h>
#include <gnuradio/sync_block.h>
#include <gnuradio/msg_queue.h>

namespace gr {
  namespace SatelliteModem {

    /*!
     * \brief Packet framer
     * \ingroup SatelliteModem
     *
     */
    class SATELLITEMODEM_API Framer : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<Framer> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of SatelliteModem::Framer.
       *
       * To avoid accidental use of raw pointers, SatelliteModem::Framer's
       * constructor is in a private implementation
       * class. SatelliteModem::Framer::make is the public interface for
       * creating new instances.
       */
      static sptr make(gr::msg_queue::sptr w_msgq, unsigned w_MTU, uint8_t w_nonBlocking);
    };

  } // namespace SatelliteModem
} // namespace gr

#endif /* INCLUDED_SATELLITEMODEM_FRAMER_H */

