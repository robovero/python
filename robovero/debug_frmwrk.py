"""Debug framework client library functions. See LPC17xx CMSIS-Compliant
Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

def UARTPutDec32(UARTx, decnum):
	return robocaller("UARTPutDec32", "void", UARTx, decnum)

def debug_frmwrk_init():
	return robocaller("debug_frmwrk_init", "void", )

def UARTPutChar(UARTx, ch):
	return robocaller("UARTPutChar", "void", UARTx, ch)

def UARTPutHex(UARTx, hexnum):
	return robocaller("UARTPutHex", "void", UARTx, hexnum)

def UARTGetChar(UARTx):
	return robocaller("UARTGetChar", "uint8_t", UARTx)

def UARTPuts_(UARTx, string):
	return robocaller("UARTPuts_", "void", UARTx, string)

def UARTPutDec(UARTx, decnum):
	return robocaller("UARTPutDec", "void", UARTx, decnum)

def UARTPutDec16(UARTx, decnum):
	return robocaller("UARTPutDec16", "void", UARTx, decnum)

def UARTPuts(UARTx, string):
	return robocaller("UARTPuts", "void", UARTx, string)

def UARTPutHex16(UARTx, hexnum):
	return robocaller("UARTPutHex16", "void", UARTx, hexnum)

def UARTPutHex32(UARTx, hexnum):
	return robocaller("UARTPutHex32", "void", UARTx, hexnum)

