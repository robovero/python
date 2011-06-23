"""LPC client library type. See LPC17xx CMSIS-Compliant Standard 
Peripheral Firmware Driver Library documentation.
"""

from internals import cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

def PARAM_SETSTATE(State):
  return ((State==RESET) or (State==SET))

def PARAM_FUNCTIONALSTATE(State):
  return ((State==DISABLE) or (State==ENABLE))

def _BIT(n):
  return (1<<n)

def _SBF(f,v):
	return (v<<f)

def _BITMASK(field_width):
  return ( _BIT(field_width) - 1)

NULL = (0)

def MAX(a, b):
	return max(a, b)

def MIN(a, b):
	return min(a, b)
	
class Status:
	ERROR = 0
	SUCCESS = 1

class UNS_8(cstruct):
	pass

class BOOL_16(cstruct):
	pass

#~ class (*PFV)()(cstruct):
	#~ pass

class INT_8(cstruct):
	pass

class SetState:
	RESET = 0
	SET = 1

class UNS_64(cstruct):
	pass

class FunctionalState:
	DISABLE = 0
	ENABLE = 1

class BOOL_32(cstruct):
	pass

class CHAR(cstruct):
	pass

class TRANSFER_BLOCK_Type:
	NONE_BLOCKING = 0
	BLOCKING = 1

class BOOL_8(cstruct):
	pass

class Bool:
	FALSE = 0
	TRUE = 1

class FlagStatus:
	RESET = 0
	SET = 1

class INT_64(cstruct):
	pass

class INT_16(cstruct):
	pass

class IntStatus:
	RESET = 0
	SET = 1

class UNS_16(cstruct):
	pass

class INT_32(cstruct):
	pass

class UNS_32(cstruct):
	pass

#~ class (*PFI)()(cstruct):
	#~ pass

