"""Quadrature encoder interface client library functions. See LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library documentation."""

from internals import robocaller, cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

QEI_DIRINV_NONE = (0)		
QEI_DIRINV_CMPL = (1)		
QEI_SIGNALMODE_QUAD = (0)		
QEI_SIGNALMODE_CLKDIR = (1)		
QEI_CAPMODE_2X = (0)		
QEI_CAPMODE_4X = (1)		
QEI_INVINX_NONE = (0)		
QEI_INVINX_EN = (1)		
QEI_TIMERRELOAD_TICKVAL = (0)	
QEI_TIMERRELOAD_USVAL = (1)	
QEI_STATUS_DIR = (1<<0)	
QEI_COMPPOS_CH_0 = (0)		
QEI_COMPPOS_CH_1 = (1)		
QEI_COMPPOS_CH_2 = (2)		
QEI_INTFLAG_INX_Int = (1<<0)	
QEI_INTFLAG_TIM_Int = (1<<1)	
QEI_INTFLAG_VELC_Int = (1<<2)	
QEI_INTFLAG_DIR_Int = (1<<3)	
QEI_INTFLAG_ERR_Int = (1<<4)	
QEI_INTFLAG_ENCLK_Int = (1<<5)	
QEI_INTFLAG_POS0_Int = (1<<6)	
QEI_INTFLAG_POS1_Int = (1<<7)	
QEI_INTFLAG_POS2_Int = (1<<8)	
QEI_INTFLAG_REV_Int = (1<<9)	
QEI_INTFLAG_POS0REV_Int = (1<<10)	
QEI_INTFLAG_POS1REV_Int = (1<<11)	
QEI_INTFLAG_POS2REV_Int = (1<<12)	
QEI_CON_RESP = (1<<0)		
QEI_CON_RESPI = (1<<1)		
QEI_CON_RESV = (1<<2)		
QEI_CON_RESI = (1<<3)		
QEI_CON_BITMASK = (0x0F)		
QEI_CONF_DIRINV = (1<<0)		
QEI_CONF_SIGMODE = (1<<1)		
QEI_CONF_CAPMODE = (1<<2)		
QEI_CONF_INVINX = (1<<3)		
QEI_CONF_BITMASK = (0x0F)		
QEI_STAT_DIR = (1<<0)		
QEI_STAT_BITMASK = (1<<0)		
QEI_INTSTAT_INX_Int = (1<<0)	
QEI_INTSTAT_TIM_Int = (1<<1)	
QEI_INTSTAT_VELC_Int = (1<<2)	
QEI_INTSTAT_DIR_Int = (1<<3)	
QEI_INTSTAT_ERR_Int = (1<<4)	
QEI_INTSTAT_ENCLK_Int = (1<<5)	
QEI_INTSTAT_POS0_Int = (1<<6)	
QEI_INTSTAT_POS1_Int = (1<<7)	
QEI_INTSTAT_POS2_Int = (1<<8)	
QEI_INTSTAT_REV_Int = (1<<9)	
QEI_INTSTAT_POS0REV_Int = (1<<10)	
QEI_INTSTAT_POS1REV_Int = (1<<11)	
QEI_INTSTAT_POS2REV_Int = (1<<12)	
QEI_INTSTAT_BITMASK = (0x1FFF)	
QEI_INTSET_INX_Int = (1<<0)	
QEI_INTSET_TIM_Int = (1<<1)	
QEI_INTSET_VELC_Int = (1<<2)	
QEI_INTSET_DIR_Int = (1<<3)	
QEI_INTSET_ERR_Int = (1<<4)	
QEI_INTSET_ENCLK_Int = (1<<5)	
QEI_INTSET_POS0_Int = (1<<6)	
QEI_INTSET_POS1_Int = (1<<7)	
QEI_INTSET_POS2_Int = (1<<8)	
QEI_INTSET_REV_Int = (1<<9)	
QEI_INTSET_POS0REV_Int = (1<<10)	
QEI_INTSET_POS1REV_Int = (1<<11)	
QEI_INTSET_POS2REV_Int = (1<<12)	
QEI_INTSET_BITMASK = (0x1FFF)	
QEI_INTCLR_INX_Int = (1<<0)	
QEI_INTCLR_TIM_Int = (1<<1)	
QEI_INTCLR_VELC_Int = (1<<2)	
QEI_INTCLR_DIR_Int = (1<<3)	
QEI_INTCLR_ERR_Int = (1<<4)	
QEI_INTCLR_ENCLK_Int = (1<<5)	
QEI_INTCLR_POS0_Int = (1<<6)	
QEI_INTCLR_POS1_Int = (1<<7)	
QEI_INTCLR_POS2_Int = (1<<8)	
QEI_INTCLR_REV_Int = (1<<9)	
QEI_INTCLR_POS0REV_Int = (1<<10)	
QEI_INTCLR_POS1REV_Int = (1<<11)	
QEI_INTCLR_POS2REV_Int = (1<<12)	
QEI_INTCLR_BITMASK = (0x1FFF)	
QEI_INTEN_INX_Int = (1<<0)	
QEI_INTEN_TIM_Int = (1<<1)	
QEI_INTEN_VELC_Int = (1<<2)	
QEI_INTEN_DIR_Int = (1<<3)	
QEI_INTEN_ERR_Int = (1<<4)	
QEI_INTEN_ENCLK_Int = (1<<5)	
QEI_INTEN_POS0_Int = (1<<6)	
QEI_INTEN_POS1_Int = (1<<7)	
QEI_INTEN_POS2_Int = (1<<8)	
QEI_INTEN_REV_Int = (1<<9)	
QEI_INTEN_POS0REV_Int = (1<<10)	
QEI_INTEN_POS1REV_Int = (1<<11)	
QEI_INTEN_POS2REV_Int = (1<<12)	
QEI_INTEN_BITMASK = (0x1FFF)	
QEI_IESET_INX_Int = (1<<0)	
QEI_IESET_TIM_Int = (1<<1)	
QEI_IESET_VELC_Int = (1<<2)	
QEI_IESET_DIR_Int = (1<<3)	
QEI_IESET_ERR_Int = (1<<4)	
QEI_IESET_ENCLK_Int = (1<<5)	
QEI_IESET_POS0_Int = (1<<6)	
QEI_IESET_POS1_Int = (1<<7)	
QEI_IESET_POS2_Int = (1<<8)	
QEI_IESET_REV_Int = (1<<9)	
QEI_IESET_POS0REV_Int = (1<<10)	
QEI_IESET_POS1REV_Int = (1<<11)	
QEI_IESET_POS2REV_Int = (1<<12)	
QEI_IESET_BITMASK = (0x1FFF)	
QEI_IECLR_INX_Int = (1<<0)	
QEI_IECLR_TIM_Int = (1<<1)	
QEI_IECLR_VELC_Int = (1<<2)	
QEI_IECLR_DIR_Int = (1<<3)	
QEI_IECLR_ERR_Int = (1<<4)	
QEI_IECLR_ENCLK_Int = (1<<5)	
QEI_IECLR_POS0_Int = (1<<6)	
QEI_IECLR_POS1_Int = (1<<7)	
QEI_IECLR_POS2_Int = (1<<8)	
QEI_IECLR_REV_Int = (1<<9)	
QEI_IECLR_POS0REV_Int = (1<<10)	
QEI_IECLR_POS1REV_Int = (1<<11)	
QEI_IECLR_POS2REV_Int = (1<<12)	
QEI_IECLR_BITMASK = (0x1FFF)
QEI_RESET_POS = QEI_CON_RESP		
QEI_RESET_POSOnIDX = QEI_CON_RESPI		
QEI_RESET_VEL = QEI_CON_RESV		
QEI_RESET_IDX = QEI_CON_RESI		

def PARAM_QEIx(n):
  return (n==LPC_QEI)

def PARAM_QEI_RESET(n):
  return (
		(n==QEI_CON_RESP) 
		or (n==QEI_RESET_POSOnIDX) 
		or (n==QEI_RESET_VEL) 
		or (n==QEI_RESET_IDX)
		)

def PARAM_QEI_DIRINV(n):
  return ((n==QEI_DIRINV_NONE) or (n==QEI_DIRINV_CMPL))

def PARAM_QEI_SIGNALMODE(n):
  return ((n==QEI_SIGNALMODE_QUAD) or (n==QEI_SIGNALMODE_CLKDIR))

def PARAM_QEI_CAPMODE(n):
  return ((n==QEI_CAPMODE_2X) or (n==QEI_CAPMODE_4X))

def PARAM_QEI_INVINX(n):
  return ((n==QEI_INVINX_NONE) or (n==QEI_INVINX_EN))

def PARAM_QEI_TIMERRELOAD(n):
  return ((n==QEI_TIMERRELOAD_TICKVAL) or (n==QEI_TIMERRELOAD_USVAL))

def PARAM_QEI_STATUS(n):
  return (n==QEI_STATUS_DIR)

def PARAM_QEI_COMPPOS_CH(n):
  return (
		(n==QEI_COMPPOS_CH_0) 
		or (n==QEI_COMPPOS_CH_1) 
		or (n==QEI_COMPPOS_CH_2)
		)

def PARAM_QEI_INTFLAG(n):
  return (
		(n==QEI_INTFLAG_INX_Int) 
		or (n==QEI_INTFLAG_TIM_Int) 
		or (n==QEI_INTFLAG_VELC_Int) 
		or (n==QEI_INTFLAG_DIR_Int) 
		or (n==QEI_INTFLAG_ERR_Int) 
		or (n==QEI_INTFLAG_ENCLK_Int) 
		or (n==QEI_INTFLAG_POS0_Int) 
		or (n==QEI_INTFLAG_POS1_Int) 
		or (n==QEI_INTFLAG_POS2_Int) 
		or (n==QEI_INTFLAG_REV_Int) 
		or (n==QEI_INTFLAG_POS0REV_Int) 
		or (n==QEI_INTFLAG_POS1REV_Int) 
		or (n==QEI_INTFLAG_POS2REV_Int)
		)
		
class QEI_CFG_Type(cstruct):
	pass

class QEI_RELOADCFG_Type(cstruct):
	pass

def QEI_GetTimer(QEIx):
	return robocaller("QEI_GetTimer", "uint32_t", QEIx)

def QEI_DeInit(QEIx):
	return robocaller("QEI_DeInit", "void", QEIx)

def QEI_GetPosition(QEIx):
	return robocaller("QEI_GetPosition", "uint32_t", QEIx)

def QEI_GetStatus(QEIx, ulFlagType):
	return robocaller("QEI_GetStatus", "FlagStatus", QEIx, ulFlagType)

def QEI_Reset(QEIx, ulResetType):
	return robocaller("QEI_Reset", "void", QEIx, ulResetType)

def QEI_SetMaxPosition(QEIx, ulMaxPos):
	return robocaller("QEI_SetMaxPosition", "void", QEIx, ulMaxPos)

def QEI_GetVelocity(QEIx):
	return robocaller("QEI_GetVelocity", "uint32_t", QEIx)

def QEI_GetVelocityCap(QEIx):
	return robocaller("QEI_GetVelocityCap", "uint32_t", QEIx)

def QEI_SetPositionComp(QEIx, bPosCompCh, ulPosComp):
	return robocaller("QEI_SetPositionComp", "void", QEIx, bPosCompCh, ulPosComp)

def QEI_SetDigiFilter(QEIx, ulSamplingPulse):
	return robocaller("QEI_SetDigiFilter", "void", QEIx, ulSamplingPulse)

def QEI_IntSet(QEIx, ulIntType):
	return robocaller("QEI_IntSet", "void", QEIx, ulIntType)

def QEI_GetIndex(QEIx):
	return robocaller("QEI_GetIndex", "uint32_t", QEIx)

def QEI_SetTimerReload(QEIx, QEIReloadStruct):
	return robocaller("QEI_SetTimerReload", "void", QEIx, QEIReloadStruct)

def QEI_ConfigStructInit(QIE_InitStruct):
	return robocaller("QEI_ConfigStructInit", "void", QIE_InitStruct)

def QEI_SetVelocityComp(QEIx, ulVelComp):
	return robocaller("QEI_SetVelocityComp", "void", QEIx, ulVelComp)

def QEI_Init(QEIx, QEI_ConfigStruct):
	return robocaller("QEI_Init", "void", QEIx, QEI_ConfigStruct)

def QEI_IntCmd(QEIx, ulIntType, NewState):
	return robocaller("QEI_IntCmd", "void", QEIx, ulIntType, NewState)

def QEI_IntClear(QEIx, ulIntType):
	return robocaller("QEI_IntClear", "void", QEIx, ulIntType)

def QEI_GetIntStatus(QEIx, ulIntType):
	return robocaller("QEI_GetIntStatus", "FlagStatus", QEIx, ulIntType)

def QEI_CalculateRPM(QEIx, ulVelCapValue, ulPPR):
	return robocaller("QEI_CalculateRPM", "uint32_t", QEIx, ulVelCapValue, ulPPR)

def QEI_SetIndexComp(QEIx, ulIndexComp):
	return robocaller("QEI_SetIndexComp", "void", QEIx, ulIndexComp)

