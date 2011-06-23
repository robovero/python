"""SPI client library functions. See LPC17xx CMSIS-Compliant Standard
Peripheral Firmware Driver Library documentation."""
from internals import robocaller, cstruct

SPI_CPHA_FIRST = (0)
SPI_CPHA_SECOND = (1<<3)
SPI_CPOL_HI = (0)
SPI_CPOL_LO = (1<<4)
SPI_SLAVE_MODE = (0)
SPI_MASTER_MODE = (1<<5)
SPI_DATA_MSB_FIRST = (0)
SPI_DATA_LSB_FIRST = (1<<6)
SPI_STAT_DONE = (1<<8)		
SPI_STAT_ERROR = (1<<9)		
SPI_SPCR_BIT_EN = (1<<2)
SPI_SPCR_CPHA_SECOND = (1<<3)
SPI_SPCR_CPOL_LOW = (1<<4)
SPI_SPCR_MSTR = (1<<5)
SPI_SPCR_LSBF = (1<<6)
SPI_SPCR_SPIE = (1<<7)

def SPI_SPCR_BITS(n):
  if (n==0): return (0)
  else: return ((n&0x0F)<<8)

SPI_SPCR_BITMASK = (0xFFC)
SPI_SPSR_ABRT = (1<<3)
SPI_SPSR_MODF = (1<<4)
SPI_SPSR_ROVR = (1<<5)
SPI_SPSR_WCOL = (1<<6)
SPI_SPSR_SPIF = (1<<7)
SPI_SPSR_BITMASK = (0xF8)
SPI_SPDR_LO_MASK = (0xFF)
SPI_SPDR_HI_MASK = (0xFF00)
SPI_SPDR_BITMASK = (0xFFFF)

def SPI_SPCCR_COUNTER(n):
  return (n&0xFF)

SPI_SPCCR_BITMASK = (0xFF)
SPI_SPTCR_TEST_MASK = (0xFE)
SPI_SPTCR_BITMASK = (0xFE)
SPI_SPTSR_ABRT = (1<<3)
SPI_SPTSR_MODF = (1<<4)
SPI_SPTSR_ROVR = (1<<5)
SPI_SPTSR_WCOL = (1<<6)
SPI_SPTSR_SPIF = (1<<7)
SPI_SPTSR_MASKBIT = (0xF8)
SPI_SPINT_INTFLAG = (1<<0)
SPI_SPINT_BITMASK = (0x01)

def PARAM_SPIx(n):
  return ((n)==(LPC_SPI))

def PARAM_SPI_CPHA(n):
  return ((n==SPI_CPHA_FIRST) or (n==SPI_CPHA_SECOND))

def PARAM_SPI_CPOL(n):
  return ((n==SPI_CPOL_HI) or (n==SPI_CPOL_LO))

def PARAM_SPI_MODE(n):
  return ((n==SPI_SLAVE_MODE) or (n==SPI_MASTER_MODE))

def PARAM_SPI_DATA_ORDER(n):
  return ((n==SPI_DATA_MSB_FIRST) or (n==SPI_DATA_LSB_FIRST))

def PARAM_SPI_DATABIT(n):
  return (
		(n==SPI_DATABIT_16) or (n==SPI_DATABIT_8) 
		or (n==SPI_DATABIT_9) or (n==SPI_DATABIT_10) 
		or (n==SPI_DATABIT_11) or (n==SPI_DATABIT_12) 
		or (n==SPI_DATABIT_13) or (n==SPI_DATABIT_14) 
		or (n==SPI_DATABIT_15)
		)
		
def PARAM_SPI_STAT(n):
  return (
		(n==SPI_STAT_ABRT) or (n==SPI_STAT_MODF) 
		or (n==SPI_STAT_ROVR) or (n==SPI_STAT_WCOL) 
		or (n==SPI_STAT_SPIF)
		)

SPI_DATABIT_16 = SPI_SPCR_BITS(0)		
SPI_DATABIT_8 = SPI_SPCR_BITS(0x08) 	
SPI_DATABIT_9 = SPI_SPCR_BITS(0x09) 	
SPI_DATABIT_10 = SPI_SPCR_BITS(0x0A) 	
SPI_DATABIT_11 = SPI_SPCR_BITS(0x0B) 	
SPI_DATABIT_12 = SPI_SPCR_BITS(0x0C) 	
SPI_DATABIT_13 = SPI_SPCR_BITS(0x0D) 	
SPI_DATABIT_14 = SPI_SPCR_BITS(0x0E) 	
SPI_DATABIT_15 = SPI_SPCR_BITS(0x0F) 	
SPI_STAT_ABRT = SPI_SPSR_ABRT
SPI_STAT_MODF = SPI_SPSR_MODF
SPI_STAT_ROVR = SPI_SPSR_ROVR
SPI_STAT_WCOL = SPI_SPSR_WCOL
SPI_STAT_SPIF = SPI_SPSR_SPIF
class SPI_CFG_Type(cstruct):
	pass

class SPI_DATA_SETUP_Type(cstruct):
	pass

class SPI_TRANSFER_Type:
	SPI_TRANSFER_POLLING = 0
	SPI_TRANSFER_INTERRUPT = 1

def SPI_SetClock(SPIx, target_clock):
	return robocaller("SPI_SetClock", "void", SPIx, target_clock)

def SPI_CheckStatus(inputSPIStatus, SPIStatus):
	return robocaller("SPI_CheckStatus", "FlagStatus", inputSPIStatus, SPIStatus)

def SPI_SendData(SPIx, Data):
	return robocaller("SPI_SendData", "void", SPIx, Data)

def SPI_GetStatus(SPIx):
	return robocaller("SPI_GetStatus", "uint32_t", SPIx)

def SPI_GetDataSize(SPIx):
	return robocaller("SPI_GetDataSize", "uint8_t", SPIx)

def SPI_ReceiveData(SPIx):
	return robocaller("SPI_ReceiveData", "uint16_t", SPIx)

def SPI_ConfigStructInit(SPI_InitStruct):
	return robocaller("SPI_ConfigStructInit", "void", SPI_InitStruct)

def SPI_GetIntStatus(SPIx):
	return robocaller("SPI_GetIntStatus", "IntStatus", SPIx)

def SPI_DeInit(SPIx):
	return robocaller("SPI_DeInit", "void", SPIx)

def SPI_IntCmd(SPIx, NewState):
	return robocaller("SPI_IntCmd", "void", SPIx, NewState)

def SPI_ReadWrite(SPIx, dataCfg, xfType):
	return robocaller("SPI_ReadWrite", "int32_t", SPIx, dataCfg, xfType)

def SPI_Init(SPIx, SPI_ConfigStruct):
	return robocaller("SPI_Init", "void", SPIx, SPI_ConfigStruct)

def SPI_ClearIntPending(SPIx):
	return robocaller("SPI_ClearIntPending", "void", SPIx)

