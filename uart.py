"""Send user messages out of UART1.
"""

from extras import Array, roboveroConfig
from LPC17xx import LPC_UART1
from lpc17xx_uart import *
from lpc_types import TRANSFER_BLOCK_Type
import time

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

roboveroConfig()

while True:
	msg_str = raw_input("enter a message:")
	msg = Array(len(msg_str), 1, msg_str)
	UART_Send(LPC_UART1, msg.ptr, msg.length, TRANSFER_BLOCK_Type.BLOCKING)
	print msg_str
	time.sleep(1)
