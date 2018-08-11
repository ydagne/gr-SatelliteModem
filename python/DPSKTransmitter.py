#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Yihenew Beyene: yihenew.beyene@gmail.com
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes

class DPSKTransmitter(gr.hier_block2):
    """
    docstring for block DPSKTransmitter
    """
    def __init__(self, amplitude=0.01, excessBW=0.35, sps=4, arity=1):
        gr.hier_block2.__init__(self,
            "DPSKTransmitter",
            gr.io_signature(1, 1, gr.sizeof_char*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.amplitude = amplitude
        self.excessBW  = excessBW
        self.sps       = sps
        self.arity     = arity

        if(arity != 2 and arity != 4):
            raise ValueError, "Unsupported modulation order '%d'" % (arity,)

        ##################################################
        # Blocks
        ##################################################
        
        if(self.arity==2):  # BPSK
            self.digital_dxpsk_mod = digital.dbpsk_mod(
                samples_per_symbol=sps,
                excess_bw=excessBW,
                mod_code="gray",
                verbose=False,
                log=False)
        else:
            self.digital_dxpsk_mod = digital.dqpsk_mod(
                samples_per_symbol=sps,
                excess_bw=excessBW,
                mod_code="gray",
                verbose=False,
                log=False)

            
        self.blocks_multiply_const_vxx = blocks.multiply_const_vcc((amplitude, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx, 0), (self, 0))    
        self.connect((self.digital_dxpsk_mod, 0), (self.blocks_multiply_const_vxx, 0))    
        self.connect((self, 0), (self.digital_dxpsk_mod, 0))    

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.blocks_multiply_const_vxx.set_k((self.amplitude, ))

    def get_excessBW(self):
        return self.excessBW

    def set_excessBW(self, excessBW):
        self.excessBW = excessBW

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
