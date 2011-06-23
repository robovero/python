"""CAN client library functions. See LPC17xx CMSIS-Compliant Standard 
Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

MSG_ENABLE = ((0))
MSG_DISABLE = ((1))
CAN1_CTRL = ((0))
CAN2_CTRL = ((1))

def PARAM_FULLCAN_IC(n):
  return  ((n==FULLCAN_IC0) or (n==FULLCAN_IC1))
  
ID_11 = 1
MAX_HW_FULLCAN_OBJ = 64
MAX_SW_FULLCAN_OBJ = 32
CAN_MOD_RM = ((1))
CAN_MOD_LOM = ((1<<1))
CAN_MOD_STM = ((1<<2))
CAN_MOD_TPM = ((1<<3))
CAN_MOD_SM = ((1<<4))
CAN_MOD_RPM = ((1<<5))
CAN_MOD_TM = ((1<<7))
CAN_CMR_TR = ((1))
CAN_CMR_AT = ((1<<1))
CAN_CMR_RRB = ((1<<2))
CAN_CMR_CDO = ((1<<3))
CAN_CMR_SRR = ((1<<4))
CAN_CMR_STB1 = ((1<<5))
CAN_CMR_STB2 = ((1<<6))
CAN_CMR_STB3 = ((1<<7))
CAN_GSR_RBS = ((1))
CAN_GSR_DOS = ((1<<1))
CAN_GSR_TBS = ((1<<2))
CAN_GSR_TCS = ((1<<3))
CAN_GSR_RS = ((1<<4))
CAN_GSR_TS = ((1<<5))
CAN_GSR_ES = ((1<<6))
CAN_GSR_BS = ((1<<7))

def CAN_GSR_RXERR(n):
  return  (((n&0xFF)<<16))
  
def CAN_GSR_TXERR(n):
  return  ((n&0xFF)<<24)
  
CAN_ICR_RI = ((1))
CAN_ICR_TI1 = ((1<<1))
CAN_ICR_EI = ((1<<2))
CAN_ICR_DOI = ((1<<3))
CAN_ICR_WUI = ((1<<4))
CAN_ICR_EPI = ((1<<5))
CAN_ICR_ALI = ((1<<6))
CAN_ICR_BEI = ((1<<7))
CAN_ICR_IDI = ((1<<8))
CAN_ICR_TI2 = ((1<<9))
CAN_ICR_TI3 = ((1<<10))

def CAN_ICR_ERRBIT(n):
  return  (((n&0x1F)<<16))
  
CAN_ICR_ERRDIR = ((1<<21))

def CAN_ICR_ERRC(n):
  return  (((n&0x3)<<22))
  
def CAN_ICR_ALCBIT(n):
  return  (((n&0xFF)<<24))
  
CAN_IER_RIE = ((1))
CAN_IER_TIE1 = ((1<<1))
CAN_IER_EIE = ((1<<2))
CAN_IER_DOIE = ((1<<3))
CAN_IER_WUIE = ((1<<4))
CAN_IER_EPIE = ((1<<5))
CAN_IER_ALIE = ((1<<6))
CAN_IER_BEIE = ((1<<7))
CAN_IER_IDIE = ((1<<8))
CAN_IER_TIE2 = ((1<<9))
CAN_IER_TIE3 = ((1<<10))

def CAN_BTR_BRP(n):
  return  ((n&0x3FF))
  
def CAN_BTR_SJM(n):
  return  (((n&0x3)<<14))
  
def CAN_BTR_TESG1(n):
  return  ((n&0xF)<<16)
  
def CAN_BTR_TESG2(n):
  return  ((n&0xF)<<20)
  
def CAN_BTR_SAM(n):
  return  ((1<<23))
  
def CAN_EWL_EWL(n):
  return  ((n&0xFF))

CAN_SR_RBS = ((1))
CAN_SR_DOS = ((1<<1))
CAN_SR_TBS1 = ((1<<2))
CAN_SR_TCS1 = ((1<<3))
CAN_SR_RS = ((1<<4))
CAN_SR_TS1 = ((1<<5))
CAN_SR_ES = ((1<<6))
CAN_SR_BS = ((1<<7))
CAN_SR_TBS2 = ((1<<10))
CAN_SR_TCS2 = ((1<<11))
CAN_SR_TS2 = ((1<<13))
CAN_SR_TBS3 = ((1<<18))
CAN_SR_TCS3 = ((1<<19))
CAN_SR_TS3 = ((1<<21))

def CAN_RFS_ID_INDEX(n):
  return  ((n&0x3FF))
  
CAN_RFS_BP = ((1<<10))

def CAN_RFS_DLC(n):
  return  ((n&0xF)<<16)
  
CAN_RFS_RTR = ((1<<30))
CAN_RFS_FF = ((1<<31))

def CAN_RID_ID_11(n):
  return  ((n&0x7FF))
  
def CAN_RID_ID_29(n):
  return  ((n&0x1FFFFFFF))
  
def CAN_RDA_DATA1(n):
  return  ((n&0xFF))
  
def CAN_RDA_DATA2(n):
  return  (((n&0xFF)<<8))
  
def CAN_RDA_DATA3(n):
  return  (((n&0xFF)<<16))
  
def CAN_RDA_DATA4(n):
  return  (((n&0xFF)<<24))
  
def CAN_RDB_DATA5(n):
  return  ((n&0xFF))
  
def CAN_RDB_DATA6(n):
  return  (((n&0xFF)<<8))
  
def CAN_RDB_DATA7(n):
  return  (((n&0xFF)<<16))
  
def CAN_RDB_DATA8(n):
  return  (((n&0xFF)<<24))
  
def CAN_TFI_PRIO(n):
  return  ((n&0xFF))
  
def CAN_TFI_DLC(n):
  return  (((n&0xF)<<16))
  
CAN_TFI_RTR = ((1<<30))
CAN_TFI_FF = ((1<<31))

def CAN_TID_ID11(n):
  return  ((n&0x7FF))
  
def CAN_TID_ID29(n):
  return  ((n&0x1FFFFFFF))
  
def CAN_TDA_DATA1(n):
  return  ((n&0xFF))
  
def CAN_TDA_DATA2(n):
  return  (((n&0xFF)<<8))
  
def CAN_TDA_DATA3(n):
  return  (((n&0xFF)<<16))
  
def CAN_TDA_DATA4(n):
  return  (((n&0xFF)<<24))
  
def CAN_TDA_DATA5(n):
  return  ((n&0xFF))
  
def CAN_TDA_DATA6(n):
  return  (((n&0xFF)<<8))
  
def CAN_TDA_DATA7(n):
  return  (((n&0xFF)<<16))
  
def CAN_TDA_DATA8(n):
  return  (((n&0xFF)<<24))
  
CAN1SLEEPCLR = ((1<<1))
CAN2SLEEPCLR = ((1<<2))
CAN_WAKEFLAGES_CAN1WAKE = ((1<<1))
CAN_WAKEFLAGES_CAN2WAKE = ((1<<2))
CAN_TSR_TS1 = ((1))
CAN_TSR_TS2 = ((1<<1))
CAN_TSR_TBS1 = ((1<<8))
CAN_TSR_TBS2 = ((1<<9))
CAN_TSR_TCS1 = ((1<<16))
CAN_TSR_TCS2 = ((1<<17))
CAN_RSR_RS1 = ((1))
CAN_RSR_RS2 = ((1<<1))
CAN_RSR_RB1 = ((1<<8))
CAN_RSR_RB2 = ((1<<9))
CAN_RSR_DOS1 = ((1<<16))
CAN_RSR_DOS2 = ((1<<17))
CAN_MSR_E1 = ((1))
CAN_MSR_E2 = ((1<<1))
CAN_MSR_BS1 = ((1<<8))
CAN_MSR_BS2 = ((1<<9))
CAN_AFMR_AccOff = ((1))
CAN_AFMR_AccBP = ((1<<1))
CAN_AFMR_eFCAN = ((1<<2))

def CAN_STT_sa(n):
  return  ((n&0x1FF)<<2)
  
def CAN_SFF_GRP_sa(n):
  return  (((n&0x3FF)<<2))
  
def CAN_EFF_sa(n):
  return  (((n&0x1FF)<<2))
  
def CAN_Eff_GRP_sa(n):
  return  (((n&0x3FF)<<2))
  
def CAN_EndofTable(n):
  return  (((n&0x3FF)<<2))
  
def CAN_LUTerrAd(n):
  return  (((n&0x1FF)<<2))
  
CAN_LUTerr = ((1))
CAN_FCANIE = ((1))

def CAN_FCANIC0_IntPnd(n):
  return  ((1<<n))
  
def CAN_FCANIC1_IntPnd(n):
  return  ((1<<(n-32)))
  
def PARAM_CANx(x):
  return  (((x)==(LPC_CAN1)) or ((x)==(LPC_CAN2)))

def PARAM_CANAFx(x):
  return  ((x)== (LPC_CANAF))
  
def PARAM_CANAFRAMx(x):
  return  ((x)== LPC_CANAF_RAM)
  
def PARAM_CANCRx(x):
  return  ((x)==(LPC_CANCR))
  
def PARAM_I2S_DATA(data):
  return  ((data>=0) and (data <= 0xFFFFFFFF))
  
def PRAM_I2S_FREQ(freq):
  return  ((freq>=16000) and (freq <= 96000))
  
def PARAM_ID_11(n):
  return  ((n>>11)==0) 
  
def PARAM_ID_29(n):
  return  ((n>>29)==0) 
  
def PARAM_DLC(n):
  return  ((n>>4)==0) 
  
def PARAM_ID_FORMAT(n):
  return  ((n==STD_ID_FORMAT) or (n==EXT_ID_FORMAT))
  
def PARAM_GRP_ID(x, y):
	return ((x<=y))
	
def PARAM_FRAME_TYPE(n):
  return  ((n==DATA_FRAME) or (n==REMOTE_FRAME))
  
def PARAM_CTRL_STS_TYPE(n):
  return  (
		(n==CANCTRL_GLOBAL_STS) or (n==CANCTRL_INT_CAP)  
		or (n==CANCTRL_ERR_WRN) or (n==CANCTRL_STS)
		)

def PARAM_CR_STS_TYPE(n):
  return  ((n==CANCR_TX_STS) or (n==CANCR_RX_STS) or (n==CANCR_MS))

def PARAM_AFMODE_TYPE(n):
  return  (
		(n==CAN_Normal) or (n==CAN_AccOff)  
		or (n==CAN_AccBP) or (n==CAN_eFCAN)
		)

def PARAM_MODE_TYPE(n):
  return  (
		(n==CAN_OPERATING_MODE) or (n==CAN_RESET_MODE)  
		or (n==CAN_LISTENONLY_MODE) or (n==CAN_SELFTEST_MODE)  
		or (n==CAN_TXPRIORITY_MODE) or (n==CAN_SLEEP_MODE)  
		or (n==CAN_RXPOLARITY_MODE) or (n==CAN_TEST_MODE)
		)

def PARAM_CTRL(n):
  return  ((n==CAN1_CTRL)|(n==CAN2_CTRL))
  
def PARAM_MSG_DISABLE(n):
  return  ((n==MSG_ENABLE)|(n==MSG_DISABLE))
  
def PARAM_INT_EN_TYPE(n):
  return  (
		(n==CANINT_RIE) or (n==CANINT_TIE1)  
		or (n==CANINT_EIE) or (n==CANINT_DOIE)  
		or (n==CANINT_WUIE) or (n==CANINT_EPIE)  
		or (n==CANINT_ALIE) or (n==CANINT_BEIE)  
		or (n==CANINT_IDIE) or (n==CANINT_TIE2)  
		or (n==CANINT_TIE3) or (n==CANINT_FCE)
		)

def PARAM_AFLUT_ENTRY_TYPE(n):
  return  (
		(n==FULLCAN_ENTRY) or (n==EXPLICIT_STANDARD_ENTRY) 
		or (n==GROUP_STANDARD_ENTRY) or (n==EXPLICIT_EXTEND_ENTRY)  
		or (n==GROUP_EXTEND_ENTRY)
		)

def PARAM_POSITION(n):
  return  ((n>=0) and (n<512))
class SFF_Entry(cstruct):
	pass

class CAN_MSG_Type(cstruct):
	pass

class CAN_ERROR:
	CAN_OK = 1
	CAN_OBJECTS_FULL_ERROR = 1
	CAN_FULL_OBJ_NOT_RCV = 2
	CAN_NO_RECEIVE_DATA = 3
	CAN_AF_ENTRY_ERROR = 4
	CAN_CONFLICT_ID_ERROR = 5
	CAN_ENTRY_NOT_EXIT_ERROR = 6

class CAN_AFMODE_Type:
	CAN_Normal = 0
	CAN_AccOff = 1
	CAN_AccBP = 2
	CAN_eFCAN = 3

class CAN_CR_STS_Type:
	CANCR_TX_STS = 0
	CANCR_RX_STS = 1
	CANCR_MS = 2

class CAN_CTRL_STS_Type:
	CANCTRL_GLOBAL_STS = 0
	CANCTRL_INT_CAP = 1
	CANCTRL_ERR_WRN = 2
	CANCTRL_STS = 3

class AFLUT_ENTRY_Type:
	FULLCAN_ENTRY = 0
	EXPLICIT_STANDARD_ENTRY = 1
	GROUP_STANDARD_ENTRY = 2
	EXPLICIT_EXTEND_ENTRY = 3
	GROUP_EXTEND_ENTRY = 4

class CAN_ID_FORMAT_Type:
	STD_ID_FORMAT = 0
	EXT_ID_FORMAT = 1

class FullCAN_Entry(cstruct):
	pass

class EFF_GPR_Entry(cstruct):
	pass

class CAN_INT_EN_Type:
	CANINT_RIE = 0
	CANINT_TIE1 = 1
	CANINT_EIE = 2
	CANINT_DOIE = 3
	CANINT_WUIE = 4
	CANINT_EPIE = 5
	CANINT_ALIE = 6
	CANINT_BEIE = 7
	CANINT_IDIE = 8
	CANINT_TIE2 = 9
	CANINT_TIE3 = 10
	CANINT_FCE = 11

class CAN_PinCFG_Type(cstruct):
	pass

class CAN_FRAME_Type:
	DATA_FRAME = 0
	REMOTE_FRAME = 1

class FullCAN_IC_Type:
	FULLCAN_IC0 = 0
	FULLCAN_IC1 = 1

class SFF_GPR_Entry(cstruct):
	pass

class CAN_MODE_Type:
	CAN_OPERATING_MODE = 0
	CAN_RESET_MODE = 1
	CAN_LISTENONLY_MODE = 2
	CAN_SELFTEST_MODE = 3
	CAN_TXPRIORITY_MODE = 4
	CAN_SLEEP_MODE = 5
	CAN_RXPOLARITY_MODE = 6
	CAN_TEST_MODE = 7

class EFF_Entry(cstruct):
	pass

class AF_SectionDef(cstruct):
	pass

def CAN_SetCommand(CANx, CMRType):
	return robocaller("CAN_SetCommand", "void", CANx, CMRType)

def CAN_IRQCmd(CANx, arg, NewState):
	return robocaller("CAN_IRQCmd", "void", CANx, arg, NewState)

def FCAN_ReadObj(CANAFx, CAN_Msg):
	return robocaller("FCAN_ReadObj", "CAN_ERROR", CANAFx, CAN_Msg)

def CAN_Init(CANx, baudrate):
	return robocaller("CAN_Init", "void", CANx, baudrate)

def CAN_ModeConfig(CANx, mode, NewState):
	return robocaller("CAN_ModeConfig", "void", CANx, mode, NewState)

def CAN_LoadExplicitEntry(CANx, ID, format):
	return robocaller("CAN_LoadExplicitEntry", "CAN_ERROR", CANx, ID, format)

def CAN_LoadFullCANEntry(CANx, ID):
	return robocaller("CAN_LoadFullCANEntry", "CAN_ERROR", CANx, ID)

def CAN_IntGetStatus(CANx):
	return robocaller("CAN_IntGetStatus", "uint32_t", CANx)

def CAN_SetAFMode(CANAFx, AFmode):
	return robocaller("CAN_SetAFMode", "void", CANAFx, AFmode)

def CAN_SendMsg(CANx, CAN_Msg):
	return robocaller("CAN_SendMsg", "Status", CANx, CAN_Msg)

def CAN_LoadGroupEntry(CANx, lowerID, upperID, format):
	return robocaller("CAN_LoadGroupEntry", "CAN_ERROR", CANx, lowerID, upperID, format)

def CAN_SetupAFLUT(CANAFx, AFSection):
	return robocaller("CAN_SetupAFLUT", "CAN_ERROR", CANAFx, AFSection)

def CAN_GetCTRLStatus(CANx, arg):
	return robocaller("CAN_GetCTRLStatus", "uint32_t", CANx, arg)

def CAN_DeInit(CANx):
	return robocaller("CAN_DeInit", "void", CANx)

def CAN_ReceiveMsg(CANx, CAN_Msg):
	return robocaller("CAN_ReceiveMsg", "Status", CANx, CAN_Msg)

def CAN_FullCANPendGetStatus(CANAFx, type):
	return robocaller("CAN_FullCANPendGetStatus", "uint32_t", CANAFx, type)

def CAN_GetCRStatus(CANCRx, arg):
	return robocaller("CAN_GetCRStatus", "uint32_t", CANCRx, arg)

def CAN_RemoveEntry(EntryType, position):
	return robocaller("CAN_RemoveEntry", "CAN_ERROR", EntryType, position)

def CAN_FullCANIntGetStatus(CANAFx):
	return robocaller("CAN_FullCANIntGetStatus", "IntStatus", CANAFx)

