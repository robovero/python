"""Send user messages out of UART1.
"""

from robovero.extras import Array, roboveroConfig
from robovero.LPC17xx import LPC_UART1
from robovero.lpc17xx_uart import UART_Send
from robovero.lpc_types import TRANSFER_BLOCK_Type
import time

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

roboveroConfig()

while True:
	_msg = raw_input("enter a message:")
	msg = Array(len(_msg), 1, _msg)
	UART_Send(LPC_UART1, msg.ptr, msg.length, TRANSFER_BLOCK_Type.BLOCKING)
	print _msg
	time.sleep(1)
