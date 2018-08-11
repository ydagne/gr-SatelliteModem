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

import numpy
from gnuradio import gr

import socket
import struct

global PR_SEQUENCE_LENGTH

PR_SEQUENCE_LENGTH = 1024

global PR_SEQUENCE

PR_SEQUENCE = [21,  52, 143, 169, 240,  10,  41, 112,  83,  23, 207, 102, 167, 145,   0, 166,
               81,  68, 117, 159, 205, 143,   6, 203,  69, 210, 176, 154,  99,  16, 255, 169,
               58,  23,  61, 231,  55, 122, 232,  49, 114, 158, 152, 170,  68, 108, 204, 238, 
              120,  78, 112,  78,  70,  35,  42, 126,  22, 237,  38,  41, 183, 172,  91,  23,
                2,  95, 201, 114,  25, 206, 168, 115, 136, 134, 161, 165,  49, 205,  50, 105,
               60,  69,   2, 237, 133, 118, 134,  86,  85, 253, 121, 191, 171, 203,  69,  72,
              183,  47, 213,  43, 244, 184,  34, 218, 238, 144, 102, 113, 179,  66,   7, 242,
              255, 199, 253, 124,  32, 118, 190, 172, 223, 194, 157,  70,  86, 213,  98,  20,
              221, 111,  44,   1, 167,  94,  96, 112, 132,  76, 122,   1,  43,  77, 190, 148,
              179, 205, 218,  30, 168, 192, 179, 154,   9,  49,  84, 164,  55,  19, 251,  52,
              251, 156,  63, 132, 182,  66,  29, 140,  56,  79, 249,  79, 242, 105,   2,  79,
               39, 254, 115, 139,  67, 225,  26, 210, 109, 235, 135, 222,  90, 102, 153, 233,
               34,  10, 102, 152, 235,  75, 139, 200,  83,  24, 113,   7, 172,  28,  51, 135,
              160,  95, 155, 216, 179, 100, 146,  63, 186,  87,  20,  77,  76,   5,  45, 220,
              167, 219,  69, 229,  53, 246, 106,  58, 209,  92, 128, 191, 212, 100,  24,  67,
              202, 239, 145, 240, 152, 252, 195,  47, 132, 163, 222, 153, 255,  33,  75, 122,
               33,  58,  46, 172,  83, 202, 139,  59, 175,  12, 146, 254,  92, 143, 237,  66,
              213,  44, 225,  71, 217, 206,  48, 250,  64, 199, 207, 127, 234,  25,  34, 219,
                4, 186, 209,  29, 125,  88, 198,  73, 211,  44, 221, 237,  48,  12, 140,   2,
              212, 232, 180,  62, 150, 240, 229, 155, 202, 214, 143,   0,  64, 110, 110, 224,
               17,  87,  45,  62, 186,  73,  60,  35,  56, 209,  96, 170, 239, 109, 154, 248,
               93, 170,  80, 226,  75,  75, 232, 126,  53,   6,  43,  77, 246, 200, 172, 215,
              107, 180, 123, 210, 111, 220,   2, 254,  70,   8,  38, 122, 227,  72, 200,  43,
              187,  63,  20, 218, 175, 245, 252, 136, 231, 122, 227,   6,  32, 189, 100, 100,
              154,   6,  99,  14, 176, 133,  19, 104, 110, 168,  55,  20, 119, 186, 157, 230,
               64,  56,  60, 207, 179, 224, 182, 169, 112, 144, 253, 245,  86,  39, 106, 141,
                7, 221, 228, 127,  53, 184, 179, 117,  43, 203, 227,  36, 240,   0, 112,   2,
               60, 180, 177,  67,  83,  23,  10, 194,  83, 133, 243, 171, 121, 166, 170,  58,
              206, 128, 111, 181, 142,  65,  19, 150, 172, 150, 136, 120,  82, 110, 195, 255,
               67, 202,  34,   9, 116, 144,  59,  37, 173,  90, 130, 177, 152, 129, 198, 175,
               81, 213, 169, 150,   4, 214,  29, 215,  86, 109, 203,  36, 155, 238, 162,  12,
              178,  65, 176,  92, 138,  56, 231,  95,  20,   7, 160, 239,  81, 190,  73,  31,
              131,  99, 250,  74, 151, 146, 157, 143,  71,  38, 187,  10, 205, 104, 212, 248,
              108,  13, 201, 161, 130, 145,  79, 191,  86, 226,  85, 203, 206,  12, 103, 247,
              106,  84, 162, 219, 201, 137, 189, 189, 113, 217, 126, 242, 204,  34,  60,  32,
              136,  14, 119, 251, 174, 222, 127,  73,  46, 246, 193, 243, 171,  47,  74,  14,
               11,  71,  43, 173, 231,  90,  25, 203, 119, 175, 174, 107, 168, 162, 134,  48,
              131, 191, 107, 188, 175, 244,  78,  87,  99,   6, 162, 144,  93, 107, 118,  80,
               57,  29,  34, 242, 126, 191,  79,   1, 157,  91, 166, 216,  25, 150, 149, 133,
              116, 247,  46, 143, 160,   7, 164, 214, 101, 111,  21, 148, 223,  52,  24,  48,
              170, 187, 161, 119,  80, 164, 143, 169,  31, 172, 174, 238, 212,  45, 243,  51,
               55,   2,  76,  70, 150, 101,  47, 100,  39, 213,  38, 173, 192,   3,  36,   7,
              207,  12, 170, 116, 205,  91,   6,  55, 181, 140, 222, 189,  26, 248, 189,   3,
              173, 124,   8,  29,  19, 155,  59,  36, 135, 238, 157, 176,  60,  52,   9, 169,
              129, 124, 220, 247, 194,  63, 173, 194, 150, 210, 237, 163,   4,  47,   6, 239,
              124, 203, 116, 126, 108, 228, 223, 162,  74,  74,  62, 180, 198, 210, 206,  64,
              204, 161,  59,  97, 116, 128, 138,  88,  74, 180, 239, 152, 151, 189,  95, 116,
              130, 237, 115, 163, 117, 141,  10, 205, 171,  51,   3, 195, 145, 167, 162, 187,
              227, 170,  30, 182, 114, 164, 166, 173,  15,  57,  43, 237, 131, 172, 170,  20,
               57,  72, 233,  58,  63, 173, 166, 180, 214, 186,   4, 149, 235,  23, 141, 238,
               51, 134,  32, 191,  80,  47, 250, 182, 211, 174, 176, 135,  48, 126, 143, 212,
               51, 135, 206,  90, 140, 183,  51, 164,   0, 131, 145,   1, 228, 213, 198, 201,
               95,  38,  90, 165, 238,  23, 189,  14, 193, 118,  11, 215,  42,  29,  69,  80,
              155, 173, 252, 254, 193,  70, 244, 105,  55, 161,   3,  11,  46,  51, 184, 113,
              216,  99, 214, 191, 149,  41, 135, 118,  97,  23,  66,  85,  96,  37,  81,  71,
              209,  87, 223,  68, 198, 155,   4, 179,   4, 175, 224, 110, 161, 150,  58, 200,
               73, 236,  76, 137,  85,  60, 139,  27,  35,  24,  79, 208, 131, 221, 251,  83,
               56, 132,  90, 220,  66, 215, 149, 184,  87,   2,  49, 129,   6, 140,  70, 178,
              225,   6,  87, 107,  20,  20,  18, 230, 248, 100,  80, 141, 202, 204, 220, 204,
                1, 235,   4,   7, 182, 137, 134, 128,  16,  58,  29, 253,  18,  15, 169,  88,
               32, 163, 191, 206,  68, 111, 102, 155, 197, 240,  33,  65,  96, 254,  87, 230,
               60,  56, 253, 243, 163, 129,  91, 196, 200,   7,  13,  82, 204, 161, 251,  40,
              157,  79,  21, 224, 151,  77,  43,  87,  17, 167,  62, 194,  76, 107,  14,   7,
               47,  69,  16,  85,  12,  25,  18, 231,  79, 151,  96, 243, 190, 227, 153, 176]

CRC_TABLE_16= [   0x0, 0x1189, 0x2312, 0x329b, 0x4624, 0x57ad, 0x6536, 0x74bf,
                0x8c48, 0x9dc1, 0xaf5a, 0xbed3, 0xca6c, 0xdbe5, 0xe97e, 0xf8f7,
                0x1081, 0x108, 0x3393, 0x221a, 0x56a5, 0x472c, 0x75b7, 0x643e,
                0x9cc9, 0x8d40, 0xbfdb, 0xae52, 0xdaed, 0xcb64, 0xf9ff, 0xe876, 
                0x2102, 0x308b, 0x210, 0x1399, 0x6726, 0x76af, 0x4434, 0x55bd,
                0xad4a, 0xbcc3, 0x8e58, 0x9fd1, 0xeb6e, 0xfae7, 0xc87c, 0xd9f5,
                0x3183, 0x200a, 0x1291, 0x318, 0x77a7, 0x662e, 0x54b5, 0x453c,
                0xbdcb, 0xac42, 0x9ed9, 0x8f50, 0xfbef, 0xea66, 0xd8fd, 0xc974,
                0x4204, 0x538d, 0x6116, 0x709f, 0x420, 0x15a9, 0x2732, 0x36bb, 
                0xce4c, 0xdfc5, 0xed5e, 0xfcd7, 0x8868, 0x99e1, 0xab7a, 0xbaf3, 
                0x5285, 0x430c, 0x7197, 0x601e, 0x14a1, 0x528, 0x37b3, 0x263a, 
                0xdecd, 0xcf44, 0xfddf, 0xec56, 0x98e9, 0x8960, 0xbbfb, 0xaa72, 
                0x6306, 0x728f, 0x4014, 0x519d, 0x2522, 0x34ab, 0x630, 0x17b9, 
                0xef4e, 0xfec7, 0xcc5c, 0xddd5, 0xa96a, 0xb8e3, 0x8a78, 0x9bf1, 
                0x7387, 0x620e, 0x5095, 0x411c, 0x35a3, 0x242a, 0x16b1, 0x738, 
                0xffcf, 0xee46, 0xdcdd, 0xcd54, 0xb9eb, 0xa862, 0x9af9, 0x8b70, 
                0x8408, 0x9581, 0xa71a, 0xb693, 0xc22c, 0xd3a5, 0xe13e, 0xf0b7, 
                0x840, 0x19c9, 0x2b52, 0x3adb, 0x4e64, 0x5fed, 0x6d76, 0x7cff, 
                0x9489, 0x8500, 0xb79b, 0xa612, 0xd2ad, 0xc324, 0xf1bf, 0xe036, 
                0x18c1, 0x948, 0x3bd3, 0x2a5a, 0x5ee5, 0x4f6c, 0x7df7, 0x6c7e, 
                0xa50a, 0xb483, 0x8618, 0x9791, 0xe32e, 0xf2a7, 0xc03c, 0xd1b5, 
                0x2942, 0x38cb, 0xa50, 0x1bd9, 0x6f66, 0x7eef, 0x4c74, 0x5dfd, 
                0xb58b, 0xa402, 0x9699, 0x8710, 0xf3af, 0xe226, 0xd0bd, 0xc134, 
                0x39c3, 0x284a, 0x1ad1, 0xb58, 0x7fe7, 0x6e6e, 0x5cf5, 0x4d7c, 
                0xc60c, 0xd785, 0xe51e, 0xf497, 0x8028, 0x91a1, 0xa33a, 0xb2b3, 
                0x4a44, 0x5bcd, 0x6956, 0x78df, 0xc60, 0x1de9, 0x2f72, 0x3efb, 
                0xd68d, 0xc704, 0xf59f, 0xe416, 0x90a9, 0x8120, 0xb3bb, 0xa232, 
                0x5ac5, 0x4b4c, 0x79d7, 0x685e, 0x1ce1, 0xd68, 0x3ff3, 0x2e7a, 
                0xe70e, 0xf687, 0xc41c, 0xd595, 0xa12a, 0xb0a3, 0x8238, 0x93b1, 
                0x6b46, 0x7acf, 0x4854, 0x59dd, 0x2d62, 0x3ceb, 0xe70, 0x1ff9, 
                0xf78f, 0xe606, 0xd49d, 0xc514, 0xb1ab, 0xa022, 0x92b9, 0x8330, 
                0x7bc7, 0x6a4e, 0x58d5, 0x495c, 0x3de3, 0x2c6a, 0x1ef1, 0xf78];


def computeCRC16(payload):

    index = 0;
    crc   = 0;
    payloadLen = len(payload)

    while index < payloadLen:
        crc         = (crc >> 8) ^ CRC_TABLE_16[((crc ^ payload[index]) & 0xFF)];
        index      += 1

    return (crc & 0xFFFF);


                                            


class Depacketizer(gr.basic_block):
    """
    docstring for block Depacketizer
    """
    def __init__(self, MTU, UDPPort):
        gr.basic_block.__init__(self,
            name="Depacketizer",
            in_sig=[numpy.uint8],
            out_sig=None)

        self.MTU     = MTU
        self.UDPPort = UDPPort

        if(MTU <= 0):
            raise ValueError, "MTU size should be larger than 0"

        self.socket    = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pktNumber = 0;

        # Scrambling sequence
        self.scramblingSeq = []
        pktLen = MTU + 6  # number of PRS values to copy from PR_SEQEUENE to self.scramblingSeq

        while  pktLen > 0:

            if pktLen > PR_SEQUENCE_LENGTH:
                self.scramblingSeq = self.scramblingSeq + PR_SEQUENCE
                pktLen -= PR_SEQUENCE_LENGTH
            else:
                self.scramblingSeq = self.scramblingSeq + PR_SEQUENCE[:pktLen]
                break

        self.scramblingSeq = numpy.array(self.scramblingSeq, dtype=numpy.uint8)

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = self.MTU + 6

    def general_work(self, input_items, output_items):
        #output_items[0][:] = input_items[0]
        
        pktLen  = self.MTU + 6
        payload = input_items[0][:pktLen]^self.scramblingSeq
        pkt     = payload.tostring()
        
        dlen = struct.unpack("H",pkt[2:4])[0]

        if(dlen>0 and dlen <= self.MTU):

            self.pktNumber = struct.unpack("H", pkt[4:6])[0]

            crcRx = payload[0]*256 + payload[1]

            crc   = computeCRC16(payload[6:(6+dlen)]) 

            if crcRx == crc:
                self.socket.sendto(pkt[6:(6+dlen)], ("localhost", self.UDPPort))

        #consume(0, self.MTU)
        self.consume_each(pktLen)

        return pktLen
