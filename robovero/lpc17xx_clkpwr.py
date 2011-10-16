"""Clock and power client library functions. Find implementation details in 
LPC17xx CMSIS-Compliant Standard Peripheral Firmware Driver Library
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

# Peripheral Clock Selection Definitions
# Peripheral clock divider bit position for WDT
CLKPWR_PCLKSEL_WDT = 0
# Peripheral clock divider bit position for TIMER0
CLKPWR_PCLKSEL_TIMER0 = 2
# Peripheral clock divider bit position for TIMER1
CLKPWR_PCLKSEL_TIMER1 = 4
# Peripheral clock divider bit position for UART0
CLKPWR_PCLKSEL_UART0 = 6
# Peripheral clock divider bit position for UART1
CLKPWR_PCLKSEL_UART1 = 8
# Peripheral clock divider bit position for PWM1
CLKPWR_PCLKSEL_PWM1 = 12
# Peripheral clock divider bit position for I2C0
CLKPWR_PCLKSEL_I2C0 = 14
# Peripheral clock divider bit position for SPI
CLKPWR_PCLKSEL_SPI = 16
# Peripheral clock divider bit position for SSP1
CLKPWR_PCLKSEL_SSP1 = 20
# Peripheral clock divider bit position for DAC
CLKPWR_PCLKSEL_DAC = 22
# Peripheral clock divider bit position for ADC
CLKPWR_PCLKSEL_ADC = 24
# Peripheral clock divider bit position for CAN1
CLKPWR_PCLKSEL_CAN1 = 26
# Peripheral clock divider bit position for CAN2
CLKPWR_PCLKSEL_CAN2 = 28
# Peripheral clock divider bit position for ACF
CLKPWR_PCLKSEL_ACF = 30
# Peripheral clock divider bit position for QEI
CLKPWR_PCLKSEL_QEI = 32
# Peripheral clock divider bit position for PCB
CLKPWR_PCLKSEL_PCB = 36
# Peripheral clock divider bit position for I2C1
CLKPWR_PCLKSEL_I2C1 = 38
# Peripheral clock divider bit position for SSP0
CLKPWR_PCLKSEL_SSP0 = 42
# Peripheral clock divider bit position for TIMER2
CLKPWR_PCLKSEL_TIMER2 = 44
# Peripheral clock divider bit position for TIMER3
CLKPWR_PCLKSEL_TIMER3 = 46
# Peripheral clock divider bit position for UART2
CLKPWR_PCLKSEL_UART2 = 48
# Peripheral clock divider bit position for UART3
CLKPWR_PCLKSEL_UART3 = 50
# Peripheral clock divider bit position for I2C2
CLKPWR_PCLKSEL_I2C2 = 52
# Peripheral clock divider bit position for I2S
CLKPWR_PCLKSEL_I2S = 54
# Peripheral clock divider bit position for RIT
CLKPWR_PCLKSEL_RIT = 58
# Peripheral clock divider bit position for SYSCON
CLKPWR_PCLKSEL_SYSCON = 60
# Peripheral clock divider bit position for MC
CLKPWR_PCLKSEL_MC = 62

#  Macro for Peripheral Clock Selection register bit values
# Peripheral clock is CCLK/4
CLKPWR_PCLKSEL_CCLK_DIV_4 = 0
# Peripheral clock is CCLK
CLKPWR_PCLKSEL_CCLK_DIV_1 = 1
# Peripheral clock is CCLK/2
CLKPWR_PCLKSEL_CCLK_DIV_2 = 2

# Power Control for Peripherals Definitions
# Timer/Counter 0 power/clock control bit
CLKPWR_PCONP_PCTIM0 = 1<<1
# Timer/Counter 1 power/clock control bit
CLKPWR_PCONP_PCTIM1 = (1<<2)
# UART0 power/clock control bit
CLKPWR_PCONP_PCUART0 = (1<<3)
# UART1 power/clock control bit
CLKPWR_PCONP_PCUART1 = (1<<4)
# PWM1 power/clock control bit
CLKPWR_PCONP_PCPWM1 = (1<<6)
# The I2C0 interface power/clock control bit
CLKPWR_PCONP_PCI2C0 = (1<<7)
# The SPI interface power/clock control bit
CLKPWR_PCONP_PCSPI = (1<<8)
# The RTC power/clock control bit
CLKPWR_PCONP_PCRTC = (1<<9)
# The SSP1 interface power/clock control bit
CLKPWR_PCONP_PCSSP1 = (1<<10)
# A/D converter 0 (ADC0) power/clock control bit
CLKPWR_PCONP_PCAD = (1<<12)
# CAN Controller 1 power/clock control bit
CLKPWR_PCONP_PCAN1 = (1<<13)
# CAN Controller 2 power/clock control bit
CLKPWR_PCONP_PCAN2 = (1<<14)
# GPIO power/clock control bit
CLKPWR_PCONP_PCGPIO = (1<<15)
# Repetitive Interrupt Timer power/clock control bit
CLKPWR_PCONP_PCRIT = (1<<16)
# Motor Control PWM
CLKPWR_PCONP_PCMC = (1<<17)
# Quadrature Encoder Interface power/clock control bit
CLKPWR_PCONP_PCQEI = (1<<18)
# The I2C1 interface power/clock control bit
CLKPWR_PCONP_PCI2C1 = (1<<19)
# The SSP0 interface power/clock control bit
CLKPWR_PCONP_PCSSP0 = (1<<21)
# Timer 2 power/clock control bit
CLKPWR_PCONP_PCTIM2 = (1<<22)
# Timer 3 power/clock control bit
CLKPWR_PCONP_PCTIM3 = (1<<23)
# UART 2 power/clock control bit
CLKPWR_PCONP_PCUART2 = (1<<24)
# UART 3 power/clock control bit
CLKPWR_PCONP_PCUART3 = (1<<25)
# I2C interface 2 power/clock control bit
CLKPWR_PCONP_PCI2C2 = (1<<26)
# I2S interface power/clock control bit
CLKPWR_PCONP_PCI2S = (1<<27)
# GP DMA function power/clock control bit
CLKPWR_PCONP_PCGPDMA = (1<<29)
# Ethernet block power/clock control bit
CLKPWR_PCONP_PCENET = (1<<30)
# USB interface power/clock control bit
CLKPWR_PCONP_PCUSB = (1<<31)

# Macro defines for Clock Source Select Register
# Internal RC oscillator
CLKPWR_CLKSRCSEL_CLKSRC_IRC = (0x00)
# Main oscillator 
CLKPWR_CLKSRCSEL_CLKSRC_MAINOSC = (0x01)
# RTC oscillator
CLKPWR_CLKSRCSEL_CLKSRC_RTC = (0x02)
# Clock source selection bit mask
CLKPWR_CLKSRCSEL_BITMASK = (0x03)

# Macro defines for Clock Output Configuration Register
# Selects the CPU clock as the CLKOUT source
CLKPWR_CLKOUTCFG_CLKOUTSEL_CPU = (0x00)
# Selects the main oscillator as the CLKOUT source
CLKPWR_CLKOUTCFG_CLKOUTSEL_MAINOSC = (0x01)
# Selects the Internal RC oscillator as the CLKOUT source
CLKPWR_CLKOUTCFG_CLKOUTSEL_RC = (0x02)
# Selects the USB clock as the CLKOUT source
CLKPWR_CLKOUTCFG_CLKOUTSEL_USB = (0x03)
# Selects the RTC oscillator as the CLKOUT source
CLKPWR_CLKOUTCFG_CLKOUTSEL_RTC = (0x04)

def CLKPWR_CLKOUTCFG_CLKOUTDIV(n):
  '''Integer value to divide the output clock by, minus one.
  '''
  return ((n&0x0F)<<4)
  
# CLKOUT enable control
CLKPWR_CLKOUTCFG_CLKOUT_EN = (1<<8)
# CLKOUT activity indication
CLKPWR_CLKOUTCFG_CLKOUT_ACT = (1<<9)
# Clock source selection bit mask
CLKPWR_CLKOUTCFG_BITMASK = (0x3FF)

# Macro defines for PPL0 Control Register
# PLL 0 control enable
CLKPWR_PLL0CON_ENABLE = (0x01)
# PLL 0 control connect
CLKPWR_PLL0CON_CONNECT = (0x02)
# PLL 0 control bit mask
CLKPWR_PLL0CON_BITMASK = (0x03)

# Macro defines for PPL0 Configuration Register
def CLKPWR_PLL0CFG_MSEL(n):
  '''PLL 0 Configuration MSEL field.
  '''
  return ((n&0x7FFF))
  
def CLKPWR_PLL0CFG_NSEL(n):
  '''PLL 0 Configuration NSEL field.
  '''
  return (((n<<16)&0xFF0000))
  
# PLL 0 Configuration bit mask
CLKPWR_PLL0CFG_BITMASK = ((0xFF7FFF))

#Macro defines for PPL0 Status Register
def CLKPWR_PLL0STAT_MSEL(n):
  '''PLL 0 MSEL value.
  '''
  return ((n&0x7FFF))


def CLKPWR_PLL0STAT_NSEL(n):
  '''PLL NSEL get value.
  '''
  return (((n>>16)&0xFF))
  
# PLL status enable bit
CLKPWR_PLL0STAT_PLLE = (1<<24)
# PLL status Connect bit
CLKPWR_PLL0STAT_PLLC = (1<<25)
# PLL status lock
CLKPWR_PLL0STAT_PLOCK = (1<<26)

# Macro defines for PPL0 Feed Register
# PLL0 Feed bit mask
CLKPWR_PLL0FEED_BITMASK = (0xFF)

# Macro defines for PLL1 Control Register
# USB PLL control enable
CLKPWR_PLL1CON_ENABLE = (0x01)
# USB PLL control connect 
CLKPWR_PLL1CON_CONNECT = (0x02)
# USB PLL control bit mask
CLKPWR_PLL1CON_BITMASK = (0x03)

# Macro defines for PLL1 Configuration Register
def CLKPWR_PLL1CFG_MSEL(n):
  '''USB PLL MSEL set value.
  '''
  return ((n&0x1F))
  
def CLKPWR_PLL1CFG_PSEL(n):
  '''USB PLL PSEL set value.
  '''
  return (((n&0x03)<<5))
  
# USB PLL configuration bit mask
CLKPWR_PLL1CFG_BITMASK = ((0x7F))

# Macro defines for PLL1 Status Register
def CLKPWR_PLL1STAT_MSEL(n):
  '''USB PLL MSEL get value.
  '''
  return ((n&0x1F))
  
def CLKPWR_PLL1STAT_PSEL(n):
  '''USB PLL PSEL get value.
  '''
  return (((n>>5)&0x03))
  
# USB PLL status enable bit
CLKPWR_PLL1STAT_PLLE = (1<<8)
# USB PLL status Connect bit
CLKPWR_PLL1STAT_PLLC = (1<<9)
# USB PLL status lock
CLKPWR_PLL1STAT_PLOCK = (1<<10)

# Macro defines for PLL1 Feed Register
# PLL1 Feed bit mask
CLKPWR_PLL1FEED_BITMASK = (0xFF)

# Macro defines for CPU Clock Configuration Register
# CLKPWR_CCLKCFG_BITMASK
CLKPWR_CCLKCFG_BITMASK = ((0xFF))

# Macro defines for USB Clock Configuration Register
# USB Clock Configuration bit mask
CLKPWR_USBCLKCFG_BITMASK = ((0x0F))

# Macro defines for IRC Trim Register
# IRC Trim bit mask
CLKPWR_IRCTRIM_BITMASK = ((0x0F))

# Macro defines for Peripheral Clock Selection Register 0 and 1
# Peripheral Clock Selection 0 mask bit
CLKPWR_PCLKSEL0_BITMASK = ((0xFFF3F3FF))
# Peripheral Clock Selection 1 mask bit
CLKPWR_PCLKSEL1_BITMASK = ((0xFCF3F0F3))

def CLKPWR_PCLKSEL_SET(p,n):
  '''Macro to set peripheral clock of each type.
  
  p: position of two bits that hold divider of peripheral clock
  n: value of divider of peripheral clock  to be set
  '''
  return _SBF(p,n)

def CLKPWR_PCLKSEL_BITMASK(p):
  '''Macro to mask peripheral clock of each type.
  
  p: position of two bits that hold divider of peripheral clock
  
  '''
  return _SBF(p,0x03)
  
def CLKPWR_PCLKSEL_GET(p, n):
  '''Macro to get peripheral clock of each type.
  
  p: position of two bits that hold divider of peripheral clock
  n: value of divider of peripheral clock  to be set
  
  '''
  return (((n>>p)&0x03))

# Macro defines for Power Mode Control Register  
# Power mode control bit 0
CLKPWR_PCON_PM0 = (1<<0)
# Power mode control bit 1
CLKPWR_PCON_PM1 = (1<<1)
# Brown-Out Reduced Power Mode
CLKPWR_PCON_BODPDM = (1<<2)
# Brown-Out Global Disable
CLKPWR_PCON_BOGD = (1<<3)
# Brown Out Reset Disable
CLKPWR_PCON_BORD = (1<<4)
#  Sleep Mode entry flag
CLKPWR_PCON_SMFLAG = (1<<8)
# Deep Sleep entry flag
CLKPWR_PCON_DSFLAG = (1<<9)
# Power-down entry flag
CLKPWR_PCON_PDFLAG = (1<<10)
# Deep Power-down entry flag
CLKPWR_PCON_DPDFLAG = (1<<11)

# Macro defines for Power Control for Peripheral Register
# Power Control for Peripherals bit mask
CLKPWR_PCONP_BITMASK = 0xEFEFF7DE


def CLKPWR_SetPCLKDiv(ClkType, DivVal):
  '''Set value of each Peripheral Clock Selection.
  
  ClkType:  Peripheral Clock Selection of each type. Should be:
            CLKPWR_PCLKSEL_WDT      : WDT
            CLKPWR_PCLKSEL_TIMER0   : Timer 0
            CLKPWR_PCLKSEL_TIMER1   : Timer 1
            CLKPWR_PCLKSEL_UART0    : UART 0
            CLKPWR_PCLKSEL_UART1    : UART 1
            CLKPWR_PCLKSEL_PWM1     : PWM 1
            CLKPWR_PCLKSEL_I2C0     : I2C 0
            CLKPWR_PCLKSEL_SPI      : SPI
            CLKPWR_PCLKSEL_SSP1     : SSP 1
            CLKPWR_PCLKSEL_DAC      : DAC
            CLKPWR_PCLKSEL_ADC      : ADC
            CLKPWR_PCLKSEL_CAN1     : CAN 1
            CLKPWR_PCLKSEL_CAN2     : CAN 2
            CLKPWR_PCLKSEL_ACF      : ACF
            CLKPWR_PCLKSEL_QEI      : QEI
            CLKPWR_PCLKSEL_PCB      : PCB
            CLKPWR_PCLKSEL_I2C1     : I2C 1
            CLKPWR_PCLKSEL_SSP0     : SSP 0
            CLKPWR_PCLKSEL_TIMER2   : Timer 2
            CLKPWR_PCLKSEL_TIMER3   : Timer 3
            CLKPWR_PCLKSEL_UART2    : UART 2
            CLKPWR_PCLKSEL_UART3    : UART 3
            CLKPWR_PCLKSEL_I2C2     : I2C 2
            CLKPWR_PCLKSEL_I2S      : I2S
            CLKPWR_PCLKSEL_RIT      : RIT
            CLKPWR_PCLKSEL_SYSCON   : SYSCON
            CLKPWR_PCLKSEL_MC       : MC
  DivVal: Value of divider, should be:
          CLKPWR_PCLKSEL_CCLK_DIV_4: PCLK_peripheral = CCLK/4
          CLKPWR_PCLKSEL_CCLK_DIV_1: PCLK_peripheral = CCLK/1
          CLKPWR_PCLKSEL_CCLK_DIV_2: PCLK_peripheral = CCLK/2
            
  '''
  return robocaller("CLKPWR_SetPCLKDiv", "void", ClkType, DivVal)

def CLKPWR_Sleep():
  '''Enter Sleep mode with co-operated instruction by the Cortex-M3.
  '''
  return robocaller("CLKPWR_Sleep", "void", )

def CLKPWR_DeepSleep():
  '''Enter Deep Sleep mode with co-operated instruction by the Cortex-M3.
  '''
  return robocaller("CLKPWR_DeepSleep", "void", )

def CLKPWR_PowerDown():
  '''Enter Power Down mode with co-operated instruction by the Cortex-M3.
  '''
  return robocaller("CLKPWR_PowerDown", "void", )

def CLKPWR_GetPCLK(ClkType):
  '''Get current value of each Peripheral Clock.
  
  ClkType:  Peripheral Clock Selection of each type. Should be:
            CLKPWR_PCLKSEL_WDT      : WDT
            CLKPWR_PCLKSEL_TIMER0   : Timer 0
            CLKPWR_PCLKSEL_TIMER1   : Timer 1
            CLKPWR_PCLKSEL_UART0    : UART 0
            CLKPWR_PCLKSEL_UART1    : UART 1
            CLKPWR_PCLKSEL_PWM1     : PWM 1
            CLKPWR_PCLKSEL_I2C0     : I2C 0
            CLKPWR_PCLKSEL_SPI      : SPI
            CLKPWR_PCLKSEL_SSP1     : SSP 1
            CLKPWR_PCLKSEL_DAC      : DAC
            CLKPWR_PCLKSEL_ADC      : ADC
            CLKPWR_PCLKSEL_CAN1     : CAN 1
            CLKPWR_PCLKSEL_CAN2     : CAN 2
            CLKPWR_PCLKSEL_ACF      : ACF
            CLKPWR_PCLKSEL_QEI      : QEI
            CLKPWR_PCLKSEL_PCB      : PCB
            CLKPWR_PCLKSEL_I2C1     : I2C 1
            CLKPWR_PCLKSEL_SSP0     : SSP 0
            CLKPWR_PCLKSEL_TIMER2   : Timer 2
            CLKPWR_PCLKSEL_TIMER3   : Timer 3
            CLKPWR_PCLKSEL_UART2    : UART 2
            CLKPWR_PCLKSEL_UART3    : UART 3
            CLKPWR_PCLKSEL_I2C2     : I2C 2
            CLKPWR_PCLKSEL_I2S      : I2S
            CLKPWR_PCLKSEL_RIT      : RIT
            CLKPWR_PCLKSEL_SYSCON   : SYSCON
            CLKPWR_PCLKSEL_MC       : MC
  return: Value of Selected Peripheral Clock
  
  '''
  return robocaller("CLKPWR_GetPCLK", "uint32_t", ClkType)

def CLKPWR_ConfigPPWR(PPType, NewState):
  '''Configure power supply for each peripheral according to NewState.
  
  PPType: Type of peripheral used to enable power, should be:
          CLKPWR_PCONP_PCTIM0     : Timer 0
          CLKPWR_PCONP_PCTIM1     : Timer 1
          CLKPWR_PCONP_PCUART0    : UART 0
          CLKPWR_PCONP_PCUART1    : UART 1
          CLKPWR_PCONP_PCPWM1     : PWM 1
          CLKPWR_PCONP_PCI2C0     : I2C 0
          CLKPWR_PCONP_PCSPI      : SPI
          CLKPWR_PCONP_PCRTC      : RTC
          CLKPWR_PCONP_PCSSP1     : SSP 1
          CLKPWR_PCONP_PCAD       : ADC
          CLKPWR_PCONP_PCAN1      : CAN 1
          CLKPWR_PCONP_PCAN2      : CAN 2
          CLKPWR_PCONP_PCGPIO     : GPIO
          CLKPWR_PCONP_PCRIT      : RIT
          CLKPWR_PCONP_PCMC       : MC
          CLKPWR_PCONP_PCQEI      : QEI
          CLKPWR_PCONP_PCI2C1     : I2C 1
          CLKPWR_PCONP_PCSSP0     : SSP 0
          CLKPWR_PCONP_PCTIM2     : Timer 2
          CLKPWR_PCONP_PCTIM3     : Timer 3
          CLKPWR_PCONP_PCUART2    : UART 2
          CLKPWR_PCONP_PCUART3    : UART 3
          CLKPWR_PCONP_PCI2C2     : I2C 2
          CLKPWR_PCONP_PCI2S      : I2S
          CLKPWR_PCONP_PCGPDMA    : GPDMA
          CLKPWR_PCONP_PCENET     : Ethernet
          CLKPWR_PCONP_PCUSB      : USB
  NewState: New state of Peripheral Power, should be:
            ENABLE: Enable power for this peripheral
            DISABLE: Disable power for this peripheral
            
  '''
  return robocaller("CLKPWR_ConfigPPWR", "void", PPType, NewState)

def CLKPWR_GetPCLKSEL(ClkType):
  '''Get current value of each Peripheral Clock Selection.
  
  ClkType:  Peripheral Clock Selection of each type. Should be:
            CLKPWR_PCLKSEL_WDT      : WDT
            CLKPWR_PCLKSEL_TIMER0   : Timer 0
            CLKPWR_PCLKSEL_TIMER1   : Timer 1
            CLKPWR_PCLKSEL_UART0    : UART 0
            CLKPWR_PCLKSEL_UART1    : UART 1
            CLKPWR_PCLKSEL_PWM1     : PWM 1
            CLKPWR_PCLKSEL_I2C0     : I2C 0
            CLKPWR_PCLKSEL_SPI      : SPI
            CLKPWR_PCLKSEL_SSP1     : SSP 1
            CLKPWR_PCLKSEL_DAC      : DAC
            CLKPWR_PCLKSEL_ADC      : ADC
            CLKPWR_PCLKSEL_CAN1     : CAN 1
            CLKPWR_PCLKSEL_CAN2     : CAN 2
            CLKPWR_PCLKSEL_ACF      : ACF
            CLKPWR_PCLKSEL_QEI      : QEI
            CLKPWR_PCLKSEL_PCB      : PCB
            CLKPWR_PCLKSEL_I2C1     : I2C 1
            CLKPWR_PCLKSEL_SSP0     : SSP 0
            CLKPWR_PCLKSEL_TIMER2   : Timer 2
            CLKPWR_PCLKSEL_TIMER3   : Timer 3
            CLKPWR_PCLKSEL_UART2    : UART 2
            CLKPWR_PCLKSEL_UART3    : UART 3
            CLKPWR_PCLKSEL_I2C2     : I2C 2
            CLKPWR_PCLKSEL_I2S      : I2S
            CLKPWR_PCLKSEL_RIT      : RIT
            CLKPWR_PCLKSEL_SYSCON   : SYSCON
            CLKPWR_PCLKSEL_MC       : MC
  return: Value of Selected Peripheral Clock Selection
  
  '''
  return robocaller("CLKPWR_GetPCLKSEL", "uint32_t", ClkType)

def CLKPWR_DeepPowerDown():
  '''Enter Deep Power Down mode with co-operated instruction by the Cortex-M3.
  '''
  return robocaller("CLKPWR_DeepPowerDown", "void", )

