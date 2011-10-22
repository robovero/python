"""CAN client library functions. Find implementation details in LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

# CAN Public Macros
MSG_ENABLE = ((0))
MSG_DISABLE = ((1))
CAN1_CTRL = ((0))
CAN2_CTRL = ((1))
def PARAM_FULLCAN_IC(n):
  return  ((n==FULLCAN_IC0) or (n==FULLCAN_IC1))
ID_11 = 1
MAX_HW_FULLCAN_OBJ = 64
MAX_SW_FULLCAN_OBJ = 32

# CAN Private Macros

# Macro defines for CAN Mode Register
# CAN Reset mode
CAN_MOD_RM = ((1))
# CAN Listen Only Mode
CAN_MOD_LOM = ((1<<1))
# CAN Self Test mode
CAN_MOD_STM = ((1<<2))
# CAN Transmit Priority mode
CAN_MOD_TPM = ((1<<3))
# CAN Sleep mode
CAN_MOD_SM = ((1<<4))
# CAN Receive Polarity mode
CAN_MOD_RPM = ((1<<5))
# CAN Test mode
CAN_MOD_TM = ((1<<7))

# Macro defines for CAN Command Register
# CAN Transmission Request
CAN_CMR_TR = ((1))
# CAN Abort Transmission
CAN_CMR_AT = ((1<<1))
# CAN Release Receive Buffer
CAN_CMR_RRB = ((1<<2))
# AN Clear Data Overrun
CAN_CMR_CDO = ((1<<3))
# CAN Self Reception Request
CAN_CMR_SRR = ((1<<4))
# CAN Select Tx Buffer 1
CAN_CMR_STB1 = ((1<<5))
# CAN Select Tx Buffer 2
CAN_CMR_STB2 = ((1<<6))
#  CAN Select Tx Buffer 3
CAN_CMR_STB3 = ((1<<7))

# Macro defines for CAN Global Status Register
# CAN Receive Buffer Status
CAN_GSR_RBS = ((1))
# CAN Data Overrun Status
CAN_GSR_DOS = ((1<<1))
# CAN Transmit Buffer Status
CAN_GSR_TBS = ((1<<2))
# CAN Transmit Complete Status
CAN_GSR_TCS = ((1<<3))
# CAN Receive Status
CAN_GSR_RS = ((1<<4))
# CAN Transmit Status
CAN_GSR_TS = ((1<<5))
# CAN Error Status
CAN_GSR_ES = ((1<<6))
# CAN Bus Status
CAN_GSR_BS = ((1<<7))

def CAN_GSR_RXERR(n):
  '''CAN Current value of the Rx Error Counter.
  '''
  return  (((n&0xFF)<<16))
  
def CAN_GSR_TXERR(n):
  '''CAN Current value of the Tx Error Counter.
  '''
  return  ((n&0xFF)<<24)

# Macro defines for CAN Interrupt and Capture Registe  
# CAN Receive Interrupt
CAN_ICR_RI = ((1))
# CAN Transmit Interrupt 1
CAN_ICR_TI1 = ((1<<1))
# CAN Error Warning Interrupt
CAN_ICR_EI = ((1<<2))
# CAN Data Overrun Interrupt
CAN_ICR_DOI = ((1<<3))
# CAN Wake-Up Interrupt 
CAN_ICR_WUI = ((1<<4))
# CAN Error Passive Interrupt
CAN_ICR_EPI = ((1<<5))
# CAN Arbitration Lost Interrupt
CAN_ICR_ALI = ((1<<6))
# CAN Bus Error Interrupt
CAN_ICR_BEI = ((1<<7))
# CAN ID Ready Interrupt
CAN_ICR_IDI = ((1<<8))
# CAN Transmit Interrupt 2
CAN_ICR_TI2 = ((1<<9))
# CAN Transmit Interrupt 3
CAN_ICR_TI3 = ((1<<10))

def CAN_ICR_ERRBIT(n):
  '''CAN Error Code Capture.
  '''
  return  (((n&0x1F)<<16))
  
# CAN Error Direction
CAN_ICR_ERRDIR = ((1<<21))

def CAN_ICR_ERRC(n):
  '''CAN Error Capture.
  '''
  return  (((n&0x3)<<22))
  
def CAN_ICR_ALCBIT(n):
  '''CAN Arbitration Lost Capture.
  '''
  return  (((n&0xFF)<<24))
  
# CAN Receive Interrupt Enable
CAN_IER_RIE = ((1))
# CAN Transmit Interrupt Enable for buffer 1
CAN_IER_TIE1 = ((1<<1))
# CAN Error Warning Interrupt Enable
CAN_IER_EIE = ((1<<2))
# CAN Data Overrun Interrupt Enable
CAN_IER_DOIE = ((1<<3))
# CAN Wake-Up Interrupt Enable
CAN_IER_WUIE = ((1<<4))
# CAN Error Passive Interrupt Enable
CAN_IER_EPIE = ((1<<5))
# CAN Arbitration Lost Interrupt Enable
CAN_IER_ALIE = ((1<<6))
# CAN Bus Error Interrupt Enable
CAN_IER_BEIE = ((1<<7))
# CAN ID Ready Interrupt Enable
CAN_IER_IDIE = ((1<<8))
# CAN Transmit Enable Interrupt for Buffer 2
CAN_IER_TIE2 = ((1<<9))
# CAN Transmit Enable Interrupt for Buffer 3
CAN_IER_TIE3 = ((1<<10))

# Macro defines for CAN Bus Timing Register
def CAN_BTR_BRP(n):
  '''CAN Baudrate Prescaler.
  '''
  return  ((n&0x3FF))
  
def CAN_BTR_SJM(n):
  '''CAN Synchronization Jump Width.
  '''
  return  (((n&0x3)<<14))
  
def CAN_BTR_TESG1(n):
  '''CAN Time Segment 1.
  '''
  return  ((n&0xF)<<16)
  
def CAN_BTR_TESG2(n):
  '''CAN Time Segment 2.
  '''
  return  ((n&0xF)<<20)
  
def CAN_BTR_SAM(n):
  '''CAN Sampling.
  '''
  return  ((1<<23))

# Macro defines for CAN Error Warning Limit Register
def CAN_EWL_EWL(n):
  '''CAN Error Warning Limit.
  '''
  return  ((n&0xFF))

# Macro defines for CAN Status Register
# CAN Receive Buffer Status
CAN_SR_RBS = ((1))
# CAN Data Overrun Status
CAN_SR_DOS = ((1<<1))
# CAN Transmit Buffer Status 1
CAN_SR_TBS1 = ((1<<2))
# CAN Transmission Complete Status of Buffer 1
CAN_SR_TCS1 = ((1<<3))
# CAN Receive Status
CAN_SR_RS = ((1<<4))
# CAN Transmit Status 1
CAN_SR_TS1 = ((1<<5))
# CAN Error Status
CAN_SR_ES = ((1<<6))
# CAN Bus Status
CAN_SR_BS = ((1<<7))
# CAN Transmit Buffer Status 2
CAN_SR_TBS2 = ((1<<10))
# CAN Transmission Complete Status of Buffer 2
CAN_SR_TCS2 = ((1<<11))
# CAN Transmit Status 2
CAN_SR_TS2 = ((1<<13))
# CAN Transmit Buffer Status 2
CAN_SR_TBS3 = ((1<<18))
# CAN Transmission Complete Status of Buffer 2
CAN_SR_TCS3 = ((1<<19))
# CAN Transmit Status 2
CAN_SR_TS3 = ((1<<21))

# Macro defines for CAN Receive Frame Status Register
def CAN_RFS_ID_INDEX(n):
  '''CAN ID Index.
  '''
  return  ((n&0x3FF))
  
# CAN Bypass
CAN_RFS_BP = ((1<<10))

def CAN_RFS_DLC(n):
  '''CAN Data Length Code.
  '''
  return  ((n&0xF)<<16)
  
# CAN Remote Transmission Request
CAN_RFS_RTR = ((1<<30))
# CAN control 11 bit or 29 bit Identifier
CAN_RFS_FF = ((1<<31))

# Macro defines for CAN Receive Identifier Register
def CAN_RID_ID_11(n):
  '''CAN 11 bit Identifier.
  '''
  return  ((n&0x7FF))
  
def CAN_RID_ID_29(n):
  '''CAN 29 bit Identifier.
  '''
  return  ((n&0x1FFFFFFF))

# Macro defines for CAN Receive Data A Register  
def CAN_RDA_DATA1(n):
  '''CAN Receive Data 1.
  '''
  return  ((n&0xFF))
  
def CAN_RDA_DATA2(n):
  '''CAN Receive Data 2.
  '''
  return  (((n&0xFF)<<8))
  
def CAN_RDA_DATA3(n):
  '''CAN Receive Data 3.
  '''
  return  (((n&0xFF)<<16))
  
def CAN_RDA_DATA4(n):
  '''CAN Receive Data 4.
  '''
  return  (((n&0xFF)<<24))

# Macro defines for CAN Receive Data B Register  
def CAN_RDB_DATA5(n):
  '''CAN Receive Data 5.
  '''
  return  ((n&0xFF))
  
def CAN_RDB_DATA6(n):
  '''CAN Receive Data 6.
  '''
  return  (((n&0xFF)<<8))
  
def CAN_RDB_DATA7(n):
  '''CAN Receive Data 7.
  '''
  return  (((n&0xFF)<<16))
  
def CAN_RDB_DATA8(n):
  '''CAN Receive Data 8.
  '''
  return  (((n&0xFF)<<24))

# Macro defines for CAN Transmit Frame Information Register  
def CAN_TFI_PRIO(n):
  '''CAN Priority.
  '''
  return  ((n&0xFF))
  
def CAN_TFI_DLC(n):
  '''CAN Data Length Code.
  '''
  return  (((n&0xF)<<16))
  
# CAN Remote Frame Transmission
CAN_TFI_RTR = ((1<<30))
# CAN control 11-bit or 29-bit Identifier
CAN_TFI_FF = ((1<<31))

# Macro defines for CAN Transmit Identifier Register
def CAN_TID_ID11(n):
  '''CAN 11-bit Identifier.
  '''
  return  ((n&0x7FF))
  
def CAN_TID_ID29(n):
  '''CAN 29-bit Identifier.
  '''
  return  ((n&0x1FFFFFFF))

# Macro defines for CAN Transmit Data A Register  
def CAN_TDA_DATA1(n):
  '''CAN Transmit Data 1.
  '''
  return  ((n&0xFF))
  
def CAN_TDA_DATA2(n):
  '''CAN Transmit Data 2.
  '''
  return  (((n&0xFF)<<8))
  
def CAN_TDA_DATA3(n):
  '''CAN Transmit Data 3.
  '''
  return  (((n&0xFF)<<16))
  
def CAN_TDA_DATA4(n):
  '''CAN Transmit Data 4.
  '''
  return  (((n&0xFF)<<24))
  
# Macro defines for CAN Transmit Data B Register
def CAN_TDA_DATA5(n):
  '''CAN Transmit Data 5.
  '''
  return  ((n&0xFF))
  
def CAN_TDA_DATA6(n):
  '''CAN Transmit Data 6.
  '''
  return  (((n&0xFF)<<8))
  
def CAN_TDA_DATA7(n):
  '''CAN Transmit Data 7.
  '''
  return  (((n&0xFF)<<16))
  
def CAN_TDA_DATA8(n):
  '''CAN Transmit Data 8.
  '''
  return  (((n&0xFF)<<24))
  
# Macro defines for CAN Sleep Clear Register
# CAN1 Sleep mode
CAN1SLEEPCLR = ((1<<1))
# CAN2 Sleep Mode
CAN2SLEEPCLR = ((1<<2))

# Macro defines for CAN Wake up Flags Register
# CAN1 Sleep mode
CAN_WAKEFLAGES_CAN1WAKE = ((1<<1))
# CAN2 Sleep Mode
CAN_WAKEFLAGES_CAN2WAKE = ((1<<2))

# Macro defines for Central transmit Status Register
# CAN Transmit 1
CAN_TSR_TS1 = ((1))
# CAN Transmit 2
CAN_TSR_TS2 = ((1<<1))
# CAN Transmit Buffer Status 1
CAN_TSR_TBS1 = ((1<<8))
# CAN Transmit Buffer Status 2
CAN_TSR_TBS2 = ((1<<9))
# CAN Transmission Complete Status 1
CAN_TSR_TCS1 = ((1<<16))
# CAN Transmission Complete Status 2
CAN_TSR_TCS2 = ((1<<17))

# Macro defines for Central Receive Status Register
# CAN Receive Status 1
CAN_RSR_RS1 = ((1))
#  CAN Receive Status 2
CAN_RSR_RS2 = ((1<<1))
# CAN Receive Buffer Status 1
CAN_RSR_RB1 = ((1<<8))
# CAN Receive Buffer Status 2
CAN_RSR_RB2 = ((1<<9))
# CAN Data Overrun Status 1
CAN_RSR_DOS1 = ((1<<16))
# CAN Data Overrun Status 2
CAN_RSR_DOS2 = ((1<<17))

# Macro defines for Central Miscellaneous Status Register
# Same CAN Error Status in CAN1GSR
CAN_MSR_E1 = ((1))
# Same CAN Error Status in CAN2GSR
CAN_MSR_E2 = ((1<<1))
# Same CAN Bus Status in CAN1GSR
CAN_MSR_BS1 = ((1<<8))
# Same CAN Bus Status in CAN2GSR
CAN_MSR_BS2 = ((1<<9))

# Macro defines for Acceptance Filter Mode Register
# CAN Acceptance Filter Off mode
CAN_AFMR_AccOff = ((1))
# CAN Acceptance File Bypass mode
CAN_AFMR_AccBP = ((1<<1))
# FullCAN Mode Enhancements
CAN_AFMR_eFCAN = ((1<<2))

# Macro defines for Standard Frame Individual Start Address Register
def CAN_STT_sa(n):
  '''The start address of the table of individual Standard Identifier.
  '''
  return  ((n&0x1FF)<<2)

# Macro defines for Standard Frame Group Start Address Register  
def CAN_SFF_GRP_sa(n):
  '''The start address of the table of grouped Standard Identifier.
  '''
  return  (((n&0x3FF)<<2))

# Macro defines for Extended Frame Start Address Register  
def CAN_EFF_sa(n):
  '''The start address of the table of individual Extended Identifier.
  '''
  return  (((n&0x1FF)<<2))

# Macro defines for Extended Frame Group Start Address Register  
def CAN_Eff_GRP_sa(n):
  '''The start address of the table of grouped Extended Identifier.
  '''
  return  (((n&0x3FF)<<2))

# Macro defines for End Of AF Table Register  
def CAN_EndofTable(n):
  '''The End of Table of AF LookUp Table.
  '''
  return  (((n&0x3FF)<<2))

# Macro defines for LUT Error Address Register  
def CAN_LUTerrAd(n):
  '''CAN Look-Up Table Error Address.
  '''
  return  (((n&0x1FF)<<2))

# Macro defines for LUT Error Registe  
# CAN Look-Up Table Error
CAN_LUTerr = ((1))

# Macro defines for Global FullCANInterrupt Enable Register
# Global FullCANInterrupt Enable
CAN_FCANIE = ((1))

# Macro defines for FullCAN Interrupt and Capture Register 0
def CAN_FCANIC0_IntPnd(n):
  '''FullCAN Interrupt and Capture (0-31).
  '''
  return  ((1<<n))

# Macro defines for FullCAN Interrupt and Capture Register 1  
def CAN_FCANIC1_IntPnd(n):
  '''FullCAN Interrupt and Capture (0-31).
  '''
  return  ((1<<(n-32)))
 
 
# CHECK PARAMETER DEFINITIONS  
def PARAM_CANx(x):
  '''Macro to determine if it is valid CAN peripheral or not.
  '''
  return  (((x)==(LPC_CAN1)) or ((x)==(LPC_CAN2)))

def PARAM_CANAFx(x):
  '''Macro to determine if it is valid CANAF or not.
  '''
  return  ((x)== (LPC_CANAF))
  
def PARAM_CANAFRAMx(x):
  '''Macro to determine if it is valid CANAF RAM or not.
  '''
  return  ((x)== LPC_CANAF_RAM)
  
def PARAM_CANCRx(x):
  '''Macro to determine if it is valid CANCR or not.
  '''
  return  ((x)==(LPC_CANCR))
  
def PARAM_I2S_DATA(data):
  '''Macro to check Data to send valid.
  '''
  return  ((data>=0) and (data <= 0xFFFFFFFF))
  
def PRAM_I2S_FREQ(freq):
  '''Macro to check frequency value.
  '''
  return  ((freq>=16000) and (freq <= 96000))
  
def PARAM_ID_11(n):
  '''Macro to check 11 bit Frame Identifier.
  '''
  return  ((n>>11)==0) 
  
def PARAM_ID_29(n):
  '''Macro to check 29 bit Frame Identifier.
  '''
  return  ((n>>29)==0) 
  
def PARAM_DLC(n):
  '''Macro to check DLC value.
  '''
  return  ((n>>4)==0) 
  
def PARAM_ID_FORMAT(n):
  '''Macro to check ID format type .
  '''
  return  ((n==STD_ID_FORMAT) or (n==EXT_ID_FORMAT))
  
def PARAM_GRP_ID(x, y):
  '''Macro to check Group identifier.
  '''
  return ((x<=y))
  
def PARAM_FRAME_TYPE(n):
  '''Macro to check Frame type.
  '''
  return  ((n==DATA_FRAME) or (n==REMOTE_FRAME))
  
def PARAM_CTRL_STS_TYPE(n):
  '''Macro to check Control/Central Status type parameter.
  '''
  return  (
    (n==CANCTRL_GLOBAL_STS) or (n==CANCTRL_INT_CAP)  
    or (n==CANCTRL_ERR_WRN) or (n==CANCTRL_STS)
    )

def PARAM_CR_STS_TYPE(n):
  '''Macro to check CR status type.
  '''
  return  ((n==CANCR_TX_STS) or (n==CANCR_RX_STS) or (n==CANCR_MS))

def PARAM_AFMODE_TYPE(n):
  '''Macro to check AF Mode type parameter.
  '''
  return  (
    (n==CAN_Normal) or (n==CAN_AccOff)  
    or (n==CAN_AccBP) or (n==CAN_eFCAN)
    )

def PARAM_MODE_TYPE(n):
  '''Macro to check Operation Mode.
  '''
  return  (
    (n==CAN_OPERATING_MODE) or (n==CAN_RESET_MODE)  
    or (n==CAN_LISTENONLY_MODE) or (n==CAN_SELFTEST_MODE)  
    or (n==CAN_TXPRIORITY_MODE) or (n==CAN_SLEEP_MODE)  
    or (n==CAN_RXPOLARITY_MODE) or (n==CAN_TEST_MODE)
    )

def PARAM_CTRL(n):
  '''Macro define for struct AF_Section parameter.
  '''
  return  ((n==CAN1_CTRL)|(n==CAN2_CTRL))
  
def PARAM_MSG_DISABLE(n):
  '''Macro define for struct AF_Section parameter.
  '''
  return  ((n==MSG_ENABLE)|(n==MSG_DISABLE))
  
def PARAM_INT_EN_TYPE(n):
  '''Macro to check Interrupt Type parameter.
  '''
  return  (
    (n==CANINT_RIE) or (n==CANINT_TIE1)  
    or (n==CANINT_EIE) or (n==CANINT_DOIE)  
    or (n==CANINT_WUIE) or (n==CANINT_EPIE)  
    or (n==CANINT_ALIE) or (n==CANINT_BEIE)  
    or (n==CANINT_IDIE) or (n==CANINT_TIE2)  
    or (n==CANINT_TIE3) or (n==CANINT_FCE)
    )

def PARAM_AFLUT_ENTRY_TYPE(n):
  '''Macro to check AFLUT Entry type.
  '''
  return  (
    (n==FULLCAN_ENTRY) or (n==EXPLICIT_STANDARD_ENTRY) 
    or (n==GROUP_STANDARD_ENTRY) or (n==EXPLICIT_EXTEND_ENTRY)  
    or (n==GROUP_EXTEND_ENTRY)
    )

def PARAM_POSITION(n):
  '''Macro to check position.
  '''
  return  ((n>=0) and (n<512))

# CAN Public Types

class SFF_Entry(cstruct):
  '''Standard ID Frame Format Entry structure.
  
  controller: CAN Controller, should be:
              CAN1_CTRL: CAN1 Controller
              CAN2_CTRL: CAN2 Controller
  disable:  Disable bit, should be:
            MSG_ENABLE: disable bit = 0
            MSG_DISABLE: disable bit = 1
  id_11:  Standard ID, should be 11-bit value
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class CAN_MSG_Type(cstruct):
  '''CAN message object structure.
  
  id: if format = STD_ID_FORMAT, id should be 11 bit identifier
      if format = EXT_ID_FORMAT, id should be 29 bit identifier
  dataA[4]: Data field A
  dataB[4]: Data field B
  len:  Length of data field in bytes, should be:
        0000b-0111b: 0-7 bytes
        1xxxb: 8 bytes
  format: Identifier Format, should be:
          STD_ID_FORMAT: Standard ID - 11 bit format
          EXT_ID_FORMAT: Extended ID - 29 bit format
  type: Remote Frame transmission, should be:
        DATA_FRAME: the number of data bytes called out by the DLC
                    field are send from the CANxTDA and CANxTDB registers
        REMOTE_FRAME: Remote Frame is sent
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass    

class CAN_ERROR:
  '''Error values that functions can return.
  '''
  # No error
  CAN_OK = 1
  # No more rx or tx objects available
  CAN_OBJECTS_FULL_ERROR = 1
  # Full CAN object not received
  CAN_FULL_OBJ_NOT_RCV = 2
  # No receive data available
  CAN_NO_RECEIVE_DATA = 3
  # Entry load in AFLUT is unvalid
  CAN_AF_ENTRY_ERROR = 4
  # ID Conflict
  CAN_CONFLICT_ID_ERROR = 5
  # Entry not exit
  CAN_ENTRY_NOT_EXIT_ERROR = 6

class CAN_AFMODE_Type:
  '''Acceptance Filter Mode type definition.
  '''
  # Normal Mode
  CAN_Normal = 0
  # Acceptance Filter Off Mode
  CAN_AccOff = 1
  # Acceptance Fileter Bypass Mode
  CAN_AccBP = 2
  # FullCAN Mode Enhancement
  CAN_eFCAN = 3

class CAN_CR_STS_Type:
  '''Central CAN status type definition.
  '''
  # Central CAN Tx Status
  CANCR_TX_STS = 0
  # Central CAN Rx Status
  CANCR_RX_STS = 1
  # Central CAN Miscellaneous Status
  CANCR_MS = 2

class CAN_CTRL_STS_Type:
  '''CAN Control status definition.
  '''
  # CAN Global Status
  CANCTRL_GLOBAL_STS = 0
  # CAN Interrupt and Capture
  CANCTRL_INT_CAP = 1
  # CAN Error Warning Limit
  CANCTRL_ERR_WRN = 2
  # CAN Control Status
  CANCTRL_STS = 3

class AFLUT_ENTRY_Type:
  '''AFLUT Entry type definition.
  '''
  FULLCAN_ENTRY = 0
  EXPLICIT_STANDARD_ENTRY = 1
  GROUP_STANDARD_ENTRY = 2
  EXPLICIT_EXTEND_ENTRY = 3
  GROUP_EXTEND_ENTRY = 4

class CAN_ID_FORMAT_Type:
  '''CAN ID format definition.
  '''
  # Use standard ID format (11 bit ID)
  STD_ID_FORMAT = 0
  # Use extended ID format (29 bit ID)
  EXT_ID_FORMAT = 1

class FullCAN_Entry(cstruct):
  '''FullCAN Entry structure.
  
  controller: CAN Controller, should be:
              CAN1_CTRL: CAN1 Controller
              CAN2_CTRL: CAN2 Controller
  disable:  Disable bit, should be:
            MSG_ENABLE: disable bit = 0
            MSG_DISABLE: disable bit = 1
  id_11:  Standard ID, should be 11-bit value
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class EFF_GPR_Entry(cstruct):
  ''' Group of Extended ID Frame Format Entry structure.
  
  controller1:  First CAN Controller, should be:
                CAN1_CTRL: CAN1 Controller
                CAN2_CTRL: CAN2 Controller
  controller2:  Second Disable bit, should be:
                MSG_ENABLE: disable bit = 0(default)
                MSG_DISABLE: disable bit = 1
  lowerEID: Extended ID lower bound, should be 29-bit value
  upperEID: Extended ID upper bound, should be 29-bit value
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class CAN_INT_EN_Type:
  '''CAN interrupt enable type definition.
  '''
  # CAN Receiver Interrupt Enable
  CANINT_RIE = 0
  # CAN Transmit Interrupt Enable
  CANINT_TIE1 = 1
  # CAN Error Warning Interrupt Enable
  CANINT_EIE = 2
  # CAN Data Overrun Interrupt Enable
  CANINT_DOIE = 3
  # CAN Wake-Up Interrupt Enable
  CANINT_WUIE = 4
  # CAN Error Passive Interrupt Enable
  CANINT_EPIE = 5
  # CAN Arbitration Lost Interrupt Enable
  CANINT_ALIE = 6
  # CAN Bus Error Interrupt Enable
  CANINT_BEIE = 7
  # CAN ID Ready Interrupt Enable
  CANINT_IDIE = 8
  # CAN Transmit Interrupt Enable for Buffer2
  CANINT_TIE2 = 9
  # CAN Transmit Interrupt Enable for Buffer3
  CANINT_TIE3 = 10
  # FullCAN Interrupt Enable
  CANINT_FCE = 11

class CAN_PinCFG_Type(cstruct):
  '''Pin Configuration structure.
  
  RD: For CAN1:
      CAN_RD1_P0_0: RD pin is on P0.0
      CAN_RD1_P0_21 : RD pin is on P0.21
      For CAN2:
      CAN_RD2_P0_4: RD pin is on P0.4
      CAN_RD2_P2_7: RD pin is on P2.7
  TD: For CAN1:
      CAN_TD1_P0_1: TD pin is on P0.1
      CAN_TD1_P0_22: TD pin is on P0.22
      For CAN2:
      CAN_TD2_P0_5: TD pin is on P0.5
      CAN_TD2_P2_8: TD pin is on P2.8
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class CAN_FRAME_Type:
  '''Symbolic names for type of CAN message.
  '''
  # Data frame
  DATA_FRAME = 0
  # Remote frame
  REMOTE_FRAME = 1

class FullCAN_IC_Type:
  '''FullCAN Interrupt Capture type definition.
  '''
  # FullCAN Interrupt and Capture 0
  FULLCAN_IC0 = 0
  # FullCAN Interrupt and Capture 1
  FULLCAN_IC1 = 1

class SFF_GPR_Entry(cstruct):
  '''Group of Standard ID Frame Format Entry structure.
  
  controller1:  First CAN Controller, should be:
                CAN1_CTRL: CAN1 Controller
                CAN2_CTRL: CAN2 Controller
  disable1: First Disable bit, should be:
            MSG_ENABLE: disable bit = 0
            MSG_DISABLE: disable bit = 1
  lowerID:  ID lower bound, should be 11-bit value
  controller2:  Second CAN Controller, should be:
                CAN1_CTRL: CAN1 Controller
                CAN2_CTRL: CAN2 Controller
  disable2: Second Disable bit, should be:
            MSG_ENABLE: disable bit = 0
            MSG_DISABLE: disable bit = 1
  upperID:  ID upper bound, should be 11-bit value and equal or greater than
            lowerID
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class CAN_MODE_Type:
  '''CAN Mode Type definition.
  '''
  # Operating Mode
  CAN_OPERATING_MODE = 0
  # Reset Mode
  CAN_RESET_MODE = 1
  # Listen Only Mode
  CAN_LISTENONLY_MODE = 2
  # Self Test Mode
  CAN_SELFTEST_MODE = 3
  # Transmit Priority Mode
  CAN_TXPRIORITY_MODE = 4
  # Sleep Mode
  CAN_SLEEP_MODE = 5
  # Receive Polarity Mode
  CAN_RXPOLARITY_MODE = 6
  # Test Mode
  CAN_TEST_MODE = 7

class EFF_Entry(cstruct):
  '''Extended ID Frame Format Entry structure.
  
  controller: CAN Controller, should be:
              CAN1_CTRL: CAN1 Controller
              CAN2_CTRL: CAN2 Controller
  ID_29:  Extend ID, shoud be 29-bit value
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class AF_SectionDef(cstruct):
  '''Acceptance Filter Section Table structure.
  
  FullCAN_Sec: The pointer point to FullCAN_Entry
  FC_NumEntry: FullCAN Entry Number
  SFF_Sec: The pointer point to SFF_Entry
  SFF_NumEntry: Standard ID Entry Number
  SFF_GPR_Sec: The pointer point to SFF_GPR_Entry
  SFF_GPR_NumEntry: Group Standard ID Entry Number
  EFF_Sec: The pointer point to EFF_Entry
  EFF_NumEntry: Extended ID Entry Number
  EFF_GPR_Sec: The pointer point to EFF_GPR_Entry
  EFF_GPR_NumEntry: Group Extended ID Entry Number
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

def CAN_SetCommand(CANx, CMRType):
  '''Set CAN command request.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  CMRType:  command request type, should be:
            CAN_CMR_TR: Transmission request
            CAN_CMR_AT: Abort Transmission request
            CAN_CMR_RRB: Release Receive Buffer request
            CAN_CMR_CDO: Clear Data Overrun request
            CAN_CMR_SRR: Self Reception request
            CAN_CMR_STB1: Select Tx Buffer 1 request
            CAN_CMR_STB2: Select Tx Buffer 2 request
            CAN_CMR_STB3: Select Tx Buffer 3 request
  return: CANICR (CAN interrupt and Capture register) value
  '''
  return robocaller("CAN_SetCommand", "void", CANx, CMRType)

def CAN_IRQCmd(CANx, arg, NewState):
  '''Enable/Disable CAN Interrupt.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  arg:  type of CAN interrupt that you want to enable/disable. Should be:
        CANINT_RIE: CAN Receiver Interrupt Enable
        CANINT_TIE1: CAN Transmit Interrupt Enable
        CANINT_EIE: CAN Error Warning Interrupt Enable
        CANINT_DOIE: CAN Data Overrun Interrupt Enable
        CANINT_WUIE: CAN Wake-Up Interrupt Enable
        CANINT_EPIE: CAN Error Passive Interrupt Enable
        CANINT_ALIE: CAN Arbitration Lost Interrupt Enable
        CANINT_BEIE: CAN Bus Error Interrupt Enable
        CANINT_IDIE: CAN ID Ready Interrupt Enable
        CANINT_TIE2: CAN Transmit Interrupt Enable for Buffer2
        CANINT_TIE3: CAN Transmit Interrupt Enable for Buffer3
        CANINT_FCE: FullCAN Interrupt Enable
  NewState: New state of this function, should be: ENABLE or DISABLE
  
  '''
  return robocaller("CAN_IRQCmd", "void", CANx, arg, NewState)

def FCAN_ReadObj(CANAFx, CAN_Msg):
  '''Receive FullCAN Object.
  
  CANAFx: CAN Acceptance Filter register, should be: LPC_CANAF
  CAN_Msg:  pointer to the CAN_MSG_Type Struct, it will contain received
            message information such as: ID, DLC, RTR, ID Format
  return: CAN_ERROR, could be:
          CAN_FULL_OBJ_NOT_RCV: FullCAN Object is not be received
          CAN_OK: Received FullCAN Object successful
  '''
  return robocaller("FCAN_ReadObj", "CAN_ERROR", CANAFx, CAN_Msg)

def CAN_Init(CANx, baudrate):
  '''Initialize CAN peripheral with given baudrate.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  baudrate: the value of CAN baudrate will be set (bps)
  
  '''
  return robocaller("CAN_Init", "void", CANx, baudrate)

def CAN_ModeConfig(CANx, mode, NewState):
  '''Enable/Disable CAN Mode.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
        
  mode: type of CAN mode that you want to enable/disable, should be:
        CAN_OPERATING_MODE: Normal Operating Mode
        CAN_RESET_MODE: Reset Mode
        CAN_LISTENONLY_MODE: Listen Only Mode
        CAN_SELFTEST_MODE: Self Test Mode
        CAN_TXPRIORITY_MODE: Transmit Priority Mode
        CAN_SLEEP_MODE: Sleep Mode
        CAN_RXPOLARITY_MODE: Receive Polarity Mode
        CAN_TEST_MODE: Test Mode
  NewState: New State of this function, should be: ENABLE or DISABLE

  '''
  return robocaller("CAN_ModeConfig", "void", CANx, mode, NewState)

def CAN_LoadExplicitEntry(CANx, ID, format):
  '''Add Explicit ID into AF Look-Up Table dynamically.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  id: The ID of entry will be added
  format: is the type of ID Frame Format, should be:
          STD_ID_FORMAT: 11-bit ID value
          EXT_ID_FORMAT: 29-bit ID value
  return: CAN Error, could be:
          CAN_OBJECTS_FULL_ERROR: No more rx or tx objects available
          CAN_ID_EXIT_ERROR: ID exited in table
          CAN_OK: ID is added into table successfully
          
  '''
  return robocaller("CAN_LoadExplicitEntry", "CAN_ERROR", CANx, ID, format)

def CAN_LoadFullCANEntry(CANx, ID):
  '''Load FullCAN entry into AFLUT.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  id: identifier of entry that will be added
  return: CAN_ERROR, could be:
          CAN_OK: loading is successful
          CAN_ID_EXIT_ERROR: ID exited in FullCAN Section
          CAN_OBJECTS_FULL_ERROR: no more space available
  '''
  return robocaller("CAN_LoadFullCANEntry", "CAN_ERROR", CANx, ID)

def CAN_IntGetStatus(CANx):
  '''Get CAN interrupt status.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  return: CANICR (CAN interrupt and Capture register) value
  
  '''
  return robocaller("CAN_IntGetStatus", "uint32_t", CANx)

def CAN_SetAFMode(CANAFx, AFmode):
  '''Check if FullCAN interrupt enable or not.
  
  CANAFx: pointer to LPC_CANAF_TypeDef object, should be: LPC_CANAF
  return: IntStatus, could be:
          SET: if FullCAN interrupt is enable
          RESET: if FullCAN interrupt is disable
  
  '''
  return robocaller("CAN_SetAFMode", "void", CANAFx, AFmode)

def CAN_SendMsg(CANx, CAN_Msg):
  '''Send message data.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  CAN_Msg:  pointer to CAN_MSG_Type Structure, it contains message information
            such as: ID, DLC, RTR, ID Format
  return: Status:
          SUCCESS: send message successfully
          ERROR: send message unsuccessfully
          
  '''
  return robocaller("CAN_SendMsg", "Status", CANx, CAN_Msg)

def CAN_LoadGroupEntry(CANx, lowerID, upperID, format):
  '''Load Group entry into AFLUT.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  lowerID: lower identifier of entry
  upperID: upper identifier of entry
  format: format: type of ID format, should be:
          STD_ID_FORMAT: Standard ID format (11-bit value)
          EXT_ID_FORMAT: Extended ID format (29-bit value)
  return: CAN_ERROR, could be:
          CAN_OK: loading is successful
          CAN_CONFLICT_ID_ERROR: Conflict ID occurs
          CAN_OBJECTS_FULL_ERROR: no more space available
  
  '''
  return robocaller("CAN_LoadGroupEntry", "CAN_ERROR", CANx, lowerID, upperID, format)

def CAN_SetupAFLUT(CANAFx, AFSection):
  '''Setup Acceptance Filter Look-Up Table.
  
  CANAFx: pointer to LPC_CANAF_TypeDef object, should be: LPC_CANAF
  AFSection:  pointer to AF_SectionDef structure it contains information 
              about 5 sections will be install in AFLUT
  return: CAN Error  could be:
          CAN_OBJECTS_FULL_ERROR: No more rx or tx objects available
          CAN_AF_ENTRY_ERROR: table error-violation of ascending numerical order
          CAN_OK: ID is added into table successfully
  '''
  return robocaller("CAN_SetupAFLUT", "CAN_ERROR", CANAFx, AFSection)

def CAN_GetCTRLStatus(CANx, arg):
  '''Get CAN Control Status.
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  arg:  type of CAN status to get from CAN status register. Should be:
        CANCTRL_GLOBAL_STS: CAN Global Status
        CANCTRL_INT_CAP: CAN Interrupt and Capture
        CANCTRL_ERR_WRN: CAN Error Warning Limit
        CANCTRL_STS: CAN Control Status
  return: Current Control Status that you want to get value
  
  '''
  return robocaller("CAN_GetCTRLStatus", "uint32_t", CANx, arg)

def CAN_DeInit(CANx):
  '''Deinitialize CAN module.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  '''
  
  return robocaller("CAN_DeInit", "void", CANx)

def CAN_ReceiveMsg(CANx, CAN_Msg):
  '''Receive message data.
  
  CANx: pointer to CAN peripheral selected, should be:
        LPC_CAN1: CAN1 peripheral
        LPC_CAN2: CAN2 peripheral
  CAN_Msg:  pointer to the CAN_MSG_Type Struct, it will contain received message 
            information such as: ID, DLC, RTR, ID Format
  return: Status:
          SUCCESS: receive message successfully
          ERROR: receive message unsuccessfully
          
  '''
  return robocaller("CAN_ReceiveMsg", "Status", CANx, CAN_Msg)

def CAN_FullCANPendGetStatus(CANAFx, ic_type):
  '''Get value of FullCAN interrupt and capture register.
  
  CANAFx: pointer to LPC_CANAF_TypeDef object, should be: LPC_CANAF
  ic_type:  FullCAN IC type, should be:
            FULLCAN_IC0: FullCAN Interrupt Capture 0
            FULLCAN_IC1: FullCAN Interrupt Capture 1
  return: FCANIC0 or FCANIC1 (FullCAN interrupt and Capture register) value
  
  '''
  return robocaller("CAN_FullCANPendGetStatus", "uint32_t", CANAFx, ic_type)

def CAN_GetCRStatus(CANCRx, arg):
  '''Get CAN Central Status.
  
  CANCRx: pointer to LPC_CANCR_TypeDef, should be: LPC_CANCR
  arg:  type of CAN status to get from CAN Central status register. Should be:
        CANCR_TX_STS: Central CAN Tx Status
        CANCR_RX_STS: Central CAN Rx Status
        CANCR_MS: Central CAN Miscellaneous Status
  return: Current Central Status that you want to get value
  
  '''
  return robocaller("CAN_GetCRStatus", "uint32_t", CANCRx, arg)

def CAN_RemoveEntry(EntryType, position):
  '''Remove AFLUT entry (FullCAN entry and Explicit Standard entry).
  
  EntryType:  the type of entry that want to remove, should be:
              FULLCAN_ENTRY
              EXPLICIT_STANDARD_ENTRY
              GROUP_STANDARD_ENTRY
              EXPLICIT_EXTEND_ENTRY
              GROUP_EXTEND_ENTRY
  position: the position of this entry in its section
  return: CAN_ERROR, could be:
          CAN_OK: removal successful
          CAN_ENTRY_NOT_EXIT_ERROR: removal failed
          
  '''
  return robocaller("CAN_RemoveEntry", "CAN_ERROR", EntryType, position)

def CAN_FullCANIntGetStatus(CANAFx):
  '''Check if FullCAN interrupt enable or not.
  
  CANAFx: pointer to LPC_CANAF_TypeDef object, should be: LPC_CANAF
  return: IntStatus, could be:
          SET: if FullCAN interrupt is enable
          RESET: if FullCAN interrupt is disable
  
  '''
  return robocaller("CAN_FullCANIntGetStatus", "IntStatus", CANAFx)

