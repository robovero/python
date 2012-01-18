"""Control the 6 wire stepper with PSMN022 MOSFETs. Connect the black 
and white wires to power, and the others to the Drain of the MOSFETs.
Signal lines from the Robovero connect to the Gate of the MOSFET through
an 1k resistor. Connect the Source of the MOSFET to ground. The order to 
connect the stepper wires are orange, red, blue, yellow for CW motion.
"""

from robovero.arduino import pinMode, digitalWrite, P1_27, P3_25, P4_29, P4_28
from robovero.arduino import OUTPUT, LOW, HIGH
import time

__author__ =			"Danny Chan"
__email__ =				"danny@gumstix.com"
__copyright__ = 	"Copyright 2012, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

# no need for roboveroConfig()

pinMode(P1_27, OUTPUT)
pinMode(P3_25, OUTPUT)
pinMode(P4_29, OUTPUT)
pinMode(P4_28, OUTPUT)
delay=0.00001

try:
  while True:
    digitalWrite(P4_28, HIGH)    
    digitalWrite(P1_27, LOW)
    digitalWrite(P3_25, LOW)
    digitalWrite(P4_29, LOW)
    time.sleep(delay)
    
    digitalWrite(P1_27, HIGH)    
    digitalWrite(P3_25, LOW)
    digitalWrite(P4_29, LOW)
    digitalWrite(P4_28, LOW)
    time.sleep(delay)
    
    digitalWrite(P3_25, HIGH)
    digitalWrite(P1_27, LOW)
    digitalWrite(P4_29, LOW)
    digitalWrite(P4_28, LOW)
    time.sleep(delay)

    digitalWrite(P4_29, HIGH)    
    digitalWrite(P1_27, LOW)
    digitalWrite(P3_25, LOW)
    digitalWrite(P4_28, LOW)
    time.sleep(delay)
    
    print("ticktickticktick")

except:
  digitalWrite(P1_27, LOW)
  digitalWrite(P3_25, LOW)
  digitalWrite(P4_29, LOW)
  digitalWrite(P4_28, LOW)
  exit("goodbye")
