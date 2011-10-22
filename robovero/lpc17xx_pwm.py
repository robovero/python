"""PWM client library functions. Find implementation details in LPC17xx 
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

def PWM_IR_PWMMRn(n):
  '''Interrupt flag for PWM match channel for 6 channel.
  '''
  if (n<4): return (1<<n)
  else: return (1<<(n+4))
  
def PWM_IR_PWMCAPn(n):
  '''Interrupt flag for capture input.
  '''
  return ((1<<(n+4)))

class PWM_MATCHCFG_Type(cstruct):
  '''PWM Match channel configuration structure.
  
  MatchChannel: Match channel, should be in range from 0..6
  IntOnMatch: Interrupt On match, should be:
              - ENABLE: Enable this function.
              - DISABLE: Disable this function.
  StopOnMatch:  Stop On match, should be:
                - ENABLE: Enable this function.
                - DISABLE: Disable this function.
  ResetOnMatch: Reset On match, should be:
                - ENABLE: Enable this function.
                - DISABLE: Disable this function.
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class PWM_TIMER_PRESCALE_OPT:
  '''PWM Timer/Counter prescale option.
  
  PWM_TIMER_PRESCALE_TICKVAL: Prescale in absolute value
  PWM_TIMER_PRESCALE_USVAL: Prescale in microsecond value
  
  '''
  PWM_TIMER_PRESCALE_TICKVAL = 0
  PWM_TIMER_PRESCALE_USVAL = 1

class PWM_TC_MODE_OPT:
  '''PMW TC mode select option.
  
  PWM_MODE_TIMER: PWM using Timer mode
  PWM_MODE_COUNTER: PWM using Counter mode
  
  '''
  PWM_MODE_TIMER = 0
  PWM_MODE_COUNTER = 1

class PWM_TIMERCFG_Type(cstruct):
  '''Configuration structure in PWM TIMER mode.

  PrescaleOption: Prescale option, should be:
                  - PWM_TIMER_PRESCALE_TICKVAL: Prescale in absolute value
                  - PWM_TIMER_PRESCALE_USVAL: Prescale in microsecond value
  PrescaleValue:  Prescale value, 32-bit long, should be matched with
                  PrescaleOption
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class PWM_MATCH_UPDATE_OPT:
  '''PWM update type.
  
  PWM_MATCH_UPDATE_NOW: PWM Match Channel Update Now
  PWM_MATCH_UPDATE_NEXT_RST:  PWM Match Channel Update on next PWM Counter
                              resetting
  
  '''
  PWM_MATCH_UPDATE_NOW = 0
  PWM_MATCH_UPDATE_NEXT_RST = 1

class PWM_INTSTAT_TYPE:
  '''PWM Interrupt status type.
  
  PWM_INTSTAT_MR0:  Interrupt flag for PWM match channel 0
  PWM_INTSTAT_MR1:  Interrupt flag for PWM match channel 1
  PWM_INTSTAT_MR2:  Interrupt flag for PWM match channel 2
  PWM_INTSTAT_MR3:  Interrupt flag for PWM match channel 3
  PWM_INTSTAT_CAP0: Interrupt flag for capture input 0
  PWM_INTSTAT_CAP1: Interrupt flag for capture input 1
  PWM_INTSTAT_MR4:  Interrupt flag for PWM match channel 4
  PWM_INTSTAT_MR6:  Interrupt flag for PWM match channel 5
  PWM_INTSTAT_MR5:  Interrupt flag for PWM match channel 6
    
  '''
  PWM_INTSTAT_MR0 = PWM_IR_PWMMRn(0)
  PWM_INTSTAT_MR1 = PWM_IR_PWMMRn(1)
  PWM_INTSTAT_MR2 = PWM_IR_PWMMRn(2)
  PWM_INTSTAT_MR3 = PWM_IR_PWMMRn(3)
  PWM_INTSTAT_CAP0 = PWM_IR_PWMCAPn(0)
  PWM_INTSTAT_CAP1 = PWM_IR_PWMCAPn(1)
  PWM_INTSTAT_MR4 = PWM_IR_PWMMRn(4)
  PWM_INTSTAT_MR6 = PWM_IR_PWMMRn(5)
  PWM_INTSTAT_MR5 = PWM_IR_PWMMRn(6)

class PWM_COUNTER_EDGE_OPT:
  '''PWM Input Edge Option in counter mode.
  
  PWM_COUNTER_RISING: Rising edge mode
  PWM_COUNTER_FALLING:  Falling edge mode
  PWM_COUNTER_ANY:  Both rising and falling mode
  
  '''
  PWM_COUNTER_RISING = 1
  PWM_COUNTER_FALLING = 2
  PWM_COUNTER_ANY = 3

class PWM_CAPTURECFG_Type(cstruct):
  '''PWM Capture Input configuration structure.
  
   CaptureChannel: Capture channel, should be in range from 0..1
  RisingEdge: caption rising edge, should be:
              - ENABLE: Enable rising edge.
              - DISABLE: Disable this function.
  FallingEdge:  caption falling edge, should be:
                - ENABLE: Enable falling edge.
                - DISABLE: Disable this function.
  IntOnCaption: Interrupt On caption, should be:
                - ENABLE: Enable interrupt function.
                - DISABLE: Disable this function.
   ptr: LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class PWM_COUNTERCFG_Type(cstruct):
  '''Configuration structure in PWM COUNTER mode.
  
  CounterOption:  Counter Option, should be:
                  - PWM_COUNTER_RISING: Rising Edge
                  - PWM_COUNTER_FALLING: Falling Edge
                  - PWM_COUNTER_ANY: Both rising and falling mode
  CountInputSelect: Counter input select, should be:
                    - PWM_COUNTER_PCAP1_0: PWM Counter input selected is 
                      PCAP1.0 pin
                    - PWM_COUNTER_PCAP1_1: PWM Counter input selected is 
                      PCAP1.1 pin
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class PWM_CHANNEL_EDGE_OPT:
  '''PWM operating mode options.
  
  PWM_CHANNEL_SINGLE_EDGE: PWM Channel Single edge mode
  PWM_CHANNEL_DUAL_EDGE: PWM Channel Dual edge mode
  
  '''
  PWM_CHANNEL_SINGLE_EDGE = 0
  PWM_CHANNEL_DUAL_EDGE = 1

class PWM_COUNTER_INPUTSEL_OPT:
  '''PWM Input Select in counter mode.
  
   PWM_COUNTER_PCAP1_0:  PWM Counter input selected is PCAP1.0 pin
  PWM_COUNTER_PCAP1_1:  PWM counter input selected is CAP1.1 pin
   
  '''
  PWM_COUNTER_PCAP1_0 = 0
  PWM_COUNTER_PCAP1_1 = 1

def PWM_DeInit(PWMx):
  '''De-initializes the PWM peripheral registers to their default reset values.
  
  PWMx: PWM peripheral, should be LPC_PWM1 
  
  '''
  return robocaller("PWM_DeInit", "void", PWMx)

def PWM_GetCaptureValue(PWMx, CaptureChannel):
  '''Read value of capture register PWM peripheral.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  CaptureChannel: capture channel number, should be in range 0 to 1
  return: Value of capture register
  
  '''
  return robocaller("PWM_GetCaptureValue", "uint32_t", PWMx, CaptureChannel)

def PWM_ConfigStructInit(PWMTimerCounterMode, PWM_InitStruct):
  '''Fills each PWM_InitStruct member with its default value.
  
  If PWMCounterMode = PWM_MODE_TIMER:
  - PrescaleOption = PWM_TIMER_PRESCALE_USVAL
  - PrescaleValue = 1
  If PWMCounterMode = PWM_MODE_COUNTER:
  - CountInputSelect = PWM_COUNTER_PCAP1_0
  - CounterOption = PWM_COUNTER_RISING
  
  PWMTimerCounterMode:  Timer or Counter mode, should be:
                        - PWM_MODE_TIMER: Counter of PWM peripheral is in Timer
                          mode
                        - PWM_MODE_COUNTER: Counter of PWM peripheral is in
                          Counter mode
  PWM_InitStruct: Pointer to structure (PWM_TIMERCFG_Type or 
                  PWM_COUNTERCFG_Type) which will be initialized.
  
  '''
  return robocaller("PWM_ConfigStructInit", "void", PWMTimerCounterMode, PWM_InitStruct)

def PWM_ChannelCmd(PWMx, PWMChannel, NewState):
  '''Enable/Disable PWM channel output.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  PWMChannel: PWM channel, should be in range from 1 to 6
  NewState: New State of this function, should be:
            - ENABLE: Enable this PWM channel output
            - DISABLE: Disable this PWM channel output            
  
  '''
  return robocaller("PWM_ChannelCmd", "void", PWMx, PWMChannel, NewState)

def PWM_ConfigCapture(PWMx, PWM_CaptureConfigStruct):
  '''Configures capture input for PWM peripheral.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  PWM_CaptureConfigStruct:  Pointer to a PWM_CAPTURECFG_Type structure that
                            contains the configuration information for the
                            specified PWM capture input function.
  
  '''
  return robocaller("PWM_ConfigCapture", "void", PWMx, PWM_CaptureConfigStruct)

def PWM_GetIntStatus(PWMx, IntFlag):
  '''Check whether specified interrupt flag in PWM is set or not.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  IntFlag:  PWM interrupt flag, should be:
            - PWM_INTSTAT_MR0: Interrupt flag for PWM match channel 0
            - PWM_INTSTAT_MR1: Interrupt flag for PWM match channel 1
            - PWM_INTSTAT_MR2: Interrupt flag for PWM match channel 2
            - PWM_INTSTAT_MR3: Interrupt flag for PWM match channel 3
            - PWM_INTSTAT_MR4: Interrupt flag for PWM match channel 4
            - PWM_INTSTAT_MR5: Interrupt flag for PWM match channel 5
            - PWM_INTSTAT_MR6: Interrupt flag for PWM match channel 6
            - PWM_INTSTAT_CAP0: Interrupt flag for capture input 0
            - PWM_INTSTAT_CAP1: Interrupt flag for capture input 1            
  return: New State of PWM interrupt flag (SET or RESET)
  
  '''
  return robocaller("PWM_GetIntStatus", "IntStatus", PWMx, IntFlag)

def PWM_ChannelConfig(PWMx, PWMChannel, ModeOption):
  '''Configure Edge mode for each PWM channel.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  PWMChannel: PWM channel, should be in range from 2 to 6
  ModeOption: ModeOption PWM mode option, should be:
              - PWM_CHANNEL_SINGLE_EDGE: Single Edge mode
              - PWM_CHANNEL_DUAL_EDGE: Dual Edge mode
  
  '''
  return robocaller("PWM_ChannelConfig", "void", PWMx, PWMChannel, ModeOption)

def PWM_Init(PWMx, PWMTimerCounterMode, PWM_ConfigStruct):
  '''Initializes the PWMx peripheral corresponding to the specified parameters
  in the PWM_ConfigStruct.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  PWMTimerCounterMode:  Timer or Counter mode, should be:
                        - PWM_MODE_TIMER: Counter of PWM peripheral is in Timer
                          mode
                        - PWM_MODE_COUNTER: Counter of PWM peripheral is in
                          Counter mode
  PWM_ConfigStruct: Pointer to structure (PWM_TIMERCFG_Type or 
                    PWM_COUNTERCFG_Type) which will be initialized.
  
  '''
  return robocaller("PWM_Init", "void", PWMx, PWMTimerCounterMode, PWM_ConfigStruct)

def PWM_MatchUpdate(PWMx, MatchChannel, MatchValue, UpdateType):
  '''Update value for each PWM channel with update type option.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  MatchChannel: Match channel
  MatchValue: Match value
  UpdateType: Type of Update, should be:
              - PWM_MATCH_UPDATE_NOW: The update value will be updated for
                this channel immediately
              - PWM_MATCH_UPDATE_NEXT_RST: The update value will be updated for
                this channel on next reset by a PWM Match event.
  
  '''
  return robocaller("PWM_MatchUpdate", "void", PWMx, MatchChannel, MatchValue, UpdateType)

def PWM_ConfigMatch(PWMx, PWM_MatchConfigStruct):
  '''Configures match for PWM peripheral.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  PWM_MatchConfigStruct:  Pointer to a PWM_MATCHCFG_Type structure that contains
                          the configuration information for the specified PWM 
                          match function.
  
  '''
  return robocaller("PWM_ConfigMatch", "void", PWMx, PWM_MatchConfigStruct)

def PWM_ResetCounter(PWMx):
  '''Reset Counter in PWM peripheral.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  
  '''
  return robocaller("PWM_ResetCounter", "void", PWMx)

def PWM_CounterCmd(PWMx, NewState):
  '''Enable/Disable Counter in PWM peripheral.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  NewState: New State of this function, should be:
            - ENABLE: Enable Counter in PWM peripheral
            - DISABLE: Disable Counter in PWM peripheral
            
  '''
  return robocaller("PWM_CounterCmd", "void", PWMx, NewState)

def PWM_Cmd(PWMx, NewState):
  '''Enable/Disable PWM peripheral.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  NewState: New State of this function, should be:
            - ENABLE: Enable Counter in PWM peripheral
            - DISABLE: Disable Counter in PWM peripheral
            
  '''
  return robocaller("PWM_Cmd", "void", PWMx, NewState)

def PWM_ClearIntPending(PWMx, IntFlag):
  '''Clear specified PWM Interrupt pending.
  
  PWMx: PWM peripheral, should be LPC_PWM1
  IntFlag:  PWM interrupt flag, should be:
            - PWM_INTSTAT_MR0: Interrupt flag for PWM match channel 0
            - PWM_INTSTAT_MR1: Interrupt flag for PWM match channel 1
            - PWM_INTSTAT_MR2: Interrupt flag for PWM match channel 2
            - PWM_INTSTAT_MR3: Interrupt flag for PWM match channel 3
            - PWM_INTSTAT_MR4: Interrupt flag for PWM match channel 4
            - PWM_INTSTAT_MR5: Interrupt flag for PWM match channel 5
            - PWM_INTSTAT_MR6: Interrupt flag for PWM match channel 6
            - PWM_INTSTAT_CAP0: Interrupt flag for capture input 0
            - PWM_INTSTAT_CAP1: Interrupt flag for capture input 1

  '''
  return robocaller("PWM_ClearIntPending", "void", PWMx, IntFlag)

