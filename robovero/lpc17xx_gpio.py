"""General purpose IO client library functions. Find implementation details in 
LPC17xx CMSIS-Compliant Standard Peripheral Firmware Driver Library 
documentation."""

from internals import robocaller, cstruct
from LPC17xx import LPC_GPIO0_BASE, LPC_GPIO1_BASE, LPC_GPIO2_BASE, \
                    LPC_GPIO3_BASE, LPC_GPIO4_BASE

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

# Fast GPIO port 0 byte accessible definition
GPIO0_Byte = ((LPC_GPIO0_BASE))
# Fast GPIO port 1 byte accessible definition
GPIO1_Byte = ((LPC_GPIO1_BASE))
# Fast GPIO port 2 byte accessible definition
GPIO2_Byte = ((LPC_GPIO2_BASE))
# Fast GPIO port 3 byte accessible definition
GPIO3_Byte = ((LPC_GPIO3_BASE))
# Fast GPIO port 4 byte accessible definition
GPIO4_Byte = ((LPC_GPIO4_BASE))
# Fast GPIO port 0 half-word accessible definition
GPIO0_HalfWord = ((LPC_GPIO0_BASE))
# Fast GPIO port 1 half-word accessible definition
GPIO1_HalfWord = ((LPC_GPIO1_BASE))
# Fast GPIO port 2 half-word accessible definition
GPIO2_HalfWord = ((LPC_GPIO2_BASE))
# Fast GPIO port 3 half-word accessible definition
GPIO3_HalfWord = ((LPC_GPIO3_BASE))
# Fast GPIO port 4 half-word accessible definition
GPIO4_HalfWord = ((LPC_GPIO4_BASE))

#class GPIO_Byte_TypeDef(cstruct):
#  '''Fast GPIO port byte type definition.
#  '''
#  pass

class GPIO_HalfWord_TypeDef(cstruct):
  '''Fast GPIO port half-word type definition.
  
  FIODIRL:  FIO direction register lower halfword part
  FIODIRU:  FIO direction register upper halfword part
  FIOMASKL: FIO mask register lower halfword part
  FIOMASKU: FIO mask register upper halfword part
  FIOPINL:  FIO pin register lower halfword part
  FIOPINU:  FIO pin register upper halfword part
  FIOSETL:  FIO set register lower halfword part
  FIOSETU:  FIO set register upper halfword part
  FIOCLRL:  FIO clear register lower halfword part
  FIOCLRU:  FIO clear register upper halfword part
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

def FIO_IntCmd(portNum, bitValue, edgeState):
  '''Enable GPIO interrupt (just used for P0.0-P0.30, P2.0-P2.13).
  
  portNum:  Port number to read value, should be: 0 or 2
  bitValue: Value that contains all bits on GPIO to enable, in range from 0 to 
            0xFFFFFFFF.
  edgeState:  state of edge, should be:
              0: Rising edge
              1: Falling edge
              
  '''
  return robocaller("FIO_IntCmd", "void", portNum, bitValue, edgeState)

def GPIO_ClearInt(portNum, bitValue):
  '''Clear GPIO interrupt (just used for P0.0-P0.30, P2.0-P2.13).
  
  portNum:  Port number to read value, should be: 0 or 2
  bitValue: Value that contains all bits on GPIO to enable, in range from 0 to
            0xFFFFFFFF.
  
  '''
  return robocaller("GPIO_ClearInt", "void", portNum, bitValue)

def GPIO_GetIntStatus(portNum, pinNum, edgeState):
  '''Get GPIO Interrupt Status (just used for P0.0-P0.30, P2.0-P2.13).
  
  portNum:  Port number to read value, should be: 0 or 2
  pinNum:   Pin number, should be: 0..30 (with port 0) and 0..13 (with port 2)
  edgeState:  state of edge, should be:
              0: Rising edge
              1: Falling edge
  return: ENABLE: Interrupt has been generated due to a rising edge on P0.0
          DISABLE: A rising edge has not been detected on P0.0
  
  '''
  return robocaller("GPIO_GetIntStatus", "FunctionalState", portNum, pinNum, edgeState)

def FIO_HalfWordClearValue(portNum, halfwordNum, bitValue):
  '''Clear bits for FIO port in halfword accessible style.
  
  portNum:  Port number, in range from 0 to 4
  halfwordNum:  HalfWord part number, should be 0 (lower) or 1(upper)
  bitValue: Value that contains all bits in to clear, in range from 0 to 0xFFFF.
  
  '''
  return robocaller("FIO_HalfWordClearValue", "void", portNum, halfwordNum, bitValue)

def GPIO_IntCmd(portNum, bitValue, edgeState):
  '''Enable GPIO interrupt (just used for P0.0-P0.30, P2.0-P2.13).
  
  portNum:  Port number to read value, should be: 0 or 2
  bitValue: Value that contains all bits on GPIO to enable, in range from 0 to 
            0xFFFFFFFF.
  edgeState:  state of edge, should be:
              0: Rising edge
              1: Falling edge
              
  '''
  return robocaller("GPIO_IntCmd", "void", portNum, bitValue, edgeState)

def FIO_ClearInt(portNum, pinNum):
  '''Clear GPIO interrupt (just used for P0.0-P0.30, P2.0-P2.13).
  
  portNum:  Port number to read value, should be: 0 or 2
  bitValue: Value that contains all bits on GPIO to enable, in range from 0 to
            0xFFFFFFFF.
  
  '''
  return robocaller("FIO_ClearInt", "void", portNum, pinNum)

def FIO_ByteSetValue(portNum, byteNum, bitValue):
  '''Set bits for FIO port in byte accessible style.
  
  portNum: Port number, in range from 0 to 4
  byteNum: Byte part number, should be in range from 0 to 3
  bitValue: Value that contains all bits in to set, in range from 0 to 0xFF.
  
  '''
  return robocaller("FIO_ByteSetValue", "void", portNum, byteNum, bitValue)

def GPIO_ReadValue(portNum):
  '''Read Current state on port pin that have input direction of GPIO.
  
  portNum: Port number to read value, in range from 0 to 4
  return: Current value of GPIO port.
  
  '''
  return robocaller("GPIO_ReadValue", "uint32_t", portNum)

def FIO_ByteSetDir(portNum, byteNum, bitValue, direction):
  '''Set direction for FIO port in byte accessible style.
  
  portNum: Port number, in range from 0 to 4
  byteNum: Byte part number, should be in range from 0 to 3
  bitValue: Value that contains all bits in to set direction, in range from 0 to
            0xFF. 
  direction:  Direction value, should be:
              0: Input
              1: Output
  
  '''
  return robocaller("FIO_ByteSetDir", "void", portNum, byteNum, bitValue, direction)

def FIO_HalfWordSetDir(portNum, halfwordNum, bitValue, direction):
  '''Set direction for FIO port in halfword accessible style.
  
  portNum: Port number, in range from 0 to 4
  halfwordNum: HalfWord part number, should be 0 (lower) or 1(upper)
  bitValue: Value that contains all bits in to set direction, in range from 0 to
            0xFFFF.
  direction:  Direction value, should be:
              0: Input
              1: Output
  
  '''
  return robocaller("FIO_HalfWordSetDir", "void", portNum, halfwordNum, bitValue, direction)

def FIO_SetValue(portNum, bitValue):
  '''Set Value for bits that have output direction on GPIO port.
  
  portNum: Port number value, should be in range from 0 to 4
  bitValue: Value that contains all bits on GPIO to set, in range from 0 to 
            0xFFFFFFFF
  
  '''
  return robocaller("FIO_SetValue", "void", portNum, bitValue)

def FIO_GetIntStatus(portNum, pinNum, edgeState):
  '''Get GPIO Interrupt Status (just used for P0.0-P0.30, P2.0-P2.13).
  
  portNum:  Port number to read value, should be: 0 or 2
  pinNum:   Pin number, should be: 0..30 (with port 0) and 0..13 (with port 2)
  edgeState:  state of edge, should be:
              0: Rising edge
              1: Falling edge
  return: ENABLE: Interrupt has been generated due to a rising edge on P0.0
          DISABLE: A rising edge has not been detected on P0.0
  
  '''
  return robocaller("FIO_GetIntStatus", "FunctionalState", portNum, pinNum, edgeState)

def FIO_HalfWordSetValue(portNum, halfwordNum, bitValue):
  '''Set bits for FIO port in halfword accessible style.
  
  portNum: Port number, in range from 0 to 4
  halfwordNum: HalfWord part number, should be 0 (lower) or 1(upper)
  bitValue: Value that contains all bits in to set, in range from 0 to 0xFFFF.
  
  '''
  return robocaller("FIO_HalfWordSetValue", "void", portNum, halfwordNum, bitValue)

def FIO_ByteClearValue(portNum, byteNum, bitValue):
  '''Clear bits for FIO port in byte accessible style.
  
  portNum: Port number, in range from 0 to 4
  byteNum: Byte part number, should be in range from 0 to 3
  bitValue: Value that contains all bits in to clear, in range from 0 to 0xFF.
  
  '''
  return robocaller("FIO_ByteClearValue", "void", portNum, byteNum, bitValue)

def FIO_ByteReadValue(portNum, byteNum):
  '''Read Current state on port pin that have input direction of GPIO in byte 
  accessible style.
  
  portNum: Port number, in range from 0 to 4
  byteNum: Byte part number, should be in range from 0 to 3
  return: Current value of FIO port pin of specified byte part.
  
  '''
  return robocaller("FIO_ByteReadValue", "uint8_t", portNum, byteNum)

def GPIO_ClearValue(portNum, bitValue):
  '''Clear Value for bits that have output direction on GPIO port..
  
  portNum: Port number value, should be in range from 0 to 4
  bitValue: Value that contains all bits on GPIO to clear, in range from 0 to 
            0xFFFFFFFF.
  
  '''
  return robocaller("GPIO_ClearValue", "void", portNum, bitValue)

def FIO_ClearValue(portNum, bitValue):
  '''Clear Value for bits that have output direction on GPIO port..
  
  portNum: Port number value, should be in range from 0 to 4
  bitValue: Value that contains all bits on GPIO to clear, in range from 0 to 
            0xFFFFFFFF.
  
  '''
  return robocaller("FIO_ClearValue", "void", portNum, bitValue)

def FIO_SetDir(portNum, bitValue, direction):
  '''Set Direction for GPIO port.
  
  portNum: Port Number value, should be in range from 0 to 4
  bitValue: Value that contains all bits to set direction, in range from 0 to 
            0xFFFFFFFF.
  direction:  Direction value, should be:
              0: Input
              1: Output
  
  '''
  return robocaller("FIO_SetDir", "void", portNum, bitValue, direction)

def FIO_SetMask(portNum, bitValue, maskValue):
  '''Set mask value for bits in FIO port.
  
  portNum: Port number, in range from 0 to 4
  bitValue: Value that contains all bits to set direction, in range from 0 to 
            0xFFFFFFFF.
  maskValue:  Mask value contains state value for each bit:
              0: not mask
              1: mask
  
  '''
  return robocaller("FIO_SetMask", "void", portNum, bitValue, maskValue)

def FIO_HalfWordReadValue(portNum, halfwordNum):
  '''Read Current state on port pin that have input direction of GPIO in 
  halfword accessible style.
  
  portNum: Port number, in range from 0 to 4 
  halfwordNum: HalfWord part number, should be 0 (lower) or 1(upper)
  return: Current value of FIO port pin of specified halfword.
  
  '''
  return robocaller("FIO_HalfWordReadValue", "uint16_t", portNum, halfwordNum)

def FIO_ByteSetMask(portNum, byteNum, bitValue, maskValue):
  '''Set mask value for bits in FIO port in byte accessible style.
  
  portNum: Port number, in range from 0 to 4
  byteNum: Byte part number, should be in range from 0 to 3
  bitValue: Value that contains all bits in to set mask, in range from 0 to 0xFF
  maskValue:  Mask value contains state value for each bit:
              0: not mask
              1: mask
  
  '''
  return robocaller("FIO_ByteSetMask", "void", portNum, byteNum, bitValue, maskValue)

def FIO_ReadValue(portNum):
  '''Read Current state on port pin that have input direction of GPIO.
  
  portNum: Port number to read value, in range from 0 to 4
  return: Current value of GPIO port.
  
  '''
  return robocaller("FIO_ReadValue", "uint32_t", portNum)

def GPIO_SetValue(portNum, bitValue):
  '''Set Value for bits that have output direction on GPIO port.
  
  portNum: Port number value, should be in range from 0 to 4
  bitValue: Value that contains all bits on GPIO to set, in range from 0 to 
            0xFFFFFFFF
  
  '''
  return robocaller("GPIO_SetValue", "void", portNum, bitValue)

def FIO_HalfWordSetMask(portNum, halfwordNum, bitValue, maskValue):
  '''Set mask value for bits in FIO port in halfword accessible style.
  
  portNum: Port number, in range from 0 to 4
  halfwordNum: HalfWord part number, should be 0 (lower) or 1(upper)
  bitValue: Value that contains all bits in to set, in range from 0 to 0xFFFF
  maskValue:  Mask value contains state value for each bit:
              0: not mask
              1: mask
  
  '''
  return robocaller("FIO_HalfWordSetMask", "void", portNum, halfwordNum, bitValue, maskValue)

def GPIO_SetDir(portNum, bitValue, direction):
  '''Set Direction for GPIO port.
  
  portNum: Port Number value, should be in range from 0 to 4
  bitValue: Value that contains all bits to set direction, in range from 0 to 
            0xFFFFFFFF.
  direction:  Direction value, should be:
              0: Input
              1: Output
  
  '''
  return robocaller("GPIO_SetDir", "void", portNum, bitValue, direction)
