"""LPC client library type. Find implementation details in LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library documentation.
"""

__author__ =      "Neil MacMunn"
__email__ =        "neil@gumstix.com"
__copyright__ =   "Copyright 2010, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =      "0.1"


def _BIT(n):
  '''sets the bit at position "n".
    
  Intended to be used in "OR" and "AND" expressions:
  e.g., "(_BIT(3) | _BIT(7))"
  
  '''
  return (1<<n)

def _SBF(f,v):
  ''' Sets the bit field starting at position "f" to value "v".
  
  Intended to be used in "OR" and "AND" expressions:
  e.g., "((_SBF(5,7) | _SBF(12,0xF)) & 0xFFFF)"
  
  '''
  return (v<<f)

def _BITMASK(field_width):
  '''Constructs a symbol with 'field_width' least significant bits set.
  
  _BITMASK(5) constructs '0x1F', _BITMASK(16) == 0xFFFF
  The symbol is intended to be used to limit the bit field width like so:
  <a_register> = (any_expression) & _BITMASK(x), where 0 < x <= 32.
  
  If "any_expression" results in a value that is larger than can be contained in
  'x' bits, the bits above 'x - 1' are masked off.  When used with the _SBF 
  example above, the example would be written:
  a_reg = ((_SBF(5,7) | _SBF(12,0xF)) & _BITMASK(16))
  
  This ensures that the value written to a_reg is no wider than 16 bits, and 
  makes the code easier to read and understand.
  
  '''
  return ( _BIT(field_width) - 1)

# NULL pointer
NULL = (0)

def MAX(a, b):
  '''Returns maximum of a and b.
  '''
  return max(a, b)

def MIN(a, b):
  '''Returns minimum of a and b.
  '''
  return min(a, b)
  
class Status:
  '''Status type definition.
  '''
  ERROR = 0
  SUCCESS = 1

#~ class UNS_8(cstruct):
  #~ pass

#~ class BOOL_16(cstruct):
  #~ pass

#~ class (*PFV)()(cstruct):
  #~ pass

#~ class INT_8(cstruct):
  #~ pass

class SetState:
  '''Flag Status and Interrupt Flag Status type definition.
  '''
  RESET = 0
  SET = 1

#~ class UNS_64(cstruct):
  #~ pass

class FunctionalState:
  '''Functional State Definition.
  '''
  DISABLE = 0
  ENABLE = 1

#~ class BOOL_32(cstruct):
  #~ pass

#~ class CHAR(cstruct):
  #~ pass

class TRANSFER_BLOCK_Type:
  '''Read/Write transfer type mode (Block or non-block).
  
  NONE_BLOCKING:  None Blocking type
  BLOCKING: Blocking type
  
  '''
  NONE_BLOCKING = 0
  BLOCKING = 1

#~ class BOOL_8(cstruct):
  #~ pass

class Bool:
  '''Boolean Type definition.
  '''
  FALSE = 0
  TRUE = 1

class FlagStatus:
  '''Flag Status and Interrupt Flag Status type definition.
  '''
  RESET = 0
  SET = 1

#~ class INT_64(cstruct):
  #~ pass

#~ class INT_16(cstruct):
  #~ pass

class IntStatus:
  '''Flag Status and Interrupt Flag Status type definition.
  '''
  RESET = 0
  SET = 1

#~ class UNS_16(cstruct):
  #~ pass

#~ class INT_32(cstruct):
  #~ pass

#~ class UNS_32(cstruct):
  #~ pass

#~ class (*PFI)()(cstruct):
  #~ pass

