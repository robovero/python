"""DAC client library functions. See LPC17xx CMSIS-Compliant Standard
Peripheral Firmware Driver Library documentation."""
from internals import robocaller, cstruct

def DAC_VALUE(n):
	return (((n&0x3FF)<<6))

DAC_BIAS_EN = ((1<<16))

def DAC_CCNT_VALUE(n):
	return ((n&0xffff))
	
DAC_DBLBUF_ENA = ((1<<1))
DAC_CNT_ENA = ((1<<2))
DAC_DMA_ENA = ((1<<3))
DAC_DACCTRL_MASK = ((0x0F))

def PARAM_DACx(n):
	return ((n)==(LPC_DAC))

def PARAM_DAC_CURRENT_OPT(OPTION):
	return ((OPTION == DAC_MAX_CURRENT_700uA) or (OPTION == DAC_MAX_CURRENT_350uA))
	
class DAC_CONVERTER_CFG_Type(cstruct):
	pass

class DAC_CURRENT_OPT:
	DAC_MAX_CURRENT_700uA = 0
	DAC_MAX_CURRENT_350uA = 1

def DAC_SetBias(DACx, bias):
	return robocaller("DAC_SetBias", "void", DACx, bias)

def DAC_ConfigDAConverterControl(DACx, DAC_ConverterConfigStruct):
	return robocaller("DAC_ConfigDAConverterControl", "void", DACx, DAC_ConverterConfigStruct)

def DAC_UpdateValue(DACx, dac_value):
	return robocaller("DAC_UpdateValue", "void", DACx, dac_value)

def DAC_Init(DACx):
	return robocaller("DAC_Init", "void", DACx)

def DAC_SetDMATimeOut(DACx, time_out):
	return robocaller("DAC_SetDMATimeOut", "void", DACx, time_out)

