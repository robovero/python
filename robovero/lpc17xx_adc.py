"""ADC client library functions. See LPC17xx CMSIS-Compliant Standard 
Peripheral Firmware Driver Library documentation."""
from internals import robocaller, cstruct

def ADC_CR_CH_SEL(n):
	return (1 << n)

def ADC_CR_CLKDIV(n):
	return (n << 8)

ADC_CR_BURST = (1 << 16)
ADC_CR_PDN = (1 << 21)
ADC_CR_START_MASK = (7 << 24)

def ADC_CR_START_MODE_SEL(SEL):
	return (SEL << 24)

ADC_CR_START_NOW = (1 << 24)
ADC_CR_START_EINT0 = (2 << 24)
ADC_CR_START_CAP01 = (3 << 24)
ADC_CR_START_MAT01 = (4 << 24)
ADC_CR_START_MAT03 = (5 << 24)
ADC_CR_START_MAT10 = (6 << 24)
ADC_CR_START_MAT11 = (7 << 24)
ADC_CR_EDGE = (1 << 27)

def ADC_GDR_RESULT(n):
	return ((n >> 4) & 0xFFF)

def ADC_GDR_CH(n):
	return ((n >> 24) & 0x7)

ADC_GDR_OVERRUN_FLAG	= (1 << 30)
ADC_GDR_DONE_FLAG = (1 << 31)
ADC_GDR_CH_MASK = (7 << 24)

def ADC_INTEN_CH(n):
	return (1 << n)

ADC_INTEN_GLOBAL = (1 << 8)

def ADC_DR_RESULT(n):
	return ((n >> 4) & 0xFFF)

ADC_DR_OVERRUN_FLAG = (1 << 30)
ADC_DR_DONE_FLAG = (1 << 31)

def ADC_STAT_CH_DONE_FLAG(n):
	return (n & 0xFF)

def ADC_STAT_CH_OVERRUN_FLAG(n):
	return ((n >> 8) & 0xFF)

ADC_STAT_INT_FLAG = (1 << 16)

def ADC_ADCOFFS(n):
	return ((n & 0xF) << 4)

def ADC_TRIM(n):
	return ((n & 0xF) << 8)

def PARAM_ADCx(n):
	return (n == LPC_ADC)

def PARAM_ADC_START_ON_EDGE_OPT(OPT):
	return ((OPT == ADC_START_ON_RISING) or (OPT == ADC_START_ON_FALLING))

def PARAM_ADC_DATA_STATUS(OPT):
	return ((OPT== ADC_DATA_BURST) or (OPT== ADC_DATA_DONE))

def PARAM_ADC_RATE(rate):
	return ((rate > 0) and (rate <= 200000))

def PARAM_ADC_CHANNEL_SELECTION(SEL):
	return (
		(SEL == ADC_CHANNEL_0) or (ADC_CHANNEL_1)
		or (SEL == ADC_CHANNEL_2) or (ADC_CHANNEL_3)
		or (SEL == ADC_CHANNEL_4) or (ADC_CHANNEL_5)
		or (SEL == ADC_CHANNEL_6) or (ADC_CHANNEL_7)
		)

def PARAM_ADC_START_OPT(OPT):
	return (
		(OPT == ADC_START_CONTINUOUS)or(OPT == ADC_START_NOW)
		or(OPT == ADC_START_ON_EINT0)or(OPT == ADC_START_ON_CAP01)
		or(OPT == ADC_START_ON_MAT01)or(OPT == ADC_START_ON_MAT03)
		or(OPT == ADC_START_ON_MAT10)or(OPT == ADC_START_ON_MAT11)
		)

def PARAM_ADC_TYPE_INT_OPT(OPT):
	return (
		(OPT == ADC_ADINTEN0) or (OPT == ADC_ADINTEN1)
		or (OPT == ADC_ADINTEN2) or (OPT == ADC_ADINTEN3)
		or (OPT == ADC_ADINTEN4) or (OPT == ADC_ADINTEN5)
		or (OPT == ADC_ADINTEN6) or (OPT == ADC_ADINTEN7)
		or (OPT == ADC_ADGINTEN)
		)

class ADC_CHANNEL_SELECTION:
	ADC_CHANNEL_0 = 0
	ADC_CHANNEL_1 = 1
	ADC_CHANNEL_2 = 2
	ADC_CHANNEL_3 = 3
	ADC_CHANNEL_4 = 4
	ADC_CHANNEL_5 = 5
	ADC_CHANNEL_6 = 6
	ADC_CHANNEL_7 = 7

class ADC_START_OPT:
	ADC_START_CONTINUOUS =0
	ADC_START_NOW = 1
	ADC_START_ON_EINT0 = 2
	ADC_START_ON_CAP01 = 3
	ADC_START_ON_MAT01 = 4
	ADC_START_ON_MAT03 = 5
	ADC_START_ON_MAT10 = 6
	ADC_START_ON_MAT11 = 7

class ADC_TYPE_INT_OPT:
	ADC_ADINTEN0 = 0
	ADC_ADINTEN1 = 1
	ADC_ADINTEN2 = 2
	ADC_ADINTEN3 = 3
	ADC_ADINTEN4 = 4
	ADC_ADINTEN5 = 5
	ADC_ADINTEN6 = 6
	ADC_ADINTEN7 = 7
	ADC_ADGINTEN = 8

class ADC_START_ON_EDGE_OPT:
	ADC_START_ON_RISING = 0
	ADC_START_ON_FALLING = 1

class ADC_DATA_STATUS:
	ADC_DATA_BURST = 0
	ADC_DATA_DONE = 1

def ADC_ChannelGetStatus(ADCx, channel, StatusType):
	return robocaller("ADC_ChannelGetStatus", "FlagStatus", ADCx, channel, StatusType)

def ADC_GlobalGetData(ADCx):
	return robocaller("ADC_GlobalGetData", "uint32_t", ADCx)

def ADC_Init(ADCx, rate):
	return robocaller("ADC_Init", "void", ADCx, rate)

def ADC_ChannelCmd(ADCx, Channel, NewState):
	return robocaller("ADC_ChannelCmd", "void", ADCx, Channel, NewState)

def ADC_GlobalGetStatus(ADCx, StatusType):
	return robocaller("ADC_GlobalGetStatus", "FlagStatus", ADCx, StatusType)

def ADC_EdgeStartConfig(ADCx, EdgeOption):
	return robocaller("ADC_EdgeStartConfig", "void", ADCx, EdgeOption)

def ADC_ChannelGetData(ADCx, channel):
	return robocaller("ADC_ChannelGetData", "uint16_t", ADCx, channel)

def ADC_DeInit(ADCx):
	return robocaller("ADC_DeInit", "void", ADCx)

def ADC_BurstCmd(ADCx, NewState):
	return robocaller("ADC_BurstCmd", "void", ADCx, NewState)

def ADC_PowerdownCmd(ADCx, NewState):
	return robocaller("ADC_PowerdownCmd", "void", ADCx, NewState)

def ADC_StartCmd(ADCx, start_mode):
	return robocaller("ADC_StartCmd", "void", ADCx, start_mode)

def ADC_IntConfig(ADCx, IntType, NewState):
	return robocaller("ADC_IntConfig", "void", ADCx, IntType, NewState)

