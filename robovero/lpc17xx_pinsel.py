"""Pin select client library functions. See LPC17xx CMSIS-Compliant
Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct
from lpc_types import _BIT

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

PINSEL_PORT_0 = ((0))	
PINSEL_PORT_1 = ((1))	
PINSEL_PORT_2 = ((2))	
PINSEL_PORT_3 = ((3))	
PINSEL_PORT_4 = ((4))	
PINSEL_FUNC_0 = ((0))	
PINSEL_FUNC_1 = ((1))	
PINSEL_FUNC_2 = ((2))	
PINSEL_FUNC_3 = ((3))	
PINSEL_PIN_0 = ((0)) 	
PINSEL_PIN_1 = ((1)) 	
PINSEL_PIN_2 = ((2)) 	
PINSEL_PIN_3 = ((3)) 	
PINSEL_PIN_4 = ((4)) 	
PINSEL_PIN_5 = ((5)) 	
PINSEL_PIN_6 = ((6)) 	
PINSEL_PIN_7 = ((7)) 	
PINSEL_PIN_8 = ((8)) 	
PINSEL_PIN_9 = ((9)) 	
PINSEL_PIN_10 = ((10)) 	
PINSEL_PIN_11 = ((11)) 	
PINSEL_PIN_12 = ((12)) 	
PINSEL_PIN_13 = ((13)) 	
PINSEL_PIN_14 = ((14)) 	
PINSEL_PIN_15 = ((15)) 	
PINSEL_PIN_16 = ((16)) 	
PINSEL_PIN_17 = ((17)) 	
PINSEL_PIN_18 = ((18)) 	
PINSEL_PIN_19 = ((19)) 	
PINSEL_PIN_20 = ((20)) 	
PINSEL_PIN_21 = ((21)) 	
PINSEL_PIN_22 = ((22)) 	
PINSEL_PIN_23 = ((23)) 	
PINSEL_PIN_24 = ((24)) 	
PINSEL_PIN_25 = ((25)) 	
PINSEL_PIN_26 = ((26)) 	
PINSEL_PIN_27 = ((27)) 	
PINSEL_PIN_28 = ((28)) 	
PINSEL_PIN_29 = ((29)) 	
PINSEL_PIN_30 = ((30)) 	
PINSEL_PIN_31 = ((31)) 	
PINSEL_PINMODE_PULLUP = ((0))	
PINSEL_PINMODE_TRISTATE = ((2))	
PINSEL_PINMODE_PULLDOWN = ((3)) 	
PINSEL_PINMODE_NORMAL = ((0))	
PINSEL_PINMODE_OPENDRAIN = ((1)) 	
PINSEL_I2C_Normal_Mode = ((0))	
PINSEL_I2C_Fast_Mode = ((1)) 	
PINSEL_I2CPADCFG_SDADRV0 = _BIT(0) 
PINSEL_I2CPADCFG_SDAI2C0 = _BIT(1) 
PINSEL_I2CPADCFG_SCLDRV0 = _BIT(2) 
PINSEL_I2CPADCFG_SCLI2C0 = _BIT(3) 

class PINSEL_CFG_Type(cstruct):
	pass

def PINSEL_SetI2C0Pins(i2cPinMode, filterSlewRateEnable):
	return robocaller("PINSEL_SetI2C0Pins", "void", i2cPinMode, filterSlewRateEnable)

def PINSEL_ConfigPin(PinCfg):
	return robocaller("PINSEL_ConfigPin", "void", PinCfg)

def PINSEL_ConfigTraceFunc(NewState):
	return robocaller("PINSEL_ConfigTraceFunc", "void", NewState)

