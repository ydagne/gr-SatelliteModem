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
#include "DPSKDemodulator_impl.h"

namespace gr {
  namespace SatelliteModem {

    DPSKDemodulator::sptr
    DPSKDemodulator::make(int w_arity)
    {
      
      if(w_arity == 2)
      {
        return gnuradio::get_initial_sptr
        (new DBPSKDemodulator_impl());
      }
      else if(w_arity == 4)
      {
        return gnuradio::get_initial_sptr
        (new DQPSKDemodulator_impl());
      }
      else
      {
        std::cout<<"Modulation order "<< w_arity <<" is not supported.\n";
        exit(-1);
      }
    }

    /*
     * The private constructor
     */
    DBPSKDemodulator_impl::DBPSKDemodulator_impl()
      : gr::sync_interpolator("DPSKDemodulator",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(float)), 1)
    {
      d_prevSymbolRe = 0.7;
    }

    /*
     * Our virtual destructor.
     */
    DBPSKDemodulator_impl::~DBPSKDemodulator_impl()
    {
    }

    int
    DBPSKDemodulator_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      float *out = (float *) output_items[0];

      out[0] = -in[0].real() * d_prevSymbolRe;
      
      for (int i = 1; i < noutput_items; i++) 
      {
        out[i] = -in[i].real() * in[i-1].real();
      }

      d_prevSymbolRe = in[noutput_items-1].real();

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }








    /*
     * The private constructor
     */
    DQPSKDemodulator_impl::DQPSKDemodulator_impl()
      : gr::sync_interpolator("DPSKDemodulator",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(float)), 2)
    {
      d_prevSymbol = 0;  // '00'
    }

    /*
     * Our virtual destructor.
     */
    DQPSKDemodulator_impl::~DQPSKDemodulator_impl()
    {
    }

    int
    DQPSKDemodulator_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      float *out = (float *) output_items[0];

      char sym = 0;
      int i=0;

      for (int j=0; j < noutput_items-1;j+=2)
      {
        if(in[i].real() < 0)
        {
          if(in[i].imag() < 0)
          {
            // symbol '11'
            // Differencially decode
            sym = 6 - d_prevSymbol;
            d_prevSymbol = 2; // 3
          }
          else
          {
            // symbol '01'
            sym = 5 - d_prevSymbol; // 5 is used instead of 1. This is to avoid negative values
            d_prevSymbol = 1;
          }

          out[j]   = -in[i].real() * QPSK_SOFT_BIT_SIGN0[sym];
          out[j+1] = -in[i].real() * QPSK_SOFT_BIT_SIGN1[sym];
        }
        else
        {
          if(in[i].imag() < 0)
          {
            // symbol '10'
            // Differencially decode
            sym = 3 - d_prevSymbol; // 6 is used instead of 2. This is to avoid negative values
            d_prevSymbol = 3; // 2
          }
          else
          {
            // symbol '00'
            sym = 4 - d_prevSymbol; // 0 is used instead of 0. This is to avoid negative values
            d_prevSymbol = 0;
          }

          out[j]   = in[i].real() * QPSK_SOFT_BIT_SIGN0[sym];
          out[j+1] = in[i].real() * QPSK_SOFT_BIT_SIGN1[sym];
        }

        ++i;
      }
      // Tell runtime system how many output items we produced.
      return i*2;
    }


  } /* namespace SatelliteModem */
} /* namespace gr */

