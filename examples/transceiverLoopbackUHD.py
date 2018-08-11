#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Transceiverloopbackuhd
# Generated: Sun Jul 16 20:56:26 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SatelliteModem
import sip
import sys
import time


class transceiverLoopbackUHD(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Transceiverloopbackuhd")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Transceiverloopbackuhd")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "transceiverLoopbackUHD")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.txUDPPort = txUDPPort = 9001
        self.txGain = txGain = 10
        self.txFreq = txFreq = 100e6
        self.sps = sps = 4
        self.samp_rate = samp_rate = 320000
        self.rxUDPPort = rxUDPPort = 9002
        self.rxGain = rxGain = 15
        self.rxFreq = rxFreq = 100e6
        self.modemConfiguration = modemConfiguration = {'encoder' : 'cc','rate' : 0.5, 'arity' : 4, 'excessBW' : 0.35, 'preambleOverhead' : 8, 'MTU' : 100}

        ##################################################
        # Message Queues
        ##################################################
        SatelliteModem_Deframer_0_msgq_out = blocks_message_source_0_msgq_in = gr.msg_queue(2)
        blocks_message_sink_0_msgq_out = SatelliteModem_Framer_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(rxFreq, 0)
        self.uhd_usrp_source_0.set_gain(rxGain, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(txFreq, 0)
        self.uhd_usrp_sink_0.set_gain(txGain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Frame", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 2,1,1,2)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Soft bits", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 2,0,1,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"RX", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 1,1,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"TX", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1,0,1,1)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_char*1, "127.0.0.1", txUDPPort, modemConfiguration['MTU'], True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, "127.0.0.1", rxUDPPort, modemConfiguration['MTU'], True)
        self.blocks_message_source_0 = blocks.message_source(gr.sizeof_char*1, blocks_message_source_0_msgq_in)
        self.blocks_message_sink_0 = blocks.message_sink(gr.sizeof_char*1, blocks_message_sink_0_msgq_out, False)
        self.SatelliteModem_SyncPreamble_0 = SatelliteModem.SyncPreamble(int((modemConfiguration['MTU']+6)/modemConfiguration['rate']), modemConfiguration['preambleOverhead'])
        self.SatelliteModem_PreambleDetector_0 = SatelliteModem.PreambleDetector(int((modemConfiguration['MTU']+6)/modemConfiguration['rate']), modemConfiguration['preambleOverhead'])
        self.SatelliteModem_Framer_0 = SatelliteModem.Framer(SatelliteModem_Framer_0_msgq_in, modemConfiguration['MTU'], 1)
        self.SatelliteModem_FECEncoder_0 = SatelliteModem.FECEncoder(modemConfiguration['encoder'], modemConfiguration['MTU']+6, modemConfiguration['rate'])
        self.SatelliteModem_FECDecoder_0 = SatelliteModem.FECDecoder(modemConfiguration['encoder'], modemConfiguration['MTU']+6, modemConfiguration['rate'])
        self.SatelliteModem_Deframer_0 = SatelliteModem.Deframer(SatelliteModem_Deframer_0_msgq_out, modemConfiguration['MTU'])
        self.SatelliteModem_DPSKTransmitter_0 = SatelliteModem.DPSKTransmitter(.1, modemConfiguration['excessBW'], sps, modemConfiguration['arity'])
        self.SatelliteModem_DPSKReceiver_0 = SatelliteModem.DPSKReceiver(modemConfiguration['excessBW'], sps, modemConfiguration['arity'])

        ##################################################
        # Connections
        ##################################################
        self.connect((self.SatelliteModem_DPSKReceiver_0, 0), (self.SatelliteModem_PreambleDetector_0, 0))    
        self.connect((self.SatelliteModem_DPSKReceiver_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.SatelliteModem_DPSKTransmitter_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.SatelliteModem_DPSKTransmitter_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.SatelliteModem_FECDecoder_0, 0), (self.SatelliteModem_Deframer_0, 0))    
        self.connect((self.SatelliteModem_FECEncoder_0, 0), (self.SatelliteModem_SyncPreamble_0, 0))    
        self.connect((self.SatelliteModem_Framer_0, 0), (self.SatelliteModem_FECEncoder_0, 0))    
        self.connect((self.SatelliteModem_PreambleDetector_0, 0), (self.SatelliteModem_FECDecoder_0, 0))    
        self.connect((self.SatelliteModem_PreambleDetector_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.SatelliteModem_SyncPreamble_0, 0), (self.SatelliteModem_DPSKTransmitter_0, 0))    
        self.connect((self.blocks_message_source_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_message_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.SatelliteModem_DPSKReceiver_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "transceiverLoopbackUHD")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_txUDPPort(self):
        return self.txUDPPort

    def set_txUDPPort(self, txUDPPort):
        self.txUDPPort = txUDPPort

    def get_txGain(self):
        return self.txGain

    def set_txGain(self, txGain):
        self.txGain = txGain
        self.uhd_usrp_sink_0.set_gain(self.txGain, 0)
        	

    def get_txFreq(self):
        return self.txFreq

    def set_txFreq(self, txFreq):
        self.txFreq = txFreq
        self.uhd_usrp_sink_0.set_center_freq(self.txFreq, 0)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_rxUDPPort(self):
        return self.rxUDPPort

    def set_rxUDPPort(self, rxUDPPort):
        self.rxUDPPort = rxUDPPort

    def get_rxGain(self):
        return self.rxGain

    def set_rxGain(self, rxGain):
        self.rxGain = rxGain
        self.uhd_usrp_source_0.set_gain(self.rxGain, 0)
        	

    def get_rxFreq(self):
        return self.rxFreq

    def set_rxFreq(self, rxFreq):
        self.rxFreq = rxFreq
        self.uhd_usrp_source_0.set_center_freq(self.rxFreq, 0)

    def get_modemConfiguration(self):
        return self.modemConfiguration

    def set_modemConfiguration(self, modemConfiguration):
        self.modemConfiguration = modemConfiguration


def main(top_block_cls=transceiverLoopbackUHD, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
