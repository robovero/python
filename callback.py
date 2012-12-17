"""Demonstrates the use of callbacks. Press the onboard button S2 to toggle led.
"""

from robovero.LPC17xx import IRQn_Type
from robovero.core import NVIC_EnableIRQ
from robovero.arduino import pinMode, digitalWrite, digitalRead, BTN, LED, OUTPUT
from robovero.extras import heartbeatOff, registerCallback
from robovero.lpc17xx_exti import EXTI_Init, EXTI_ClearEXTIFlag
from robovero.lpc17xx_pinsel import PINSEL_CFG_Type, PINSEL_ConfigPin
from time import sleep
from random import choice

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"


responses = (
  "Please", "Hey", "OK I surrender, just", "I said", "Ouch",
  "I'm afraid I can't let you do that, Dave. Also,",
  "Hammer says"
  )

def EINT0Callback():
	"""Callback function for EINT0.
	"""
	while not digitalRead(BTN):
		sleep(0)
	print "%s don't touch that!" % choice(responses)
	state = digitalRead(LED)
	digitalWrite(LED, state ^ 1)
	EXTI_ClearEXTIFlag(0)

# control the LED manually
heartbeatOff()
pinMode(LED, OUTPUT)

# setup EINT0 on pin 2.10
PinCfg = PINSEL_CFG_Type()
PinCfg.Funcnum = 1
PinCfg.OpenDrain = 0
PinCfg.Pinmode = 0
PinCfg.Pinnum = 10
PinCfg.Portnum = 2
PINSEL_ConfigPin(PinCfg.ptr)
EXTI_Init()

# register the callback
registerCallback(IRQn_Type.EINT0_IRQn, EINT0Callback)

# enable EINT0
NVIC_EnableIRQ(IRQn_Type.EINT0_IRQn)

# the callback does everything from here
while True:
	sleep(1)

