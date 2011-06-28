"""Send some data on CAN bus.
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

#~ TXMsg = CAN_MSG_Type()
#~ TXMsg.format = CAN_ID_FORMAT_Type.EXT_ID_FORMAT
#~ TXMsg.id = 0x00000000
#~ TXMsg.len = 8
#~ TXMsg.type = CAN_FRAME_Type.DATA_FRAME
#~ TXMsg.dataA = [0 10 20 30]
#~ TXMsg.dataB = [40 50 60 70]
#~ print CAN_SendMsg(LPC_CAN1, TXMsg.ptr)

dataA = [0, 0, 0, 0]
RXMsg = CAN_MSG_Type()
RXMsg.format = 0x00
RXMsg.id = 0x00
RXMsg.len = 0x00
RXMsg.type = 0x00
RXMsg.dataA = dataA

CAN_Init(LPC_CAN1, 100000)
CAN_SetAFMode(LPC_CANAF, CAN_AFMODE_Type.CAN_AccBP)

print "waiting for messages.."
while True:
  print CAN_ReceiveMsg(LPC_CAN1, RXMsg.ptr), RXMsg.dataA
  dataA[0] += 1
  RXMsg.dataA = dataA
  time.sleep(1)
