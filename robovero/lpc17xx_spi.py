"""SPI client library functions. Find implementation details in LPC17xx
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

# SPI configuration parameter defines
# Clock phase control bit
SPI_CPHA_FIRST = (0)
SPI_CPHA_SECOND = (1<<3)

# Clock polarity control bit
SPI_CPOL_HI = (0)
SPI_CPOL_LO = (1<<4)

# SPI master mode enable
SPI_SLAVE_MODE = (0)
SPI_MASTER_MODE = (1<<5)

# LSB enable bit
SPI_DATA_MSB_FIRST = (0)
SPI_DATA_LSB_FIRST = (1<<6)

# SPI data bit number defines
# Databit number = 16
SPI_DATABIT_16 = SPI_SPCR_BITS(0)    
# Databit number = 8
SPI_DATABIT_8 = SPI_SPCR_BITS(0x08)   
# Databit number = 9
SPI_DATABIT_9 = SPI_SPCR_BITS(0x09)   
# Databit number = 10
SPI_DATABIT_10 = SPI_SPCR_BITS(0x0A)   
# Databit number = 11
SPI_DATABIT_11 = SPI_SPCR_BITS(0x0B)   
# Databit number = 12
SPI_DATABIT_12 = SPI_SPCR_BITS(0x0C)   
# Databit number = 13
SPI_DATABIT_13 = SPI_SPCR_BITS(0x0D)   
# Databit number = 14
SPI_DATABIT_14 = SPI_SPCR_BITS(0x0E)   
# Databit number = 15
SPI_DATABIT_15 = SPI_SPCR_BITS(0x0F)

# SPI Status Flag defines
# Slave abort
SPI_STAT_ABRT = SPI_SPSR_ABRT
# Mode fault
SPI_STAT_MODF = SPI_SPSR_MODF
# Read overrun
SPI_STAT_ROVR = SPI_SPSR_ROVR
# Write collision
SPI_STAT_WCOL = SPI_SPSR_WCOL
# SPI transfer complete flag
SPI_STAT_SPIF = SPI_SPSR_SPIF

# SPI Status Implementation definitions
# Done
SPI_STAT_DONE = (1<<8)    
# Error
SPI_STAT_ERROR = (1<<9)

# Macro defines for SPI Control Register
def SPI_SPCR_BITS(n):
  '''When bit 2 of this register is 1, this field controls the
  number of bits per transfer.
  '''
  if (n==0): return (0)
  else: return ((n&0x0F)<<8)

# Macro defines for  SPI Status Register
# Slave abort
SPI_SPSR_ABRT = (1<<3)
# Mode fault
SPI_SPSR_MODF = (1<<4)
# Read overrun
SPI_SPSR_ROVR = (1<<5)
# Write collision
SPI_SPSR_WCOL = (1<<6)
# SPI transfer complete flag
SPI_SPSR_SPIF = (1<<7)


class SPI_CFG_Type(cstruct):
  '''SPI configuration structure.
  
  Databit:  Databit number, should be SPI_DATABIT_x, where x is in range from 
            8 - 16
  CPHA: Clock phase, should be:
        - SPI_CPHA_FIRST: first clock edge
        - SPI_CPHA_SECOND: second clock edge
  CPOL: Clock polarity, should be:
        - SPI_CPOL_HI: high level
        - SPI_CPOL_LO: low level
  Mode: SPI mode, should be:
        - SPI_MASTER_MODE: Master mode
        - SPI_SLAVE_MODE: Slave mode
  DataOrder:  Data order, should be:
              - SPI_DATA_MSB_FIRST: MSB first
              - SPI_DATA_LSB_FIRST: LSB first
  ClockRate:  Clock rate,in Hz, should not exceed  (SPI peripheral clock)/8
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
  
  '''
  pass

class SPI_DATA_SETUP_Type(cstruct):
  '''SPI Data configuration structure definitions.
  
  tx_data:  Pointer to transmit data
  rx_data:  Pointer to transmit data
  length: Length of transfer data
  counter:  Data counter index
  status: Current status of SPI activity
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
  
  '''
  pass

class SPI_TRANSFER_Type:
  '''SPI Transfer Type definitions.
  
  SPI_TRANSFER_POLLING: Polling transfer
  SPI_TRANSFER_INTERRUPT: Interrupt transfer
    
  '''
  SPI_TRANSFER_POLLING = 0
  SPI_TRANSFER_INTERRUPT = 1

def SPI_SetClock(SPIx, target_clock):
  '''Setup clock rate for SPI device.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  target_clock:  clock of SPI (Hz)
  
  '''
  return robocaller("SPI_SetClock", "void", SPIx, target_clock)

def SPI_CheckStatus(inputSPIStatus, SPIStatus):
  '''Checks whether the specified SPI Status flag is set or not via
  inputSPIStatus parameter.
  
  inputSPIStatus: Value to check status of each flag type. This value is the 
                  return value from SPI_GetStatus().
  SPIStatus:  Specifies the SPI status flag to check, should be one of:
              - SPI_STAT_ABRT: Slave abort.
              - SPI_STAT_MODF: Mode fault.
              - SPI_STAT_ROVR: Read overrun.
              - SPI_STAT_WCOL: Write collision.
              - SPI_STAT_SPIF: SPI transfer complete. 
  return: The new state of SPIStatus (SET or RESET)
  
  '''
  return robocaller("SPI_CheckStatus", "FlagStatus", inputSPIStatus, SPIStatus)

def SPI_SendData(SPIx, Data):
  '''Transmit a single data through SPIx peripheral.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  Data: Data to transmit (must be 16 or 8-bit long, this depend on SPI data bit
        number configured)
   
  '''
  return robocaller("SPI_SendData", "void", SPIx, Data)

def SPI_GetStatus(SPIx):
  '''Get current value of SPI Status register in SPIx peripheral.
  
  The return value of this function must be used with SPI_CheckStatus() to 
  determine current flag status corresponding to each SPI status type. Because 
  some flags in SPI Status register will be cleared after reading, the next 
  reading SPI Status register could not be correct. So this function used to 
  read SPI status register in one time only, then the return value used to check
  all flags.
 
  SPIx: SPI peripheral definition, should be LPC_SPI
  return: Current value of SPI Status register in SPI peripheral.
  
  '''
  return robocaller("SPI_GetStatus", "uint32_t", SPIx)

def SPI_GetDataSize(SPIx):
  '''Get data bit size per transfer.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  return: number of bit per transfer, could be 8-16
  
  '''
  return robocaller("SPI_GetDataSize", "uint8_t", SPIx)

def SPI_ReceiveData(SPIx):
  '''Receive a single data from SPIx peripheral.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  return: Data received (16-bit long)
  
  '''
  return robocaller("SPI_ReceiveData", "uint16_t", SPIx)

def SPI_ConfigStructInit(SPI_InitStruct):
  '''Fills each SPI_InitStruct member with its default value.
  
  CPHA = SPI_CPHA_FIRST
  CPOL = SPI_CPOL_HI
  ClockRate = 1000000
  DataOrder = SPI_DATA_MSB_FIRST
  Databit = SPI_DATABIT_8
  Mode = SPI_MASTER_MODE
  
  SPI_InitStruct: Pointer to a SPI_CFG_Type structure which will be initialized.
  
  
  '''
  return robocaller("SPI_ConfigStructInit", "void", SPI_InitStruct)

def SPI_GetIntStatus(SPIx):
  '''Checks whether the SPI interrupt flag is set or not.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  return: The new state of SPI Interrupt Flag (SET or RESET)
  
  '''
  return robocaller("SPI_GetIntStatus", "IntStatus", SPIx)

def SPI_DeInit(SPIx):
  '''De-initializes the SPIx peripheral registers to their reset values.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  
  
  '''
  return robocaller("SPI_DeInit", "void", SPIx)

def SPI_IntCmd(SPIx, NewState):
  '''Enable or disable SPIx interrupt.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  NewState: New state of specified UART interrupt type, should be:
            - ENABLE: Enable this SPI interrupt.
            - DISABLE: Disable this SPI interrupt. 
            
  '''
  return robocaller("SPI_IntCmd", "void", SPIx, NewState)

def SPI_ReadWrite(SPIx, dataCfg, xfType):
  '''Read write data function.
  
  This function can be used in both master and slave mode.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  dataCfg:  Pointer to a SPI_DATA_SETUP_Type structure that contains specified 
            information about transmit data configuration. 
  xfType: Transfer type, should be:
          - SPI_TRANSFER_POLLING: Polling mode
          - SPI_TRANSFER_INTERRUPT: Interrupt mode
  return: Actual Data length has been transferred in polling mode.
          In interrupt mode, always return (0). Return (-1) if error.
  
  '''
  return robocaller("SPI_ReadWrite", "int32_t", SPIx, dataCfg, xfType)

def SPI_Init(SPIx, SPI_ConfigStruct):
  '''Initializes the SPIx peripheral according to the specified parameters in 
  the UART_ConfigStruct.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  SPI_ConfigStruct: Pointer to a SPI_CFG_Type structure that contains the 
                    configuration information for the specified SPI peripheral.
  
  '''
  return robocaller("SPI_Init", "void", SPIx, SPI_ConfigStruct)

def SPI_ClearIntPending(SPIx):
  '''Clear SPI interrupt flag.
  
  SPIx: SPI peripheral definition, should be LPC_SPI
  
  '''
  return robocaller("SPI_ClearIntPending", "void", SPIx)
