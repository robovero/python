"""PWM client library functions. See LPC17xx CMSIS-Compliant Standard 
Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

def PWM_IR_PWMMRn(n):
	if (n<4): return (1<<n)
	else: return (1<<(n+4))
  
def PWM_IR_PWMCAPn(n):
  return ((1<<(n+4)))
  
PWM_IR_BITMASK = ((0x0000073F))
PWM_TCR_BITMASK = ((0x0000000B))
PWM_TCR_COUNTER_ENABLE = ((1<<0)) 
PWM_TCR_COUNTER_RESET = ((1<<1)) 
PWM_TCR_PWM_ENABLE = ((1<<3)) 
PWM_CTCR_BITMASK = ((0x0000000F))

def PWM_CTCR_MODE(n):
  return ((n&0x03))
  
def PWM_CTCR_SELECT_INPUT(n):
  return (((n&0x03)<<2))
  
PWM_MCR_BITMASK = ((0x001FFFFF))

def PWM_MCR_INT_ON_MATCH(n):
  return ((1<<(((n&0x7)<<1)+(n&0x07))))
  
def PWM_MCR_RESET_ON_MATCH(n):
  return ((1<<(((n&0x7)<<1)+(n&0x07)+1)))
  
def PWM_MCR_STOP_ON_MATCH(n):
  return ((1<<(((n&0x7)<<1)+(n&0x07)+2)))
  
PWM_CCR_BITMASK = ((0x0000003F))

def PWM_CCR_CAP_RISING(n):
  return ((1<<(((n&0x2)<<1)+(n&0x1))))
  
def PWM_CCR_CAP_FALLING(n):
  return ((1<<(((n&0x2)<<1)+(n&0x1)+1)))
  
def PWM_CCR_INT_ON_CAP(n):
  return ((1<<(((n&0x2)<<1)+(n&0x1)+2)))
  
PWM_PCR_BITMASK = 0x00007E7C

def PWM_PCR_PWMSELn(n):
	if ((n&0x7)<2): return 0
	else: return (1<<n)
  
def PWM_PCR_PWMENAn(n):
  if ((n&0x7)<1): return 0
  else: return (1<<(n+8))
  
PWM_LER_BITMASK = ((0x0000007F))

def PWM_LER_EN_MATCHn_LATCH(n):
  if (n<7): return (1<<n)
  else: return 0
  
def PARAM_PWMx(n):
  return ((n)==(LPC_PWM1))
  
def PARAM_PWM1_MATCH_CHANNEL(n):
  return ((n>=0) and (n<=6))
  
def PARAM_PWM1_CHANNEL(n):
  return ((n>=1) and (n<=6))
  
def PARAM_PWM1_EDGE_MODE_CHANNEL(n):
  return ((n>=2) and (n<=6))
  
def PARAM_PWM1_CAPTURE_CHANNEL(n):
  return ((n==0) or (n==1))
  
def PARAM_PWM_INTSTAT(n):
	return (
		(n==PWM_INTSTAT_MR0) or (n==PWM_INTSTAT_MR1) or (n==PWM_INTSTAT_MR2) 
		or (n==PWM_INTSTAT_MR3) or (n==PWM_INTSTAT_MR4) or (n==PWM_INTSTAT_MR5) 
		or (n==PWM_INTSTAT_MR6) or (n==PWM_INTSTAT_CAP0) or (n==PWM_INTSTAT_CAP1)
		)

def PARAM_PWM_TC_MODE(n):
  return ((n==PWM_MODE_TIMER) or (n==PWM_MODE_COUNTER))
  
def PARAM_PWM_TIMER_PRESCALE(n):
  return ((n==PWM_TIMER_PRESCALE_TICKVAL) or (n==PWM_TIMER_PRESCALE_USVAL))
  
def PARAM_PWM_COUNTER_INPUTSEL(n):
  return ((n==PWM_COUNTER_PCAP1_0) or (n==PWM_COUNTER_PCAP1_1))
  
def PARAM_PWM_COUNTER_EDGE(n):
  return ((n==PWM_COUNTER_RISING) or (n==PWM_COUNTER_FALLING) or (n==PWM_COUNTER_ANY))

def PARAM_PWM_CHANNEL_EDGE(n):
  return ((n==PWM_CHANNEL_SINGLE_EDGE) or (n==PWM_CHANNEL_DUAL_EDGE))
  
def PARAM_PWM_MATCH_UPDATE(n):
  return ((n==PWM_MATCH_UPDATE_NOW) or (n==PWM_MATCH_UPDATE_NEXT_RST))

class PWM_MATCHCFG_Type(cstruct):
	pass

class PWM_TIMER_PRESCALE_OPT:
	PWM_TIMER_PRESCALE_TICKVAL = 0
	PWM_TIMER_PRESCALE_USVAL = 1

class PWM_TC_MODE_OPT:
	PWM_MODE_TIMER = 0
	PWM_MODE_COUNTER = 1

class PWM_TIMERCFG_Type(cstruct):
	pass

class PWM_MATCH_UPDATE_OPT:
	PWM_MATCH_UPDATE_NOW = 0
	PWM_MATCH_UPDATE_NEXT_RST = 1

class PWM_INTSTAT_TYPE:
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
	PWM_COUNTER_RISING = 1
	PWM_COUNTER_FALLING = 2
	PWM_COUNTER_ANY = 3

class PWM_CAPTURECFG_Type(cstruct):
	pass

class PWM_COUNTERCFG_Type(cstruct):
	pass

class PWM_CHANNEL_EDGE_OPT:
	PWM_CHANNEL_SINGLE_EDGE = 0
	PWM_CHANNEL_DUAL_EDGE = 1

class PWM_COUNTER_INPUTSEL_OPT:
	PWM_COUNTER_PCAP1_0 = 0
	PWM_COUNTER_PCAP1_1 = 1

def PWM_DeInit(PWMx):
	return robocaller("PWM_DeInit", "void", PWMx)

def PWM_PinConfig(PWMx, PWM_Channel, PinselOption):
	return robocaller("PWM_PinConfig", "void", PWMx, PWM_Channel, PinselOption)

def PWM_GetCaptureValue(PWMx, CaptureChannel):
	return robocaller("PWM_GetCaptureValue", "uint32_t", PWMx, CaptureChannel)

def PWM_ConfigStructInit(PWMTimerCounterMode, PWM_InitStruct):
	return robocaller("PWM_ConfigStructInit", "void", PWMTimerCounterMode, PWM_InitStruct)

def PWM_ChannelCmd(PWMx, PWMChannel, NewState):
	return robocaller("PWM_ChannelCmd", "void", PWMx, PWMChannel, NewState)

def PWM_ConfigCapture(PWMx, PWM_CaptureConfigStruct):
	return robocaller("PWM_ConfigCapture", "void", PWMx, PWM_CaptureConfigStruct)

def PWM_GetIntStatus(PWMx, IntFlag):
	return robocaller("PWM_GetIntStatus", "IntStatus", PWMx, IntFlag)

def PWM_ChannelConfig(PWMx, PWMChannel, ModeOption):
	return robocaller("PWM_ChannelConfig", "void", PWMx, PWMChannel, ModeOption)

def PWM_Init(PWMx, PWMTimerCounterMode, PWM_ConfigStruct):
	return robocaller("PWM_Init", "void", PWMx, PWMTimerCounterMode, PWM_ConfigStruct)

def PWM_MatchUpdate(PWMx, MatchChannel, MatchValue, UpdateType):
	return robocaller("PWM_MatchUpdate", "void", PWMx, MatchChannel, MatchValue, UpdateType)

def PWM_ConfigMatch(PWMx, PWM_MatchConfigStruct):
	return robocaller("PWM_ConfigMatch", "void", PWMx, PWM_MatchConfigStruct)

def PWM_ResetCounter(PWMx):
	return robocaller("PWM_ResetCounter", "void", PWMx)

def PWM_CounterCmd(PWMx, NewState):
	return robocaller("PWM_CounterCmd", "void", PWMx, NewState)

def PWM_Cmd(PWMx, NewState):
	return robocaller("PWM_Cmd", "void", PWMx, NewState)

def PWM_ClearIntPending(PWMx, IntFlag):
	return robocaller("PWM_ClearIntPending", "void", PWMx, IntFlag)

