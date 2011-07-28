"""Set position of servo 1 (PWM1) to an angle provided by the user.

You must have an RC servo connected to PWM1 for this example. Otherwise, you
can observe the control signal with an oscilloscope or logic analyzer.
"""

from robovero.LPC17xx import LPC_PWM1
from robovero.lpc17xx_pwm import PWM_TC_MODE_OPT, \
					PWM_MATCH_UPDATE_OPT, PWM_MATCHCFG_Type, \
					PWM_MatchUpdate, PWM_ConfigMatch, PWM_ChannelCmd, \
					PWM_ResetCounter, PWM_CounterCmd, PWM_Cmd
from robovero.extras import roboveroConfig, initMatch
from robovero.lpc_types import FunctionalState

from robovero.arduino import analogWrite, PWM1

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"


def getServoAngle():
	"""Get an angle from the user and calculate new duty cycle.
	"""
	user_angle = raw_input("New angle: ")
	try:
		angle = int(user_angle)
		if angle < 0 or angle > 180:
			raise InputError
	except:
		print "enter an angle between 0 and 180 degrees"
		return None
	match_value = 1250 + (angle*500/180)
	return match_value

def initPulse(channel, pulse_width):
	initMatch(channel, pulse_width)
	
def initPeriod(period):
	initMatch(0, period)

def initPWM():
	"""Set up PWM to output a 1.5ms pulse at 50Hz.
	"""

	# Set the period to 20000us = 20ms = 50Hz
	initPeriod(20000)

	# Set the pulse width to 1.5ms
	initPulse(1, 1500)
	
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
		PWM_MatchUpdate(LPC_PWM1, 1, match_value, PWM_MATCH_UPDATE_OPT.PWM_MATCH_UPDATE_NOW)
		


