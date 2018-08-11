#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Transceiverloopbacksimulator
# Generated: Sat Aug 11 10:48:59 2018
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
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import SatelliteModem
import sip
import sys


class transceiverLoopbackSimulator(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Transceiverloopbacksimulator")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Transceiverloopbacksimulator")
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

        self.settings = Qt.QSettings("GNU Radio", "transceiverLoopbackSimulator")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.txUDPPort = txUDPPort = 9001
        self.time_offset = time_offset = 1.00
        self.sps = sps = 4
        self.snr = snr = 25
        self.samp_rate = samp_rate = 320000
        self.rxUDPPort = rxUDPPort = 9002
        self.modemConfiguration = modemConfiguration = {'encoder' : 'cc','rate' : 0.5, 'arity' : 4, 'excessBW' : 0.35, 'preambleOverhead' : 8, 'MTU' : 100}
        self.freq_offset = freq_offset = 0

        ##################################################
        # Message Queues
        ##################################################
        SatelliteModem_Deframer_0_msgq_out = blocks_message_source_0_msgq_in = gr.msg_queue(2)
        blocks_message_sink_0_msgq_out = SatelliteModem_Framer_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(0.999, 1.001, 0.0001, 1.00, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, "Timing Offset", "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 0,2,1,1)
        self._freq_offset_range = Range(-0.25, 0.25, 0.001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 0,1,1,1)
        self._snr_range = Range(0, 30, 1, 25, 200)
        self._snr_win = RangeWidget(self._snr_range, self.set_snr, "SNR (dB)", "counter_slider", float)
        self.top_grid_layout.addWidget(self._snr_win, 0,0,1,1)
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
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
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
        self.connect((self.SatelliteModem_DPSKReceiver_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.SatelliteModem_DPSKTransmitter_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.SatelliteModem_DPSKTransmitter_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.SatelliteModem_FECDecoder_0, 0), (self.SatelliteModem_Deframer_0, 0))    
        self.connect((self.SatelliteModem_FECEncoder_0, 0), (self.SatelliteModem_SyncPreamble_0, 0))    
        self.connect((self.SatelliteModem_Framer_0, 0), (self.SatelliteModem_FECEncoder_0, 0))    
        self.connect((self.SatelliteModem_PreambleDetector_0, 0), (self.SatelliteModem_FECDecoder_0, 0))    
        self.connect((self.SatelliteModem_PreambleDetector_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.SatelliteModem_SyncPreamble_0, 0), (self.SatelliteModem_DPSKTransmitter_0, 0))    
        self.connect((self.blocks_message_source_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_message_sink_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.SatelliteModem_DPSKReceiver_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "transceiverLoopbackSimulator")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_txUDPPort(self):
        return self.txUDPPort

    def set_txUDPPort(self, txUDPPort):
        self.txUDPPort = txUDPPort

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_snr(self):
        return self.snr

    def set_snr(self, snr):
        self.snr = snr

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_rxUDPPort(self):
        return self.rxUDPPort

    def set_rxUDPPort(self, rxUDPPort):
        self.rxUDPPort = rxUDPPort

    def get_modemConfiguration(self):
        return self.modemConfiguration

    def set_modemConfiguration(self, modemConfiguration):
        self.modemConfiguration = modemConfiguration

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)


def main(top_block_cls=transceiverLoopbackSimulator, options=None):

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
