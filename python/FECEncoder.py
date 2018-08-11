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
from gnuradio import fec
from gnuradio import gr
from gnuradio.filter import firdes
import SatelliteModem

class FECEncoder(gr.hier_block2):
    """
    docstring for block FECEncoder
    """
    def __init__(self, encoderType, packetLength, rate):
        gr.hier_block2.__init__(self,
            "FECEncoder",
            gr.io_signature(1, 1, gr.sizeof_char*1),
            gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.packetLength  = packetLength
        self.rate = rate
        self.encoderType = encoderType

        if encoderType == "cc":
            if(rate == 0.5):  # Rate 1/2
                self.puncpat = puncpat = '11'
            elif(rate == 0.75): # Rate 3/4
                self.puncpat = puncpat = '101'
            elif(rate == 0.875): # Rate 7/8
                self.puncpat = puncpat = '1010101'
            else:
                raise ValueError, "Unsupported coding rate '%f' for CC" % (rate,)
        elif encoderType == "ldpc":
            if(rate == 0.42):  # Rate 0.42
                self.puncpat = puncpat = '11'
            else:
                raise ValueError, "Unsupported coding rate '%f' for LDPC" % (rate,)
        else:
            raise ValueError, "Unsupported channel encoder %s" % (encoderType,)

        
        if(encoderType == "cc"):

            ##################################################
            # Variables
            ##################################################
            self.polys = polys = [109, 79]
            self.k = k = 7
            
            
            self.enc_cc = enc_cc = fec.cc_encoder_make(packetLength*8, k, 2, (polys), 0, fec.CC_TAILBITING, False)
                

            ##################################################
            # Blocks
            ##################################################
            self.fec_extended_encoder = fec.extended_encoder(encoder_obj_list=enc_cc, threading='capillary', puncpat=puncpat)
            self.blocks_unpacked_to_packed_xx = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
            self.blocks_unpack_k_bits_bb = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)

            ##################################################
            # Connections
            ##################################################
            self.connect((self.blocks_unpacked_to_packed_xx, 0), (self, 0))    
            self.connect((self.blocks_unpack_k_bits_bb, 0), (self.fec_extended_encoder, 0))    
            self.connect((self.fec_extended_encoder, 0), (self.blocks_unpacked_to_packed_xx, 0))    
            self.connect((self, 0), (self.blocks_unpack_k_bits_bb, 0))

        else:
            
            ##################################################
            # Variables
            ##################################################
            self.ldpc_enc = ldpc_enc = fec.ldpc_encoder_make(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist"); 
                

            ##################################################
            # Blocks
            ##################################################
            self.SatelliteModem_padForLDPC_0 = SatelliteModem.padForLDPC(packetLength*8, 42)
            self.fec_extended_encoder = fec.extended_encoder(encoder_obj_list=ldpc_enc, threading='capillary', puncpat=puncpat)
            self.blocks_unpacked_to_packed_xx = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
            self.blocks_unpack_k_bits_bb = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)

            ##################################################
            # Connections
            ##################################################
            self.connect((self.blocks_unpacked_to_packed_xx, 0), (self, 0))    
            self.connect((self.blocks_unpack_k_bits_bb, 0), (self.SatelliteModem_padForLDPC_0, 0)) 
            self.connect((self.SatelliteModem_padForLDPC_0, 0), (self.fec_extended_encoder, 0))    
            self.connect((self.fec_extended_encoder, 0), (self.blocks_unpacked_to_packed_xx, 0))    
            self.connect((self, 0), (self.blocks_unpack_k_bits_bb, 0))


    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    """

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc
    """

