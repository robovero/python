"""Receive user messages from UART1.
"""

from robovero.extras import Array, roboveroConfig
from robovero.LPC17xx import LPC_UART1
from robovero.lpc17xx_uart import UART_Receive, UART_FIFO_CFG_Type, UART_FIFOConfig, UART_FIFOConfigStructInit
from robovero.lpc_types import TRANSFER_BLOCK_Type
import time

__author__ =			"Danny Chan"
__email__ =				"danny@gumstix.com"
__copyright__ = 	"Copyright 2012, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

roboveroConfig()

UARTFIFOConfigStruct = UART_FIFO_CFG_Type()
UART_FIFOConfigStructInit(UARTFIFOConfigStruct.ptr)
UART_FIFOConfig(LPC_UART1, UARTFIFOConfigStruct.ptr);

msg = Array(1, 1, "")

try:
  while True: 
    length = UART_Receive(LPC_UART1, msg.ptr, 1, TRANSFER_BLOCK_Type.NONE_BLOCKING)
    if length!=0:
      print chr(msg[0])
    time.sleep(1) 

except:
  exit("goodbye")

