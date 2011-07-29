"""Receive some data on CAN bus.
"""

from robovero.lpc17xx_can import CAN_MSG_Type, CAN_SetAFMode, CAN_AFMODE_Type, \
							CAN_ReceiveMsg, CAN_Init
from robovero.LPC17xx import LPC_CAN1, LPC_CANAF
from robovero.extras import roboveroConfig
import time

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"


roboveroConfig()

RXMsg = CAN_MSG_Type()
RXMsg.format = 0x00
RXMsg.id = 0x00
RXMsg.len = 0x00
RXMsg.type = 0x00

CAN_Init(LPC_CAN1, 100000)
CAN_SetAFMode(LPC_CANAF, CAN_AFMODE_Type.CAN_AccBP)


while True:
  if CAN_ReceiveMsg(LPC_CAN1, RXMsg.ptr):
		print RXMsg.dataA, RXMsg.dataB
  time.sleep(0.1)
