"""Synchronous serial port client library functions. See LPC17xx
CMSIS-Compliant Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

def SSP_CR0_DSS(n):
	return ((n-1)&0xF)

SSP_CR0_FRF_SPI = (0<<4)
SSP_CR0_FRF_TI = (1<<4)
SSP_CR0_FRF_MICROWIRE = (2<<4)
SSP_CR0_CPOL_HI = (1<<6)
SSP_CR0_CPHA_SECOND = (1<<7)

def SSP_CR0_SCR(n):
	return ((n&0xFF)<<8)

SSP_CR0_BITMASK = (0xFFFF)
SSP_CR1_LBM_EN = (1<<0)
SSP_CR1_SSP_EN = (1<<1)
SSP_CR1_SLAVE_EN = (1<<2)
SSP_CR1_SO_DISABLE = (1<<3)
SSP_CR1_BITMASK = (0x0F)

def SSP_DR_BITMASK(n):
	return ((n)&0xFFFF)

SSP_SR_TFE = (1<<0)
SSP_SR_TNF = (1<<1)
SSP_SR_RNE = (1<<2)
SSP_SR_RFF = (1<<3)
SSP_SR_BSY = (1<<4)
SSP_SR_BITMASK = (0x1F)

def SSP_CPSR_CPDVSR(n):
	return (n&0xFF)

SSP_CPSR_BITMASK = (0xFF)
SSP_IMSC_ROR = (1<<0)
SSP_IMSC_RT = (1<<1)
SSP_IMSC_RX = (1<<2)
SSP_IMSC_TX = (1<<3)
SSP_IMSC_BITMASK = (0x0F)
SSP_RIS_ROR = (1<<0)
SSP_RIS_RT = (1<<1)
SSP_RIS_RX = (1<<2)
SSP_RIS_TX = (1<<3)
SSP_RIS_BITMASK = (0x0F)
SSP_MIS_ROR = (1<<0)
SSP_MIS_RT = (1<<1)
SSP_MIS_RX = (1<<2)
SSP_MIS_TX = (1<<3)
SSP_MIS_BITMASK = (0x0F)
SSP_ICR_ROR = (1<<0)
SSP_ICR_RT = (1<<1)
SSP_ICR_BITMASK = (0x03)
SSP_DMA_RXDMA_EN = (1<<0)
SSP_DMA_TXDMA_EN = (1<<1)
SSP_DMA_BITMASK = (0x03)

SSP_CPHA_FIRST = (0)
SSP_CPHA_SECOND = SSP_CR0_CPHA_SECOND
SSP_CPOL_HI = (0)
SSP_CPOL_LO = SSP_CR0_CPOL_HI
SSP_SLAVE_MODE = SSP_CR1_SLAVE_EN
SSP_MASTER_MODE = (0)
SSP_DATABIT_4 = SSP_CR0_DSS(4) 			
SSP_DATABIT_5 = SSP_CR0_DSS(5) 			
SSP_DATABIT_6 = SSP_CR0_DSS(6) 			
SSP_DATABIT_7 = SSP_CR0_DSS(7) 			
SSP_DATABIT_8 = SSP_CR0_DSS(8) 			
SSP_DATABIT_9 = SSP_CR0_DSS(9) 			
SSP_DATABIT_10 = SSP_CR0_DSS(10) 		
SSP_DATABIT_11 = SSP_CR0_DSS(11) 		
SSP_DATABIT_12 = SSP_CR0_DSS(12) 		
SSP_DATABIT_13 = SSP_CR0_DSS(13) 		
SSP_DATABIT_14 = SSP_CR0_DSS(14) 		
SSP_DATABIT_15 = SSP_CR0_DSS(15) 		
SSP_DATABIT_16 = SSP_CR0_DSS(16) 		
SSP_FRAME_SPI = SSP_CR0_FRF_SPI
SSP_FRAME_TI = SSP_CR0_FRF_TI
SSP_FRAME_MICROWIRE = SSP_CR0_FRF_MICROWIRE
SSP_STAT_TXFIFO_EMPTY = SSP_SR_TFE
SSP_STAT_TXFIFO_NOTFULL = SSP_SR_TNF
SSP_STAT_RXFIFO_NOTEMPTY = SSP_SR_RNE
SSP_STAT_RXFIFO_FULL = SSP_SR_RFF
SSP_STAT_BUSY = SSP_SR_BSY
SSP_INTCFG_ROR = SSP_IMSC_ROR
SSP_INTCFG_RT = SSP_IMSC_RT
SSP_INTCFG_RX = SSP_IMSC_RX
SSP_INTCFG_TX = SSP_IMSC_TX
SSP_INTSTAT_ROR = SSP_MIS_ROR
SSP_INTSTAT_RT = SSP_MIS_RT
SSP_INTSTAT_RX = SSP_MIS_RX
SSP_INTSTAT_TX = SSP_MIS_TX
SSP_INTSTAT_RAW_ROR = SSP_RIS_ROR
SSP_INTSTAT_RAW_RT = SSP_RIS_RT
SSP_INTSTAT_RAW_RX = SSP_RIS_RX
SSP_INTSTAT_RAW_TX = SSP_RIS_TX
SSP_INTCLR_ROR = SSP_ICR_ROR
SSP_INTCLR_RT = SSP_ICR_RT
SSP_DMA_RX = SSP_DMA_RXDMA_EN
SSP_DMA_TX = SSP_DMA_TXDMA_EN
SSP_STAT_DONE = (1<<8)		
SSP_STAT_ERROR = (1<<9)

def PARAM_SSPx(n):
	return ((n)==(LPC_SSP0) or (n)==(LPC_SSP1))

def PARAM_SSP_CPHA(n):
	return (n==SSP_CPHA_FIRST) or (n==SSP_CPHA_SECOND)

def PARAM_SSP_CPOL(n):
	return (n==SSP_CPOL_HI) or (n==SSP_CPOL_LO)

def PARAM_SSP_MODE(n):
	return (n==SSP_SLAVE_MODE) or (n==SSP_MASTER_MODE)

def PARAM_SSP_DATABIT(n):
	return (
		(n==SSP_DATABIT_4) or (n==SSP_DATABIT_5) 
		or (n==SSP_DATABIT_6) or (n==SSP_DATABIT_16) 
		or (n==SSP_DATABIT_7) or (n==SSP_DATABIT_8) 
		or (n==SSP_DATABIT_9) or (n==SSP_DATABIT_10) 
		or (n==SSP_DATABIT_11) or (n==SSP_DATABIT_12) 
		or (n==SSP_DATABIT_13) or (n==SSP_DATABIT_14) 
		or (n==SSP_DATABIT_15)
		)

def PARAM_SSP_FRAME(n):
	return (
		(n==SSP_FRAME_SPI)
		or (n==SSP_FRAME_TI)
		or (n==SSP_FRAME_MICROWIRE)
		)

def PARAM_SSP_STAT(n):
	return (
		(n==SSP_STAT_TXFIFO_EMPTY) or (n==SSP_STAT_TXFIFO_NOTFULL)
		or (n==SSP_STAT_RXFIFO_NOTEMPTY) or (n==SSP_STAT_RXFIFO_FULL) 
		or (n==SSP_STAT_BUSY)
		)

def PARAM_SSP_INTCFG(n):
	return (
		(n==SSP_INTCFG_ROR) or (n==SSP_INTCFG_RT) 
		or (n==SSP_INTCFG_RX) or (n==SSP_INTCFG_TX)
		)

def PARAM_SSP_INTSTAT(n):
	return (
		(n==SSP_INTSTAT_ROR) or (n==SSP_INTSTAT_RT)
		or (n==SSP_INTSTAT_RX) or (n==SSP_INTSTAT_TX)
		)

def PARAM_SSP_INTSTAT_RAW(n):
	return (
		(n==SSP_INTSTAT_RAW_ROR) or (n==SSP_INTSTAT_RAW_RT) 
		or (n==SSP_INTSTAT_RAW_RX) or (n==SSP_INTSTAT_RAW_TX)
		)

def PARAM_SSP_INTCLR(n):
	return (n==SSP_INTCLR_ROR) or (n==SSP_INTCLR_RT)

def PARAM_SSP_DMA(n):
	return (n==SSP_DMA_TX) or (n==SSP_DMA_RX)

class SSP_CFG_Type(cstruct):
	pass

class SSP_DATA_SETUP_Type(cstruct):
	pass

class SSP_TRANSFER_Type:
	SSP_TRANSFER_POLLING = 0
	SSP_TRANSFER_INTERRUPT = 1

def SSP_LoopBackCmd(SSPx, NewState):
	return robocaller("SSP_LoopBackCmd", "void", SSPx, NewState)

def SSP_GetRawIntStatus(SSPx, RawIntType):
	return robocaller("SSP_GetRawIntStatus", "IntStatus", SSPx, RawIntType)

def SSP_Init(SSPx, SSP_ConfigStruct):
	return robocaller("SSP_Init", "void", SSPx, SSP_ConfigStruct)

def SSP_DMACmd(SSPx, DMAMode, NewState):
	return robocaller("SSP_DMACmd", "void", SSPx, DMAMode, NewState)

def SSP_GetDataSize(SSPx):
	return robocaller("SSP_GetDataSize", "uint8_t", SSPx)

def SSP_Cmd(SSPx, NewState):
	return robocaller("SSP_Cmd", "void", SSPx, NewState)

def SSP_IntConfig(SSPx, IntType, NewState):
	return robocaller("SSP_IntConfig", "void", SSPx, IntType, NewState)

def SSP_SlaveOutputCmd(SSPx, NewState):
	return robocaller("SSP_SlaveOutputCmd", "void", SSPx, NewState)

def SSP_ClearIntPending(SSPx, IntType):
	return robocaller("SSP_ClearIntPending", "void", SSPx, IntType)

def SSP_ReadWrite(SSPx, dataCfg, xfType):
	return robocaller("SSP_ReadWrite", "int32_t", SSPx, dataCfg, xfType)

def SSP_DeInit(SSPx):
	return robocaller("SSP_DeInit", "void", SSPx)

def SSP_GetStatus(SSPx, FlagType):
	return robocaller("SSP_GetStatus", "FlagStatus", SSPx, FlagType)

def SSP_GetRawIntStatusReg(SSPx):
	return robocaller("SSP_GetRawIntStatusReg", "uint32_t", SSPx)

def SSP_ConfigStructInit(SSP_InitStruct):
	return robocaller("SSP_ConfigStructInit", "void", SSP_InitStruct)

def SSP_ReceiveData(SSPx):
	return robocaller("SSP_ReceiveData", "uint16_t", SSPx)

def SSP_GetIntStatus(SSPx, IntType):
	return robocaller("SSP_GetIntStatus", "IntStatus", SSPx, IntType)

def SSP_SendData(SSPx, Data):
	return robocaller("SSP_SendData", "void", SSPx, Data)

