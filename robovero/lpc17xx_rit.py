"""Repetitive interrupt timer client library functions. See LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library
documentation."""
from internals import robocaller, cstruct
from lpc_types import _BIT

RIT_CTRL_INTEN = (1)
RIT_CTRL_ENCLR = _BIT(1)
RIT_CTRL_ENBR	= _BIT(2)
RIT_CTRL_TEN = _BIT(3)

def PARAM_RITx(n):
	return (n == LPC_RIT)

def RIT_DeInit(RITx):
	return robocaller("RIT_DeInit", "void", RITx)

def RIT_Init(RITx):
	return robocaller("RIT_Init", "void", RITx)

def RIT_Cmd(RITx, NewState):
	return robocaller("RIT_Cmd", "void", RITx, NewState)

def RIT_GetIntStatus(RITx):
	return robocaller("RIT_GetIntStatus", "IntStatus", RITx)

def RIT_TimerConfig(RITx, time_interval):
	return robocaller("RIT_TimerConfig", "void", RITx, time_interval)

def RIT_TimerClearCmd(RITx, NewState):
	return robocaller("RIT_TimerClearCmd", "void", RITx, NewState)

def RIT_TimerDebugCmd(RITx, NewState):
	return robocaller("RIT_TimerDebugCmd", "void", RITx, NewState)

