"""ADC client library functions. Find implementation details in LPC17xx 
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

def ADC_CR_CH_SEL(n):
  '''Selects which of the AD0.0:7 pins is (are) to be sampled and converted.
  '''
  return (1 << n)

def ADC_CR_CLKDIV(n):
  '''The APB clock (PCLK) is divided by (this value plus one) to produce the
  clock for the A/D.
  '''
  return (n << 8)

# Repeated conversions A/D enable bit
ADC_CR_BURST = (1 << 16)
# ADC convert in power down mode
ADC_CR_PDN = (1 << 21)
# Start mask bits
ADC_CR_START_MASK = (7 << 24)

def ADC_CR_START_MODE_SEL(SEL):
  '''Select Start Mode.
  '''
  return (SEL << 24)

# Start conversion now
ADC_CR_START_NOW = (1 << 24)
# Start conversion when the edge selected by bit 27 occurs on P2.10/EINT0
ADC_CR_START_EINT0 = (2 << 24)
# Start conversion when the edge selected by bit 27 occurs on P1.27/CAP0.1
ADC_CR_START_CAP01 = (3 << 24)
# Start conversion when the edge selected by bit 27 occurs on MAT0.1
ADC_CR_START_MAT01 = (4 << 24)
# Start conversion when the edge selected by bit 27 occurs on MAT0.3
ADC_CR_START_MAT03 = (5 << 24)
# Start conversion when the edge selected by bit 27 occurs on MAT1.0
ADC_CR_START_MAT10 = (6 << 24)
# Start conversion when the edge selected by bit 27 occurs on MAT1.1
ADC_CR_START_MAT11 = (7 << 24)
# Start conversion on a falling edge on the selected CAP/MAT signal
ADC_CR_EDGE = (1 << 27)

def ADC_GDR_RESULT(n):
  ''' When DONE is 1, this field contains result value of ADC conversion.
  '''
  return ((n >> 4) & 0xFFF)

def ADC_GDR_CH(n):
  ''' These bits contain the channel from which the LS bits were converted.
  '''
  return ((n >> 24) & 0x7)

# This bit is 1 in burst mode if the results of one or more conversions was (were) lost
ADC_GDR_OVERRUN_FLAG  = (1 << 30)
# This bit is set to 1 when an A/D conversion completes
ADC_GDR_DONE_FLAG = (1 << 31)
# This bits is used to mask for Channel
ADC_GDR_CH_MASK = (7 << 24)

def ADC_INTEN_CH(n):
  ''' These bits allow control over which A/D channels generate interrupts for 
  conversion completion.
  '''
  return (1 << n)

# When 1, enables the global DONE flag in ADDR to generate an interrupt
ADC_INTEN_GLOBAL = (1 << 8)

def ADC_DR_RESULT(n):
  ''' When DONE is 1, this field contains result value of ADC conversion.
  '''
  return ((n >> 4) & 0xFFF)

# These bits mirror the OVERRRUN status flags that appear in the result register for each A/D channel
ADC_DR_OVERRUN_FLAG = (1 << 30)
# This bit is set to 1 when an A/D conversion completes. It is cleared when this register is read
ADC_DR_DONE_FLAG = (1 << 31)

def ADC_STAT_CH_DONE_FLAG(n):
  ''' These bits mirror the DONE status flags that appear in the result register
  for each A/D channel.
  '''
  return (n & 0xFF)

def ADC_STAT_CH_OVERRUN_FLAG(n):
  ''' These bits mirror the OVERRRUN status flags that appear in the result 
  register for each A/D channel
  '''
  return ((n >> 8) & 0xFF)

# This bit is the A/D interrupt flag
ADC_STAT_INT_FLAG = (1 << 16)

def ADC_ADCOFFS(n):
  ''' Offset trim bits for ADC operation.
  '''
  return ((n & 0xF) << 4)

def ADC_TRIM(n):
  ''' Written to boot code.
  '''
  return ((n & 0xF) << 8)

class ADC_CHANNEL_SELECTION:
  '''Channel Selection.
  '''
  # Channel 0
  ADC_CHANNEL_0 = 0
  # Channel 1
  ADC_CHANNEL_1 = 1
  # Channel 2
  ADC_CHANNEL_2 = 2
  # Channel 3
  ADC_CHANNEL_3 = 3
  # Channel 4
  ADC_CHANNEL_4 = 4
  # Channel 5
  ADC_CHANNEL_5 = 5
  # Channel 6
  ADC_CHANNEL_6 = 6
  # Channel 7
  ADC_CHANNEL_7 = 7

class ADC_START_OPT:
  '''Type of start option.
  '''
  # Continuous mode
  ADC_START_CONTINUOUS =0
  # Start conversion now
  ADC_START_NOW = 1
  # Start conversion when the edge selected by bit 27 occurs on P2.10/EINT0
  ADC_START_ON_EINT0 = 2
  # Start conversion when the edge selected by bit 27 occurs on P1.27/CAP0.1
  ADC_START_ON_CAP01 = 3
  # Start conversion when the edge selected by bit 27 occurs on MAT0.1
  ADC_START_ON_MAT01 = 4
  # Start conversion when the edge selected by bit 27 occurs on MAT0.3
  ADC_START_ON_MAT03 = 5
  # Start conversion when the edge selected by bit 27 occurs on MAT1.0
  ADC_START_ON_MAT10 = 6
  # Start conversion when the edge selected by bit 27 occurs on MAT1.1
  ADC_START_ON_MAT11 = 7

class ADC_TYPE_INT_OPT:
  '''Type of edge when start conversion on the selected CAP/MAT signal.
  '''
  # Interrupt channel 0
  ADC_ADINTEN0 = 0
  # Interrupt channel 1
  ADC_ADINTEN1 = 1
  # Interrupt channel 2
  ADC_ADINTEN2 = 2
  # Interrupt channel 3
  ADC_ADINTEN3 = 3
  # Interrupt channel 4
  ADC_ADINTEN4 = 4
  # Interrupt channel 5
  ADC_ADINTEN5 = 5
  # Interrupt channel 6
  ADC_ADINTEN6 = 6
  # Interrupt channel 7
  ADC_ADINTEN7 = 7
  # Individual channel/global flag done generate an interrupt
  ADC_ADGINTEN = 8

class ADC_START_ON_EDGE_OPT:
  '''Type of edge when start conversion on the selected CAP/MAT signal.
  '''
  # Start conversion on a rising edge on the selected CAP/MAT signal
  ADC_START_ON_RISING = 0
  # Start conversion on a falling edge on the selected CAP/MAT signal
  ADC_START_ON_FALLING = 1

class ADC_DATA_STATUS:
  '''ADC Data  status.
  '''
  # Burst bit
  ADC_DATA_BURST = 0
  # Done bit
  ADC_DATA_DONE = 1

def ADC_ChannelGetStatus(ADCx, channel, StatusType):
  '''Get ADC Channel status from ADC data register.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  channel: channel number, should be 0..7
  StatusType:  0:Burst status, 1:Done status
  return: SET / RESET
  
  '''
  return robocaller("ADC_ChannelGetStatus", "FlagStatus", ADCx, channel, StatusType)

def ADC_GlobalGetData(ADCx):
  '''Get ADC Data from AD Global register.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  return: Result of conversion
  
  '''
  return robocaller("ADC_GlobalGetData", "uint32_t", ADCx)

def ADC_Init(ADCx, rate):
  '''Initialize ADC.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  rate: ADC conversion rate, should be <=200KHz
  
  '''
  return robocaller("ADC_Init", "void", ADCx, rate)

def ADC_ChannelCmd(ADCx, Channel, NewState):
  '''Enable/Disable ADC channel number.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  Channel: channel number
  NewState: Enable or Disable
  
  '''
  return robocaller("ADC_ChannelCmd", "void", ADCx, Channel, NewState)

def ADC_GlobalGetStatus(ADCx, StatusType):
  '''Get ADC Chanel status from AD global data register.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  StatusType:  0:Burst status, 1:Done status
  return: SET / RESET
  
  '''
  return robocaller("ADC_GlobalGetStatus", "FlagStatus", ADCx, StatusType)

def ADC_EdgeStartConfig(ADCx, EdgeOption):
  ''' Set Edge start configuration.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  EdgeOption: ADC_START_ON_RISING and ADC_START_ON_FALLING
  
  '''
  return robocaller("ADC_EdgeStartConfig", "void", ADCx, EdgeOption)

def ADC_ChannelGetData(ADCx, channel):
  '''Get ADC result.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  channel: channel number, should be 0...7
  return: Data conversion
  
  '''
  return robocaller("ADC_ChannelGetData", "uint16_t", ADCx, channel)

def ADC_DeInit(ADCx):
  '''Close ADC.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  
  '''
  return robocaller("ADC_DeInit", "void", ADCx)

def ADC_BurstCmd(ADCx, NewState):
  '''ADC Burst mode setting.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  NewState:  0:Reset Burst mode, 1:Set Burst mode
  
  '''
  return robocaller("ADC_BurstCmd", "void", ADCx, NewState)

def ADC_PowerdownCmd(ADCx, NewState):
  '''Set AD conversion in power mode.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  NewState: 1: AD converter is optional, 0: AD Converter is in power down mode
  
  '''
  return robocaller("ADC_PowerdownCmd", "void", ADCx, NewState)

def ADC_StartCmd(ADCx, start_mode):
  '''Set start mode for ADC
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  start_mode: one of modes in 'ADC_START_OPT' class
  
  '''
  return robocaller("ADC_StartCmd", "void", ADCx, start_mode)

def ADC_IntConfig(ADCx, IntType, NewState):
  '''ADC interrupt configuration.
  
  ADCx: pointer to LPC_ADC_TypeDef, should be: LPC_ADC
  IntType: one of interrupt types in 'ADC_TYPE_INT_OPT' class
  NewState: SET : enable ADC interrupt, RESET: disable ADC interrupt
  
  '''
  return robocaller("ADC_IntConfig", "void", ADCx, IntType, NewState)

