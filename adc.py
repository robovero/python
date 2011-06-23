"""Acquire and display ADC readings using the Arduino API.
"""

from robovero.arduino import analogRead, AD0_0
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
	  print analogRead(AD0_0)
	  sleep(1)

except KeyboardInterrupt:
  print ""
  print "keyboard interrupt: how rude!"
  exit()
  
