"""Motor control PWM client library functions. Find implementation details in
LPC17xx CMSIS-Compliant Standard Peripheral Firmware Driver Library
documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

# Edge aligned mode for channel in MCPWM
MCPWM_CHANNEL_EDGE_MODE = ((0))
# Center aligned mode for channel in MCPWM
MCPWM_CHANNEL_CENTER_MODE = ((1))
# Polarity of the MCOA and MCOB pins: Passive state is LOW, active state is HIGH
MCPWM_CHANNEL_PASSIVE_LO = ((0))
# Polarity of the MCOA and MCOB pins: Passive state is HIGH, active state is LOW
MCPWM_CHANNEL_PASSIVE_HI = ((1))

# Output Patent in 3-phase DC mode, the internal MCOA0 signal is routed to any or all of
# the six output pins under the control of the bits in this register
# MCOA0 tracks internal MCOA0
MCPWM_PATENT_A0 = ((1<<0))  
# MCOB0 tracks internal MCOA0
MCPWM_PATENT_B0 = ((1<<1))  
# MCOA1 tracks internal MCOA0
MCPWM_PATENT_A1 = ((1<<2))  
# MCOB1 tracks internal MCOA0
MCPWM_PATENT_B1 = ((1<<3))  
# MCOA2 tracks internal MCOA0
MCPWM_PATENT_A2 = ((1<<4))  
# MCOB2 tracks internal MCOA0
MCPWM_PATENT_B2 = ((1<<5))

# Limit interrupt for channel (n)
def MCPWM_INT_ILIM(n):
  if ((n>=0)&(n<=2)):
    return (1<<((n*4)+0))
  else:
    return 0

# Match interrupt for channel (n)
def MCPWM_INT_IMAT(n):
  if ((n>=0)&(n<=2)):
    return (1<<((n*4)+1))
  else:
    return 0

# Capture interrupt for channel (n)
def MCPWM_INT_ICAP(n):
  if ((n>=0)&(n<=2)):
    return (1<<((n*4)+2))
  else:
    return 0
    
# Fast abort interrupt
MCPWM_INT_ABORT = (1<<15)

# Interrupt type in MCPWM
# Limit interrupt for channel (0)
MCPWM_INTFLAG_LIM0 = MCPWM_INT_ILIM(0)
# Match interrupt for channel (0)
MCPWM_INTFLAG_MAT0 = MCPWM_INT_IMAT(0)
# Capture interrupt for channel (0)
MCPWM_INTFLAG_CAP0 = MCPWM_INT_ICAP(0)
# Limit interrupt for channel (1)
MCPWM_INTFLAG_LIM1 = MCPWM_INT_ILIM(1)
# Match interrupt for channel (1) 
MCPWM_INTFLAG_MAT1 = MCPWM_INT_IMAT(1)
# Capture interrupt for channel (1)
MCPWM_INTFLAG_CAP1 = MCPWM_INT_ICAP(1)
# Limit interrupt for channel (2)
MCPWM_INTFLAG_LIM2 = MCPWM_INT_ILIM(2)
# Match interrupt for channel (2)
MCPWM_INTFLAG_MAT2 = MCPWM_INT_IMAT(2)
# Capture interrupt for channel (2)
MCPWM_INTFLAG_CAP2 = MCPWM_INT_ICAP(2)
# Fast abort interrupt
MCPWM_INTFLAG_ABORT = MCPWM_INT_ABORT

class MCPWM_CHANNEL_CFG_Type(cstruct):
  '''Motor Control PWM Channel Configuration structure type definition.
  
   channelType:  Edge/center aligned mode for this channel, should be:
                MCPWM_CHANNEL_EDGE_MODE: Channel is in Edge mode
                MCPWM_CHANNEL_CENTER_MODE: Channel is in Center mode
  channelPolarity:  Polarity of the MCOA and MCOB pins, should be:
                    MCPWM_CHANNEL_PASSIVE_LO: Passive state is LOW, active state
                    is HIGH
                    MCPWM_CHANNEL_PASSIVE_HI: Passive state is HIGH, active 
                    state is LOW
  channelDeadtimeEnable:  Enable/Disable DeadTime function for channel, should
                          be: ENABLE or DISABLE.
  channelDeadtimeValue: DeadTime value, should be less than 0x3FF
  channelUpdateEnable:  Enable/Disable updates of functional registers, should
                        be: ENABLE or DISABLE.
  channelTimercounterValue: MCPWM Timer Counter value
  channelPeriodValue:  MCPWM Period value
  channelPulsewidthValue:  MCPWM Pulse Width value
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class MCPWM_COUNT_CFG_Type(cstruct):
  '''MCPWM Count Control Configuration type definition.
  
  counterChannel: Counter Channel Number, should be in range from 0 to 2
  countRising:  Enable/Disable Capture on Rising Edge event, should be: ENABLE 
                or DISABLE.
  countFalling: Enable/Disable Capture on Falling Edge event, should be: ENABLE
                or DISABLE.
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class MCPWM_CAPTURE_CFG_Type(cstruct):
  '''MCPWM Capture Configuration type definition.
  
  captureChannel: Capture Channel Number, should be in range from 0 to 2 */
  captureRising:  Enable/Disable Capture on Rising Edge event, should be:
                  ENABLE or DISABLE.
  captureFalling: Enable/Disable Capture on Falling Edge event, should be:
                  ENABLE or DISABLE.
  timerReset: Enable/Disable Timer reset function an capture, should be:
              ENABLE or DISABLE.
  hnfEnable:  Enable/Disable Hardware noise filter function, should be:
              ENABLE or DISABLE.
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

def MCPWM_ConfigCapture(MCPWMx, channelNum, captureConfig):
  '''Configures capture function in MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  channelNum: MCI (Motor Control Input pin) number. Should be: 0..2
  captureConfig:  Pointer to a MCPWM_CAPTURE_CFG_Type structure that contains 
                  the configuration information for the specified MCPWM capture.
  
  '''
  return robocaller("MCPWM_ConfigCapture", "void", MCPWMx, channelNum, captureConfig)

def MCPWM_IntConfig(MCPWMx, ulIntType, NewState):
  '''Configures the specified interrupt in MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  ulIntType:  Interrupt type, should be:
              MCPWM_INTFLAG_LIM0: Limit interrupt for channel (0)
              MCPWM_INTFLAG_MAT0: Match interrupt for channel (0)
              MCPWM_INTFLAG_CAP0: Capture interrupt for channel (0)
              MCPWM_INTFLAG_LIM1: Limit interrupt for channel (1)
              MCPWM_INTFLAG_MAT1: Match interrupt for channel (1)
              MCPWM_INTFLAG_CAP1: Capture interrupt for channel (1)
              MCPWM_INTFLAG_LIM2: Limit interrupt for channel (2)
              MCPWM_INTFLAG_MAT2: Match interrupt for channel (2)
              MCPWM_INTFLAG_CAP2: Capture interrupt for channel (2)
              MCPWM_INTFLAG_ABORT: Fast abort interrupt  
  NewState: New State of this command, should be: ENABLE or DISABLE.
  
  '''
  return robocaller("MCPWM_IntConfig", "void", MCPWMx, ulIntType, NewState)

def MCPWM_ACMode(MCPWMx, acMode):
  '''Enables/Disables 3-phase AC motor mode on MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  acMode: State of this command, should be: ENABLE or DISABLE.
  
  '''
  return robocaller("MCPWM_ACMode", "void", MCPWMx, acMode)

def MCPWM_Init(MCPWMx):
  '''Initializes the MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  
  '''
  return robocaller("MCPWM_Init", "void", MCPWMx)

def MCPWM_GetIntStatus(MCPWMx, ulIntType):
  '''Check whether if the specified interrupt in MCPWM is set or not.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  ulIntType:  Interrupt type, should be:
              MCPWM_INTFLAG_LIM0: Limit interrupt for channel (0)
              MCPWM_INTFLAG_MAT0: Match interrupt for channel (0)
              MCPWM_INTFLAG_CAP0: Capture interrupt for channel (0)
              MCPWM_INTFLAG_LIM1: Limit interrupt for channel (1)
              MCPWM_INTFLAG_MAT1: Match interrupt for channel (1)
              MCPWM_INTFLAG_CAP1: Capture interrupt for channel (1)
              MCPWM_INTFLAG_LIM2: Limit interrupt for channel (2)
              MCPWM_INTFLAG_MAT2: Match interrupt for channel (2)
              MCPWM_INTFLAG_CAP2: Capture interrupt for channel (2)
              MCPWM_INTFLAG_ABORT: Fast abort interrupt 
  return: SET or RESET
  
  '''
  return robocaller("MCPWM_GetIntStatus", "FlagStatus", MCPWMx, ulIntType)

def MCPWM_Stop(MCPWMx, channel0, channel1, channel2):
  '''Stop MCPWM activity for each MCPWM channel.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  channel0: State of this command on channel 0:
            ENABLE: 'Stop' command will effect on channel 0
            DISABLE: 'Stop' command will not effect on channel 0
  channel1: State of this command on channel 1:
            ENABLE: 'Stop' command will effect on channel 1
            DISABLE: 'Stop' command will not effect on channel 1
  channel2: State of this command on channel 2:
            ENABLE: 'Stop' command will effect on channel 2
            DISABLE: 'Stop' command will not effect on channel 2
  
  '''
  return robocaller("MCPWM_Stop", "void", MCPWMx, channel0, channel1, channel2)

def MCPWM_Start(MCPWMx, channel0, channel1, channel2):
  '''Start MCPWM activity for each MCPWM channel.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  channel0: State of this command on channel 0:
            ENABLE: 'Start' command will effect on channel 0
            DISABLE: 'Start' command will not effect on channel 0
  channel1: State of this command on channel 1:
            ENABLE: 'Start' command will effect on channel 1
            DISABLE: 'Start' command will not effect on channel 1
  channel2: State of this command on channel 2:
            ENABLE: 'Start' command will effect on channel 2
            DISABLE: 'Start' command will not effect on channel 2 
  
  '''
  return robocaller("MCPWM_Start", "void", MCPWMx, channel0, channel1, channel2)

def MCPWM_GetCapture(MCPWMx, captureChannel):
  '''Get current captured value in specified capture channel.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  captureChannel: Capture channel number, should be: 0..2
  return: Captured value in channel 0, 1, or 2
    
  '''
  return robocaller("MCPWM_GetCapture", "uint32_t", MCPWMx, captureChannel)

def MCPWM_IntSet(MCPWMx, ulIntType):
  '''Sets/Forces the specified interrupt for MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  ulIntType:  Interrupt type, should be:
              MCPWM_INTFLAG_LIM0: Limit interrupt for channel (0)
              MCPWM_INTFLAG_MAT0: Match interrupt for channel (0)
              MCPWM_INTFLAG_CAP0: Capture interrupt for channel (0)
              MCPWM_INTFLAG_LIM1: Limit interrupt for channel (1)
              MCPWM_INTFLAG_MAT1: Match interrupt for channel (1)
              MCPWM_INTFLAG_CAP1: Capture interrupt for channel (1)
              MCPWM_INTFLAG_LIM2: Limit interrupt for channel (2)
              MCPWM_INTFLAG_MAT2: Match interrupt for channel (2)
              MCPWM_INTFLAG_CAP2: Capture interrupt for channel (2)
              MCPWM_INTFLAG_ABORT: Fast abort interrupt  
  
  '''
  return robocaller("MCPWM_IntSet", "void", MCPWMx, ulIntType)

def MCPWM_ConfigChannel(MCPWMx, channelNum, channelSetup):
  '''Configures each channel in MCPWM peripheral according to the specified
  parameters in the MCPWM_CHANNEL_CFG_Type.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  channelNum: Channel number, should be: 0..2.
  channelSetup: Pointer to a MCPWM_CHANNEL_CFG_Type structure that contains the
                configuration information for the specified MCPWM channel.
  
  '''
  return robocaller("MCPWM_ConfigChannel", "void", MCPWMx, channelNum, channelSetup)

def MCPWM_ClearCapture(MCPWMx, captureChannel):
  '''Clears current captured value in specified capture channel.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  captureChannel: Capture channel number, should be: 0..2
  
  '''
  return robocaller("MCPWM_ClearCapture", "void", MCPWMx, captureChannel)

def MCPWM_DCMode(MCPWMx, dcMode, outputInvered, outputPattern):
  '''Enables/Disables 3-phase DC motor mode on MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  dcMode: State of this command, should be: ENABLE or DISABLE.
  outputInvered:  Polarity of the MCOB outputs for all 3 channels, should be:
                  ENABLE: The MCOB outputs have opposite polarity from the MCOA
                  outputs.
                  DISABLE: The MCOB outputs have the same basic polarity as the 
                  MCOA outputs.
  outputPattern:  A value contains bits that enables/disables the specified 
                  output pins route to the internal MCOA0 signal, should be:
                  MCPWM_PATENT_A0:    MCOA0 tracks internal MCOA0
                  MCPWM_PATENT_B0:    MCOB0 tracks internal MCOA0
                  MCPWM_PATENT_A1:    MCOA1 tracks internal MCOA0
                  MCPWM_PATENT_B1:    MCOB1 tracks internal MCOA0
                  MCPWM_PATENT_A2:    MCOA2 tracks internal MCOA0
                  MCPWM_PATENT_B2:    MCOB2 tracks internal MCOA0
  
  '''
  return robocaller("MCPWM_DCMode", "void", MCPWMx, dcMode, outputInvered, outputPattern)

def MCPWM_CountConfig(MCPWMx, channelNum, countMode, countConfig):
  '''Configures Count control in MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  channelNum: Channel number, should be: 0..2
  countMode:  Count mode, should be:
              ENABLE: Enables count mode.
              DISABLE: Disable count mode, the channel is in timer mode.
  countConfig:  Pointer to a MCPWM_COUNT_CFG_Type structure that contains the
                configuration information for the specified MCPWM count control.
  
  '''
  return robocaller("MCPWM_CountConfig", "void", MCPWMx, channelNum, countMode, countConfig)

def MCPWM_WriteToShadow(MCPWMx, channelNum, channelSetup):
  '''Write to MCPWM shadow registers - Update the value for period and pulse
  width in MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  channelNum: Channel number, should be: 0..2
  channelSetup: Pointer to a MCPWM_CHANNEL_CFG_Type structure that contains the
                configuration information for the specified MCPWM channel.
  
  '''
  return robocaller("MCPWM_WriteToShadow", "void", MCPWMx, channelNum, channelSetup)

def MCPWM_IntClear(MCPWMx, ulIntType):
  '''Clear the specified interrupt pending for MCPWM peripheral.
  
  MCPWMx: Motor Control PWM peripheral selected. Should be: LPC_MCPWM
  ulIntType:  Interrupt type, should be:
              MCPWM_INTFLAG_LIM0: Limit interrupt for channel (0)
              MCPWM_INTFLAG_MAT0: Match interrupt for channel (0)
              MCPWM_INTFLAG_CAP0: Capture interrupt for channel (0)
              MCPWM_INTFLAG_LIM1: Limit interrupt for channel (1)
              MCPWM_INTFLAG_MAT1: Match interrupt for channel (1)
              MCPWM_INTFLAG_CAP1: Capture interrupt for channel (1)
              MCPWM_INTFLAG_LIM2: Limit interrupt for channel (2)
              MCPWM_INTFLAG_MAT2: Match interrupt for channel (2)
              MCPWM_INTFLAG_CAP2: Capture interrupt for channel (2)
              MCPWM_INTFLAG_ABORT: Fast abort interrupt   
  
  '''
  return robocaller("MCPWM_IntClear", "void", MCPWMx, ulIntType)

