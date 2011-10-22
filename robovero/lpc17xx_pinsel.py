"""Pin select client library functions. Find implementation details in  LPC17xx
CMSIS-Compliant Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

# Macros define for PORT Selection
# PORT 0
PINSEL_PORT_0 = ((0))  
# PORT 1
PINSEL_PORT_1 = ((1))  
# PORT 2
PINSEL_PORT_2 = ((2))  
# PORT 3
PINSEL_PORT_3 = ((3))  
# PORT 4
PINSEL_PORT_4 = ((4))

# Macros define for Pin Function selection
# default function
PINSEL_FUNC_0 = ((0))  
# first alternate function
PINSEL_FUNC_1 = ((1))  
# second alternate function
PINSEL_FUNC_2 = ((2))  
# third or reserved alternate function
PINSEL_FUNC_3 = ((3))  

# Macros define for Pin Number of Port
# Pin 0
PINSEL_PIN_0 = ((0))   
# Pin 1
PINSEL_PIN_1 = ((1))   
# Pin 2
PINSEL_PIN_2 = ((2))   
# Pin 3
PINSEL_PIN_3 = ((3))   
# Pin 4
PINSEL_PIN_4 = ((4))   
# Pin 5
PINSEL_PIN_5 = ((5))   
# Pin 6
PINSEL_PIN_6 = ((6))   
# Pin 7
PINSEL_PIN_7 = ((7))   
# Pin 8
PINSEL_PIN_8 = ((8))   
# Pin 9
PINSEL_PIN_9 = ((9))   
# Pin 10
PINSEL_PIN_10 = ((10))   
# Pin 11
PINSEL_PIN_11 = ((11))   
# Pin 12
PINSEL_PIN_12 = ((12))   
# Pin 13
PINSEL_PIN_13 = ((13))   
# Pin 14
PINSEL_PIN_14 = ((14))   
# Pin 15
PINSEL_PIN_15 = ((15))   
# Pin 16
PINSEL_PIN_16 = ((16))   
# Pin 17
PINSEL_PIN_17 = ((17))   
# Pin 18
PINSEL_PIN_18 = ((18))   
# Pin 19
PINSEL_PIN_19 = ((19))   
# Pin 20
PINSEL_PIN_20 = ((20))   
# Pin 21
PINSEL_PIN_21 = ((21))   
# Pin 22
PINSEL_PIN_22 = ((22))   
# Pin 23
PINSEL_PIN_23 = ((23))   
# Pin 24
PINSEL_PIN_24 = ((24))   
# Pin 25
PINSEL_PIN_25 = ((25))   
# Pin 26
PINSEL_PIN_26 = ((26))   
# Pin 27
PINSEL_PIN_27 = ((27))   
# Pin 28
PINSEL_PIN_28 = ((28))   
# Pin 29
PINSEL_PIN_29 = ((29))   
# Pin 30
PINSEL_PIN_30 = ((30))   
# Pin 31
PINSEL_PIN_31 = ((31)) 

# Macros define for Pin mode
# PINSEL_PINMODE_PULLUP
PINSEL_PINMODE_PULLUP = ((0))  
# Tri-state
PINSEL_PINMODE_TRISTATE = ((2))  
# Internal pull-down resistor
PINSEL_PINMODE_PULLDOWN = ((3))   
# Pin is in the normal (not open drain) mode
PINSEL_PINMODE_NORMAL = ((0))  
# Pin is in the open drain mode
PINSEL_PINMODE_OPENDRAIN = ((1))

# Macros define for I2C mode
# The standard drive mode
PINSEL_I2C_Normal_Mode = ((0))  
# Fast Mode Plus drive mode
PINSEL_I2C_Fast_Mode = ((1))   

class PINSEL_CFG_Type(cstruct):
  '''Pin configuration structure.
  
  Portnum:  Port Number, should be PINSEL_PORT_x, where x should be in range
            from 0 to 4
  Pinnum: Pin Number, should be PINSEL_PIN_x, where x should be in range from 0
          to 31
  Funcnum:  Function Number, should be PINSEL_FUNC_x, where x should be in range
            from 0 to 3
  Pinmode:  Pin Mode, should be:
            PINSEL_PINMODE_PULLUP: Internal pull-up resistor
            PINSEL_PINMODE_TRISTATE: Tri-state
            PINSEL_PINMODE_PULLDOWN: Internal pull-down resistor
  OpenDrain:  OpenDrain mode, should be:
              PINSEL_PINMODE_NORMAL: Pin is in the normal (not open drain) mode
              PINSEL_PINMODE_OPENDRAIN: Pin is in the open drain mode  
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
          
  '''
  pass

def PINSEL_SetI2C0Pins(i2cPinMode, filterSlewRateEnable):
  '''Setup I2C0 pins.
  
  i2cPinMode: I2C pin mode, should be one of the following:
              PINSEL_I2C_Normal_Mode : The standard drive mode
              PINSEL_I2C_Fast_Mode : Fast Mode Plus drive mode
  filterSlewRateEnable: should be:
                        ENABLE: Enable filter and slew rate.
                        DISABLE: Disable filter and slew rate.
    
  '''
  return robocaller("PINSEL_SetI2C0Pins", "void", i2cPinMode, filterSlewRateEnable)

def PINSEL_ConfigPin(PinCfg):
  '''Configure Pin corresponding to specified parameters passed in the PinCfg.
  
  PinCfg: Pointer to a PINSEL_CFG_Type structure that contains the configuration
          information for the specified pin.
  
  '''
  return robocaller("PINSEL_ConfigPin", "void", PinCfg)

def PINSEL_ConfigTraceFunc(NewState):
  '''Configure trace function.
  
  NewState: should be one of the following:
            ENABLE : Enable Trace Function
            DISABLE : Disable Trace Function
  
  '''
  return robocaller("PINSEL_ConfigTraceFunc", "void", NewState)
