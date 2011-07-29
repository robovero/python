"""Send some data on CAN bus.
"""

from robovero.lpc17xx_can import CAN_MSG_Type, CAN_SetAFMode, CAN_AFMODE_Type, \
							CAN_SendMsg, CAN_Init, CAN_ID_FORMAT_Type, CAN_FRAME_Type
from robovero.LPC17xx import LPC_CAN1, LPC_CANAF
from robovero.extras import roboveroConfig
import time, sys

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"


roboveroConfig()

dataA = [0, 10, 20, 30]
dataB = [40, 50, 60, 70]

TXMsg = CAN_MSG_Type()
TXMsg.format = CAN_ID_FORMAT_Type.EXT_ID_FORMAT
TXMsg.id = 0x00000000
TXMsg.len = 8
TXMsg.type = CAN_FRAME_Type.DATA_FRAME
TXMsg.dataA = dataA
TXMsg.dataB = dataB
CAN_Init(LPC_CAN1, 100000)
CAN_SetAFMode(LPC_CANAF, CAN_AFMODE_Type.CAN_AccBP)

count = 0

while True:
	sys.stdout.write("\r" + chr(27) + "[2K")
	sys.stdout.write("Messages sent: %d" % count)
	sys.stdout.flush()
	CAN_SendMsg(LPC_CAN1, TXMsg.ptr)
	for i in range(0,4):
		dataA[i] += 1
		dataB[i] += 1
		
	TXMsg.dataA = dataA
	TXMsg.dataB = dataB
	count += 1
	time.sleep(1)
	
