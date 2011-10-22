"""Synchronous serial port client library functions. Find implementation details
in LPC17xx CMSIS-Compliant Standard Peripheral Firmware Driver Library 
documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

def SSP_CR0_DSS(n):
  '''SSP data size select, must be 4 bits to 16 bits.
  '''
  return ((n-1)&0xF)

# SSP control 0 Motorola SPI mode
SSP_CR0_FRF_SPI = (0<<4)
# SSP control 0 TI synchronous serial mode
SSP_CR0_FRF_TI = (1<<4)
# SSP control 0 National Micro-wire mode
SSP_CR0_FRF_MICROWIRE = (2<<4)

# SPI clock polarity bit (used in SPI mode only), (1) = maintains the bus clock 
# high between frames, (0) = low
SSP_CR0_CPOL_HI = (1<<6)
# SPI clock out phase bit (used in SPI mode only), (1) = captures data on the 
# second clock transition of the frame, (0) = first
SSP_CR0_CPHA_SECOND = (1<<7)

# SSP serial clock rate value load macro, divider rate is 
# PERIPH_CLK / (cpsr * (SCR + 1))
SSP_CR1_SLAVE_EN = (1<<2)

# SSP status TX FIFO Empty bit
SSP_SR_TFE = (1<<0)
# SSP status TX FIFO not full bit
SSP_SR_TNF = (1<<1)
# SSP status RX FIFO not empty bit
SSP_SR_RNE = (1<<2)
# SSP status RX FIFO full bit
SSP_SR_RFF = (1<<3)
# SSP status SSP Busy bit
SSP_SR_BSY = (1<<4)

# Receive Overrun
SSP_IMSC_ROR = (1<<0)
# Receive TimeOut
SSP_IMSC_RT = (1<<1)
# Rx FIFO is at least half full
SSP_IMSC_RX = (1<<2)
# Tx FIFO is at least half empty
SSP_IMSC_TX = (1<<3)
# Receive Overrun
SSP_RIS_ROR = (1<<0)
# Receive TimeOut
SSP_RIS_RT = (1<<1)
# Rx FIFO is at least half full
SSP_RIS_RX = (1<<2)
# Tx FIFO is at least half empty
SSP_RIS_TX = (1<<3)
# Receive Overrun
SSP_MIS_ROR = (1<<0)
# Receive TimeOut
SSP_MIS_RT = (1<<1)
# Rx FIFO is at least half full
SSP_MIS_RX = (1<<2)
# Tx FIFO is at least half empty
SSP_MIS_TX = (1<<3)
# Writing a 1 to this bit clears the "frame was received when RxFIFO was full"
# interrupt
SSP_ICR_ROR = (1<<0)
# Writing a 1 to this bit clears the "Rx FIFO was not empty and has not been 
# read for a timeout period" interrupt
SSP_ICR_RT = (1<<1)
# SSP bit for enabling RX DMA
SSP_DMA_RXDMA_EN = (1<<0)
# SSP bit for enabling TX DMA
SSP_DMA_TXDMA_EN = (1<<1)

# Clock phase control bit
SSP_CPHA_FIRST = (0)
SSP_CPHA_SECOND = SSP_CR0_CPHA_SECOND

# Clock polarity control bit
SSP_CPOL_HI = (0)
SSP_CPOL_LO = SSP_CR0_CPOL_HI

# SSP master mode enable
SSP_SLAVE_MODE = SSP_CR1_SLAVE_EN
SSP_MASTER_MODE = (0)

# SSP data bit number defines
# Databit number = 4
SSP_DATABIT_4 = SSP_CR0_DSS(4)       
# Databit number = 5
SSP_DATABIT_5 = SSP_CR0_DSS(5)       
# Databit number = 6 
SSP_DATABIT_6 = SSP_CR0_DSS(6)       
# Databit number = 7
SSP_DATABIT_7 = SSP_CR0_DSS(7)       
# Databit number = 8
SSP_DATABIT_8 = SSP_CR0_DSS(8)       
# Databit number = 9
SSP_DATABIT_9 = SSP_CR0_DSS(9)       
# Databit number = 10
SSP_DATABIT_10 = SSP_CR0_DSS(10)     
# Databit number = 11
SSP_DATABIT_11 = SSP_CR0_DSS(11)     
# Databit number = 12
SSP_DATABIT_12 = SSP_CR0_DSS(12)     
# Databit number = 13
SSP_DATABIT_13 = SSP_CR0_DSS(13)     
# Databit number = 14
SSP_DATABIT_14 = SSP_CR0_DSS(14)     
# Databit number = 15
SSP_DATABIT_15 = SSP_CR0_DSS(15)     
# Databit number = 16
SSP_DATABIT_16 = SSP_CR0_DSS(16)
    
# SSP Frame Format definition
# Motorola SPI mode
SSP_FRAME_SPI = SSP_CR0_FRF_SPI
# TI synchronous serial mode
SSP_FRAME_TI = SSP_CR0_FRF_TI
# National Micro-wire mode
SSP_FRAME_MICROWIRE = SSP_CR0_FRF_MICROWIRE

# SSP Status defines
# SSP status TX FIFO Empty bit
SSP_STAT_TXFIFO_EMPTY = SSP_SR_TFE
# SSP status TX FIFO not full bit
SSP_STAT_TXFIFO_NOTFULL = SSP_SR_TNF
# SSP status RX FIFO not empty bit
SSP_STAT_RXFIFO_NOTEMPTY = SSP_SR_RNE
# SSP status RX FIFO full bit
SSP_STAT_RXFIFO_FULL = SSP_SR_RFF
# SSP status SSP Busy bit
SSP_STAT_BUSY = SSP_SR_BSY

# SSP Interrupt Configuration defines
# Receive Overrun
SSP_INTCFG_ROR = SSP_IMSC_ROR
# Receive TimeOut
SSP_INTCFG_RT = SSP_IMSC_RT
# Rx FIFO is at least half full
SSP_INTCFG_RX = SSP_IMSC_RX
# Tx FIFO is at least half empty
SSP_INTCFG_TX = SSP_IMSC_TX

# SSP Configured Interrupt Status defines
# Receive Overrun
SSP_INTSTAT_ROR = SSP_MIS_ROR
# Receive TimeOut
SSP_INTSTAT_RT = SSP_MIS_RT
# Rx FIFO is at least half full
SSP_INTSTAT_RX = SSP_MIS_RX
# Tx FIFO is at least half empty
SSP_INTSTAT_TX = SSP_MIS_TX

# SSP Raw Interrupt Status defines
# Receive Overrun
SSP_INTSTAT_RAW_ROR = SSP_RIS_ROR
# Receive TimeOut
SSP_INTSTAT_RAW_RT = SSP_RIS_RT
# Rx FIFO is at least half full
SSP_INTSTAT_RAW_RX = SSP_RIS_RX
# Tx FIFO is at least half empty
SSP_INTSTAT_RAW_TX = SSP_RIS_TX

# SSP Interrupt Clear defines
# Writing a 1 to this bit clears the "frame was received when RxFIFO was full"
# interrupt
SSP_INTCLR_ROR = SSP_ICR_ROR
# Writing a 1 to this bit clears the "Rx FIFO was not empty and has not been 
# read for a timeout period" interrupt
SSP_INTCLR_RT = SSP_ICR_RT

# SSP DMA defines
# SSP bit for enabling RX DMA
SSP_DMA_RX = SSP_DMA_RXDMA_EN
# SSP bit for enabling TX DMA
SSP_DMA_TX = SSP_DMA_TXDMA_EN

# SSP Status Implementation definitions
# Done
SSP_STAT_DONE = (1<<8)    
# Error
SSP_STAT_ERROR = (1<<9)

class SSP_CFG_Type(cstruct):
  '''SSP configuration structure.
  
  Databit:  Databit number, should be SSP_DATABIT_x, where x is in range from 
            4 - 16
  CPHA: Clock phase, should be:
              - SSP_CPHA_FIRST: first clock edge
              - SSP_CPHA_SECOND: second clock edge
  CPOL: Clock polarity, should be:
              - SSP_CPOL_HI: high level
              - SSP_CPOL_LO: low level
  Mode: SSP mode, should be:
              - SSP_MASTER_MODE: Master mode
              - SSP_SLAVE_MODE: Slave mode
  FrameFormat:  Frame Format:
                - SSP_FRAME_SPI: Motorola SPI frame format
                - SSP_FRAME_TI: TI frame format
                - SSP_FRAME_MICROWIRE: National Microwire frame format
  ClockRate:  Clock rate,in Hz
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
  
  '''
  pass

class SSP_DATA_SETUP_Type(cstruct):
  '''SPI Data configuration structure definitions.
  
  tx_data:  Pointer to transmit data
  tx_cnt:   Transmit counter
  rx_data:  Pointer to transmit data
  rx_cnt:   Receive counter
  length:   Length of transfer data
  status:   Current status of SSP activity
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
  
  '''
  pass

class SSP_TRANSFER_Type:
  '''SSP Transfer Type definitions.
  
  SSP_TRANSFER_POLLING: Polling transfer
  SSP_TRANSFER_INTERRUPT: Interrupt transfer
  
  '''
  SSP_TRANSFER_POLLING = 0
  SSP_TRANSFER_INTERRUPT = 1

def SSP_LoopBackCmd(SSPx, NewState):
  '''Enable or disable Loop Back mode function in SSP peripheral.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  NewState: New State of Loop Back mode, should be:
            - ENABLE: Enable this function
            - DISABLE: Disable this function
  
  '''
  return robocaller("SSP_LoopBackCmd", "void", SSPx, NewState)

def SSP_GetRawIntStatus(SSPx, RawIntType):
  '''Check whether the specified Raw interrupt status flag is set or not.
  
  Enabling/Disabling specified interrupt in SSP peripheral does not effect the
  Raw Interrupt Status flag.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  RawIntType: Raw Interrupt Type, should be:
              - SSP_INTSTAT_RAW_ROR: Receive Overrun interrupt
              - SSP_INTSTAT_RAW_RT: Receive Time out interrupt
              - SSP_INTSTAT_RAW_RX: RX FIFO is at least half full interrupt
              - SSP_INTSTAT_RAW_TX: TX FIFO is at least half empty interrupt
  return: New State of specified Raw interrupt status flag in SSP peripheral
  
  '''
  return robocaller("SSP_GetRawIntStatus", "IntStatus", SSPx, RawIntType)

def SSP_Init(SSPx, SSP_ConfigStruct):
  '''Initializes the SSPx peripheral according to the specified parameters in 
  the SSP_ConfigStruct.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  SSP_ConfigStruct: Pointer to a SSP_CFG_Type structure that contains the 
                    configuration information for the specified SSP peripheral.
        
  '''
  return robocaller("SSP_Init", "void", SSPx, SSP_ConfigStruct)

def SSP_DMACmd(SSPx, DMAMode, NewState):
  '''Enable/Disable DMA function for SSP peripheral.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  DMAMode:  Type of DMA, should be:
             - SSP_DMA_TX: DMA for the transmit FIFO
             - SSP_DMA_RX: DMA for the Receive FIFO
  NewState:  New State of DMA function on SSP peripheral, should be:
            - ENABLE: Enable this function
            - DISABLE: Disable this function
        
  '''
  return robocaller("SSP_DMACmd", "void", SSPx, DMAMode, NewState)

def SSP_GetDataSize(SSPx):
  '''Get data size bit selected.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  return: Data size, could be:
          - SSP_DATABIT_4: 4 bit transfer
          - SSP_DATABIT_5: 5 bit transfer
            ...
          - SSP_DATABIT_16: 16 bit transfer
  
  '''
  return robocaller("SSP_GetDataSize", "uint8_t", SSPx)

def SSP_Cmd(SSPx, NewState):
  '''Enable or disable SSP peripheral's operation.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  NewState: New State of SSPx peripheral's operation
        
  '''
  return robocaller("SSP_Cmd", "void", SSPx, NewState)

def SSP_IntConfig(SSPx, IntType, NewState):
  '''Enable or disable specified interrupt type in SSP peripheral.
    
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  IntType:  Interrupt type in SSP peripheral, should be:
            - SSP_INTCFG_ROR: Receive Overrun interrupt
            - SSP_INTCFG_RT: Receive Time out interrupt
            - SSP_INTCFG_RX: RX FIFO is at least half full interrupt
            - SSP_INTCFG_TX: TX FIFO is at least half empty interrupt
  NewState: New State of specified interrupt type, should be:
            - ENABLE: Enable this interrupt type
            - DISABLE: Disable this interrupt type
  
  '''
  return robocaller("SSP_IntConfig", "void", SSPx, IntType, NewState)

def SSP_SlaveOutputCmd(SSPx, NewState):
  '''Enable or disable Slave Output function in SSP peripheral.
  
  This function is available when SSP peripheral in Slave mode
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  NewState: New State of Slave Output function, should be:
            - ENABLE: Slave Output in normal operation
            - DISABLE: Slave Output is disabled. This blocks SSP controller from
              driving the transmit data line (MISO)
        
  '''
  return robocaller("SSP_SlaveOutputCmd", "void", SSPx, NewState)

def SSP_ClearIntPending(SSPx, IntType):
  '''Clear specified interrupt pending in SSP peripheral.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  IntType:  IntType  Interrupt pending to clear, should be:
            - SSP_INTCLR_ROR: clears the "frame was received when RxFIFO was
              full" interrupt.
            - SSP_INTCLR_RT: clears the "Rx FIFO was not empty and has not been
              read for a timeout period" interrupt.
        
  '''
  return robocaller("SSP_ClearIntPending", "void", SSPx, IntType)

def SSP_ReadWrite(SSPx, dataCfg, xfType):
  '''SSP Read write data function.
  
  This function can be used in both master and slave mode.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  dataCfg:  Pointer to a SSP_DATA_SETUP_Type structure that contains specified 
            information about transmit data configuration.
  xfType: xfType  Transfer type, should be:
          - SSP_TRANSFER_POLLING: Polling mode
          - SSP_TRANSFER_INTERRUPT: Interrupt mode
  return: Actual Data length has been transferred in polling mode. In interrupt 
          mode, always return (0). Return (-1) if error.
  
  '''
  return robocaller("SSP_ReadWrite", "int32_t", SSPx, dataCfg, xfType)

def SSP_DeInit(SSPx):
  '''De-initializes the SSPx peripheral registers to their default reset values.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
        
  '''
  return robocaller("SSP_DeInit", "void", SSPx)

def SSP_GetStatus(SSPx, FlagType):
  '''Checks whether the specified SSP status flag is set or not.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  FlagType: Type of flag to check status, should be one of following:
            - SSP_STAT_TXFIFO_EMPTY: TX FIFO is empty
            - SSP_STAT_TXFIFO_NOTFULL: TX FIFO is not full
            - SSP_STAT_RXFIFO_NOTEMPTY: RX FIFO is not empty
            - SSP_STAT_RXFIFO_FULL: RX FIFO is full
            - SSP_STAT_BUSY: SSP peripheral is busy
  return: New State of specified SSP status flag
        
  '''
  return robocaller("SSP_GetStatus", "FlagStatus", SSPx, FlagType)

def SSP_GetRawIntStatusReg(SSPx):
  '''Get Raw Interrupt Status register.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  return: Raw Interrupt Status (RIS) register value
        
  '''
  return robocaller("SSP_GetRawIntStatusReg", "uint32_t", SSPx)

def SSP_ConfigStructInit(SSP_InitStruct):
  '''Fills each SSP_InitStruct member with its default value.
  
  - CPHA = SSP_CPHA_FIRST
  - CPOL = SSP_CPOL_HI
  - ClockRate = 1000000
  - Databit = SSP_DATABIT_8
  - Mode = SSP_MASTER_MODE
  - FrameFormat = SSP_FRAME_SSP.
  
  SSP_InitStruct:  Pointer to a SSP_CFG_Type structure which will be initialized
  
  '''
  return robocaller("SSP_ConfigStructInit", "void", SSP_InitStruct)

def SSP_ReceiveData(SSPx):
  '''Receive a single word from SSPx peripheral.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  return: Data received (16-bit long)
        
  '''
  return robocaller("SSP_ReceiveData", "uint16_t", SSPx)

def SSP_GetIntStatus(SSPx, IntType):
  '''Check whether the specified interrupt status flag is set or not.
  
  Enabling/Disabling specified interrupt in SSP peripheral effects the Interrupt
  Status flag.
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  IntType:  Raw Interrupt Type, should be:
            - SSP_INTSTAT_ROR: Receive Overrun interrupt
            - SSP_INTSTAT_RT: Receive Time out interrupt
            - SSP_INTSTAT_RX: RX FIFO is at least half full interrupt
            - SSP_INTSTAT_TX: TX FIFO is at least half empty interrupt
  return: New State of specified interrupt status flag in SSP peripheral
        
  '''
  return robocaller("SSP_GetIntStatus", "IntStatus", SSPx, IntType)

def SSP_SendData(SSPx, Data):
  '''Transmit a single word or byte through SSPx peripheral.
  
  SSPx: SSP peripheral selected, should be:
        - LPC_SSP0: SSP0 peripheral
        - LPC_SSP1: SSP1 peripheral
  Data: Data to transmit (must be 16 or 8-bit long, depends on SSP data bit 
        number configuration)
  
  '''
  return robocaller("SSP_SendData", "void", SSPx, Data)
