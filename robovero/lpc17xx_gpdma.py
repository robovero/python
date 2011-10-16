"""General purpose DMA client library functions. Find implementation details in
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

# DMA Connection number definitions
# SSP0 Tx
GPDMA_CONN_SSP0_Tx = ((0))     
# SSP0 Rx
GPDMA_CONN_SSP0_Rx = ((1))     
# SSP1 Tx
GPDMA_CONN_SSP1_Tx = ((2))     
# SSP1 Rx 
GPDMA_CONN_SSP1_Rx = ((3))     
# ADC
GPDMA_CONN_ADC = ((4))     
# I2S channel 0
GPDMA_CONN_I2S_Channel_0 = ((5))     
# I2S channel 1
GPDMA_CONN_I2S_Channel_1 = ((6))     
# DAC
GPDMA_CONN_DAC = ((7))     
# UART0 Tx
GPDMA_CONN_UART0_Tx = ((8))     
# UART0 Rx
GPDMA_CONN_UART0_Rx = ((9))     
# UART1 Tx
GPDMA_CONN_UART1_Tx = ((10))     
# UART1 Rx
GPDMA_CONN_UART1_Rx = ((11))     
# UART2 Tx
GPDMA_CONN_UART2_Tx = ((12))     
# UART2 Rx
GPDMA_CONN_UART2_Rx = ((13))     
# UART3 Tx
GPDMA_CONN_UART3_Tx = ((14))     
# UART3 Rx
GPDMA_CONN_UART3_Rx = ((15))     
# MAT0.0
GPDMA_CONN_MAT0_0 = ((16))     
# MAT0.1
GPDMA_CONN_MAT0_1 = ((17))     
# MAT1.0
GPDMA_CONN_MAT1_0 = ((18))     
# MAT1.1
GPDMA_CONN_MAT1_1 = ((19))     
# MAT2.0
GPDMA_CONN_MAT2_0 = ((20))     
# MAT2.1
GPDMA_CONN_MAT2_1 = ((21))     
# MAT3.0
GPDMA_CONN_MAT3_0 = ((22))     
# MAT3.1
GPDMA_CONN_MAT3_1 = ((23))

# GPDMA Transfer type definitions 
# Memory to memory - DMA control
GPDMA_TRANSFERTYPE_M2M = ((0))   
# Memory to peripheral - DMA control
GPDMA_TRANSFERTYPE_M2P = ((1))   
# Peripheral to memory - DMA control
GPDMA_TRANSFERTYPE_P2M = ((2))   
# Source peripheral to destination peripheral - DMA control
GPDMA_TRANSFERTYPE_P2P = ((3))   

# Burst size in Source and Destination definitions
# Burst size = 1
GPDMA_BSIZE_1 = ((0)) 
# Burst size = 4
GPDMA_BSIZE_4 = ((1)) 
# Burst size = 8
GPDMA_BSIZE_8 = ((2)) 
# Burst size = 16
GPDMA_BSIZE_16 = ((3)) 
# Burst size = 32
GPDMA_BSIZE_32 = ((4)) 
# Burst size = 64
GPDMA_BSIZE_64 = ((5)) 
# Burst size = 128
GPDMA_BSIZE_128 = ((6)) 
# Burst size = 256
GPDMA_BSIZE_256 = ((7))

# Width in Source transfer width and Destination transfer width definitions
# Width = 1 byte
GPDMA_WIDTH_BYTE = ((0)) 
# Width = 2 bytes
GPDMA_WIDTH_HALFWORD = ((1)) 
# Width = 4 bytes
GPDMA_WIDTH_WORD = ((2)) 

# DMA Request Select Mode definitions
# UART TX/RX is selected
GPDMA_REQSEL_UART = ((0)) 
# Timer match is selected
GPDMA_REQSEL_TIMER = ((1))

# Macro defines for DMA Interrupt Status register
def GPDMA_DMACIntStat_Ch(n):
  return (((1<<n)&0xFF))
GPDMA_DMACIntStat_BITMASK = ((0xFF))

# Macro defines for DMA Interrupt Terminal Count Request Status register
def GPDMA_DMACIntTCStat_Ch(n):
  return (((1<<n)&0xFF))
GPDMA_DMACIntTCStat_BITMASK = ((0xFF))

# Macro defines for DMA Interrupt Terminal Count Request Clear register
def GPDMA_DMACIntTCClear_Ch(n):
  return (((1<<n)&0xFF))
GPDMA_DMACIntTCClear_BITMASK = ((0xFF))

# Macro defines for DMA Interrupt Error Status register
def GPDMA_DMACIntErrStat_Ch(n):
  return (((1<<n)&0xFF))
GPDMA_DMACIntErrStat_BITMASK = ((0xFF))

# Macro defines for DMA Interrupt Error Clear register
def GPDMA_DMACIntErrClr_Ch(n):
  return (((1<<n)&0xFF))
GPDMA_DMACIntErrClr_BITMASK = ((0xFF))

# Macro defines for DMA Raw Interrupt Terminal Count Status register
def GPDMA_DMACRawIntTCStat_Ch(n):

  return (((1<<n)&0xFF))
GPDMA_DMACRawIntTCStat_BITMASK = ((0xFF))

# Macro defines for DMA Raw Error Interrupt Status register
def GPDMA_DMACRawIntErrStat_Ch(n):
  return (((1<<n)&0xFF))
GPDMA_DMACRawIntErrStat_BITMASK = ((0xFF))

# Macro defines for DMA Enabled Channel register
def GPDMA_DMACEnbldChns_Ch(n):
  return (((1<<n)&0xFF))
GPDMA_DMACEnbldChns_BITMASK = ((0xFF))

# Macro defines for DMA Software Burst Request register
def GPDMA_DMACSoftBReq_Src(n):
  return (((1<<n)&0xFFFF))
GPDMA_DMACSoftBReq_BITMASK = ((0xFFFF))

# Macro defines for DMA Software Single Request register
def GPDMA_DMACSoftSReq_Src(n):
  return (((1<<n)&0xFFFF))
GPDMA_DMACSoftSReq_BITMASK = ((0xFFFF))

# Macro defines for DMA Software Last Burst Request register
def GPDMA_DMACSoftLBReq_Src(n):
  return (((1<<n)&0xFFFF))
GPDMA_DMACSoftLBReq_BITMASK = ((0xFFFF))

# Macro defines for DMA Software Last Single Request register
def GPDMA_DMACSoftLSReq_Src(n):
  return (((1<<n)&0xFFFF))
GPDMA_DMACSoftLSReq_BITMASK = ((0xFFFF))

# Macro defines for DMA Configuration register
# DMA Controller enable
GPDMA_DMACConfig_E = ((0x01))   
# AHB Master endianness configuration
GPDMA_DMACConfig_M = ((0x02))   
GPDMA_DMACConfig_BITMASK = ((0x03))

# Macro defines for DMA Synchronization register
def GPDMA_DMACSync_Src(n):
  return (((1<<n)&0xFFFF))
GPDMA_DMACSync_BITMASK = ((0xFFFF))

# Macro defines for DMA Request Select register
def GPDMA_DMAReqSel_Input(n):
  return (((1<<(n-8))&0xFF))
GPDMA_DMAReqSel_BITMASK = ((0xFF))

# Macro defines for DMA Channel Linked List Item registers
# DMA Channel Linked List Item registers bit mask
GPDMA_DMACCxLLI_BITMASK = ((0xFFFFFFFC))

# Macro defines for DMA channel control registers
def GPDMA_DMACCxControl_TransferSize(n):
  '''Transfer size.
  '''
  return (((n&0xFFF)<<0))   

def GPDMA_DMACCxControl_SBSize(n):
  '''Source burst size.
  '''
  return (((n&0x07)<<12))   

def GPDMA_DMACCxControl_DBSize(n):
  '''Destination burst size.
  '''
  return (((n&0x07)<<15))   

def GPDMA_DMACCxControl_SWidth(n):
  '''Source transfer width.
  '''
  return (((n&0x07)<<18))   

def GPDMA_DMACCxControl_DWidth(n):
  '''Destination transfer width.
  '''
  return (((n&0x07)<<21))   

# Source increment
GPDMA_DMACCxControl_SI = ((1<<26))     
# Destination increment
GPDMA_DMACCxControl_DI = ((1<<27))     
# Indicates that the access is in user mode or privileged mode
GPDMA_DMACCxControl_Prot1 = ((1<<28))     
# Indicates that the access is bufferable or not bufferable
GPDMA_DMACCxControl_Prot2 = ((1<<29))     
# Indicates that the access is cacheable or not cacheable
GPDMA_DMACCxControl_Prot3 = ((1<<30))     
# Terminal count interrupt enable bit
GPDMA_DMACCxControl_I = ((1<<31))     
# DMA channel control registers bit mask
GPDMA_DMACCxControl_BITMASK = ((0xFCFFFFFF))

# Macro defines for DMA Channel Configuration registers
# DMA control enable
GPDMA_DMACCxConfig_E = ((1<<0))

def GPDMA_DMACCxConfig_SrcPeripheral(n):
  '''Source peripheral.
  '''
  return (((n&0x1F)<<1))   

def GPDMA_DMACCxConfig_DestPeripheral(n):
  '''Destination peripheral.
  '''
  return (((n&0x1F)<<6))   

def GPDMA_DMACCxConfig_TransferType(n):
  '''This value indicates the type of transfer.
  '''
  return (((n&0x7)<<11))   

# Interrupt error mask
GPDMA_DMACCxConfig_IE = ((1<<14))      
# Terminal count interrupt mask
GPDMA_DMACCxConfig_ITC = ((1<<15))     
# Lock
GPDMA_DMACCxConfig_L = ((1<<16))     
# Active
GPDMA_DMACCxConfig_A = ((1<<17))     
# Halt
GPDMA_DMACCxConfig_H = ((1<<18))     
# DMA Channel Configuration registers bit mask
GPDMA_DMACCxConfig_BITMASK = ((0x7FFFF))

def PARAM_GPDMA_CHANNEL(n):
  '''Macros check GPDMA channel.
  '''
  return ((n>=0) and (n<=7))

def PARAM_GPDMA_CONN(n):
  '''Macros check GPDMA connection type.
  '''
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
  '''Macros check GPDMA burst size type.
  '''
  return (
    (n==GPDMA_BSIZE_1) or (n==GPDMA_BSIZE_4)
    or (n==GPDMA_BSIZE_8) or (n==GPDMA_BSIZE_16)
    or (n==GPDMA_BSIZE_32) or (n==GPDMA_BSIZE_64)
    or (n==GPDMA_BSIZE_128) or (n==GPDMA_BSIZE_256)
    )
    
def PARAM_GPDMA_WIDTH(n):
  '''Macros check GPDMA width type.
  '''
  return (
    (n==GPDMA_WIDTH_BYTE) 
    or (n==GPDMA_WIDTH_HALFWORD)
    or (n==GPDMA_WIDTH_WORD)
    )
    
def PARAM_GPDMA_STAT(n):
  '''Macros check GPDMA status type.
  '''
  return (
    (n==GPDMA_STAT_INT) or (n==GPDMA_STAT_INTTC)
    or (n==GPDMA_STAT_INTERR) or (n==GPDMA_STAT_RAWINTTC)
    or (n==GPDMA_STAT_RAWINTERR) or (n==GPDMA_STAT_ENABLED_CH)
    )
    
def PARAM_GPDMA_TRANSFERTYPE(n):
  '''Macros check GPDMA transfer type.
  '''
  return (
    (n==GPDMA_TRANSFERTYPE_M2M) or (n==GPDMA_TRANSFERTYPE_M2P)
    or (n==GPDMA_TRANSFERTYPE_P2M) or (n==GPDMA_TRANSFERTYPE_P2P)
    )
    
def PARAM_GPDMA_STATCLR(n):
  '''Macros check GPDMA state clear type.
  '''
  return ((n==GPDMA_STATCLR_INTTC) or (n==GPDMA_STATCLR_INTERR))

def PARAM_GPDMA_REQSEL(n):
  '''Macros check GPDMA request select type.
  '''
  return ((n==GPDMA_REQSEL_UART) or (n==GPDMA_REQSEL_TIMER))

class GPDMA_StateClear_Type:
  '''GPDMA Interrupt clear status enumeration.
  '''
  # GPDMA Interrupt Terminal Count Request Clear
  GPDMA_STATCLR_INTTC = 0
  # GPDMA Interrupt Error Clear
  GPDMA_STATCLR_INTERR = 1

class GPDMA_LLI_Type(cstruct):
  '''GPDMA Linker List Item structure type definition.
  
  SrcAddr: Source Address
  DstAddr: Destination address
  NextLLI: Next LLI address, otherwise set to '0'
  Control: GPDMA Control of this LLI
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class GPDMA_Channel_CFG_Type(cstruct):
  '''GPDMA Channel configuration structure type definition.
  
  ChannelNum: DMA channel number, should be in range from 0 to 7. DMA channel 0
              has the highest priority and DMA channel 7 the lowest priority.
  TransferSize: Length/Size of transfer
  TransferWidth:  Transfer width - used for TransferType is 
                  GPDMA_TRANSFERTYPE_M2M only
  SrcMemAddr: Physical Source Address, used in case TransferType is chosen as
              GPDMA_TRANSFERTYPE_M2M or GPDMA_TRANSFERTYPE_M2P
  DstMemAddr: Physical Destination Address, used in case TransferType is chosen
              as GPDMA_TRANSFERTYPE_M2M or GPDMA_TRANSFERTYPE_P2M
  TransferType: Transfer Type, should be one of the following:
                GPDMA_TRANSFERTYPE_M2M: Memory to memory - DMA control
                GPDMA_TRANSFERTYPE_M2P: Memory to peripheral - DMA control
                GPDMA_TRANSFERTYPE_P2M: Peripheral to memory - DMA control
                GPDMA_TRANSFERTYPE_P2P: Source peripheral to destination 
                                        peripheral - DMA control
  SrcConn:  Peripheral Source Connection type, used in case TransferType is
            chosen as GPDMA_TRANSFERTYPE_P2M or GPDMA_TRANSFERTYPE_P2P, should
            be one of:  
            GPDMA_CONN_SSP0_Tx: SSP0, Tx
            GPDMA_CONN_SSP0_Rx: SSP0, Rx
            GPDMA_CONN_SSP1_Tx: SSP1, Tx
            GPDMA_CONN_SSP1_Rx: SSP1, Rx
            GPDMA_CONN_ADC: ADC
            GPDMA_CONN_I2S_Channel_0: I2S Channel 0
            GPDMA_CONN_I2S_Channel_1: I2S Channel 1
            GPDMA_CONN_DAC: DAC
            GPDMA_CONN_UART0_Tx_MAT0_0: UART0 Tx / MAT0.0
            GPDMA_CONN_UART0_Rx_MAT0_1: UART0 Rx / MAT0.1
            GPDMA_CONN_UART1_Tx_MAT1_0: UART1 Tx / MAT1.0
            GPDMA_CONN_UART1_Rx_MAT1_1: UART1 Rx / MAT1.1
            GPDMA_CONN_UART2_Tx_MAT2_0: UART2 Tx / MAT2.0
            GPDMA_CONN_UART2_Rx_MAT2_1: UART2 Rx / MAT2.1
            GPDMA_CONN_UART3_Tx_MAT3_0: UART3 Tx / MAT3.0
            GPDMA_CONN_UART3_Rx_MAT3_1: UART3 Rx / MAT3.1
  DstConn:  Peripheral Destination Connection type, used in case TransferType is
            chosen as GPDMA_TRANSFERTYPE_M2P or GPDMA_TRANSFERTYPE_P2P, should 
            be one of:
            GPDMA_CONN_SSP0_Tx: SSP0, Tx
            GPDMA_CONN_SSP0_Rx: SSP0, Rx
            GPDMA_CONN_SSP1_Tx: SSP1, Tx
            GPDMA_CONN_SSP1_Rx: SSP1, Rx
            GPDMA_CONN_ADC: ADC
            GPDMA_CONN_I2S_Channel_0: I2S Channel 0
            GPDMA_CONN_I2S_Channel_1: I2S Channel 1
            GPDMA_CONN_DAC: DAC
            GPDMA_CONN_UART0_Tx_MAT0_0: UART0 Tx / MAT0.0
            GPDMA_CONN_UART0_Rx_MAT0_1: UART0 Rx / MAT0.1
            GPDMA_CONN_UART1_Tx_MAT1_0: UART1 Tx / MAT1.0
            GPDMA_CONN_UART1_Rx_MAT1_1: UART1 Rx / MAT1.1
            GPDMA_CONN_UART2_Tx_MAT2_0: UART2 Tx / MAT2.0
            GPDMA_CONN_UART2_Rx_MAT2_1: UART2 Rx / MAT2.1
            GPDMA_CONN_UART3_Tx_MAT3_0: UART3 Tx / MAT3.0
            GPDMA_CONN_UART3_Rx_MAT3_1: UART3 Rx / MAT3.1
  DMALLI: Linker List Item structure data address if there's no Linker List, set
          as '0'
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class GPDMA_Status_Type:
  '''GPDMA Status enumeration.
  '''
  # GPDMA Interrupt Status
  GPDMA_STAT_INT = 0
  # GPDMA Interrupt Terminal Count Request Status
  GPDMA_STAT_INTTC = 1
  # GPDMA Interrupt Error Status
  GPDMA_STAT_INTERR = 2
  # GPDMA Raw Interrupt Terminal Count Status
  GPDMA_STAT_RAWINTTC = 3
  # GPDMA Raw Error Interrupt Status
  GPDMA_STAT_RAWINTERR = 4
  # GPDMA Enabled Channel Status
  GPDMA_STAT_ENABLED_CH = 5

def GPDMA_Init():
  '''Initialize GPDMA controller.
  '''
  return robocaller("GPDMA_Init", "void", )

def GPDMA_ChannelCmd(channelNum, NewState):
  '''Enable/Disable DMA channel.
  
  channelNum: GPDMA channel, should be in range from 0 to 7
  NewState: New State of this command, should be:
            ENABLE
            DISABLE
            
  '''
  return robocaller("GPDMA_ChannelCmd", "void", channelNum, NewState)

def GPDMA_Setup(GPDMAChannelConfig):
  '''Setup GPDMA channel peripheral according to the specified parameters in the
  GPDMAChannelConfig.
  
  GPDMAChannelConfig: Pointer to a GPDMA_CH_CFG_Type structure that contains the
                      configuration information for the specified GPDMA channel
                      peripheral.
  return: ERROR if selected channel is enabled before
          SUCCESS if channel is configured successfully
          
  '''
  return robocaller("GPDMA_Setup", "Status", GPDMAChannelConfig)

def GPDMA_IntGetStatus(stat_type, channel):
  '''Check if corresponding channel does have an active interrupt request or
  not.
  
  stat_type:  type of status, should be:
              GPDMA_STAT_INT: GPDMA Interrupt Status
              GPDMA_STAT_INTTC: GPDMA Interrupt Terminal Count Request Status
              GPDMA_STAT_INTERR: GPDMA Interrupt Error Status
              GPDMA_STAT_RAWINTTC: GPDMA Raw Interrupt Terminal Count Status
              GPDMA_STAT_RAWINTERR: GPDMA Raw Error Interrupt Status
              GPDMA_STAT_ENABLED_CH: GPDMA Enabled Channel Status
  channel: GPDMA channel, should be in range from 0 to 7
  return: status of DMA channel interrupt after masking
          SET: the corresponding channel has no active interrupt request
          RESET: the corresponding channel does have an active interrupt request
          
  '''
  return robocaller("GPDMA_IntGetStatus", "IntStatus", stat_type, channel)

def GPDMA_ClearIntPending(int_type, channel):
  '''Clear one or more interrupt requests on DMA channels.
  
  int_type: GPDMA_STATCLR_INTTC: GPDMA Interrupt Terminal Count Request Clear
            GPDMA_STATCLR_INTERR: GPDMA Interrupt Error Clear
  channel:  GPDMA channel, should be in range from 0 to 7
  
  '''
  return robocaller("GPDMA_ClearIntPending", "void", int_type, channel)
