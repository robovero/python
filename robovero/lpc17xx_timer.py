"""Timer client library functions. See LPC17xx CMSIS-Compliant Standard
Peripheral Firmware Driver Library documentation."""
from internals import robocaller, cstruct
from lpc_types import _BIT, _SBF

def TIM_IR_CLR(n):
	return _BIT(n)

def TIM_MATCH_INT(n):
	return (_BIT(n & 0x0F))

def TIM_CAP_INT(n):
	return (_BIT((n & 0x0F) + 4))

TIM_ENABLE = (1<<0)
TIM_RESET = (1<<1)
TIM_TCR_MASKBIT = (3)

def TIM_INT_ON_MATCH(n):
	return (_BIT(n * 3))

def TIM_RESET_ON_MATCH(n):
	return (_BIT((n * 3) + 1))

def TIM_STOP_ON_MATCH(n):
	return (_BIT((n * 3) + 2))

TIM_MCR_MASKBIT = (0x0FFF)

def TIM_MCR_CHANNEL_MASKBIT(n):
	return (7<<(n*3))

def TIM_CAP_RISING(n):
	return (_BIT(n * 3))

def TIM_CAP_FALLING(n):
	return (_BIT((n * 3) + 1))

def TIM_INT_ON_CAP(n):
	return (_BIT((n * 3) + 2))

def TIM_EDGE_MASK(n):
	return (_SBF((n * 3), 0x03))

TIM_CCR_MASKBIT = (0x3F)

def TIM_CCR_CHANNEL_MASKBIT(n):
	return (7<<(n*3))

def TIM_EM(n):
	return _BIT(n)

TIM_EM_NOTHING = (0x0)
TIM_EM_LOW = (0x1)
TIM_EM_HIGH = (0x2)
TIM_EM_TOGGLE = (0x3)

def TIM_EM_SET(n,s):	
	return (_SBF(((n << 1) + 4), (s & 0x03)))

def TIM_EM_MASK(n):
	return (_SBF(((n << 1) + 4), 0x03))

TIM_EMR_MASKBIT = 0x0FFF
TIM_CTCR_MODE_MASK = 0x3
TIM_CTCR_INPUT_MASK = 0xC
TIM_CTCR_MASKBIT = 0xF
TIM_COUNTER_MODE = (1)

def PARAM_TIMx(n):
	return (
		(n)==(LPC_TIM0)) or ((n)==(LPC_TIM1) 
		or (n)==(LPC_TIM2)) or ((n)==(LPC_TIM3)
		)

def PARAM_TIM_INT_TYPE(TYPE):
	return (
		(TYPE ==TIM_MR0_INT)or(TYPE ==TIM_MR1_INT)
		or(TYPE ==TIM_MR2_INT)or(TYPE ==TIM_MR3_INT)
		or(TYPE ==TIM_CR0_INT)or(TYPE ==TIM_CR1_INT)
		)

def PARAM_TIM_MODE_OPT(MODE):
	return (
		(MODE == TIM_TIMER_MODE)
		or (MODE == TIM_COUNTER_RISING_MODE)
		or (MODE == TIM_COUNTER_RISING_MODE)
		or (MODE == TIM_COUNTER_RISING_MODE)
		)

def PARAM_TIM_PRESCALE_OPT(OPT):
	return ((OPT == TIM_PRESCALE_TICKVAL) or (OPT == TIM_PRESCALE_USVAL))

def PARAM_TIM_COUNTER_INPUT_OPT(OPT):
	return (OPT == TIM_COUNTER_INCAP0) or (OPT == TIM_COUNTER_INCAP1)

def PARAM_TIM_EXTMATCH_OPT(OPT):
	return (
		(OPT == TIM_EXTMATCH_NOTHING) or (OPT == TIM_EXTMATCH_LOW)
		or (OPT == TIM_EXTMATCH_HIGH) or (OPT == TIM_EXTMATCH_TOGGLE)
		)
	
def PARAM_TIM_CAP_MODE_OPT(OPT):
	return (
		(OPT == TIM_CAPTURE_NONE) or (OPT == TIM_CAPTURE_RISING) 
		or (OPT == TIM_CAPTURE_FALLING) or (OPT == TIM_CAPTURE_ANY)
		)

class TIM_EXTMATCH_OPT:
	TIM_EXTMATCH_NOTHING = 0
	TIM_EXTMATCH_LOW = 1
	TIM_EXTMATCH_HIGH = 2
	TIM_EXTMATCH_TOGGLE = 3

class TIM_MODE_OPT:
	TIM_TIMER_MODE = 0
	TIM_COUNTER_RISING_MODE = 1
	TIM_COUNTER_FALLING_MODE = 2
	TIM_COUNTER_ANY_MODE = 3

class TIM_CAP_MODE_OPT:
	TIM_CAPTURE_NONE = 0
	TIM_CAPTURE_RISING = 1
	TIM_CAPTURE_FALLING = 2
	TIM_CAPTURE_ANY = 3

class TIM_CAPTURECFG_Type(cstruct):
	pass

class TIM_INT_TYPE:
	TIM_MR0_INT =0
	TIM_MR1_INT =1
	TIM_MR2_INT =2
	TIM_MR3_INT =3
	TIM_CR0_INT =4
	TIM_CR1_INT =5

class TIM_COUNTER_INPUT_OPT:
	TIM_COUNTER_INCAP0 = 0
	TIM_COUNTER_INCAP1 = 1

class TIM_MATCHCFG_Type(cstruct):
	pass

class TIM_COUNTERCFG_Type(cstruct):
	pass

class TIM_TIMERCFG_Type(cstruct):
	pass

class TIM_PRESCALE_OPT:
	TIM_PRESCALE_TICKVAL = 0
	TIM_PRESCALE_USVAL = 1

def TIM_GetIntCaptureStatus(TIMx, IntFlag):
	return robocaller("TIM_GetIntCaptureStatus", "FlagStatus", TIMx, IntFlag)

def TIM_ConfigMatch(TIMx, TIM_MatchConfigStruct):
	return robocaller("TIM_ConfigMatch", "void", TIMx, TIM_MatchConfigStruct)

def TIM_ClearIntCapturePending(TIMx, IntFlag):
	return robocaller("TIM_ClearIntCapturePending", "void", TIMx, IntFlag)

def TIM_SetMatchExt(TIMx, ext_match):
	return robocaller("TIM_SetMatchExt", "void", TIMx, ext_match)

def TIM_ConfigStructInit(TimerCounterMode, TIM_ConfigStruct):
	return robocaller("TIM_ConfigStructInit", "void", TimerCounterMode, TIM_ConfigStruct)

def TIM_GetIntStatus(TIMx, IntFlag):
	return robocaller("TIM_GetIntStatus", "FlagStatus", TIMx, IntFlag)

def TIM_Cmd(TIMx, NewState):
	return robocaller("TIM_Cmd", "void", TIMx, NewState)

def TIM_DeInit(TIMx):
	return robocaller("TIM_DeInit", "void", TIMx)

def TIM_ResetCounter(TIMx):
	return robocaller("TIM_ResetCounter", "void", TIMx)

def TIM_ConfigCapture(TIMx, TIM_CaptureConfigStruct):
	return robocaller("TIM_ConfigCapture", "void", TIMx, TIM_CaptureConfigStruct)

def TIM_GetCaptureValue(TIMx, CaptureChannel):
	return robocaller("TIM_GetCaptureValue", "uint32_t", TIMx, CaptureChannel)

def TIM_ClearIntPending(TIMx, IntFlag):
	return robocaller("TIM_ClearIntPending", "void", TIMx, IntFlag)

def TIM_UpdateMatchValue(TIMx, MatchChannel, MatchValue):
	return robocaller("TIM_UpdateMatchValue", "void", TIMx, MatchChannel, MatchValue)

def TIM_Init(TIMx, TimerCounterMode, TIM_ConfigStruct):
	return robocaller("TIM_Init", "void", TIMx, TimerCounterMode, TIM_ConfigStruct)

