"""Nested vector interrupt controller client library functions. Find 
implementation details in LPC17xx CMSIS-Compliant Standard Peripheral Firmware 
Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

def NVIC_SetVTOR(offset):
  '''Set Vector Table Offset value.
  
  offset: Offset value
  
  '''
  return robocaller("NVIC_SetVTOR", "void", offset)

def NVIC_SCBDeInit():
  '''De-initializes the SCB peripheral registers to their default reset values.
  
  These following SCB NVIC peripheral registers will be de-initialized:
  - Interrupt Control State register
  - Interrupt Vector Table Offset register
  - Application Interrupt/Reset Control register
  - System Control register
  - Configuration Control register
  - System Handlers Priority Registers
  - System Handler Control and State Register
  - Configurable Fault Status Register
  - Hard Fault Status Register
  - Debug Fault Status Register
  
  '''
  return robocaller("NVIC_SCBDeInit", "void")

def NVIC_DeInit():
  '''De-initializes the NVIC peripheral registers to their default reset values.
  
  These following NVIC peripheral registers will be de-initialized:
  - Disable Interrupt (32 IRQ interrupt sources that matched with LPC17xx)
  - Clear all Pending Interrupts (32 IRQ interrupt source that matched with LPC17xx)
  - Clear all Interrupt Priorities (32 IRQ interrupt source that matched with LPC17xx)
  
  '''
  return robocaller("NVIC_DeInit", "void")
