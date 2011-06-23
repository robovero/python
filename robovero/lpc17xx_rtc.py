"""RTC client library functions. See LPC17xx CMSIS-Compliant Standard 
Peripheral Firmware Driver Library documentation."""
from internals import robocaller, cstruct

class RTC_INT_OPT:
	RTC_INT_COUNTER_INCREASE = RTC_IRL_RTCCIF
	RTC_INT_ALARM = RTC_IRL_RTCALF

class RTC_TIME_Type(cstruct):
	pass

class RTC_TIMETYPE_Num:
	RTC_TIMETYPE_SECOND = 0
	RTC_TIMETYPE_MINUTE = 1
	RTC_TIMETYPE_HOUR = 2
	RTC_TIMETYPE_DAYOFWEEK = 3
	RTC_TIMETYPE_DAYOFMONTH = 4
	RTC_TIMETYPE_DAYOFYEAR = 5
	RTC_TIMETYPE_MONTH = 6
	RTC_TIMETYPE_YEAR = 7

def RTC_CntIncrIntConfig(RTCx, CntIncrIntType, NewState):
	return robocaller("RTC_CntIncrIntConfig", "void", RTCx, CntIncrIntType, NewState)

def RTC_ClearIntPending(RTCx, IntType):
	return robocaller("RTC_ClearIntPending", "void", RTCx, IntType)

def RTC_SetFullTime(RTCx, pFullTime):
	return robocaller("RTC_SetFullTime", "void", RTCx, pFullTime)

def RTC_SetAlarmTime(RTCx, Timetype, ALValue):
	return robocaller("RTC_SetAlarmTime", "void", RTCx, Timetype, ALValue)

def RTC_GetIntPending(RTCx, IntType):
	return robocaller("RTC_GetIntPending", "IntStatus", RTCx, IntType)

def RTC_SetTime(RTCx, Timetype, TimeValue):
	return robocaller("RTC_SetTime", "void", RTCx, Timetype, TimeValue)

def RTC_GetFullAlarmTime(RTCx, pFullTime):
	return robocaller("RTC_GetFullAlarmTime", "void", RTCx, pFullTime)

def RTC_DeInit(RTCx):
	return robocaller("RTC_DeInit", "void", RTCx)

def RTC_Init(RTCx):
	return robocaller("RTC_Init", "void", RTCx)

def RTC_ReadGPREG(RTCx, Channel):
	return robocaller("RTC_ReadGPREG", "uint32_t", RTCx, Channel)

def RTC_GetAlarmTime(RTCx, Timetype):
	return robocaller("RTC_GetAlarmTime", "uint32_t", RTCx, Timetype)

def RTC_AlarmIntConfig(RTCx, AlarmTimeType, NewState):
	return robocaller("RTC_AlarmIntConfig", "void", RTCx, AlarmTimeType, NewState)

def RTC_GetTime(RTCx, Timetype):
	return robocaller("RTC_GetTime", "uint32_t", RTCx, Timetype)

def RTC_CalibCounterCmd(RTCx, NewState):
	return robocaller("RTC_CalibCounterCmd", "void", RTCx, NewState)

def RTC_GetFullTime(RTCx, pFullTime):
	return robocaller("RTC_GetFullTime", "void", RTCx, pFullTime)

def RTC_CalibConfig(RTCx, CalibValue, CalibDir):
	return robocaller("RTC_CalibConfig", "void", RTCx, CalibValue, CalibDir)

def RTC_Cmd(RTCx, NewState):
	return robocaller("RTC_Cmd", "void", RTCx, NewState)

def RTC_SetFullAlarmTime(RTCx, pFullTime):
	return robocaller("RTC_SetFullAlarmTime", "void", RTCx, pFullTime)

def RTC_WriteGPREG(RTCx, Channel, Value):
	return robocaller("RTC_WriteGPREG", "void", RTCx, Channel, Value)

def RTC_ResetClockTickCounter(RTCx):
	return robocaller("RTC_ResetClockTickCounter", "void", RTCx)

