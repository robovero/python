"""System tick timer client library functions. Find implementation details in 
LPC17xx CMSIS-Compliant Standard Peripheral Firmware Driver Library
documentation.
"""

from internals import robocaller

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

def SYSTICK_IntCmd(NewState):
  '''Enable/disable System Tick interrupt.
  
  NewState: System Tick interrupt status, should be:
            - ENABLE
            - DISABLE
  
  '''
  return robocaller("SYSTICK_IntCmd", "void", NewState)

def SYSTICK_GetCurrentValue():
  '''Get current value of System Tick counter.
  
  return: current value of System Tick counter
  
  '''
  return robocaller("SYSTICK_GetCurrentValue", "uint32_t")

def SYSTICK_ClearCounterFlag():
  '''Clear Counter flag.
  '''
  return robocaller("SYSTICK_ClearCounterFlag", "void")

def SYSTICK_InternalInit(time):
  '''Initialize System Tick using internal CPU clock source.
  
  time: time interval(ms)
  
  '''
  return robocaller("SYSTICK_InternalInit", "void", time)

def SYSTICK_ExternalInit(freq, time):
  '''Initialize System Tick using external clock source.
  
  freq: external clock frequency(Hz)
  time: time interval(ms)
  
  '''
  return robocaller("SYSTICK_ExternalInit", "void", freq, time)

def SYSTICK_Cmd(NewState):
  '''Enable/disable System Tick counter.
  
  NewState: System Tick counter status, should be:
            - ENABLE
            - DISABLE
  
  '''
  return robocaller("SYSTICK_Cmd", "void", NewState)
