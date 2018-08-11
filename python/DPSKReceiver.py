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


from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
import SatelliteModem

class DPSKReceiver(gr.hier_block2):
    """
    docstring for block DPSKReceiver
    """
    def __init__(self, excessBW=0.35, sps=4, arity=2):
        gr.hier_block2.__init__(self,
            "DPSKReceiver",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.arity    = arity
        self.excessBW = excessBW
        self.sps      = sps

        if(arity !=2 and arity != 4):
            raise ValueError, "Unsupported modulation order '%d'" % (arity,)


        ##################################################
        # Variables
        ##################################################
        self.nfilts = nfilts = 32
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), excessBW, 45*nfilts)

        ##################################################
        # Blocks
        ##################################################
        self.digital_pfb_clock_sync_xxx = digital.pfb_clock_sync_ccf(sps, 0.1, (rrc_taps), nfilts, nfilts/2, 1.5, 1)
        self.digital_costas_loop_cc = digital.costas_loop_cc(0.1, arity, False)
        self.digital_cma_equalizer_cc = digital.cma_equalizer_cc(6, 1, 0.1, 1)
        self.SatelliteModem_DPSKDemodulator = SatelliteModem.DPSKDemodulator(arity)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.SatelliteModem_DPSKDemodulator, 0), (self, 0))    
        self.connect((self.digital_cma_equalizer_cc, 0), (self.digital_costas_loop_cc, 0))    
        self.connect((self.digital_costas_loop_cc, 0), (self.SatelliteModem_DPSKDemodulator, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx, 0), (self.digital_cma_equalizer_cc, 0))    
        self.connect((self, 0), (self.digital_pfb_clock_sync_xxx, 0))   


    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity

    def get_excessBW(self):
        return self.excessBW

    def set_excessBW(self, excessBW):
        self.excessBW = excessBW
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excessBW, 45*self.nfilts))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excessBW, 45*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excessBW, 45*self.nfilts))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx.update_taps((self.rrc_taps))

