/* -*- c++ -*- */

#define SATELLITEMODEM_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "SatelliteModem_swig_doc.i"

%{
#include "SatelliteModem/DPSKDemodulator.h"
#include "SatelliteModem/SyncPreamble.h"
#include "SatelliteModem/PreambleDetector.h"
#include "SatelliteModem/Framer.h"
#include "SatelliteModem/Deframer.h"
#include "SatelliteModem/padForLDPC.h"
#include "SatelliteModem/depadForLDPC.h"
%}


%include "SatelliteModem/DPSKDemodulator.h"
GR_SWIG_BLOCK_MAGIC2(SatelliteModem, DPSKDemodulator);
%include "SatelliteModem/SyncPreamble.h"
GR_SWIG_BLOCK_MAGIC2(SatelliteModem, SyncPreamble);
%include "SatelliteModem/PreambleDetector.h"
GR_SWIG_BLOCK_MAGIC2(SatelliteModem, PreambleDetector);

%include "SatelliteModem/Framer.h"
GR_SWIG_BLOCK_MAGIC2(SatelliteModem, Framer);
%include "SatelliteModem/Deframer.h"
GR_SWIG_BLOCK_MAGIC2(SatelliteModem, Deframer);
%include "SatelliteModem/padForLDPC.h"
GR_SWIG_BLOCK_MAGIC2(SatelliteModem, padForLDPC);
%include "SatelliteModem/depadForLDPC.h"
GR_SWIG_BLOCK_MAGIC2(SatelliteModem, depadForLDPC);
