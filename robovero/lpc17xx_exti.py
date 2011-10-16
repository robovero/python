"""External interrupt client library functions. Find implementation details in
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

# Macro defines for EXTI  control register
EXTI_EINT0_BIT_MARK = 0x01
EXTI_EINT1_BIT_MARK = 0x02
EXTI_EINT2_BIT_MARK = 0x04
EXTI_EINT3_BIT_MARK = 0x08

class EXTI_MODE_ENUM:
  '''EXTI mode option.
  '''
  # Level sensitivity is selected
  EXTI_MODE_LEVEL_SENSITIVE = 0
  # Edge sensitivity is selected
  EXTI_MODE_EDGE_SENSITIVE = 1

class EXTI_InitTypeDef(cstruct):
  '''EXTI Initialize structure.
  
  EXTI_Line: Select external interrupt pin (EINT0, EINT1, EINT 2, EINT3)
  EXTI_Mode: Choose between Level-sensitivity or Edge sensitivity
  EXTI_polarity:  If EXTI mode is level-sensitive: this element use to select
                  low or high active level
                  if EXTI mode is polarity-sensitive: this element use to select
                  falling or rising edge
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class EXTI_POLARITY_ENUM:
  '''EXTI polarity option.
  '''
  # Low active or falling edge sensitive depending on pin mode
  EXTI_POLARITY_LOW_ACTIVE_OR_FALLING_EDGE = 0
  # High active or rising edge sensitive depending on pin mode
  EXTI_POLARITY_HIGH_ACTIVE_OR_RISING_EDGE = 1

class EXTI_LINE_ENUM:
  '''EXTI external interrupt line option.
  '''
  # External interrupt 0, P2.10
  EXTI_EINT0 = 0
  # External interrupt 0, P2.11
  EXTI_EINT1 = 1
  # External interrupt 0, P2.12
  EXTI_EINT2 = 2
  # External interrupt 0, P2.13
  EXTI_EINT3 = 3

def EXTI_Init():
  '''Set EXTINT, EXTMODE, EXTPOLAR registers to default value.
  '''
  return robocaller("EXTI_Init", "void", )

def EXTI_ClearEXTIFlag(EXTILine):
  '''Clear External interrupt flag.
  
  EXTILine: external interrupt line, should be:
            EXTI_EINT0: external interrupt line 0
            EXTI_EINT1: external interrupt line 1
            EXTI_EINT2: external interrupt line 2
            EXTI_EINT3: external interrupt line 3
  
  '''
  return robocaller("EXTI_ClearEXTIFlag", "void", EXTILine)

def EXTI_Config(EXTICfg):
  '''Configuration for EXT. Set EXTINT, EXTMODE, EXTPOLAR register.
  
  EXTICfg:  Pointer to a EXTI_InitTypeDef structure that contains the
            configuration information for the specified external interrupt
            
  '''
  return robocaller("EXTI_Config", "void", EXTICfg)

def EXTI_SetMode(EXTILine, mode):
  '''Set mode for EXTI pin.
  
  EXTILine: external interrupt line, should be:
            EXTI_EINT0: external interrupt line 0
            EXTI_EINT1: external interrupt line 1
            EXTI_EINT2: external interrupt line 2
            EXTI_EINT3: external interrupt line 3
  mode: external mode, should be:
        EXTI_MODE_LEVEL_SENSITIVE
        EXTI_MODE_EDGE_SENSITIVE
  
  '''
  return robocaller("EXTI_SetMode", "void", EXTILine, mode)

def EXTI_DeInit():
  '''Close EXT.
  '''
  return robocaller("EXTI_DeInit", "void", )

def EXTI_SetPolarity(EXTILine, polarity):
  '''Set polarity for EXTI pin.
  
  EXTILine: external interrupt line, should be:
            EXTI_EINT0: external interrupt line 0
            EXTI_EINT1: external interrupt line 1
            EXTI_EINT2: external interrupt line 2
            EXTI_EINT3: external interrupt line 3
  polarity: external polarity value, should be:
            EXTI_POLARITY_LOW_ACTIVE_OR_FALLING_EDGE
            EXTI_POLARITY_LOW_ACTIVE_OR_FALLING_EDGE
            
  '''
  return robocaller("EXTI_SetPolarity", "void", EXTILine, polarity)

