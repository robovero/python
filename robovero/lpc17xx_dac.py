"""DAC client library functions. See LPC17xx CMSIS-Compliant Standard
Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

def DAC_VALUE(n):
  '''After the selected settling time after this field is written with a new
  VALUE, the voltage on the AOUT pin (with respect to VSSA) is VALUE/1024 × VREF.
  '''
  return (((n&0x3FF)<<6))

# If this bit = 0: The settling time of the DAC is 1 microsecond max,
# and the maximum current is 700 microAmpere
# If this bit = 1: The settling time of the DAC is 2.5 microsecond
# and the maximum current is 350 microAmpere
DAC_BIAS_EN = ((1<<16))

def DAC_CCNT_VALUE(n):
  '''Value to reload interrupt DMA counter.
  '''
  return ((n&0xffff))
  
# DCAR double buffering
DAC_DBLBUF_ENA = ((1<<1))
# DCAR Time out count enable
DAC_CNT_ENA = ((1<<2))
# DCAR DMA access
DAC_DMA_ENA = ((1<<3))
# DCAR DACCTRL mask bit
DAC_DACCTRL_MASK = ((0x0F))

def PARAM_DACx(n):
  '''Macro to determine if it is valid DAC peripheral.
  '''
  return ((n)==(LPC_DAC))

def PARAM_DAC_CURRENT_OPT(OPTION):
  '''Macro to check DAC current optional parameter.
  '''
  return ((OPTION == DAC_MAX_CURRENT_700uA) or (OPTION == DAC_MAX_CURRENT_350uA))

class DAC_CONVERTER_CFG_Type(cstruct):
  '''Configuration for DAC converter control register.
  
  DBLBUF_ENA: 0: Disable DACR double buffering
              1: when bit CNT_ENA, enable DACR double buffering feature
  CNT_ENA:  0: Time out counter is disable
            1: Time out conter is enable
  DMA_ENA:  0: DMA access is disable
            1: DMA burst request
  
  '''
  pass

class DAC_CURRENT_OPT:
  '''Current option in DAC configuration option.
  '''
  # The settling time of the DAC is 1 us max and the maximum current is 700 uA
  DAC_MAX_CURRENT_700uA = 0
  # The settling time of the DAC is 2.5 us and the maximum current is 350 uA
  DAC_MAX_CURRENT_350uA = 1

def DAC_SetBias(DACx, bias):
  '''Set Maximum current for DAC.
  
  DACx: pointer to LPC_DAC_TypeDef, should be: LPC_DAC
  bias: 0 is 700 uA
        1 is 350 uA
        
  '''
  return robocaller("DAC_SetBias", "void", DACx, bias)

def DAC_ConfigDAConverterControl(DACx, DAC_ConverterConfigStruct):
  '''To enable the DMA operation and control DMA timer.
  
  DACx: pointer to LPC_DAC_TypeDef, should be: LPC_DAC
  DAC_ConverterConfigStruct: pointer to DAC_CONVERTER_CFG_Type
  
  '''
  return robocaller("DAC_ConfigDAConverterControl", "void", DACx, DAC_ConverterConfigStruct)

def DAC_UpdateValue(DACx, dac_value):
  '''Update value to DAC.
  
  DACx: pointer to LPC_DAC_TypeDef, should be: LPC_DAC
  dac_value: value 10 bit to be converted to output
  
  '''
  return robocaller("DAC_UpdateValue", "void", DACx, dac_value)

def DAC_Init(DACx):
  '''Initial ADC configuration. Maximum  current is 700 uA, Value to AOUT is 0.
    
  DACx: pointer to LPC_DAC_TypeDef, should be: LPC_DAC
  
  '''
  return robocaller("DAC_Init", "void", DACx)

def DAC_SetDMATimeOut(DACx, time_out):
  '''Set reload value for interrupt/DMA counter.
    
  DACx: pointer to LPC_DAC_TypeDef, should be: LPC_DAC
  time_out: time out to reload for interrupt/DMA counter
  
  '''
  return robocaller("DAC_SetDMATimeOut", "void", DACx, time_out)

