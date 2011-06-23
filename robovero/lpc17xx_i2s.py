"""I2S client library functions. See LPC17xx CMSIS-Compliant
Standard Peripheral Firmware Driver Library documentation."""
from internals import robocaller, cstruct

I2S_WORDWIDTH_8 = ((0))
I2S_WORDWIDTH_16 = ((1))
I2S_WORDWIDTH_32 = ((3))
I2S_STEREO = ((0))
I2S_MONO = ((1))
I2S_MASTER_MODE = ((0))
I2S_SLAVE_MODE = ((1))
I2S_STOP_ENABLE = ((1))
I2S_STOP_DISABLE = ((0))
I2S_RESET_ENABLE = ((1))
I2S_RESET_DISABLE = ((0))
I2S_MUTE_ENABLE = ((1))
I2S_MUTE_DISABLE = ((0))
I2S_TX_MODE = ((0))
I2S_RX_MODE = ((1))
I2S_CLKSEL_FRDCLK = ((0))
I2S_CLKSEL_MCLK = ((2))
I2S_4PIN_ENABLE = ((1))
I2S_4PIN_DISABLE = ((0))
I2S_MCLK_ENABLE = ((1))
I2S_MCLK_DISABLE = ((0))
I2S_DMA_1 = ((0))
I2S_DMA_2 = ((1))
I2S_DAO_WORDWIDTH_8 = ((0))		
I2S_DAO_WORDWIDTH_16 = ((1))		
I2S_DAO_WORDWIDTH_32 = ((3))		
I2S_DAO_MONO = ((1<<2))
I2S_DAO_STOP = ((1<<3))
I2S_DAO_RESET = ((1<<4))
I2S_DAO_SLAVE = ((1<<5))
def I2S_DAO_WS_HALFPERIOD(n):
  return ((n<<6))

I2S_DAO_MUTE = ((1<<15))
I2S_DAI_WORDWIDTH_8 = ((0))		
I2S_DAI_WORDWIDTH_16 = ((1))		
I2S_DAI_WORDWIDTH_32 = ((3))		
I2S_DAI_MONO = ((1<<2))
I2S_DAI_STOP = ((1<<3))
I2S_DAI_RESET = ((1<<4))
I2S_DAI_SLAVE = ((1<<5))
def I2S_DAI_WS_HALFPERIOD(n):
  return (((n&0x1FF)<<6))

I2S_DAI_MUTE = ((1<<15))
I2S_STATE_IRQ = ((1))
I2S_STATE_DMA1 = ((1<<1))
I2S_STATE_DMA2 = ((1<<2))
def I2S_STATE_RX_LEVEL(n):
  return (((n&0x1F)<<8))

def I2S_STATE_TX_LEVEL(n):
  return (((n&0x1F)<<16))

I2S_DMA1_RX_ENABLE = ((1))
I2S_DMA1_TX_ENABLE = ((1<<1))
def I2S_DMA1_RX_DEPTH(n):
  return (((n&0x1F)<<8))

def I2S_DMA1_TX_DEPTH(n):
  return (((n&0x1F)<<16))

I2S_DMA2_RX_ENABLE = ((1))
I2S_DMA2_TX_ENABLE = ((1<<1))
def I2S_DMA2_RX_DEPTH(n):
  return (((n&0x1F)<<8))

def I2S_DMA2_TX_DEPTH(n):
  return (((n&0x1F)<<16))

I2S_IRQ_RX_ENABLE = ((1))
I2S_IRQ_TX_ENABLE = ((1<<1))
def I2S_IRQ_RX_DEPTH(n):
  return (((n&0x1F)<<8))

def I2S_IRQ_TX_DEPTH(n):
  return (((n&0x1F)<<16))

def I2S_TXRATE_Y_DIVIDER(n):
  return ((n&0xFF))

def I2S_TXRATE_X_DIVIDER(n):
  return (((n&0xFF)<<8))

def I2S_RXRATE_Y_DIVIDER(n):
  return ((n&0xFF))

def I2S_RXRATE_X_DIVIDER(n):
  return (((n&0xFF)<<8))

def I2S_TXBITRATE(n):
  return ((n&0x3F))

def I2S_RXBITRATE(n):
  return ((n&0x3F))

def I2S_TXMODE_CLKSEL(n):
  return ((n&0x03))

I2S_TXMODE_4PIN_ENABLE = ((1<<2))
I2S_TXMODE_MCENA = ((1<<3))
def I2S_RXMODE_CLKSEL(n):
  return ((n&0x03))

I2S_RXMODE_4PIN_ENABLE = ((1<<2))
I2S_RXMODE_MCENA = ((1<<3))
def PARAM_I2Sx(n):
  return ((n)==(LPC_I2S))

def PRAM_I2S_FREQ(freq):
  return ((freq>=16000)and(freq <= 96000))

def PARAM_I2S_WORDWIDTH(n):
  return ((n==I2S_WORDWIDTH_8)or(n==I2S_WORDWIDTH_16)\

or(n==I2S_WORDWIDTH_32))
def PARAM_I2S_CHANNEL(n):
  return ((n==I2S_STEREO)or(n==I2S_MONO))

def PARAM_I2S_WS_SEL(n):
  return ((n==I2S_MASTER_MODE)or(n==I2S_SLAVE_MODE))

def PARAM_I2S_STOP(n):
  return ((n==I2S_STOP_ENABLE)or(n==I2S_STOP_DISABLE))

def PARAM_I2S_RESET(n):
  return ((n==I2S_RESET_ENABLE)or(n==I2S_RESET_DISABLE))

def PARAM_I2S_MUTE(n):
  return ((n==I2S_MUTE_ENABLE)or(n==I2S_MUTE_DISABLE))

def PARAM_I2S_TRX(n):
  return ((n==I2S_TX_MODE)or(n==I2S_RX_MODE))

def PARAM_I2S_CLKSEL(n):
  return ((n==I2S_CLKSEL_FRDCLK)or(n==I2S_CLKSEL_MCLK))

def PARAM_I2S_4PIN(n):
  return ((n==I2S_4PIN_ENABLE)or(n==I2S_4PIN_DISABLE))

def PARAM_I2S_MCLK(n):
  return ((n==I2S_MCLK_ENABLE)or(n==I2S_MCLK_DISABLE))

def PARAM_I2S_DMA(n):
  return ((n==I2S_DMA_1)or(n==I2S_DMA_2))

def PARAM_I2S_DMA_DEPTH(n):
  return ((n>=0)or(n<=31))

def PARAM_I2S_IRQ_LEVEL(n):
  return ((n>=0)or(n<=31))

def PARAM_I2S_HALFPERIOD(n):
  return ((n>0)and(n<512))

def PARAM_I2S_BITRATE(n):
  return ((n>=0)and(n<=63))

class I2S_CFG_Type(cstruct):
	pass

class I2S_DMAConf_Type(cstruct):
	pass

class I2S_MODEConf_Type(cstruct):
	pass

def I2S_GetLevel(I2Sx, TRMode):
	return robocaller("I2S_GetLevel", "uint8_t", I2Sx, TRMode)

def I2S_GetIRQDepth(I2Sx, TRMode):
	return robocaller("I2S_GetIRQDepth", "uint8_t", I2Sx, TRMode)

def I2S_Mute(I2Sx, TRMode):
	return robocaller("I2S_Mute", "void", I2Sx, TRMode)

def I2S_Start(I2Sx):
	return robocaller("I2S_Start", "void", I2Sx)

def I2S_Pause(I2Sx, TRMode):
	return robocaller("I2S_Pause", "void", I2Sx, TRMode)

def I2S_Init(I2Sx):
	return robocaller("I2S_Init", "void", I2Sx)

def I2S_SetBitRate(I2Sx, bitrate, TRMode):
	return robocaller("I2S_SetBitRate", "void", I2Sx, bitrate, TRMode)

def I2S_FreqConfig(I2Sx, Freq, TRMode):
	return robocaller("I2S_FreqConfig", "Status", I2Sx, Freq, TRMode)

def I2S_DMACmd(I2Sx, DMAIndex, TRMode, NewState):
	return robocaller("I2S_DMACmd", "void", I2Sx, DMAIndex, TRMode, NewState)

def I2S_Send(I2Sx, BufferData):
	return robocaller("I2S_Send", "void", I2Sx, BufferData)

def I2S_Receive(I2Sx):
	return robocaller("I2S_Receive", "uint32_t", I2Sx)

def I2S_DeInit(I2Sx):
	return robocaller("I2S_DeInit", "void", I2Sx)

def I2S_Config(I2Sx, TRMode, ConfigStruct):
	return robocaller("I2S_Config", "void", I2Sx, TRMode, ConfigStruct)

def I2S_IRQCmd(I2Sx, TRMode, NewState):
	return robocaller("I2S_IRQCmd", "void", I2Sx, TRMode, NewState)

def I2S_IRQConfig(I2Sx, TRMode, level):
	return robocaller("I2S_IRQConfig", "void", I2Sx, TRMode, level)

def I2S_Stop(I2Sx, TRMode):
	return robocaller("I2S_Stop", "void", I2Sx, TRMode)

def I2S_DMAConfig(I2Sx, DMAConfig, TRMode):
	return robocaller("I2S_DMAConfig", "void", I2Sx, DMAConfig, TRMode)

def I2S_ModeConfig(I2Sx, ModeConfig, TRMode):
	return robocaller("I2S_ModeConfig", "void", I2Sx, ModeConfig, TRMode)

def I2S_GetIRQStatus(I2Sx, TRMode):
	return robocaller("I2S_GetIRQStatus", "FunctionalState", I2Sx, TRMode)

