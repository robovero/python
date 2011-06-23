"""General purpose DMA client library functions. See LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library 
documentation."""
from internals import robocaller, cstruct

GPDMA_CONN_SSP0_Tx = ((0)) 		
GPDMA_CONN_SSP0_Rx = ((1)) 		
GPDMA_CONN_SSP1_Tx = ((2)) 		
GPDMA_CONN_SSP1_Rx = ((3)) 		
GPDMA_CONN_ADC = ((4)) 		
GPDMA_CONN_I2S_Channel_0 = ((5)) 		
GPDMA_CONN_I2S_Channel_1 = ((6)) 		
GPDMA_CONN_DAC = ((7)) 		
GPDMA_CONN_UART0_Tx = ((8)) 		
GPDMA_CONN_UART0_Rx = ((9)) 		
GPDMA_CONN_UART1_Tx = ((10)) 		
GPDMA_CONN_UART1_Rx = ((11)) 		
GPDMA_CONN_UART2_Tx = ((12)) 		
GPDMA_CONN_UART2_Rx = ((13)) 		
GPDMA_CONN_UART3_Tx = ((14)) 		
GPDMA_CONN_UART3_Rx = ((15)) 		
GPDMA_CONN_MAT0_0 = ((16)) 		
GPDMA_CONN_MAT0_1 = ((17)) 		
GPDMA_CONN_MAT1_0 = ((18)) 		
GPDMA_CONN_MAT1_1 = ((19)) 		
GPDMA_CONN_MAT2_0 = ((20)) 		
GPDMA_CONN_MAT2_1 = ((21)) 		
GPDMA_CONN_MAT3_0 = ((22)) 		
GPDMA_CONN_MAT3_1 = ((23)) 		
GPDMA_TRANSFERTYPE_M2M = ((0)) 	
GPDMA_TRANSFERTYPE_M2P = ((1)) 	
GPDMA_TRANSFERTYPE_P2M = ((2)) 	
GPDMA_TRANSFERTYPE_P2P = ((3)) 	
GPDMA_BSIZE_1 = ((0)) 
GPDMA_BSIZE_4 = ((1)) 
GPDMA_BSIZE_8 = ((2)) 
GPDMA_BSIZE_16 = ((3)) 
GPDMA_BSIZE_32 = ((4)) 
GPDMA_BSIZE_64 = ((5)) 
GPDMA_BSIZE_128 = ((6)) 
GPDMA_BSIZE_256 = ((7)) 
GPDMA_WIDTH_BYTE = ((0)) 
GPDMA_WIDTH_HALFWORD = ((1)) 
GPDMA_WIDTH_WORD = ((2)) 
GPDMA_REQSEL_UART = ((0)) 
GPDMA_REQSEL_TIMER = ((1))

def GPDMA_DMACIntStat_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACIntStat_BITMASK = ((0xFF))

def GPDMA_DMACIntTCStat_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACIntTCStat_BITMASK = ((0xFF))

def GPDMA_DMACIntTCClear_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACIntTCClear_BITMASK = ((0xFF))

def GPDMA_DMACIntErrStat_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACIntErrStat_BITMASK = ((0xFF))

def GPDMA_DMACIntErrClr_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACIntErrClr_BITMASK = ((0xFF))

def GPDMA_DMACRawIntTCStat_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACRawIntTCStat_BITMASK = ((0xFF))

def GPDMA_DMACRawIntErrStat_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACRawIntErrStat_BITMASK = ((0xFF))

def GPDMA_DMACEnbldChns_Ch(n):
  return (((1<<n)&0xFF))

GPDMA_DMACEnbldChns_BITMASK = ((0xFF))

def GPDMA_DMACSoftBReq_Src(n):
  return (((1<<n)&0xFFFF))

GPDMA_DMACSoftBReq_BITMASK = ((0xFFFF))

def GPDMA_DMACSoftSReq_Src(n):
  return (((1<<n)&0xFFFF))

GPDMA_DMACSoftSReq_BITMASK = ((0xFFFF))

def GPDMA_DMACSoftLBReq_Src(n):
  return (((1<<n)&0xFFFF))

GPDMA_DMACSoftLBReq_BITMASK = ((0xFFFF))

def GPDMA_DMACSoftLSReq_Src(n):
  return (((1<<n)&0xFFFF))

GPDMA_DMACSoftLSReq_BITMASK = ((0xFFFF))
GPDMA_DMACConfig_E = ((0x01))	 
GPDMA_DMACConfig_M = ((0x02))	 
GPDMA_DMACConfig_BITMASK = ((0x03))

def GPDMA_DMACSync_Src(n):
  return (((1<<n)&0xFFFF))

GPDMA_DMACSync_BITMASK = ((0xFFFF))

def GPDMA_DMAReqSel_Input(n):
  return (((1<<(n-8))&0xFF))

GPDMA_DMAReqSel_BITMASK = ((0xFF))
GPDMA_DMACCxLLI_BITMASK = ((0xFFFFFFFC))

def GPDMA_DMACCxControl_TransferSize(n):
  return (((n&0xFFF)<<0)) 	

def GPDMA_DMACCxControl_SBSize(n):
  return (((n&0x07)<<12)) 	

def GPDMA_DMACCxControl_DBSize(n):
  return (((n&0x07)<<15)) 	

def GPDMA_DMACCxControl_SWidth(n):
  return (((n&0x07)<<18)) 	

def GPDMA_DMACCxControl_DWidth(n):
  return (((n&0x07)<<21)) 	

GPDMA_DMACCxControl_SI = ((1<<26)) 		
GPDMA_DMACCxControl_DI = ((1<<27)) 		
GPDMA_DMACCxControl_Prot1 = ((1<<28)) 		
GPDMA_DMACCxControl_Prot2 = ((1<<29)) 		
GPDMA_DMACCxControl_Prot3 = ((1<<30)) 		
GPDMA_DMACCxControl_I = ((1<<31)) 		
GPDMA_DMACCxControl_BITMASK = ((0xFCFFFFFF))
GPDMA_DMACCxConfig_E = ((1<<0))

def GPDMA_DMACCxConfig_SrcPeripheral(n):
  return (((n&0x1F)<<1)) 	

def GPDMA_DMACCxConfig_DestPeripheral(n):
  return (((n&0x1F)<<6)) 	

def GPDMA_DMACCxConfig_TransferType(n):
  return (((n&0x7)<<11)) 	

GPDMA_DMACCxConfig_IE = ((1<<14))			
GPDMA_DMACCxConfig_ITC = ((1<<15)) 		
GPDMA_DMACCxConfig_L = ((1<<16)) 		
GPDMA_DMACCxConfig_A = ((1<<17)) 		
GPDMA_DMACCxConfig_H = ((1<<18)) 		
GPDMA_DMACCxConfig_BITMASK = ((0x7FFFF))

def PARAM_GPDMA_CHANNEL(n):
  return ((n>=0) and (n<=7))

def PARAM_GPDMA_CONN(n):
	return (
		(n==GPDMA_CONN_SSP0_Tx) or (n==GPDMA_CONN_SSP0_Rx)
    or (n==GPDMA_CONN_SSP1_Tx) or (n==GPDMA_CONN_SSP1_Rx)
    or (n==GPDMA_CONN_ADC) or (n==GPDMA_CONN_I2S_Channel_0)
    or (n==GPDMA_CONN_I2S_Channel_1) or (n==GPDMA_CONN_DAC)
    or (n==GPDMA_CONN_UART0_Tx) or (n==GPDMA_CONN_UART0_Rx)
    or (n==GPDMA_CONN_UART1_Tx) or (n==GPDMA_CONN_UART1_Rx)
    or (n==GPDMA_CONN_UART2_Tx) or (n==GPDMA_CONN_UART2_Rx)
    or (n==GPDMA_CONN_UART3_Tx) or (n==GPDMA_CONN_UART3_Rx)
    or (n==GPDMA_CONN_MAT0_0) or (n==GPDMA_CONN_MAT0_1)
    or (n==GPDMA_CONN_MAT1_0) or (n==GPDMA_CONN_MAT1_1)
    or (n==GPDMA_CONN_MAT2_0) or (n==GPDMA_CONN_MAT2_1)
    or (n==GPDMA_CONN_MAT3_0) or (n==GPDMA_CONN_MAT3_1)
    )
    
def PARAM_GPDMA_BSIZE(n):
	return (
		(n==GPDMA_BSIZE_1) or (n==GPDMA_BSIZE_4)
    or (n==GPDMA_BSIZE_8) or (n==GPDMA_BSIZE_16)
    or (n==GPDMA_BSIZE_32) or (n==GPDMA_BSIZE_64)
    or (n==GPDMA_BSIZE_128) or (n==GPDMA_BSIZE_256)
    )
    
def PARAM_GPDMA_WIDTH(n):
	return (
		(n==GPDMA_WIDTH_BYTE) 
		or (n==GPDMA_WIDTH_HALFWORD)
    or (n==GPDMA_WIDTH_WORD)
    )
    
def PARAM_GPDMA_STAT(n):
	return (
		(n==GPDMA_STAT_INT) or (n==GPDMA_STAT_INTTC)
    or (n==GPDMA_STAT_INTERR) or (n==GPDMA_STAT_RAWINTTC)
    or (n==GPDMA_STAT_RAWINTERR) or (n==GPDMA_STAT_ENABLED_CH)
    )
    
def PARAM_GPDMA_TRANSFERTYPE(n):
	return (
		(n==GPDMA_TRANSFERTYPE_M2M) or (n==GPDMA_TRANSFERTYPE_M2P)
    or (n==GPDMA_TRANSFERTYPE_P2M) or (n==GPDMA_TRANSFERTYPE_P2P)
    )
    
def PARAM_GPDMA_STATCLR(n):
  return ((n==GPDMA_STATCLR_INTTC) or (n==GPDMA_STATCLR_INTERR))

def PARAM_GPDMA_REQSEL(n):
  return ((n==GPDMA_REQSEL_UART) or (n==GPDMA_REQSEL_TIMER))

class GPDMA_StateClear_Type:
	GPDMA_STATCLR_INTTC = 0
	GPDMA_STATCLR_INTERR = 1

class GPDMA_LLI_Type(cstruct):
	pass

class GPDMA_Channel_CFG_Type(cstruct):
	pass

class GPDMA_Status_Type:
	GPDMA_STAT_INT = 0
	GPDMA_STAT_INTTC = 1
	GPDMA_STAT_INTERR = 2
	GPDMA_STAT_RAWINTTC = 3
	GPDMA_STAT_RAWINTERR = 4
	GPDMA_STAT_ENABLED_CH = 5

def GPDMA_Init():
	return robocaller("GPDMA_Init", "void", )

def GPDMA_ChannelCmd(channelNum, NewState):
	return robocaller("GPDMA_ChannelCmd", "void", channelNum, NewState)

def GPDMA_Setup(GPDMAChannelConfig):
	return robocaller("GPDMA_Setup", "Status", GPDMAChannelConfig)

def GPDMA_IntGetStatus(type, channel):
	return robocaller("GPDMA_IntGetStatus", "IntStatus", type, channel)

def GPDMA_ClearIntPending(type, channel):
	return robocaller("GPDMA_ClearIntPending", "void", type, channel)

