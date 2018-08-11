#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Transceiverloopbacksimulator Nogui
# Generated: Sun Jul 16 20:28:38 2017
##################################################

from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SatelliteModem


class transceiverLoopbackSimulator_noGUI(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Transceiverloopbacksimulator Nogui")

        ##################################################
        # Variables
        ##################################################
        self.txUDPPort = txUDPPort = 9001
        self.sps = sps = 4
        self.samp_rate = samp_rate = 320000
        self.rxUDPPort = rxUDPPort = 9002
        self.modemConfiguration = modemConfiguration = {'encoder' : 'cc','rate' : 0.5, 'arity' : 4, 'excessBW' : 0.35, 'preambleOverhead' : 8, 'MTU' : 100}

        ##################################################
        # Message Queues
        ##################################################
        SatelliteModem_Deframer_0_msgq_out = blocks_message_source_0_msgq_in = gr.msg_queue(2)
        blocks_message_sink_0_msgq_out = SatelliteModem_Framer_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0,
        	frequency_offset=.01,
        	epsilon=1,
        	taps=(-1, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_char*1, "127.0.0.1", txUDPPort, modemConfiguration['MTU'], True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, "127.0.0.1", rxUDPPort, modemConfiguration['MTU'], True)
        self.blocks_message_source_0 = blocks.message_source(gr.sizeof_char*1, blocks_message_source_0_msgq_in)
        self.blocks_message_sink_0 = blocks.message_sink(gr.sizeof_char*1, blocks_message_sink_0_msgq_out, False)
        self.SatelliteModem_SyncPreamble_0 = SatelliteModem.SyncPreamble(int((modemConfiguration['MTU']+6)/modemConfiguration['rate']), modemConfiguration['preambleOverhead'])
        self.SatelliteModem_PreambleDetector_0 = SatelliteModem.PreambleDetector(int((modemConfiguration['MTU']+6)/modemConfiguration['rate']), modemConfiguration['preambleOverhead'])
        self.SatelliteModem_Framer_0 = SatelliteModem.Framer(SatelliteModem_Framer_0_msgq_in, modemConfiguration['MTU'], 0)
        self.SatelliteModem_FECEncoder_0 = SatelliteModem.FECEncoder(modemConfiguration['encoder'], modemConfiguration['MTU']+6, modemConfiguration['rate'])
        self.SatelliteModem_FECDecoder_0 = SatelliteModem.FECDecoder(modemConfiguration['encoder'], modemConfiguration['MTU']+6, modemConfiguration['rate'])
        self.SatelliteModem_Deframer_0 = SatelliteModem.Deframer(SatelliteModem_Deframer_0_msgq_out, modemConfiguration['MTU'])
        self.SatelliteModem_DPSKTransmitter_0 = SatelliteModem.DPSKTransmitter(1, modemConfiguration['excessBW'], sps, modemConfiguration['arity'])
        self.SatelliteModem_DPSKReceiver_0 = SatelliteModem.DPSKReceiver(modemConfiguration['excessBW'], sps, modemConfiguration['arity'])

        ##################################################
        # Connections
        ##################################################
        self.connect((self.SatelliteModem_DPSKReceiver_0, 0), (self.SatelliteModem_PreambleDetector_0, 0))    
        self.connect((self.SatelliteModem_DPSKTransmitter_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.SatelliteModem_FECDecoder_0, 0), (self.SatelliteModem_Deframer_0, 0))    
        self.connect((self.SatelliteModem_FECEncoder_0, 0), (self.SatelliteModem_SyncPreamble_0, 0))    
        self.connect((self.SatelliteModem_Framer_0, 0), (self.SatelliteModem_FECEncoder_0, 0))    
        self.connect((self.SatelliteModem_PreambleDetector_0, 0), (self.SatelliteModem_FECDecoder_0, 0))    
        self.connect((self.SatelliteModem_SyncPreamble_0, 0), (self.SatelliteModem_DPSKTransmitter_0, 0))    
        self.connect((self.blocks_message_source_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_message_sink_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.SatelliteModem_DPSKReceiver_0, 0))    

    def get_txUDPPort(self):
        return self.txUDPPort

    def set_txUDPPort(self, txUDPPort):
        self.txUDPPort = txUDPPort

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rxUDPPort(self):
        return self.rxUDPPort

    def set_rxUDPPort(self, rxUDPPort):
        self.rxUDPPort = rxUDPPort

    def get_modemConfiguration(self):
        return self.modemConfiguration

    def set_modemConfiguration(self, modemConfiguration):
        self.modemConfiguration = modemConfiguration


def main(top_block_cls=transceiverLoopbackSimulator_noGUI, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
