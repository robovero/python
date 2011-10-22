"""I2S client library functions. Find implementation details in LPC17xx 
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

# I2S configuration parameter defines
# I2S Wordwidth bit
I2S_WORDWIDTH_8 = ((0))
I2S_WORDWIDTH_16 = ((1)) 
I2S_WORDWIDTH_32 = ((3))
# I2S Channel bit
I2S_STEREO = ((0))
I2S_MONO = ((1))
# I2S Master/Slave mode bit
I2S_MASTER_MODE = ((0))
I2S_SLAVE_MODE = ((1))
# I2S Stop bit
I2S_STOP_ENABLE = ((1))
I2S_STOP_DISABLE = ((0))
# I2S Reset bit
I2S_RESET_ENABLE = ((1))
I2S_RESET_DISABLE = ((0))
# I2S Mute bit
I2S_MUTE_ENABLE = ((1))
I2S_MUTE_DISABLE = ((0))
# I2S Transmit/Receive bit
I2S_TX_MODE = ((0))
I2S_RX_MODE = ((1))
# I2S Clock Select bit
I2S_CLKSEL_FRDCLK = ((0))
I2S_CLKSEL_MCLK = ((2))
# I2S 4-pin Mode bit
I2S_4PIN_ENABLE = ((1))
I2S_4PIN_DISABLE = ((0))
# I2S MCLK Enable bit 
I2S_MCLK_ENABLE = ((1))
I2S_MCLK_DISABLE = ((0))
# I2S select DMA bit
I2S_DMA_1 = ((0))
I2S_DMA_2 = ((1))

# Macro defines for DAO-Digital Audio Output register
# I2S wordwide - the number of bytes in data
# 8 bit
I2S_DAO_WORDWIDTH_8 = ((0))    
# 16 bit
I2S_DAO_WORDWIDTH_16 = ((1))    
# 32 bit
I2S_DAO_WORDWIDTH_32 = ((3))    
# I2S control mono or stereo format 
I2S_DAO_MONO = ((1<<2))
# I2S control stop mode
I2S_DAO_STOP = ((1<<3))
# I2S control reset mode
I2S_DAO_RESET = ((1<<4))
# I2S control master/slave mode
I2S_DAO_SLAVE = ((1<<5))

def I2S_DAO_WS_HALFPERIOD(n):
  '''I2S word select half period minus one.
  '''
  return ((n<<6))

# I2S control mute mode
I2S_DAO_MUTE = ((1<<15))

# Macro defines for DAI-Digital Audio Input register
# I2S wordwide - the number of bytes in data
# 8 bit
I2S_DAI_WORDWIDTH_8 = ((0))    
# 16 bit
I2S_DAI_WORDWIDTH_16 = ((1))    
# 32 bit
I2S_DAI_WORDWIDTH_32 = ((3))    
# I2S control mono or stereo format
I2S_DAI_MONO = ((1<<2))
# I2S control stop mode
I2S_DAI_STOP = ((1<<3))
# I2S control reset mode
I2S_DAI_RESET = ((1<<4))
# I2S control master/slave mode
I2S_DAI_SLAVE = ((1<<5))

def I2S_DAI_WS_HALFPERIOD(n):
  '''I2S word select half period minus one (9 bits).
  '''
  return (((n&0x1FF)<<6))

# I2S control mute mode
I2S_DAI_MUTE = ((1<<15))

# Macro defines for STAT register (Status Feedback register)
# I2S Status Receive or Transmit Interrupt
I2S_STATE_IRQ = ((1))
# I2S Status Receive or Transmit DMA1
I2S_STATE_DMA1 = ((1<<1))
# I2S Status Receive or Transmit DMA2
I2S_STATE_DMA2 = ((1<<2))

def I2S_STATE_RX_LEVEL(n):
  '''I2S Status Current level of the Receive FIFO (5 bits).
  '''
  return (((n&0x1F)<<8))

def I2S_STATE_TX_LEVEL(n):
  '''I2S Status Current level of the Transmit FIFO (5 bits).
  '''
  return (((n&0x1F)<<16))

# Macro defines for DMA1 register (DMA1 Configuration register)
# I2S control DMA1 for I2S receive
I2S_DMA1_RX_ENABLE = ((1))
# I2S control DMA1 for I2S transmit
I2S_DMA1_TX_ENABLE = ((1<<1))

def I2S_DMA1_RX_DEPTH(n):
  '''I2S set FIFO level that trigger a receive DMA request on DMA1.
  '''
  return (((n&0x1F)<<8))

def I2S_DMA1_TX_DEPTH(n):
  '''I2S set FIFO level that trigger a transmit DMA request on DMA1.
  '''
  return (((n&0x1F)<<16))

# I2S control DMA2 for I2S receive
I2S_DMA2_RX_ENABLE = ((1))
# I2S control DMA2 for I2S transmit
I2S_DMA2_TX_ENABLE = ((1<<1))

# Macro defines for DMA2 register (DMA2 Configuration register)
def I2S_DMA2_RX_DEPTH(n):
  '''I2S set FIFO level that trigger a receive DMA request on DMA2.
  '''
  return (((n&0x1F)<<8))

def I2S_DMA2_TX_DEPTH(n):
  '''I2S set FIFO level that trigger a transmit DMA request on DMA2.
  '''
  return (((n&0x1F)<<16))

# Macro defines for IRQ register (Interrupt Request Control register)
# I2S control I2S receive interrupt
I2S_IRQ_RX_ENABLE = ((1))
# I2S control I2S transmit interrupt
I2S_IRQ_TX_ENABLE = ((1<<1))

def I2S_IRQ_RX_DEPTH(n):
  '''I2S set the FIFO level on which to create an irq request.
  '''
  return (((n&0x1F)<<8))

def I2S_IRQ_TX_DEPTH(n):
  '''I2S set the FIFO level on which to create an irq request.
  '''
  return (((n&0x1F)<<16))
  
# Macro defines for TXRATE/RXRATE register (Transmit/Receive Clock Rate register)
def I2S_TXRATE_Y_DIVIDER(n):
  '''I2S Transmit MCLK rate denominator.
  '''
  return ((n&0xFF))

def I2S_TXRATE_X_DIVIDER(n):
  '''I2S Transmit MCLK rate denominator.
  '''
  return (((n&0xFF)<<8))

def I2S_RXRATE_Y_DIVIDER(n):
  '''I2S Receive MCLK rate denominator.
  '''
  return ((n&0xFF))

def I2S_RXRATE_X_DIVIDER(n):
  '''I2S Receive MCLK rate denominator.
  '''
  return (((n&0xFF)<<8))
  
# Macro defines for TXBITRATE & RXBITRATE register
def I2S_TXBITRATE(n):
  '''Transmit Bit Rate registe.
  '''
  return ((n&0x3F))

def I2S_RXBITRATE(n):
  '''Receive Bit Rate register.
  '''
  return ((n&0x3F))

# Macro defines for TXMODE/RXMODE register (Transmit/Receive Mode Control register)
def I2S_TXMODE_CLKSEL(n):
  '''I2S Transmit select clock source (2 bits).
  '''
  return ((n&0x03))


# I2S Transmit control 4-pin mode
I2S_TXMODE_4PIN_ENABLE = ((1<<2))
# I2S Transmit control the TX_MCLK output
I2S_TXMODE_MCENA = ((1<<3))

def I2S_RXMODE_CLKSEL(n):
  '''I2S Receive select clock source.
  '''
  return ((n&0x03))

# I2S Receive control 4-pin mode
I2S_RXMODE_4PIN_ENABLE = ((1<<2))
# I2S Receive control the TX_MCLK output
I2S_RXMODE_MCENA = ((1<<3))

def PARAM_I2Sx(n):
  '''Macro to determine if it is valid I2S peripheral.
  '''
  return ((n)==(LPC_I2S))

def PRAM_I2S_FREQ(freq):
  '''Macro to check Data to send valid.
  '''
  return ((freq>=16000)and(freq <= 96000))

def PARAM_I2S_WORDWIDTH(n):
  '''Macro check I2S word width type.
  '''
  return ((n==I2S_WORDWIDTH_8) or (n==I2S_WORDWIDTH_16) or (n==I2S_WORDWIDTH_32))
  
def PARAM_I2S_CHANNEL(n):
  '''Macro check I2S channel type.
  '''
  return ((n==I2S_STEREO) or (n==I2S_MONO))

def PARAM_I2S_WS_SEL(n):
  '''Macro check I2S master/slave mode.
  '''
  return ((n==I2S_MASTER_MODE)or(n==I2S_SLAVE_MODE))

def PARAM_I2S_STOP(n):
  '''Macro check I2S stop mode.
  '''
  return ((n==I2S_STOP_ENABLE)or(n==I2S_STOP_DISABLE))

def PARAM_I2S_RESET(n):
  '''Macro check I2S reset mode.
  '''
  return ((n==I2S_RESET_ENABLE)or(n==I2S_RESET_DISABLE))

def PARAM_I2S_MUTE(n):
  '''Macro check I2S reset mode.
  '''
  return ((n==I2S_MUTE_ENABLE)or(n==I2S_MUTE_DISABLE))

def PARAM_I2S_TRX(n):
  '''Macro check I2S transmit/receive mode.
  '''
  return ((n==I2S_TX_MODE)or(n==I2S_RX_MODE))

def PARAM_I2S_CLKSEL(n):
  '''Macro check I2S clock select mode.
  '''
  return ((n==I2S_CLKSEL_FRDCLK)or(n==I2S_CLKSEL_MCLK))

def PARAM_I2S_4PIN(n):
  '''Macro check I2S 4-pin mode.
  '''
  return ((n==I2S_4PIN_ENABLE)or(n==I2S_4PIN_DISABLE))

def PARAM_I2S_MCLK(n):
  '''Macro check I2S MCLK mode.
  '''
  return ((n==I2S_MCLK_ENABLE)or(n==I2S_MCLK_DISABLE))

def PARAM_I2S_DMA(n):
  '''Macro check I2S DMA mode.
  '''
  return ((n==I2S_DMA_1)or(n==I2S_DMA_2))

def PARAM_I2S_DMA_DEPTH(n):
  '''Macro check I2S DMA depth value.
  '''
  return ((n>=0)or(n<=31))

def PARAM_I2S_IRQ_LEVEL(n):
  '''Macro check I2S irq level value.
  '''
  return ((n>=0)or(n<=31))

def PARAM_I2S_HALFPERIOD(n):
  '''Macro check I2S half-period value.
  '''
  return ((n>0)and(n<512))

def PARAM_I2S_BITRATE(n):
  '''Macro check I2S bit-rate value.
  '''
  return ((n>=0)and(n<=63))

class I2S_CFG_Type(cstruct):
  '''I2S configuration structure definition.
  
  wordwidth:  the number of bytes in data as follow:
              I2S_WORDWIDTH_8: 8 bit data
              I2S_WORDWIDTH_16: 16 bit data
              I2S_WORDWIDTH_32: 32 bit data
  mono: Set mono/stereo mode, should be:
        I2S_STEREO: stereo mode
        I2S_MONO: mono mode
  stop: Disables accesses on FIFOs, should be:
        I2S_STOP_ENABLE: enable stop mode
        I2S_STOP_DISABLE: disable stop mode
  reset:  Asynchronously reset tje transmit channel and FIFO, should be:
          I2S_RESET_ENABLE: enable reset mode
          I2S_RESET_DISABLE: disable reset mode
  ws_sel: Set Master/Slave mode, should be:
          I2S_MASTER_MODE: I2S master mode
          I2S_SLAVE_MODE: I2S slave mode
  mute: MUTE mode: when true, the transmit channel sends only zeroes, shoule be:
        I2S_MUTE_ENABLE: enable mute mode
        I2S_MUTE_DISABLE: disable mute mode
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class I2S_DMAConf_Type(cstruct):
  '''I2S DMA configuration structure definition.
  
  DMAIndex: Select DMA1 or DMA2, should be:
            I2S_DMA_1: DMA1
            I2S_DMA_2: DMA2
  depth:  FIFO level that triggers a DMA request 
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
  
  '''
  pass

class I2S_MODEConf_Type(cstruct):
  '''I2S mode configuration structure definition.
  
  clksel: Clock source selection, should be:
          I2S_CLKSEL_FRDCLK: Select the fractional rate divider clock output
          I2S_CLKSEL_MCLK: Select the MCLK signal as the clock source
  fpin: Select four pin mode, should be:
        I2S_4PIN_ENABLE: 4-pin enable
        I2S_4PIN_DISABLE: 4-pin disable
  mcena:  Select MCLK mode, should be:
          I2S_MCLK_ENABLE: MCLK enable for output
          I2S_MCLK_DISABLE: MCLK disable for output
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

def I2S_GetLevel(I2Sx, TRMode):
  '''Get I2S Buffer Level.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode
  return: current level of Transmit/Receive Buffer
  
  '''
  return robocaller("I2S_GetLevel", "uint8_t", I2Sx, TRMode)

def I2S_GetIRQDepth(I2Sx, TRMode):
  '''Get I2S interrupt depth.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  return: depth of FIFO level on which to create an irq request
  
  '''
  return robocaller("I2S_GetIRQDepth", "uint8_t", I2Sx, TRMode)

def I2S_Mute(I2Sx, TRMode):
  '''I2S Mute.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  
  '''
  return robocaller("I2S_Mute", "void", I2Sx, TRMode)

def I2S_Start(I2Sx):
  '''Clear all STOP,RESET and MUTE bit, ready to operate.
   
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  
  '''
  return robocaller("I2S_Start", "void", I2Sx)

def I2S_Pause(I2Sx, TRMode):
  '''I2S Pause.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  
  '''
  return robocaller("I2S_Pause", "void", I2Sx, TRMode)

def I2S_Init(I2Sx):
  '''Initialize I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S

  '''
  return robocaller("I2S_Init", "void", I2Sx)

def I2S_SetBitRate(I2Sx, bitrate, TRMode):
  '''I2S set bitrate.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  bitrate:  bitrate value should be in range: 0 .. 63
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  
  '''
  return robocaller("I2S_SetBitRate", "void", I2Sx, bitrate, TRMode)

def I2S_FreqConfig(I2Sx, Freq, TRMode):
  '''Set frequency for I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  Freq: The frequency to be set. It can range from 16-96 kHz(16, 22.05, 32, 
        44.1, 48, 96kHz)
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  return: Status: ERROR or SUCCESS
  
  '''
  return robocaller("I2S_FreqConfig", "Status", I2Sx, Freq, TRMode)

def I2S_DMACmd(I2Sx, DMAIndex, TRMode, NewState):
  '''Enable/Disable DMA operation for I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  DMAIndex: DMAIndex chose what DMA is used, should be:
            I2S_DMA_1 = 0: DMA1
            I2S_DMA_2 = 1: DMA2
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  NewState: new state of DMA operation, should be:
            ENABLE
            DISABLE
  
  '''
  return robocaller("I2S_DMACmd", "void", I2Sx, DMAIndex, TRMode, NewState)

def I2S_Send(I2Sx, BufferData):
  '''I2S Send data.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  BufferData: pointer to uint32_t is the data will be send
  
  '''
  return robocaller("I2S_Send", "void", I2Sx, BufferData)

def I2S_Receive(I2Sx):
  '''I2S Receive Data.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  return: received value
  
  '''
  return robocaller("I2S_Receive", "uint32_t", I2Sx)

def I2S_DeInit(I2Sx):
  '''Deinitialize I2S transmit or receive.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S

  '''
  return robocaller("I2S_DeInit", "void", I2Sx)

def I2S_Config(I2Sx, TRMode, ConfigStruct):
  '''Configure I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  ConfigStruct: pointer to I2S_CFG_Type structure which will be initialized
  
  '''
  return robocaller("I2S_Config", "void", I2Sx, TRMode, ConfigStruct)

def I2S_IRQCmd(I2Sx, TRMode, NewState):
  '''Enable/Disable IRQ for I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  NewState: ENABLE or DISABLE
  
  '''
  return robocaller("I2S_IRQCmd", "void", I2Sx, TRMode, NewState)

def I2S_IRQConfig(I2Sx, TRMode, level):
  '''Configure IRQ for I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  level:  the FIFO level that triggers IRQ request
  
  '''
  return robocaller("I2S_IRQConfig", "void", I2Sx, TRMode, level)

def I2S_Stop(I2Sx, TRMode):
  '''I2S Stop.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  
  '''
  return robocaller("I2S_Stop", "void", I2Sx, TRMode)

def I2S_DMAConfig(I2Sx, DMAConfig, TRMode):
  '''Configure DMA operation for I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  DMAConfig:  pointer to I2S_DMAConf_Type used for configuration
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  
  '''
  return robocaller("I2S_DMAConfig", "void", I2Sx, DMAConfig, TRMode)

def I2S_ModeConfig(I2Sx, ModeConfig, TRMode):
  '''Configuration operating mode for I2S.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  ModeConfig: pointer to I2S_MODEConf_Type used for configuration
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  
  '''
  return robocaller("I2S_ModeConfig", "void", I2Sx, ModeConfig, TRMode)

def I2S_GetIRQStatus(I2Sx, TRMode):
  '''Get I2S interrupt status.
  
  I2Sx: I2S peripheral selected, should be: LPC_I2S
  TRMode: Transmit/receive mode, should be:
          I2S_TX_MODE = 0: transmit mode
          I2S_RX_MODE = 1: receive mode 
  return: FunctionalState should be: ENABLE or DISABLE
  
  '''
  return robocaller("I2S_GetIRQStatus", "FunctionalState", I2Sx, TRMode)
