"""Watchdog client library functions. See LPC17xx CMSIS-Compliant
Standard Peripheral Firmware Driver Library documentation."""
from internals import robocaller

WDT_WDMOD_WDEN = ((1<<0))
WDT_WDMOD_WDRESET = ((1<<1))
WDT_WDMOD_WDTOF = ((1<<2))
WDT_WDMOD_WDINT = ((1<<3))

def WDT_WDMOD(n):
	return ((1<<1))

WDT_US_INDEX = ((1000000))
WDT_TIMEOUT_MIN = ((0xFF))
WDT_TIMEOUT_MAX = ((0xFFFFFFFF))
WDT_WDMOD_MASK = (0x02)
WDT_WDTC_MASK = (0xFFFFFFFF)
WDT_WDFEED_MASK = (0x000000FF)
WDT_WDCLKSEL_MASK = (0x03)
WDT_WDCLKSEL_RC = (0x00)
WDT_WDCLKSEL_PCLK = (0x01)
WDT_WDCLKSEL_RTC = (0x02)

def PARAM_WDT_CLK_OPT(OPTION):
	return (
		(OPTION ==WDT_CLKSRC_IRC)or(OPTION ==WDT_CLKSRC_IRC)
		or(OPTION ==WDT_CLKSRC_IRC)
		)

def PARAM_WDT_MODE_OPT(OPTION):
	return ((OPTION ==WDT_MODE_INT_ONLY)or(OPTION ==WDT_MODE_RESET))

class WDT_MODE_OPT:
	WDT_MODE_INT_ONLY = 0
	WDT_MODE_RESET = 1

class WDT_CLK_OPT:
	WDT_CLKSRC_IRC = 0
	WDT_CLKSRC_PCLK = 1
	WDT_CLKSRC_RTC = 2

def WDT_Start(TimeOut):
	return robocaller("WDT_Start", "void", TimeOut)

def WDT_ClrTimeOutFlag():
	return robocaller("WDT_ClrTimeOutFlag", "void")

def WDT_ReadTimeOutFlag():
	return robocaller("WDT_ReadTimeOutFlag", "FlagStatus")

def WDT_UpdateTimeOut(TimeOut):
	return robocaller("WDT_UpdateTimeOut", "void", TimeOut)

def WDT_Init(ClkSrc, WDTMode):
	return robocaller("WDT_Init", "void", ClkSrc, WDTMode)

def WDT_Feed():
	return robocaller("WDT_Feed", "void")

def WDT_GetCurrentCount():
	return robocaller("WDT_GetCurrentCount", "uint32_t")

