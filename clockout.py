"""Outputs a fraction fo the core system clock on P1_27
"""

from robovero.lpc17xx_pinsel import PINSEL_CFG_Type, PINSEL_ConfigPin
from robovero.internals import deref
import time

__author__ =      "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

clkoutcfg_reg = 0x400FC1C8

PinCfg = PINSEL_CFG_Type()
PinCfg.Portnum = 1
PinCfg.Pinnum = 27
PinCfg.Pinmode = 0
PinCfg.OpenDrain = 0
PinCfg.Funcnum = 1
PINSEL_ConfigPin(PinCfg.ptr)

print "Possible clock output frequencies:"
for i in range(1, 17):
  print "%2d) %.2fMHz" % (i, 120.0/float(i))
user_clkout_sel = raw_input("Enter your selection: ")

try:
  clkout_sel = int(user_clkout_sel)
  if clkout_sel < 1 or clkout_sel > 16:
    raise InputError  
except:
  print "error: invalid input"
  clkout_sel = 1

clkoutcfg_val = deref(clkoutcfg_reg, 4)
clkoutcfg_val &= 0xFFFFFF0F
clkoutcfg_val += ((clkout_sel - 1) << 4)
deref(clkoutcfg_reg, 4, clkoutcfg_val)

print "You should now see a %.2fMHz square wave on P1_27" % (120.0/float(clkout_sel))

while True:
  time.sleep(1)
