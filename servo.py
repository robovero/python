"""Set position of servo 1 (PWM1) to an angle provided by the user.
"""

from robovero.LPC17xx import LPC_PWM1
from robovero.lpc17xx_pwm import PWM_TIMER_PRESCALE_OPT, PWM_TC_MODE_OPT, \
					PWM_MATCH_UPDATE_OPT, PWM_TIMERCFG_Type, PWM_MATCHCFG_Type, \
					PWM_Init, PWM_MatchUpdate, PWM_ConfigMatch, PWM_ChannelCmd, \
					PWM_ResetCounter, PWM_CounterCmd, PWM_Cmd
from robovero.extras import roboveroConfig
from robovero.lpc_types import FunctionalState


__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"


def getServoAngle():
	"""Get an angle from the user and calculate new duty cycle"""
	user_angle = raw_input("New angle: ")
	try:
		angle = int(user_angle)
		if angle < 0 or angle > 90:
			raise InputError
	except:
		print "enter an angle between 0 and 90 degrees"
		return None
	match_value = angle/7 + 13
	return match_value

def initPWM():
	"""Set up PWM to output at 50Hz and 50% duty cycle to start."""
	PWMCfgDat = PWM_TIMERCFG_Type()
	PWMCfgDat.PrescaleOption = PWM_TIMER_PRESCALE_OPT.PWM_TIMER_PRESCALE_TICKVAL
	PWMCfgDat.PrescaleValue = 1953
	PWM_Init(LPC_PWM1, PWM_TC_MODE_OPT.PWM_MODE_TIMER, PWMCfgDat.ptr)

	PWMMatchCfgDat = PWM_MATCHCFG_Type()
	PWM_MatchUpdate(LPC_PWM1, 0, 256, PWM_MATCH_UPDATE_OPT.PWM_MATCH_UPDATE_NOW)
	PWMMatchCfgDat.IntOnMatch = FunctionalState.DISABLE
	PWMMatchCfgDat.MatchChannel = 0
	PWMMatchCfgDat.ResetOnMatch = FunctionalState.ENABLE
	PWMMatchCfgDat.StopOnMatch = FunctionalState.DISABLE
	PWM_ConfigMatch(LPC_PWM1, PWMMatchCfgDat.ptr)

	PWM_MatchUpdate(LPC_PWM1, 1, 19, PWM_MATCH_UPDATE_OPT.PWM_MATCH_UPDATE_NOW)
	PWMMatchCfgDat.IntOnMatch = FunctionalState.DISABLE
	PWMMatchCfgDat.MatchChannel = 1
	PWMMatchCfgDat.ResetOnMatch = FunctionalState.DISABLE
	PWMMatchCfgDat.StopOnMatch = FunctionalState.DISABLE
	PWM_ConfigMatch(LPC_PWM1, PWMMatchCfgDat.ptr)
	PWM_ChannelCmd(LPC_PWM1, 1, FunctionalState.ENABLE)

	PWM_ResetCounter(LPC_PWM1)
	PWM_CounterCmd(LPC_PWM1, FunctionalState.ENABLE)
	PWM_Cmd(LPC_PWM1, FunctionalState.ENABLE)

# Entry Point
roboveroConfig()
initPWM()	

while True:
	match_value = getServoAngle()
	if match_value:
		PWM_MatchUpdate(
			LPC_PWM1, 1, match_value, 
			PWM_MATCH_UPDATE_OPT.PWM_MATCH_UPDATE_NOW
			)

