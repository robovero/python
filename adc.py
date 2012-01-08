"""Acquire and display ADC readings using the Arduino API.
"""

from robovero.arduino import analogRead, AD0_0, AD0_1, AD0_2, AD0_3, AD0_5, AD0_6, AD0_7
from robovero.extras import roboveroConfig
from time import sleep

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

roboveroConfig()

try:
  while True:
    data = [
      analogRead(AD0_0),
      analogRead(AD0_1),
      analogRead(AD0_2),
      analogRead(AD0_3),
      analogRead(AD0_5),
      analogRead(AD0_6),
      analogRead(AD0_7)
    ]
    print data

except KeyboardInterrupt:
  exit("\nkeyboard interrupt: how rude!")
  
