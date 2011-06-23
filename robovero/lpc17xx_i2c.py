"""I2C client library functions. See LPC17xx CMSIS-Compliant Standard 
Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

I2C_I2CONSET_AA = ((0x04)) 
I2C_I2CONSET_SI = ((0x08)) 
I2C_I2CONSET_STO = ((0x10)) 
I2C_I2CONSET_STA = ((0x20)) 
I2C_I2CONSET_I2EN = ((0x40)) 
I2C_I2CONCLR_AAC = ((1<<2))
I2C_I2CONCLR_SIC = ((1<<3))
I2C_I2CONCLR_STAC = ((1<<5))
I2C_I2CONCLR_I2ENC = ((1<<6))
I2C_STAT_CODE_BITMASK = ((0xF8))
I2C_I2STAT_NO_INF = ((0xF8))
I2C_I2STAT_M_TX_START = ((0x08))
I2C_I2STAT_M_TX_RESTART = ((0x10))
I2C_I2STAT_M_TX_SLAW_ACK = ((0x18))
I2C_I2STAT_M_TX_SLAW_NACK = ((0x20))
I2C_I2STAT_M_TX_DAT_ACK = ((0x28))
I2C_I2STAT_M_TX_DAT_NACK = ((0x30))
I2C_I2STAT_M_TX_ARB_LOST = ((0x38))
I2C_I2STAT_M_RX_START = ((0x08))
I2C_I2STAT_M_RX_RESTART = ((0x10))
I2C_I2STAT_M_RX_ARB_LOST = ((0x38))
I2C_I2STAT_M_RX_SLAR_ACK = ((0x40))
I2C_I2STAT_M_RX_SLAR_NACK = ((0x48))
I2C_I2STAT_M_RX_DAT_ACK = ((0x50))
I2C_I2STAT_M_RX_DAT_NACK = ((0x58))
I2C_I2STAT_S_RX_SLAW_ACK = ((0x60))
I2C_I2STAT_S_RX_ARB_LOST_M_SLA = ((0x68))
I2C_I2STAT_S_RX_GENCALL_ACK = ((0x70))
I2C_I2STAT_S_RX_ARB_LOST_M_GENCALL = ((0x78))
I2C_I2STAT_S_RX_PRE_SLA_DAT_ACK = ((0x80))
I2C_I2STAT_S_RX_PRE_SLA_DAT_NACK = ((0x88))
I2C_I2STAT_S_RX_PRE_GENCALL_DAT_ACK = ((0x90))
I2C_I2STAT_S_RX_PRE_GENCALL_DAT_NACK = ((0x98))
I2C_I2STAT_S_RX_STA_STO_SLVREC_SLVTRX = ((0xA0))
I2C_I2STAT_S_TX_SLAR_ACK = ((0xA8))
I2C_I2STAT_S_TX_ARB_LOST_M_SLA = ((0xB0))
I2C_I2STAT_S_TX_DAT_ACK = ((0xB8))
I2C_I2STAT_S_TX_DAT_NACK = ((0xC0))
I2C_I2STAT_S_TX_LAST_DAT_ACK = ((0xC8))
I2C_SLAVE_TIME_OUT = 0x10000
I2C_I2DAT_BITMASK = ((0xFF))
I2C_I2DAT_IDLE_CHAR = (0xFF)
I2C_I2MMCTRL_MM_ENA = ((1<<0))		
I2C_I2MMCTRL_ENA_SCL = ((1<<1))		
I2C_I2MMCTRL_MATCH_ALL = ((1<<2))		
I2C_I2MMCTRL_BITMASK = ((0x07))		
I2DATA_BUFFER_BITMASK = ((0xFF))
I2C_I2ADR_GC = ((1<<0))
I2C_I2ADR_BITMASK = ((0xFF))

def I2C_I2MASK_MASK(n):
	return ((n&0xFE))
	
I2C_I2SCLH_BITMASK = ((0xFFFF))
I2C_I2SCLL_BITMASK = ((0xFFFF))
I2C_SETUP_STATUS_ARBF = (1<<8)	
I2C_SETUP_STATUS_NOACKF = (1<<9)	
I2C_SETUP_STATUS_DONE = (1<<10)	
I2C_MONITOR_CFG_SCL_OUTPUT = I2C_I2MMCTRL_ENA_SCL		
I2C_MONITOR_CFG_MATCHALL = I2C_I2MMCTRL_MATCH_ALL

def PARAM_I2C_SLAVEADDR_CH(n):
	return ((n>=0) and (n<=3))
	
def PARAM_I2Cx(n):
	return (((n)==(LPC_I2C0)) or ((n)==(LPC_I2C1)) or ((n)==(LPC_I2C2)))
	
def PARAM_I2C_MONITOR_CFG(n):
	return ((n==I2C_MONITOR_CFG_SCL_OUTPUT) or (I2C_MONITOR_CFG_MATCHALL))
	
class I2C_M_SETUP_Type(cstruct):
	pass

class I2C_OWNSLAVEADDR_CFG_Type(cstruct):
	pass

class I2C_TRANSFER_OPT_Type:
	I2C_TRANSFER_POLLING = 0
	I2C_TRANSFER_INTERRUPT = 1

class I2C_S_SETUP_Type(cstruct):
	pass

def I2C_MonitorModeCmd(I2Cx, NewState):
	return robocaller("I2C_MonitorModeCmd", "void", I2Cx, NewState)

def I2C_IntCmd(I2Cx, NewState):
	return robocaller("I2C_IntCmd", "void", I2Cx, NewState)

def I2C_DeInit(I2Cx):
	return robocaller("I2C_DeInit", "void", I2Cx)

def I2C_SlaveHandler(I2Cx):
	return robocaller("I2C_SlaveHandler", "void", I2Cx)

def I2C_MonitorModeConfig(I2Cx, MonitorCfgType, NewState):
	return robocaller("I2C_MonitorModeConfig", "void", I2Cx, MonitorCfgType, NewState)

def I2C_MasterTransferData(I2Cx, TransferCfg, Opt):
	return robocaller("I2C_MasterTransferData", "Status", I2Cx, TransferCfg, Opt)

def I2C_SlaveTransferComplete(I2Cx):
	return robocaller("I2C_SlaveTransferComplete", "uint32_t", I2Cx)

def I2C_SlaveTransferData(I2Cx, TransferCfg, Opt):
	return robocaller("I2C_SlaveTransferData", "Status", I2Cx, TransferCfg, Opt)

def I2C_SetOwnSlaveAddr(I2Cx, OwnSlaveAddrConfigStruct):
	return robocaller("I2C_SetOwnSlaveAddr", "void", I2Cx, OwnSlaveAddrConfigStruct)

def I2C_MasterTransferComplete(I2Cx):
	return robocaller("I2C_MasterTransferComplete", "uint32_t", I2Cx)

def I2C_MasterHandler(I2Cx):
	return robocaller("I2C_MasterHandler", "void", I2Cx)

def I2C_MonitorHandler(I2Cx, buffer, size):
	return robocaller("I2C_MonitorHandler", "BOOL_8", I2Cx, buffer, size)

def I2C_Init(I2Cx, clockrate):
	return robocaller("I2C_Init", "void", I2Cx, clockrate)

def I2C_MonitorGetDatabuffer(I2Cx):
	return robocaller("I2C_MonitorGetDatabuffer", "uint8_t", I2Cx)

def I2C_GetLastStatusCode(I2Cx):
	return robocaller("I2C_GetLastStatusCode", "uint8_t", I2Cx)

def I2C_Cmd(I2Cx, NewState):
	return robocaller("I2C_Cmd", "void", I2Cx, NewState)

