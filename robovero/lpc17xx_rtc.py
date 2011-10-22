"""RTC client library functions. See LPC17xx CMSIS-Compliant Standard 
Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"


# ILR register definitions
# Bit inform the source interrupt is counter increment
RTC_IRL_RTCCIF = (1)
# Bit inform the source interrupt is alarm match
RTC_IRL_RTCALF = (2)


class RTC_INT_OPT:
  '''RTC interrupt source.
  
  RTC_INT_COUNTER_INCREASE: Counter Increment Interrupt
  RTC_INT_ALARM = RTC_IRL_RTCALF: The alarm interrupt
  
  '''
  RTC_INT_COUNTER_INCREASE = RTC_IRL_RTCCIF
  RTC_INT_ALARM = RTC_IRL_RTCALF

class RTC_TIME_Type(cstruct):
  '''Time structure definitions for simple manipulation.
  
  SEC:  Seconds Register
  MIN:  Minutes Register
  HOUR: Hours Register
  DOM:  Day of Month Register
  DOW:  Day of Week Register
  DOY:  Day of Year Register
  MONTH:  Months Register
  YEAR: Years Register
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
  the C reference operator (&).
  
  '''
  pass

class RTC_TIMETYPE_Num:
  '''RTC time type option.
  
  RTC_TIMETYPE_SECOND:  Second
  RTC_TIMETYPE_MINUTE:  Month
  RTC_TIMETYPE_HOUR:  Hour
  RTC_TIMETYPE_DAYOFWEEK: Day of week
  RTC_TIMETYPE_DAYOFMONTH:  Day of month
  RTC_TIMETYPE_DAYOFYEAR: Day of year
  RTC_TIMETYPE_MONTH: Month
  RTC_TIMETYPE_YEAR:  Year
  
  '''
  RTC_TIMETYPE_SECOND = 0
  RTC_TIMETYPE_MINUTE = 1
  RTC_TIMETYPE_HOUR = 2
  RTC_TIMETYPE_DAYOFWEEK = 3
  RTC_TIMETYPE_DAYOFMONTH = 4
  RTC_TIMETYPE_DAYOFYEAR = 5
  RTC_TIMETYPE_MONTH = 6
  RTC_TIMETYPE_YEAR = 7

def RTC_CntIncrIntConfig(RTCx, CntIncrIntType, NewState):
  '''Enable/Disable Counter increment interrupt for each time type in RTC 
  peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  CntIncrIntType: Counter Increment Interrupt type, an increment of the type 
                  value below will generates an interrupt, should be:
                  - RTC_TIMETYPE_SECOND
                  - RTC_TIMETYPE_MINUTE
                  - RTC_TIMETYPE_HOUR
                  - RTC_TIMETYPE_DAYOFWEEK
                  - RTC_TIMETYPE_DAYOFMONTH
                  - RTC_TIMETYPE_DAYOFYEAR
                  - RTC_TIMETYPE_MONTH
                  - RTC_TIMETYPE_YEAR                  
  NewState: New state of this function, should be:
            - ENABLE: Counter Increment interrupt for this time type are enabled
            - DISABLE: Counter Increment interrupt for this time type are 
              disabled                
                  
  '''
  return robocaller("RTC_CntIncrIntConfig", "void", RTCx, CntIncrIntType, NewState)

def RTC_ClearIntPending(RTCx, IntType):
  '''Clear specified Location interrupt pending in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  IntType:  Interrupt location type, should be:
            - RTC_INT_COUNTER_INCREASE: Clear Counter Increment Interrupt
              pending.
            - RTC_INT_ALARM: Clear alarm interrupt pending
  
  '''
  return robocaller("RTC_ClearIntPending", "void", RTCx, IntType)

def RTC_SetFullTime(RTCx, pFullTime):
  '''Set full of time in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  pFullTime:  Pointer to a RTC_TIME_Type structure that contains time value in
              full.
  
  '''
  return robocaller("RTC_SetFullTime", "void", RTCx, pFullTime)

def RTC_SetAlarmTime(RTCx, Timetype, ALValue):
  '''Set alarm time value for each time type.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  Timetype: Time Type, should be:
            - RTC_TIMETYPE_SECOND
            - RTC_TIMETYPE_MINUTE
            - RTC_TIMETYPE_HOUR
            - RTC_TIMETYPE_DAYOFWEEK
            - RTC_TIMETYPE_DAYOFMONTH
            - RTC_TIMETYPE_DAYOFYEAR
            - RTC_TIMETYPE_MONTH
            - RTC_TIMETYPE_YEAR
  ALValue:  Alarm time value to set
  
  '''
  return robocaller("RTC_SetAlarmTime", "void", RTCx, Timetype, ALValue)

def RTC_GetIntPending(RTCx, IntType):
  '''Check whether if specified Location interrupt in RTC peripheral is set or
  not.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  IntType:  Interrupt location type, should be:
            - RTC_INT_COUNTER_INCREASE: Counter Increment Interrupt block
              generated an interrupt.
            - RTC_INT_ALARM: Alarm generated an interrupt.
  
  '''
  return robocaller("RTC_GetIntPending", "IntStatus", RTCx, IntType)

def RTC_SetTime(RTCx, Timetype, TimeValue):
  '''Set current time value for each time type in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  Timetype: Time Type, should be:
            - RTC_TIMETYPE_SECOND
            - RTC_TIMETYPE_MINUTE
            - RTC_TIMETYPE_HOUR
            - RTC_TIMETYPE_DAYOFWEEK
            - RTC_TIMETYPE_DAYOFMONTH
            - RTC_TIMETYPE_DAYOFYEAR
            - RTC_TIMETYPE_MONTH
            - RTC_TIMETYPE_YEAR
  TimeValue:  Time value to set
  
  '''
  return robocaller("RTC_SetTime", "void", RTCx, Timetype, TimeValue)

def RTC_GetFullAlarmTime(RTCx, pFullTime):
  '''Get full of alarm time in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  pFullTime:  Pointer to a RTC_TIME_Type structure that will be stored alarm 
              time in full.
  
  '''
  return robocaller("RTC_GetFullAlarmTime", "void", RTCx, pFullTime)

def RTC_DeInit(RTCx):
  '''De-initializes the RTC peripheral registers to their default reset values.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  
  '''
  return robocaller("RTC_DeInit", "void", RTCx)

def RTC_Init(RTCx):
  '''Initializes the RTC peripheral..
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  
  '''
  return robocaller("RTC_Init", "void", RTCx)

def RTC_ReadGPREG(RTCx, Channel):
  '''Read value from General purpose registers.
  
  These General purpose registers can be used to store important
  information when the main power supply is off. The value in these
  registers is not affected by chip reset. 
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  Channel:  General purpose registers Channel number,should be in range from 0
            to 4.
  return: Read Value
  
  '''
  return robocaller("RTC_ReadGPREG", "uint32_t", RTCx, Channel)

def RTC_GetAlarmTime(RTCx, Timetype):
  '''Get alarm time value for each time type.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  Timetype: Time Type, should be:
            - RTC_TIMETYPE_SECOND
            - RTC_TIMETYPE_MINUTE
            - RTC_TIMETYPE_HOUR
            - RTC_TIMETYPE_DAYOFWEEK
            - RTC_TIMETYPE_DAYOFMONTH
            - RTC_TIMETYPE_DAYOFYEAR
            - RTC_TIMETYPE_MONTH
            - RTC_TIMETYPE_YEAR
  return: Value of Alarm time according to specified time type
  
  '''
  return robocaller("RTC_GetAlarmTime", "uint32_t", RTCx, Timetype)

def RTC_AlarmIntConfig(RTCx, AlarmTimeType, NewState):
  '''Enable/Disable Alarm interrupt for each time type in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  AlarmTimeType:  Alarm Time Interrupt type, an matching of this type value 
                  below with current time in RTC will generates an interrupt,
                  should be:
                  - RTC_TIMETYPE_SECOND
                  - RTC_TIMETYPE_MINUTE
                  - RTC_TIMETYPE_HOUR
                  - RTC_TIMETYPE_DAYOFWEEK
                  - RTC_TIMETYPE_DAYOFMONTH
                  - RTC_TIMETYPE_DAYOFYEAR
                  - RTC_TIMETYPE_MONTH
                  - RTC_TIMETYPE_YEAR 
  NewState: New State of this function, should be:
            - ENABLE: Alarm interrupt for this time type are enabled
            - DISABLE: Alarm interrupt for this time type are disabled 
  
  '''
  return robocaller("RTC_AlarmIntConfig", "void", RTCx, AlarmTimeType, NewState)

def RTC_GetTime(RTCx, Timetype):
  '''Get current time value for each type time type.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  Timetype: Time Type, should be:
            - RTC_TIMETYPE_SECOND
            - RTC_TIMETYPE_MINUTE
            - RTC_TIMETYPE_HOUR
            - RTC_TIMETYPE_DAYOFWEEK
            - RTC_TIMETYPE_DAYOFMONTH
            - RTC_TIMETYPE_DAYOFYEAR
            - RTC_TIMETYPE_MONTH
            - RTC_TIMETYPE_YEAR
  return: Value of time according to specified time type
  
  '''
  return robocaller("RTC_GetTime", "uint32_t", RTCx, Timetype)

def RTC_CalibCounterCmd(RTCx, NewState):
  '''Enable/Disable calibration counter in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  NewState: New State of this function, should be:
            - ENABLE: The calibration counter is enabled and counting
            - DISABLE: The calibration counter is disabled and reset to zero
  
  '''
  return robocaller("RTC_CalibCounterCmd", "void", RTCx, NewState)

def RTC_GetFullTime(RTCx, pFullTime):
  '''Get full of time in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  pFullTime:  Pointer to a RTC_TIME_Type structure that will be stored time in
              full.
  
  '''
  return robocaller("RTC_GetFullTime", "void", RTCx, pFullTime)

def RTC_CalibConfig(RTCx, CalibValue, CalibDir):
  '''Configures Calibration in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  CalibValue: Calibration value, should be in range from 0 to 131,072
  CalibDir: Calibration Direction, should be:
            - RTC_CALIB_DIR_FORWARD: Forward calibration
            - RTC_CALIB_DIR_BACKWARD: Backward calibration
  
  '''
  return robocaller("RTC_CalibConfig", "void", RTCx, CalibValue, CalibDir)

def RTC_Cmd(RTCx, NewState):
  '''Start/Stop RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  NewState: New State of this function, should be:
            - ENABLE: The time counters are enabled
            - DISABLE: The time counters are disabled
  
  '''
  return robocaller("RTC_Cmd", "void", RTCx, NewState)

def RTC_SetFullAlarmTime(RTCx, pFullTime):
  '''Set full of alarm time in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  pFullTime:  Pointer to a RTC_TIME_Type structure that contains alarm time 
              value in full.
  
  '''
  return robocaller("RTC_SetFullAlarmTime", "void", RTCx, pFullTime)

def RTC_WriteGPREG(RTCx, Channel, Value):
  '''Write value to General purpose registers.
  
  Note: These General purpose registers can be used to store important
  information when the main power supply is off. The value in these
  registers is not affected by chip reset.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  Channel:  General purpose registers Channel number, should be in range from 0 
            to 4.
  Value:  Value to write
  
  '''
  return robocaller("RTC_WriteGPREG", "void", RTCx, Channel, Value)

def RTC_ResetClockTickCounter(RTCx):
  '''Reset clock tick counter in RTC peripheral.
  
  RTCx: RTC peripheral selected, should be LPC_RTC
  
  '''
  return robocaller("RTC_ResetClockTickCounter", "void", RTCx)
