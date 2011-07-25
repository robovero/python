"""Core library functions. See LPC17xx CMSIS-Compliant Standard Peripheral
Firmware Driver Library documentation.
"""

from internals import robocaller

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"


def NVIC_EnableIRQ(IRQn):
	"""Enable an interrupt.
	"""
	return robocaller("NVIC_EnableIRQ", "void", IRQn)

def NVIC_ClearPendingIRQ(IRQn):
	"""Clear a pending interrupt.
	
	Note that this is automatically done for you after your ISR is called,
	before 
	"""
	return robocaller("NVIC_ClearPendingIRQ", "void", IRQn)
