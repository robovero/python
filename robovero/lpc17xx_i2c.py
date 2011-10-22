"""I2C client library functions. Find implementation details in LPC17xx 
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

# I2C Control Set register description
# Assert acknowledge flag
I2C_I2CONSET_AA = ((0x04)) 
# I2C interrupt flag
I2C_I2CONSET_SI = ((0x08)) 
# STOP flag
I2C_I2CONSET_STO = ((0x10)) 
# START flag
I2C_I2CONSET_STA = ((0x20)) 
# I2C interface enable
I2C_I2CONSET_I2EN = ((0x40)) 

# I2C Control Clear register description
# Assert acknowledge Clear bit
I2C_I2CONCLR_AAC = ((1<<2))
# I2C interrupt Clear bit
I2C_I2CONCLR_SIC = ((1<<3))
# START flag Clear bit
I2C_I2CONCLR_STAC = ((1<<5))
# I2C interface Disable bit
I2C_I2CONCLR_I2ENC = ((1<<6))

# I2C Status Code definition (I2C Status register)
# Return Code in I2C status register
I2C_STAT_CODE_BITMASK = ((0xF8))

# I2C return status code definitions
# No relevant information
I2C_I2STAT_NO_INF = ((0xF8))

# Master transmit mode
# A start condition has been transmitted
I2C_I2STAT_M_TX_START = ((0x08))
# A repeat start condition has been transmitted
I2C_I2STAT_M_TX_RESTART = ((0x10))
# SLA+W has been transmitted, ACK has been received
I2C_I2STAT_M_TX_SLAW_ACK = ((0x18))
# SLA+W has been transmitted, NACK has been received
I2C_I2STAT_M_TX_SLAW_NACK = ((0x20))
# Data has been transmitted, ACK has been received
I2C_I2STAT_M_TX_DAT_ACK = ((0x28))
# Data has been transmitted, NACK has been received
I2C_I2STAT_M_TX_DAT_NACK = ((0x30))
# Arbitration lost in SLA+R/W or Data bytes
I2C_I2STAT_M_TX_ARB_LOST = ((0x38))

# Master receive mode
# A start condition has been transmitted
I2C_I2STAT_M_RX_START = ((0x08))
# A repeat start condition has been transmitted
I2C_I2STAT_M_RX_RESTART = ((0x10))
# Arbitration lost
I2C_I2STAT_M_RX_ARB_LOST = ((0x38))
# SLA+R has been transmitted, ACK has been received
I2C_I2STAT_M_RX_SLAR_ACK = ((0x40))
# SLA+R has been transmitted, NACK has been received
I2C_I2STAT_M_RX_SLAR_NACK = ((0x48))
# Data has been received, ACK has been returned
I2C_I2STAT_M_RX_DAT_ACK = ((0x50))
# Data has been received, NACK has been return
I2C_I2STAT_M_RX_DAT_NACK = ((0x58))

# Slave receive mode
# Own slave address has been received, ACK has been returned
I2C_I2STAT_S_RX_SLAW_ACK = ((0x60))
# Arbitration lost in SLA+R/W as master
I2C_I2STAT_S_RX_ARB_LOST_M_SLA = ((0x68))
# General call address has been received, ACK has been returned
I2C_I2STAT_S_RX_GENCALL_ACK = ((0x70))
# Arbitration lost in SLA+R/W (GENERAL CALL) as master
I2C_I2STAT_S_RX_ARB_LOST_M_GENCALL = ((0x78))
# Previously addressed with own SLV address;
# Data has been received, ACK has been return
I2C_I2STAT_S_RX_PRE_SLA_DAT_ACK = ((0x80))
# Previously addressed with own SLA;
# Data has been received and NOT ACK has been return 
I2C_I2STAT_S_RX_PRE_SLA_DAT_NACK = ((0x88))
# Previously addressed with General Call;
# Data has been received and ACK has been return
I2C_I2STAT_S_RX_PRE_GENCALL_DAT_ACK = ((0x90))
# Previously addressed with General Call;
# Data has been received and NOT ACK has been return
I2C_I2STAT_S_RX_PRE_GENCALL_DAT_NACK = ((0x98))
# A STOP condition or repeated START condition has
# been received while still addressed as SLV/REC
# (Slave Receive) or SLV/TRX (Slave Transmit)
I2C_I2STAT_S_RX_STA_STO_SLVREC_SLVTRX = ((0xA0))
# Slave transmit mode
# Own SLA+R has been received, ACK has been returned
I2C_I2STAT_S_TX_SLAR_ACK = ((0xA8))
# Arbitration lost in SLA+R/W as master
I2C_I2STAT_S_TX_ARB_LOST_M_SLA = ((0xB0))
# Data has been transmitted, ACK has been received
I2C_I2STAT_S_TX_DAT_ACK = ((0xB8))
# Data has been transmitted, NACK has been received
I2C_I2STAT_S_TX_DAT_NACK = ((0xC0))
# Last data byte in I2DAT has been transmitted (AA = 0);
# ACK has been received
I2C_I2STAT_S_TX_LAST_DAT_ACK = ((0xC8))
# Time out in case of using I2C slave mode
I2C_SLAVE_TIME_OUT = 0x10000

# I2C Data register definition
# Mask for I2DAT register
I2C_I2DAT_BITMASK = ((0xFF))
# Idle data value will be send out in slave mode in case of the actual
# expecting data requested from the master is greater than its sending data
# length that can be supported
I2C_I2DAT_IDLE_CHAR = (0xFF)

# I2C Monitor mode control register description
# Monitor mode enable
I2C_I2MMCTRL_MM_ENA = ((1<<0))    
# SCL output enable
I2C_I2MMCTRL_ENA_SCL = ((1<<1))    
# Select interrupt register match
I2C_I2MMCTRL_MATCH_ALL = ((1<<2))    
# Mask for I2MMCTRL register
I2C_I2MMCTRL_BITMASK = ((0x07))
  
# I2C Data buffer register description
# I2C Data buffer register bit mask
I2DATA_BUFFER_BITMASK = ((0xFF))

# I2C Slave Address registers definition
# General Call enable bit
I2C_I2ADR_GC = ((1<<0))
# I2C Slave Address registers bit mask
I2C_I2ADR_BITMASK = ((0xFF))

# I2C Mask Register definition
def I2C_I2MASK_MASK(n):
  '''I2C Mask Register mask field.
  '''
  return ((n&0xFE))
  
# I2C SCL HIGH duty cycle Register definition
# I2C SCL HIGH duty cycle Register bit mask
I2C_I2SCLH_BITMASK = ((0xFFFF))

# I2C SCL LOW duty cycle Register definition
# I2C SCL LOW duty cycle Register bit mask
I2C_I2SCLL_BITMASK = ((0xFFFF))

# I2C status values
# Arbitration false
I2C_SETUP_STATUS_ARBF = (1<<8)  
# No ACK returned
I2C_SETUP_STATUS_NOACKF = (1<<9)  
# Status DONE
I2C_SETUP_STATUS_DONE = (1<<10)

# I2C monitor control configuration defines
# SCL output enable
I2C_MONITOR_CFG_SCL_OUTPUT = I2C_I2MMCTRL_ENA_SCL    
# Select interrupt register match
I2C_MONITOR_CFG_MATCHALL = I2C_I2MMCTRL_MATCH_ALL

def PARAM_I2C_SLAVEADDR_CH(n):
  '''Macros check I2C slave address.
  '''
  return ((n>=0) and (n<=3))
  
def PARAM_I2Cx(n):
  '''Macro to determine if it is valid SSP port numbe.
  '''
  return (((n)==(LPC_I2C0)) or ((n)==(LPC_I2C1)) or ((n)==(LPC_I2C2)))
  
def PARAM_I2C_MONITOR_CFG(n):
  '''Macros check I2C monitor configuration type.
  '''
  return ((n==I2C_MONITOR_CFG_SCL_OUTPUT) or (I2C_MONITOR_CFG_MATCHALL))
  
class I2C_M_SETUP_Type(cstruct):
  '''Master transfer setup data structure definitions.
  
  sl_addr7bit:  Slave address in 7bit mode
  tx_data:  Pointer to Transmit data - NULL if data transmit is not used
  tx_length:  Transmit data length - 0 if data transmit is not used
  tx_count: Current Transmit data counter
  rx_data:  Pointer to Receive data - NULL if data receive is not used
  rx_length:  Receive data length - 0 if data receive is not used
  rx_count: Current Receive data counter
  retransmissions_max:  Max Re-Transmission value
  retransmissions_count:  Current Re-Transmission counter
  status: Current status of I2C activity
  callback: Pointer to Call back function when transmission complete used in 
            interrupt transfer mode
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class I2C_OWNSLAVEADDR_CFG_Type(cstruct):
  '''I2C Own slave address setting structure.
  
  SlaveAddrChannel: Slave Address channel in I2C control, should be in range
                    from 0..3
  SlaveAddr_7bit: Value of 7-bit slave address
  GeneralCallState: Enable/Disable General Call Functionality when I2C control 
                    being in Slave mode, should be:
                    ENABLE: Enable General Call function.
                    DISABLE: Disable General Call function.
  SlaveAddrMaskValue: Any bit in this 8-bit value (bit 7:1) which is set to '1'
                      will cause an automatic compare on the corresponding bit
                      of the received address when it is compared to the 
                      SlaveAddr_7bit value associated with this mask register.
                      In other words, bits in SlaveAddr_7bit value which are 
                      masked are not taken into account in determining an 
                      address match
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
                          
  '''
  pass

class I2C_TRANSFER_OPT_Type:
  '''Transfer option type definitions.
  '''
  # Transfer in polling mode
  I2C_TRANSFER_POLLING = 0
  # Transfer in interrupt mode
  I2C_TRANSFER_INTERRUPT = 1

class I2C_S_SETUP_Type(cstruct):
  '''Slave transfer setup data structure definitions.
  
  tx_data:  Pointer to Transmit data - NULL if data transmit is not used
  tx_length:  Transmit data length - 0 if data transmit is not used
  tx_count: Current Transmit data counter
  rx_data:  Pointer to Receive data - NULL if data receive is not used
  rx_length:  Receive data length - 0 if data receive is not used
  rx_count: Current Receive data counter
  status: Current status of I2C activity
  callback: Pointer to Call back function when transmission complete used in 
            interrupt transfer mode
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
            
  '''
  pass

def I2C_MonitorModeCmd(I2Cx, NewState):
  '''Enable/Disable I2C monitor mode.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  NewState: New State of this function, should be:
            ENABLE: Enable monitor mode.
            DISABLE: Disable monitor mode.
            
  '''
  return robocaller("I2C_MonitorModeCmd", "void", I2Cx, NewState)

def I2C_IntCmd(I2Cx, NewState):
  '''Enable/Disable interrupt for I2C peripheral.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  NewState: New State of I2C peripheral interrupt in NVIC core should be:
            ENABLE: enable interrupt for this I2C peripheral
            DISABLE: disable interrupt for this I2C peripheral

  '''
  return robocaller("I2C_IntCmd", "void", I2Cx, NewState)

def I2C_DeInit(I2Cx):
  '''De-initializes the I2C peripheral registers to their default reset values.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
        
  '''
  return robocaller("I2C_DeInit", "void", I2Cx)

def I2C_SlaveHandler(I2Cx):
  '''General Slave Interrupt handler for I2C peripheral.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
        
  '''
  return robocaller("I2C_SlaveHandler", "void", I2Cx)

def I2C_MonitorModeConfig(I2Cx, MonitorCfgType, NewState):
  '''Configures functionality in I2C monitor mode.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  MonitorCfgType: Monitor Configuration type, should be:
                  I2C_MONITOR_CFG_SCL_OUTPUT: I2C module can 'stretch' the clock
                  line (hold it low) until it has had time to respond to an I2C 
                  interrupt.
                  I2C_MONITOR_CFG_MATCHALL: When this bit is set to '1' and the 
                  I2C is in monitor mode, an interrupt will be generated on ANY 
                  address received.
  NewState: New State of this function, should be:
            ENABLE: Enable this function.
            DISABLE: Disable this function.
            
  '''
  return robocaller("I2C_MonitorModeConfig", "void", I2Cx, MonitorCfgType, NewState)

def I2C_MasterTransferData(I2Cx, TransferCfg, Opt):
  '''Transmit and Receive data in master mode.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
        
  TransferCfg:  Pointer to a I2C_M_SETUP_Type structure that contains specified
                information about the configuration for master transfer.
  Opt:  a I2C_TRANSFER_OPT_Type type that selected for interrupt or polling mode
  return: SUCCESS or ERROR
  
   '''
  return robocaller("I2C_MasterTransferData", "Status", I2Cx, TransferCfg, Opt)

def I2C_SlaveTransferComplete(I2Cx):
  '''Get status of Slave Transfer.
  
  I2Cx: I2C peripheral selected, should be
      LPC_I2C0
      LPC_I2C1
      LPC_I2C2
  return: Complete status, could be: TRUE/FALSE
  
  '''
  return robocaller("I2C_SlaveTransferComplete", "uint32_t", I2Cx)

def I2C_SlaveTransferData(I2Cx, TransferCfg, Opt):
  '''Get status of Slave Transfer.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  return: Complete status, could be: TRUE/FALSE
  
  '''
  return robocaller("I2C_SlaveTransferData", "Status", I2Cx, TransferCfg, Opt)

def I2C_SetOwnSlaveAddr(I2Cx, OwnSlaveAddrConfigStruct):
  '''Set Own slave address in I2C peripheral corresponding to parameter 
  specified in OwnSlaveAddrConfigStruct.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  OwnSlaveAddrConfigStruct: Pointer to a I2C_OWNSLAVEADDR_CFG_Type structure
                            that contains the configuration information for the
                            specified I2C slave address.
                            
  '''
  return robocaller("I2C_SetOwnSlaveAddr", "void", I2Cx, OwnSlaveAddrConfigStruct)

def I2C_MasterTransferComplete(I2Cx):
  '''Get status of Master Transfer.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  return: Master transfer status, could be:
          TRUE: master transfer completed
          FALSE: master transfer have not completed yet
          
  '''
  return robocaller("I2C_MasterTransferComplete", "uint32_t", I2Cx)

def I2C_MasterHandler(I2Cx):
  '''General Master Interrupt handler for I2C peripheral.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
        
  '''
  return robocaller("I2C_MasterHandler", "void", I2Cx)

def I2C_MonitorHandler(I2Cx, buffer, size):
  '''.
 
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  '''
  return robocaller("I2C_MonitorHandler", "BOOL_8", I2Cx, buffer, size)

def I2C_Init(I2Cx, clockrate):
  '''Initializes the I2Cx peripheral with specified parameter.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  clockrate: Target clock rate value to initialized I2C peripheral (Hz)
  
  '''
  return robocaller("I2C_Init", "void", I2Cx, clockrate)

def I2C_MonitorGetDatabuffer(I2Cx):
  '''Get data from I2C data buffer in monitor mode.

  In monitor mode, the I2C module may lose the ability to stretch the clock 
  (stall the bus) if the ENA_SCL bit is not set. This means that the processor
  will have a limited amount of time to read the contents of the data received
  on the bus. If the processor reads the I2DAT shift register, as it ordinarily
  would, it could have only one bit-time to respond to the interrupt before the
  received data is overwritten by new data.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  return: uint8_t
  
  '''
  return robocaller("I2C_MonitorGetDatabuffer", "uint8_t", I2Cx)

def I2C_Cmd(I2Cx, NewState):
  '''Enable or disable I2C peripheral's operation.
  
  I2Cx: I2C peripheral selected, should be
        LPC_I2C0
        LPC_I2C1
        LPC_I2C2
  NewState: New State of I2Cx peripheral's operation
  
  '''
  return robocaller("I2C_Cmd", "void", I2Cx, NewState)
