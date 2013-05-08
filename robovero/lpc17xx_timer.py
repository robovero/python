"""Timer client library functions. Find implementation details in LPC17xx 
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

class TIM_EXTMATCH_OPT:
  '''Timer/Counter external match option.
  
  TIM_EXTMATCH_NOTHING: Do nothing for external output pin if match
  TIM_EXTMATCH_LOW: Force external output pin to low if match
  TIM_EXTMATCH_HIGH:  Force external output pin to high if match
  TIM_EXTMATCH_TOGGLE:  Toggle external output pin if match
  
  '''
  TIM_EXTMATCH_NOTHING = 0
  TIM_EXTMATCH_LOW = 1
  TIM_EXTMATCH_HIGH = 2
  TIM_EXTMATCH_TOGGLE = 3

class TIM_MODE_OPT:
  '''Timer/counter operating mode.
  
  TIM_TIMER_MODE: Timer mode
  TIM_COUNTER_RISING_MODE:  Counter rising mode
  TIM_COUNTER_FALLING_MODE: Counter falling mode
  TIM_COUNTER_ANY_MODE: Counter on both edges
  
  '''
  TIM_TIMER_MODE = 0
  TIM_COUNTER_RISING_MODE = 1
  TIM_COUNTER_FALLING_MODE = 2
  TIM_COUNTER_ANY_MODE = 3

class TIM_CAP_MODE_OPT:
  '''Timer/counter capture mode options.
  
  TIM_CAPTURE_NONE: No Capture
  TIM_CAPTURE_RISING: Rising capture mode
  TIM_CAPTURE_FALLING:  Falling capture mode
  TIM_CAPTURE_ANY:  On both edges
  
  '''
  TIM_CAPTURE_NONE = 0
  TIM_CAPTURE_RISING = 1
  TIM_CAPTURE_FALLING = 2
  TIM_CAPTURE_ANY = 3

class TIM_CAPTURECFG_Type(cstruct):
  '''Capture Input configuration structure.
  
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
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
  '''
  pass

class TIM_INT_TYPE:
  '''Interrupt type.
  
  TIM_MR0_INT:  interrupt for Match channel 0
  TIM_MR1_INT:  interrupt for Match channel 1
  TIM_MR2_INT:  interrupt for Match channel 2
  TIM_MR3_INT:  interrupt for Match channel 3
  TIM_CR0_INT:  interrupt for Capture channel 0
  TIM_CR1_INT:  interrupt for Capture channel 1
  
  '''
  TIM_MR0_INT =0
  TIM_MR1_INT =1
  TIM_MR2_INT =2
  TIM_MR3_INT =3
  TIM_CR0_INT =4
  TIM_CR1_INT =5

class TIM_COUNTER_INPUT_OPT:
  '''Counter input option.
  
  TIM_COUNTER_INCAP0: CAPn.0 input pin for TIMERn
  TIM_COUNTER_INCAP1: CAPn.1 input pin for TIMERn
  
  '''
  TIM_COUNTER_INCAP0 = 0
  TIM_COUNTER_INCAP1 = 1

class TIM_MATCHCFG_Type(cstruct):
  '''Match channel configuration structure.
  
  MatchChannel: Match channel, should be in range from 0..3
  IntOnMatch: Interrupt On match, should be:
              - ENABLE: Enable this function.
              - DISABLE: Disable this function.
  StopOnMatch:  Stop On match, should be:
              - ENABLE: Enable this function.
              - DISABLE: Disable this function.
  ResetOnMatch: Reset On match, should be:
              - ENABLE: Enable this function.
              - DISABLE: Disable this function.
  ExtMatchOutputType: External Match Output type, should be:
               -  TIM_EXTMATCH_NOTHING: Do nothing for external output pin if 
                  match
               -  TIM_EXTMATCH_LOW: Force external output pin to low if match
               -  TIM_EXTMATCH_HIGH: Force external output pin to high if match
               -  TIM_EXTMATCH_TOGGLE: Toggle external output pin if match.
  MatchValue: Match value
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class TIM_COUNTERCFG_Type(cstruct):
  '''Configuration structure in COUNTER mode.
  
  CounterOption:  Counter Option, should be:
                  - TIM_COUNTER_INCAP0: CAPn.0 input pin for TIMERn
                  - TIM_COUNTER_INCAP1: CAPn.1 input pin for TIMERn
  CountInputSelect
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&). 
  
  '''
  pass

class TIM_TIMERCFG_Type(cstruct):
  '''Configuration structure in TIMER mode. 
  
  PrescaleOption: Timer Prescale option, should be:
                  - TIM_PRESCALE_TICKVAL: Prescale in absolute value
                  - TIM_PRESCALE_USVAL: Prescale in microsecond value
  PrescaleValue:  Prescale value
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&). 
  
  '''
  pass

class TIM_PRESCALE_OPT:
  '''Timer/Counter prescale option. 
  
  TIM_PRESCALE_TICKVAL: Prescale in absolute value
  TIM_PRESCALE_USVAL: Prescale in microsecond value
  
  '''
  TIM_PRESCALE_TICKVAL = 0
  TIM_PRESCALE_USVAL = 1

def TIM_GetIntCaptureStatus(TIMx, IntFlag):
  '''Get Capture Interrupt Status.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  IntFlag:  interrupt type, should be:
            - TIM_MR0_INT: Interrupt for Match channel 0
            - TIM_MR1_INT: Interrupt for Match channel 1
            - TIM_MR2_INT: Interrupt for Match channel 2
            - TIM_MR3_INT: Interrupt for Match channel 3
            - TIM_CR0_INT: Interrupt for Capture channel 0
            - TIM_CR1_INT: Interrupt for Capture channel 1
  return: FlagStatus
          - SET : interrupt
          - RESET : no interrupt
  
  '''
  return robocaller("TIM_GetIntCaptureStatus", "FlagStatus", TIMx, IntFlag)

def TIM_ConfigMatch(TIMx, TIM_MatchConfigStruct):
  '''Configuration for Match register.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  TIM_MatchConfigStruct:  Pointer to TIM_MATCHCFG_Type
                          - MatchChannel: choose channel 0 or 1
                          - IntOnMatch: if SET, interrupt will be generated when
                            MRxx match the value in TC
                          - StopOnMatch:  if SET, TC and PC will be stopped 
                                          whenM Rxx match the value in TC
                          - ResetOnMatch: if SET, Reset on MR0 when MRxx match
                                          the value in TC
                          - ExtMatchOutputType: Select output for external match
                            0:  Do nothing for external output pin if match
                            1:  Force external output pin to low if match
                            2: Force external output pin to high if match
                            3: Toggle external output pin if match
                            MatchValue: Set the value to be compared with TC 
                                        value
  
  '''
  return robocaller("TIM_ConfigMatch", "void", TIMx, TIM_MatchConfigStruct)

def TIM_ClearIntCapturePending(TIMx, IntFlag):
  '''Clear Capture Interrupt pending.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  IntFlag:  interrupt type, should be:
            - TIM_MR0_INT: Interrupt for Match channel 0
            - TIM_MR1_INT: Interrupt for Match channel 1
            - TIM_MR2_INT: Interrupt for Match channel 2
            - TIM_MR3_INT: Interrupt for Match channel 3
            - TIM_CR0_INT: Interrupt for Capture channel 0
            - TIM_CR1_INT: Interrupt for Capture channel 1
  
  '''
  return robocaller("TIM_ClearIntCapturePending", "void", TIMx, IntFlag)

def TIM_ConfigStructInit(TimerCounterMode, TIM_ConfigStruct):
  '''Configuration for Timer at initial time.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  TIM_ConfigStruct: pointer to TIM_TIMERCFG_Type or TIM_COUNTERCFG_Type
        
  '''
  return robocaller("TIM_ConfigStructInit", "void", TimerCounterMode, TIM_ConfigStruct)

def TIM_GetIntStatus(TIMx, IntFlag):
  '''Get Interrupt Status.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  IntFlag:  interrupt type, should be:
            - TIM_MR0_INT: Interrupt for Match channel 0
            - TIM_MR1_INT: Interrupt for Match channel 1
            - TIM_MR2_INT: Interrupt for Match channel 2
            - TIM_MR3_INT: Interrupt for Match channel 3
            - TIM_CR0_INT: Interrupt for Capture channel 0
            - TIM_CR1_INT: Interrupt for Capture channel 1
  return: FlagStatus
          - SET : interrupt
          - RESET : no interrupt

  '''
  return robocaller("TIM_GetIntStatus", "FlagStatus", TIMx, IntFlag)

def TIM_Cmd(TIMx, NewState):
  '''Start/Stop Timer/Counter device.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  NewState: - ENABLE  : set timer enable
            - DISABLE : disable timer
  
  '''
  return robocaller("TIM_Cmd", "void", TIMx, NewState)

def TIM_DeInit(TIMx):
  '''Close Timer/Counter device.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral

  '''
  return robocaller("TIM_DeInit", "void", TIMx)

def TIM_ResetCounter(TIMx):
  '''Reset Timer/Counter device.
  
  Make TC and PC are synchronously reset on the next positive edge of PCLK
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral

  '''
  return robocaller("TIM_ResetCounter", "void", TIMx)

def TIM_ConfigCapture(TIMx, TIM_CaptureConfigStruct):
  '''Configuration for Capture register.

  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  TIM_CaptureConfigStruct:  Pointer to TIM_CAPTURECFG_Type
  
  '''
  return robocaller("TIM_ConfigCapture", "void", TIMx, TIM_CaptureConfigStruct)

def TIM_GetCaptureValue(TIMx, CaptureChannel):
  '''Read value of capture register in timer/counter device.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  CaptureChannel: capture channel number, should be:
                  - TIM_COUNTER_INCAP0: CAPn.0 input pin for TIMERn
                  - TIM_COUNTER_INCAP1: CAPn.1 input pin for TIMERn
  return: Value of capture register
  
  '''
  return robocaller("TIM_GetCaptureValue", "uint32_t", TIMx, CaptureChannel)

def TIM_ClearIntPending(TIMx, IntFlag):
  '''Clear Interrupt pending.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  IntFlag:  interrupt type, should be:
            - TIM_MR0_INT: Interrupt for Match channel 0
            - TIM_MR1_INT: Interrupt for Match channel 1
            - TIM_MR2_INT: Interrupt for Match channel 2
            - TIM_MR3_INT: Interrupt for Match channel 3
            - TIM_CR0_INT: Interrupt for Capture channel 0
            - TIM_CR1_INT: Interrupt for Capture channel 1
  
  '''
  return robocaller("TIM_ClearIntPending", "void", TIMx, IntFlag)

def TIM_UpdateMatchValue(TIMx, MatchChannel, MatchValue):
  '''Update Match value.
  
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  MatchChannel: Match channel, should be: 0..3
  MatchValue: updated match value
  
  '''
  return robocaller("TIM_UpdateMatchValue", "void", TIMx, MatchChannel, MatchValue)

def TIM_Init(TIMx, TimerCounterMode, TIM_ConfigStruct):
  '''Initialize Timer/Counter device.
    
  TIMx: Timer selection, should be:
        - LPC_TIM0: TIMER0 peripheral
        - LPC_TIM1: TIMER1 peripheral
        - LPC_TIM2: TIMER2 peripheral
        - LPC_TIM3: TIMER3 peripheral
  TimerCounterMode: Timer counter mode, should be:
                    - TIM_TIMER_MODE: Timer mode
                    - TIM_COUNTER_RISING_MODE: Counter rising mode
                    - TIM_COUNTER_FALLING_MODE: Counter falling mode
                    - TIM_COUNTER_ANY_MODE:Counter on both edges
  TIM_ConfigStruct: pointer to TIM_TIMERCFG_Type that contains the configuration
                    information for the specified Timer peripheral.
        
  '''
  return robocaller("TIM_Init", "void", TIMx, TimerCounterMode, TIM_ConfigStruct)
