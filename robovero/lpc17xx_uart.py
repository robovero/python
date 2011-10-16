"""UART client library functions. See LPC17xx CMSIS-Compliant Standard
Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

UART_BLOCKING_TIMEOUT = (0xFFFFFFFF)
UART_ACCEPTED_BAUDRATE_ERROR = (3)			
UART_RBR_MASKBIT = (0xFF) 		
UART_THR_MASKBIT = (0xFF)

def UART_LOAD_DLL(div):
	return ((div) & 0xFF)	

UART_DLL_MASKBIT = (0xFF)	
UART_DLM_MASKBIT = (0xFF)

def UART_LOAD_DLM(div):
	return (((div) >> 8) & 0xFF)	

UART_IER_RBRINT_EN = ((1<<0)) 	
UART_IER_THREINT_EN = ((1<<1)) 	
UART_IER_RLSINT_EN = ((1<<2)) 	
UART1_IER_MSINT_EN = ((1<<3))	
UART1_IER_CTSINT_EN = ((1<<7))	
UART_IER_ABEOINT_EN = ((1<<8)) 	
UART_IER_ABTOINT_EN = ((1<<9)) 	
UART_IER_BITMASK = ((0x307)) 
UART1_IER_BITMASK = ((0x38F)) 
UART_IIR_INTSTAT_PEND = ((1<<0))	
UART_IIR_INTID_RLS = ((3<<1)) 	
UART_IIR_INTID_RDA = ((2<<1)) 	
UART_IIR_INTID_CTI = ((6<<1)) 	
UART_IIR_INTID_THRE = ((1<<1)) 	
UART1_IIR_INTID_MODEM = ((0<<1)) 	
UART_IIR_INTID_MASK = ((7<<1))	
UART_IIR_FIFO_EN = ((3<<6)) 	
UART_IIR_ABEO_INT = ((1<<8)) 	
UART_IIR_ABTO_INT = ((1<<9)) 	
UART_IIR_BITMASK = ((0x3CF))	
UART_FCR_FIFO_EN = ((1<<0)) 	
UART_FCR_RX_RS = ((1<<1)) 	
UART_FCR_TX_RS = ((1<<2)) 	
UART_FCR_DMAMODE_SEL = ((1<<3)) 	
UART_FCR_TRG_LEV0 = ((0)) 		
UART_FCR_TRG_LEV1 = ((1<<6)) 	
UART_FCR_TRG_LEV2 = ((2<<6)) 	
UART_FCR_TRG_LEV3 = ((3<<6)) 	
UART_FCR_BITMASK = ((0xCF))	
UART_TX_FIFO_SIZE = (16)
UART_LCR_WLEN5 = ((0))   		
UART_LCR_WLEN6 = ((1<<0))   	
UART_LCR_WLEN7 = ((2<<0))   	
UART_LCR_WLEN8 = ((3<<0))   	
UART_LCR_STOPBIT_SEL = ((1<<2))   	
UART_LCR_PARITY_EN = ((1<<3))		
UART_LCR_PARITY_ODD = ((0))         	
UART_LCR_PARITY_EVEN = ((1<<4))		
UART_LCR_PARITY_F_1 = ((2<<4))		
UART_LCR_PARITY_F_0 = ((3<<4))		
UART_LCR_BREAK_EN = ((1<<6))		
UART_LCR_DLAB_EN = ((1<<7))    	
UART_LCR_BITMASK = ((0xFF))		
UART1_MCR_DTR_CTRL = ((1<<0))		
UART1_MCR_RTS_CTRL = ((1<<1))		
UART1_MCR_LOOPB_EN = ((1<<4))		
UART1_MCR_AUTO_RTS_EN = ((1<<6))		
UART1_MCR_AUTO_CTS_EN = ((1<<7))		
UART1_MCR_BITMASK = ((0x0F3))		
UART_LSR_RDR = ((1<<0)) 	
UART_LSR_OE = ((1<<1)) 	
UART_LSR_PE = ((1<<2)) 	
UART_LSR_FE = ((1<<3)) 	
UART_LSR_BI = ((1<<4)) 	
UART_LSR_THRE = ((1<<5)) 	
UART_LSR_TEMT = ((1<<6)) 	
UART_LSR_RXFE = ((1<<7)) 	
UART_LSR_BITMASK = ((0xFF)) 	
UART1_MSR_DELTA_CTS = ((1<<0))	
UART1_MSR_DELTA_DSR = ((1<<1))	
UART1_MSR_LO2HI_RI = ((1<<2))	
UART1_MSR_DELTA_DCD = ((1<<3))	
UART1_MSR_CTS = ((1<<4))	
UART1_MSR_DSR = ((1<<5))	
UART1_MSR_RI = ((1<<6))	
UART1_MSR_DCD = ((1<<7))	
UART1_MSR_BITMASK = ((0xFF))	
UART_SCR_BIMASK = ((0xFF))	
UART_ACR_START = ((1<<0))	
UART_ACR_MODE = ((1<<1))	
UART_ACR_AUTO_RESTART = ((1<<2))	
UART_ACR_ABEOINT_CLR = ((1<<8))	
UART_ACR_ABTOINT_CLR = ((1<<9))	
UART_ACR_BITMASK = ((0x307))	
UART_ICR_IRDAEN = ((1<<0))			
UART_ICR_IRDAINV = ((1<<1))			
UART_ICR_FIXPULSE_EN = ((1<<2))

def UART_ICR_PULSEDIV(n):
	return (((n&0x07)<<3))	

UART_ICR_BITMASK = ((0x3F))

def UART_FDR_DIVADDVAL(n):
	return ((n&0x0F))		

def UART_FDR_MULVAL(n):
	return (((n<<4)&0xF0))	

UART_FDR_BITMASK = ((0xFF))			
UART_TER_TXEN = ((1<<7)) 		
UART_TER_BITMASK = ((0x80))		
UART1_RS485CTRL_NMM_EN = ((1<<0))	
UART1_RS485CTRL_RX_DIS = ((1<<1))	
UART1_RS485CTRL_AADEN = ((1<<2))	
UART1_RS485CTRL_SEL_DTR = ((1<<3))	
UART1_RS485CTRL_DCTRL_EN = ((1<<4))	
UART1_RS485CTRL_OINV_1 = ((1<<5))	
UART1_RS485CTRL_BITMASK = ((0x3F))	
UART1_RS485ADRMATCH_BITMASK = ((0xFF)) 	
UART1_RS485DLY_BITMASK = ((0xFF))

def UART_FIFOLVL_RXFIFOLVL(n):
	return ((n&0x0F))		

def UART_FIFOLVL_TXFIFOLVL(n):
	return (((n>>8)&0x0F))	

UART_FIFOLVL_BITMASK = ((0x0F0F))

def PARAM_UART_DATABIT(databit):
	return (
		(databit==UART_DATABIT_5) or (databit==UART_DATABIT_6)
		or (databit==UART_DATABIT_7) or (databit==UART_DATABIT_8)
		)
		
def PARAM_UART_STOPBIT(stopbit):
	return ((stopbit==UART_STOPBIT_1) or (stopbit==UART_STOPBIT_2))

def PARAM_UART_PARITY(parity):
	return (
		(parity==UART_PARITY_NONE) or (parity==UART_PARITY_ODD) 
		or (parity==UART_PARITY_EVEN) or (parity==UART_PARITY_SP_1) 
		or (parity==UART_PARITY_SP_0)
		)

def PARAM_UART_FIFO_LEVEL(fifo):
	return (
		(fifo==UART_FIFO_TRGLEV0) 
		or (fifo==UART_FIFO_TRGLEV1) or (fifo==UART_FIFO_TRGLEV2) 
		or (fifo==UART_FIFO_TRGLEV3)
		)

def PARAM_UART_INTCFG(IntCfg):
	return (
		(IntCfg==UART_INTCFG_RBR) or (IntCfg==UART_INTCFG_THRE) 
		or (IntCfg==UART_INTCFG_RLS) or (IntCfg==UART_INTCFG_ABEO) 
		or (IntCfg==UART_INTCFG_ABTO)
		)

def PARAM_UART1_INTCFG(IntCfg):
	return ((IntCfg==UART1_INTCFG_MS) or (IntCfg==UART1_INTCFG_CTS))

def PARAM_UART_AUTOBAUD_MODE(ABmode):
	return ((ABmode==UART_AUTOBAUD_MODE0) or (ABmode==UART_AUTOBAUD_MODE1))

def PARAM_UART_AUTOBAUD_INTSTAT(ABIntStat):
	return (
		(ABIntStat==UART_AUTOBAUD_INTSTAT_ABEO) or 
		(ABIntStat==UART_AUTOBAUD_INTSTAT_ABTO)
		)
		
def PARAM_UART_IrDA_PULSEDIV(PulseDiv):
	return (
		(PulseDiv==UART_IrDA_PULSEDIV2) or (PulseDiv==UART_IrDA_PULSEDIV4) 
		or (PulseDiv==UART_IrDA_PULSEDIV8) or (PulseDiv==UART_IrDA_PULSEDIV16) 
		or (PulseDiv==UART_IrDA_PULSEDIV32) or (PulseDiv==UART_IrDA_PULSEDIV64) 
		or (PulseDiv==UART_IrDA_PULSEDIV128) or (PulseDiv==UART_IrDA_PULSEDIV256)
		)
		
def PARAM_UART1_SIGNALSTATE(x):
	return ((x==INACTIVE) or (x==ACTIVE))

def PARAM_UART1_MODEM_PIN(x):
	return ((x==UART1_MODEM_PIN_DTR) or (x==UART1_MODEM_PIN_RTS))

def PARAM_UART1_MODEM_MODE(x):
	return ((x==UART1_MODEM_MODE_LOOPBACK) or (x==UART1_MODEM_MODE_AUTO_RTS) 
		or (x==UART1_MODEM_MODE_AUTO_CTS))

def PARAM_UART_RS485_DIRCTRL_PIN(x):
	return ((x==UART1_RS485_DIRCTRL_RTS) or (x==UART1_RS485_DIRCTRL_DTR))

def PARAM_UARTx(x):
	return (
		((x)==(LPC_UART0)) 
		or ((x)==(LPC_UART1)) 
		or ((x)==(LPC_UART2)) 
		or ((x)==(LPC_UART3))
		)
	
def PARAM_UART_IrDA(x):
	return ((x)==(LPC_UART3))

def PARAM_UART1_MODEM(x):
	return ((x)==(LPC_UART1))

def PARAM_UART1_RS485_CFG_MATCHADDRVALUE(x):
	return ((x<0xFF))

def PARAM_UART1_RS485_CFG_DELAYVALUE(x):
	return ((x<0xFF))

class UART_AB_MODE_Type:
	UART_AUTOBAUD_MODE0 = 0
	UART_AUTOBAUD_MODE1 = 1

class UART1_RS485_CTRLCFG_Type(cstruct):
	pass

class UART_IrDA_PULSE_Type:
	UART_IrDA_PULSEDIV2 = 0
	UART_IrDA_PULSEDIV4 = 1
	UART_IrDA_PULSEDIV8 = 2
	UART_IrDA_PULSEDIV16 = 3
	UART_IrDA_PULSEDIV32 = 4
	UART_IrDA_PULSEDIV64 = 5
	UART_IrDA_PULSEDIV128 = 6
	UART_IrDA_PULSEDIV256 = 7

class UART_MODEM_PIN_Type:
	UART1_MODEM_PIN_DTR = 0
	UART1_MODEM_PIN_RTS = 1

class UART_FIFO_CFG_Type(cstruct):
	pass

class UART_STOPBIT_Type:
	UART_STOPBIT_1 = (0)
	UART_STOPBIT_2 = 1

class UART_ABEO_Type:
	UART_AUTOBAUD_INTSTAT_ABEO = UART_IIR_ABEO_INT
	UART_AUTOBAUD_INTSTAT_ABTO = UART_IIR_ABTO_INT

class UART_RS485_DIRCTRL_PIN_Type:
	UART1_RS485_DIRCTRL_RTS = 0
	UART1_RS485_DIRCTRL_DTR = 1

class UART1_SignalState:
	INACTIVE = 0
	ACTIVE = 1

class UART_CFG_Type(cstruct):
	pass

class UART_AB_CFG_Type(cstruct):
	pass

class UART_MODEM_MODE_Type:
	UART1_MODEM_MODE_LOOPBACK = 0
	UART1_MODEM_MODE_AUTO_RTS = 1
	UART1_MODEM_MODE_AUTO_CTS = 2

class UART_FITO_LEVEL_Type:
	UART_FIFO_TRGLEV0 = 0
	UART_FIFO_TRGLEV1 = 1
	UART_FIFO_TRGLEV2 = 2
	UART_FIFO_TRGLEV3 = 3

class UART_INT_Type:
	UART_INTCFG_RBR = 0
	UART_INTCFG_THRE = 1
	UART_INTCFG_RLS = 2
	UART1_INTCFG_MS = 3
	UART1_INTCFG_CTS = 4
	UART_INTCFG_ABEO = 5
	UART_INTCFG_ABTO = 6

class UART_LS_Type:
	UART_LINESTAT_RDR = UART_LSR_RDR
	UART_LINESTAT_OE = UART_LSR_OE
	UART_LINESTAT_PE = UART_LSR_PE
	UART_LINESTAT_FE = UART_LSR_FE
	UART_LINESTAT_BI = UART_LSR_BI
	UART_LINESTAT_THRE = UART_LSR_THRE
	UART_LINESTAT_TEMT = UART_LSR_TEMT
	UART_LINESTAT_RXFE = UART_LSR_RXFE

class UART_DATABIT_Type:
	UART_DATABIT_5 = 0
	UART_DATABIT_6 = 1
	UART_DATABIT_7 = 2
	UART_DATABIT_8 = 3

class UART_MODEM_STAT_type:
	UART1_MODEM_STAT_DELTA_CTS = UART1_MSR_DELTA_CTS
	UART1_MODEM_STAT_DELTA_DSR = UART1_MSR_DELTA_DSR
	UART1_MODEM_STAT_LO2HI_RI = UART1_MSR_LO2HI_RI
	UART1_MODEM_STAT_DELTA_DCD = UART1_MSR_DELTA_DCD
	UART1_MODEM_STAT_CTS = UART1_MSR_CTS
	UART1_MODEM_STAT_DSR = UART1_MSR_DSR
	UART1_MODEM_STAT_RI = UART1_MSR_RI
	UART1_MODEM_STAT_DCD = UART1_MSR_DCD

class UART_PARITY_Type:
	UART_PARITY_NONE = 0
	UART_PARITY_ODD = 1
	UART_PARITY_EVEN = 2
	UART_PARITY_SP_1 = 3
	UART_PARITY_SP_0 = 4

def UART_RS485SendSlvAddr(UARTx, SlvAddr):
	return robocaller("UART_RS485SendSlvAddr", "void", UARTx, SlvAddr)

def UART_ABClearIntPending(UARTx, ABIntType):
	return robocaller("UART_ABClearIntPending", "void", UARTx, ABIntType)

def UART_IrDAPulseDivConfig(UARTx, PulseDiv):
	return robocaller("UART_IrDAPulseDivConfig", "void", UARTx, PulseDiv)

def UART_RS485Config(UARTx, RS485ConfigStruct):
	return robocaller("UART_RS485Config", "void", UARTx, RS485ConfigStruct)

def UART_Receive(UARTx, rxbuf, buflen, flag):
	return robocaller("UART_Receive", "uint32_t", UARTx, rxbuf, buflen, flag)

def UART_ReceiveByte(UARTx):
	return robocaller("UART_ReceiveByte", "uint8_t", UARTx)

def UART_GetIntId(UARTx):
	return robocaller("UART_GetIntId", "uint32_t", UARTx)

def UART_ForceBreak(UARTx):
	return robocaller("UART_ForceBreak", "void", UARTx)

def UART_FIFOConfig(UARTx, FIFOCfg):
	return robocaller("UART_FIFOConfig", "void", UARTx, FIFOCfg)

def UART_DeInit(UARTx):
	return robocaller("UART_DeInit", "void", UARTx)

def UART_Send(UARTx, txbuf, buflen, flag):
	return robocaller("UART_Send", "uint32_t", UARTx, txbuf, buflen, flag)

def UART_FIFOConfigStructInit(UART_FIFOInitStruct):
	return robocaller("UART_FIFOConfigStructInit", "void", UART_FIFOInitStruct)

def UART_FullModemForcePinState(UARTx, Pin, NewState):
	return robocaller("UART_FullModemForcePinState", "void", UARTx, Pin, NewState)

def UART_RS485ReceiverCmd(UARTx, NewState):
	return robocaller("UART_RS485ReceiverCmd", "void", UARTx, NewState)

def UART_CheckBusy(UARTx):
	return robocaller("UART_CheckBusy", "FlagStatus", UARTx)

def UART_SendByte(UARTx, Data):
	return robocaller("UART_SendByte", "void", UARTx, Data)

def UART_ABCmd(UARTx, ABConfigStruct, NewState):
	return robocaller("UART_ABCmd", "void", UARTx, ABConfigStruct, NewState)

def UART_GetLineStatus(UARTx):
	return robocaller("UART_GetLineStatus", "uint8_t", UARTx)

def UART_FullModemConfigMode(UARTx, Mode, NewState):
	return robocaller("UART_FullModemConfigMode", "void", UARTx, Mode, NewState)

def UART_FullModemGetStatus(UARTx):
	return robocaller("UART_FullModemGetStatus", "uint8_t", UARTx)

def UART_Init(UARTx, UART_ConfigStruct):
	return robocaller("UART_Init", "void", UARTx, UART_ConfigStruct)

def UART_IrDACmd(UARTx, NewState):
	return robocaller("UART_IrDACmd", "void", UARTx, NewState)

def UART_TxCmd(UARTx, NewState):
	return robocaller("UART_TxCmd", "void", UARTx, NewState)

def UART_ConfigStructInit(UART_InitStruct):
	return robocaller("UART_ConfigStructInit", "void", UART_InitStruct)

def UART_IntConfig(UARTx, UARTIntCfg, NewState):
	return robocaller("UART_IntConfig", "void", UARTx, UARTIntCfg, NewState)

def UART_IrDAInvtInputCmd(UARTx, NewState):
	return robocaller("UART_IrDAInvtInputCmd", "void", UARTx, NewState)

def UART_RS485SendData(UARTx, pData, size):
	return robocaller("UART_RS485SendData", "uint32_t", UARTx, pData, size)

