"""Control the LED with the pushbutton using the Arduino API.
"""

from robovero.arduino import pinMode, digitalWrite, digitalRead, BTN, LED
from robovero.arduino import INPUT, OUTPUT
from robovero.extras import heartbeatOff

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

# no need for roboveroConfig()

heartbeatOff()

pinMode(BTN, INPUT)
pinMode(LED, OUTPUT)

while True:
	digitalWrite(LED, digitalRead(BTN))
