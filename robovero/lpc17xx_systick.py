"""System tick timer client library functions. See LPC17xx CMSIS-Compliant 
Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

ST_CTRL_ENABLE = (1<<0)
ST_CTRL_TICKINT = (1<<1)
ST_CTRL_CLKSOURCE = (1<<2)
ST_CTRL_COUNTFLAG = (1<<16)

def ST_RELOAD_RELOAD(n):
	return (n & 0x00FFFFFF)

def ST_RELOAD_CURRENT(n):
	return (n & 0x00FFFFFF)

def ST_CALIB_TENMS(n):
	return (n & 0x00FFFFFF)

ST_CALIB_SKEW = (1<<30)
ST_CALIB_NOREF = (1<<31)
CLKSOURCE_EXT = (0)
CLKSOURCE_CPU = (1)

def SYSTICK_IntCmd(NewState):
	return robocaller("SYSTICK_IntCmd", "void", NewState)

def SYSTICK_GetCurrentValue():
	return robocaller("SYSTICK_GetCurrentValue", "uint32_t", )

def SYSTICK_ClearCounterFlag():
	return robocaller("SYSTICK_ClearCounterFlag", "void", )

def SYSTICK_InternalInit(time):
	return robocaller("SYSTICK_InternalInit", "void", time)

def SYSTICK_ExternalInit(freq, time):
	return robocaller("SYSTICK_ExternalInit", "void", freq, time)

def SYSTICK_Cmd(NewState):
	return robocaller("SYSTICK_Cmd", "void", NewState)

