"""Ethernet MAC client library functions. Find implementation details in LPC17xx
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

# EMAC PHY status type definitions
# Link Status
EMAC_PHY_STAT_LINK = (0)
# Speed Status
EMAC_PHY_STAT_SPEED = (1)    
# Duplex Status
EMAC_PHY_STAT_DUP = (2)

# EMAC PHY device Speed definitions
# Auto-negotiation mode
EMAC_MODE_AUTO = (0)    
# 10Mbps FullDuplex mode
EMAC_MODE_10M_FULL = (1)    
# 10Mbps HalfDuplex mode
EMAC_MODE_10M_HALF = (2)    
# 100Mbps FullDuplex mode
EMAC_MODE_100M_FULL = (3)    
# 100Mbps HalfDuplex mode
EMAC_MODE_100M_HALF = (4)  

# EMAC Memory Buffer configuration for 16K Ethernet RAM
# Num.of RX Fragments 4*1536= 6.0kB
EMAC_NUM_RX_FRAG = 4           
# Num.of TX Fragments 3*1536= 4.6kB
EMAC_NUM_TX_FRAG = 3           
# Max. Ethernet Frame Size
EMAC_ETH_MAX_FLEN = 1536        
# Frame Transmit timeout count
EMAC_TX_FRAME_TOUT = 0x00100000  

# Macro defines for MAC Configuration Register 1
# Receive Enable
EMAC_MAC1_REC_EN = 0x00000001  
# Pass All Receive Frames
EMAC_MAC1_PASS_ALL = 0x00000002  
# RX Flow Control
EMAC_MAC1_RX_FLOWC = 0x00000004  
# TX Flow Control
EMAC_MAC1_TX_FLOWC = 0x00000008  
# Loop Back Mode
EMAC_MAC1_LOOPB = 0x00000010  
# Reset TX Logic
EMAC_MAC1_RES_TX = 0x00000100  
# Reset MAC TX Control Sublayer
EMAC_MAC1_RES_MCS_TX = 0x00000200  
# Reset RX Logic
EMAC_MAC1_RES_RX = 0x00000400  
# Reset MAC RX Control Sublayer
EMAC_MAC1_RES_MCS_RX = 0x00000800  
# Simulation Reset
EMAC_MAC1_SIM_RES = 0x00004000  
# Soft Reset MAC
EMAC_MAC1_SOFT_RES = 0x00008000 

# Macro defines for MAC Configuration Register 2 
# Full-Duplex Mode
EMAC_MAC2_FULL_DUP = 0x00000001  
# Frame Length Checking
EMAC_MAC2_FRM_LEN_CHK = 0x00000002  
# Huge Frame Enable
EMAC_MAC2_HUGE_FRM_EN = 0x00000004  
# Delayed CRC Mode
EMAC_MAC2_DLY_CRC = 0x00000008  
# Append CRC to every Frame
EMAC_MAC2_CRC_EN = 0x00000010  
# Pad all Short Frames
EMAC_MAC2_PAD_EN = 0x00000020  
# VLAN Pad Enable
EMAC_MAC2_VLAN_PAD_EN = 0x00000040  
# Auto Detect Pad Enable
EMAC_MAC2_ADET_PAD_EN = 0x00000080  
# Pure Preamble Enforcement
EMAC_MAC2_PPREAM_ENF = 0x00000100  
# Long Preamble Enforcement
EMAC_MAC2_LPREAM_ENF = 0x00000200  
# No Backoff Algorithm
EMAC_MAC2_NO_BACKOFF = 0x00001000  
# Backoff Presurre / No Backoff
EMAC_MAC2_BACK_PRESSURE = 0x00002000  
# Excess Defer
EMAC_MAC2_EXCESS_DEF = 0x00004000  

# Macro defines for Back-to-Back Inter-Packet-Gap Register
def EMAC_IPGT_BBIPG(n):
  '''Programmable field representing the nibble time offset of the minimum
  possible period between the end of any transmitted packet to the beginning of
  the next.
  '''
  return (n&0x7F)
  
# Recommended value for Full Duplex of Programmable field representing the
# nibble time offset of the minimum possible period between the end of any
# transmitted packet to the beginning of the next
EMAC_IPGT_FULL_DUP = (EMAC_IPGT_BBIPG(0x15))
# Recommended value for Half Duplex of Programmable field representing the
# nibble time offset of the minimum possible period between the end of any
# transmitted packet to the beginning of the next
EMAC_IPGT_HALF_DUP = (EMAC_IPGT_BBIPG(0x12))

# Macro defines for Non Back-to-Back Inter-Packet-Gap Register
def EMAC_IPGR_NBBIPG_P2(n):
  '''Programmable field representing the Non-Back-to-Back Inter-Packet-Gap.
  '''
  return (n&0x7F)
  
# Recommended value for Programmable field representing the Non-Back-to-Back Inter-Packet-Gap Part 1
EMAC_IPGR_P2_DEF = (EMAC_IPGR_NBBIPG_P2(0x12))

def EMAC_IPGR_NBBIPG_P1(n):
  '''Programmable field representing the optional carrierSense window referenced
  in IEEE 802.3/4.2.3.2.1 'Carrier Deference'.
  '''
  return ((n&0x7F)<<8)
  
# Recommended value for Programmable field representing the Non-Back-to-Back
# Inter-Packet-Gap Part 2
EMAC_IPGR_P1_DEF = EMAC_IPGR_NBBIPG_P1(0x0C)

# Macro defines for Collision Window/Retry Register
def EMAC_CLRT_MAX_RETX(n):
  '''Programmable field specifying the number of retransmission attempts
  following a collision before aborting the packet due to excessive collisions.
  '''
  return (n&0x0F)

def EMAC_CLRT_COLL(n):
  '''Programmable field representing the slot time or collision window during
  which collisions occur in properly configured networks.
  '''
  return ((n&0x3F)<<8)

# Default value for Collision Window / Retry register
EMAC_CLRT_DEF = ((EMAC_CLRT_MAX_RETX(0x0F))|(EMAC_CLRT_COLL(0x37)))

# Macro defines for Maximum Frame Register
def EMAC_MAXF_MAXFRMLEN(n):
  '''Represents a maximum receive frame of 1536 octets.
  '''
  return (n&0xFFFF)

# Macro defines for PHY Support Register
# Reduced MII Logic Current Speed
EMAC_SUPP_SPEED = 0x00000100    
# Reset Reduced MII Logic
EMAC_SUPP_RES_RMII = 0x00000800

# Macro defines for Test Register    
# Shortcut Pause Quanta
EMAC_TEST_SHCUT_PQUANTA = 0x00000001    
# Test Pause
EMAC_TEST_TST_PAUSE = 0x00000002    
# Test Back Pressure
EMAC_TEST_TST_BACKP = 0x00000004

# Macro defines for MII Management Configuration Register
# Scan Increment PHY Address
EMAC_MCFG_SCAN_INC = 0x00000001    
# Suppress Preamble
EMAC_MCFG_SUPP_PREAM = 0x00000002

def EMAC_MCFG_CLK_SEL(n):
  '''Clock Select Field.
  '''
  return ((n&0x0F)<<2)
  
# Reset MII Management Hardware
EMAC_MCFG_RES_MII = 0x00008000    
# MII Clock max
EMAC_MCFG_MII_MAXCLK = 2500000

# Macro defines for MII Management Command Register
# MII Read
EMAC_MCMD_READ = 0x00000001    
# MII Scan continuously
EMAC_MCMD_SCAN = 0x00000002    
# MII Write timeout count
EMAC_MII_WR_TOUT = 0x00050000    
# MII Read timeout count
EMAC_MII_RD_TOUT = 0x00050000 

# Macro defines for MII Management Address Register
def EMAC_MADR_REG_ADR(n):
  '''MII Register Address field.
  '''
  return (n&0x1F)

def EMAC_MADR_PHY_ADR(n):
  '''PHY Address Field.
  '''
  return ((n&0x1F)<<8)

# Macro defines for MII Management Write Data Register  
def EMAC_MWTD_DATA(n):
  '''Data field for MMI Management Write Data register.
  '''
  return (n&0xFFFF)

# Macro defines for MII Management Read Data Register    
def EMAC_MRDD_DATA(n):
  '''Data field for MMI Management Read Data register.
  '''
  return (n&0xFFFF)
    
# Macro defines for MII Management Indicators Register
# MII is Busy
EMAC_MIND_BUSY = 0x00000001    
# MII Scanning in Progress
EMAC_MIND_SCAN = 0x00000002    
# MII Read Data not valid
EMAC_MIND_NOT_VAL = 0x00000004    
# MII Link Failed
EMAC_MIND_MII_LINK_FAIL = 0x00000008  

# Macro defines for Command Register  
# Enable Receive
EMAC_CR_RX_EN = 0x00000001    
# Enable Transmit
EMAC_CR_TX_EN = 0x00000002    
# Reset Host Registers
EMAC_CR_REG_RES = 0x00000008    
# Reset Transmit Datapath
EMAC_CR_TX_RES = 0x00000010    
# Reset Receive Datapath
EMAC_CR_RX_RES = 0x00000020    
# Pass Runt Frames
EMAC_CR_PASS_RUNT_FRM = 0x00000040    
# Pass RX Filter
EMAC_CR_PASS_RX_FILT = 0x00000080    
# TX Flow Control
EMAC_CR_TX_FLOW_CTRL = 0x00000100    
# Reduced MII Interface
EMAC_CR_RMII = 0x00000200    
# Full Duplex
EMAC_CR_FULL_DUP = 0x00000400 

# Macro defines for Status Register  
# Enable Receive
EMAC_SR_RX_EN = 0x00000001    
# Enable Transmit
EMAC_SR_TX_EN = 0x00000002

# Macro defines for Transmit Status Vector 0 Register
# CRC error
EMAC_TSV0_CRC_ERR = 0x00000001  
# Length Check Error
EMAC_TSV0_LEN_CHKERR = 0x00000002  
# Length Out of Range
EMAC_TSV0_LEN_OUTRNG = 0x00000004  
# Tramsmission Completed
EMAC_TSV0_DONE = 0x00000008  
# Multicast Destination
EMAC_TSV0_MCAST = 0x00000010  
# Broadcast Destination
EMAC_TSV0_BCAST = 0x00000020  
# Packet Deferred
EMAC_TSV0_PKT_DEFER = 0x00000040  
# Excessive Packet Deferral
EMAC_TSV0_EXC_DEFER = 0x00000080  
# Excessive Collision
EMAC_TSV0_EXC_COLL = 0x00000100  
# Late Collision Occured
EMAC_TSV0_LATE_COLL = 0x00000200  
# Giant Frame
EMAC_TSV0_GIANT = 0x00000400  
# Buffer Underrun
EMAC_TSV0_UNDERRUN = 0x00000800  
# Total Bytes Transferred
EMAC_TSV0_BYTES = 0x0FFFF000  
# Control Frame
EMAC_TSV0_CTRL_FRAME = 0x10000000  
# Pause Frame 
EMAC_TSV0_PAUSE = 0x20000000  
# Backpressure Method Applied
EMAC_TSV0_BACK_PRESS = 0x40000000  
# VLAN Frame
EMAC_TSV0_VLAN = 0x80000000

# Macro defines for Transmit Status Vector 1 Register 
# Transmit Byte Count
EMAC_TSV1_BYTE_CNT = 0x0000FFFF  
# Transmit Collision Count
EMAC_TSV1_COLL_CNT = 0x000F0000

# Macro defines for Receive Status Vector Register
# Receive Byte Count
EMAC_RSV_BYTE_CNT = 0x0000FFFF  
# Packet Previously Ignored
EMAC_RSV_PKT_IGNORED = 0x00010000  
# RXDV Event Previously Seen
EMAC_RSV_RXDV_SEEN = 0x00020000  
# Carrier Event Previously Seen
EMAC_RSV_CARR_SEEN = 0x00040000  
# Receive Code Violation
EMAC_RSV_REC_CODEV = 0x00080000  
# CRC Error
EMAC_RSV_CRC_ERR = 0x00100000  
# Length Check Error
EMAC_RSV_LEN_CHKERR = 0x00200000  
# Length Out of Range
EMAC_RSV_LEN_OUTRNG = 0x00400000  
# Frame Received OK
EMAC_RSV_REC_OK = 0x00800000  
# Multicast Frame
EMAC_RSV_MCAST = 0x01000000  
# Broadcast Frame
EMAC_RSV_BCAST = 0x02000000  
# Dribble Nibble
EMAC_RSV_DRIB_NIBB = 0x04000000  
# Control Frame
EMAC_RSV_CTRL_FRAME = 0x08000000  
# Pause Frame
EMAC_RSV_PAUSE = 0x10000000  
# Unsupported Opcode
EMAC_RSV_UNSUPP_OPC = 0x20000000  
# VLAN Frame
EMAC_RSV_VLAN = 0x40000000

# Macro defines for Flow Control Counter Register
def EMAC_FCC_MIRR_CNT(n):
  '''Mirror Counter.
  '''
  return (n&0xFFFF)
      
def EMAC_FCC_PAUSE_TIM(n):
  '''Pause Timer.
  '''
  return ((n&0xFFFF)<<16)

# Macro defines for Flow Control Status Register    
def EMAC_FCS_MIRR_CNT(n):
  '''Mirror Counter Current.
  '''
  return (n&0xFFFF)

# Macro defines for Receive Filter Control Register      
# Accept Unicast Frames Enable
EMAC_RFC_UCAST_EN = 0x00000001  
# Accept Broadcast Frames Enable
EMAC_RFC_BCAST_EN = 0x00000002  
# Accept Multicast Frames Enable
EMAC_RFC_MCAST_EN = 0x00000004  
# Accept Unicast Hash Filter Frames
EMAC_RFC_UCAST_HASH_EN = 0x00000008  
# Accept Multicast Hash Filter Frames
EMAC_RFC_MCAST_HASH_EN = 0x00000010  
# Accept Perfect Match Enable
EMAC_RFC_PERFECT_EN = 0x00000020  
# Magic Packet Filter WoL Enable
EMAC_RFC_MAGP_WOL_EN = 0x00001000  
# Perfect Filter WoL Enable
EMAC_RFC_PFILT_WOL_EN = 0x00002000  

# Macro defines for Receive Filter WoL Status/Clear Registers
# Unicast Frame caused WoL
EMAC_WOL_UCAST = 0x00000001  
# Broadcast Frame caused WoL
EMAC_WOL_BCAST = 0x00000002  
# Multicast Frame caused WoL
EMAC_WOL_MCAST = 0x00000004  
# Unicast Hash Filter Frame WoL
EMAC_WOL_UCAST_HASH = 0x00000008  
# Multicast Hash Filter Frame WoL
EMAC_WOL_MCAST_HASH = 0x00000010  
# Perfect Filter WoL
EMAC_WOL_PERFECT = 0x00000020  
# RX Filter caused WoL
EMAC_WOL_RX_FILTER = 0x00000080  
# Magic Packet Filter caused WoL
EMAC_WOL_MAG_PACKET = 0x00000100  
# Receive Filter WoL Status/Clear bitmasl value
EMAC_WOL_BITMASK = 0x01BF

# Macro defines for Interrupt Status/Enable/Clear/Set Registers
# Overrun Error in RX Queue
EMAC_INT_RX_OVERRUN = 0x00000001  
# Receive Error
EMAC_INT_RX_ERR = 0x00000002  
# RX Finished Process Descriptors
EMAC_INT_RX_FIN = 0x00000004  
# Receive Done
EMAC_INT_RX_DONE = 0x00000008  
# Transmit Underrun
EMAC_INT_TX_UNDERRUN = 0x00000010  
# Transmit Error
EMAC_INT_TX_ERR = 0x00000020  
# TX Finished Process Descriptors
EMAC_INT_TX_FIN = 0x00000040  
# Transmit Done
EMAC_INT_TX_DONE = 0x00000080  
# Software Triggered Interrupt
EMAC_INT_SOFT_INT = 0x00001000  
# Wakeup Event Interrupt
EMAC_INT_WAKEUP = 0x00002000

# Macro defines for Power Down Register
# Power Down MAC 
EMAC_PD_POWER_DOWN = 0x80000000 

# Macro defines for RX Descriptor Control Word
def EMAC_RCTRL_SIZE(n):
  '''Buffer size field.
  '''
  return (n&0x7FF)
    
# Generate RxDone Interrupt
EMAC_RCTRL_INT = 0x80000000

# Macro defines for RX Status Hash CRC Word  
# Hash CRC for Source Address
EMAC_RHASH_SA = 0x000001FF    
# Hash CRC for Destination Address
EMAC_RHASH_DA = 0x001FF000

# Macro defines for RX Status Information Word
# Data size in bytes
EMAC_RINFO_SIZE = 0x000007FF  
# Control Frame
EMAC_RINFO_CTRL_FRAME = 0x00040000  
# VLAN Frame
EMAC_RINFO_VLAN = 0x00080000  
# RX Filter Failed
EMAC_RINFO_FAIL_FILT = 0x00100000  
# Multicast Frame
EMAC_RINFO_MCAST = 0x00200000  
# Broadcast Frame 
EMAC_RINFO_BCAST = 0x00400000  
# CRC Error in Frame
EMAC_RINFO_CRC_ERR = 0x00800000  
# Symbol Error from PHY
EMAC_RINFO_SYM_ERR = 0x01000000  
# Length Error
EMAC_RINFO_LEN_ERR = 0x02000000  
# Range Error (exceeded max. size)
EMAC_RINFO_RANGE_ERR = 0x04000000  
# Alignment Error
EMAC_RINFO_ALIGN_ERR = 0x08000000  
# Receive overrun
EMAC_RINFO_OVERRUN = 0x10000000  
# No new Descriptor available
EMAC_RINFO_NO_DESCR = 0x20000000  
# Last Fragment in Frame 
EMAC_RINFO_LAST_FLAG = 0x40000000  
# Error Occured (OR of all errors)
EMAC_RINFO_ERR = 0x80000000  
EMAC_RINFO_ERR_MASK =  (EMAC_RINFO_FAIL_FILT | EMAC_RINFO_CRC_ERR   | \
                        EMAC_RINFO_SYM_ERR | EMAC_RINFO_LEN_ERR | \
                        EMAC_RINFO_ALIGN_ERR | EMAC_RINFO_OVERRUN)

# Macro defines for TX Descriptor Control Word
# Size of data buffer in bytes
EMAC_TCTRL_SIZE = 0x000007FF  
# Override Default MAC Registers
EMAC_TCTRL_OVERRIDE = 0x04000000  
# Enable Huge Frame
EMAC_TCTRL_HUGE = 0x08000000  
# Pad short Frames to 64 bytes
EMAC_TCTRL_PAD = 0x10000000  
# Append a hardware CRC to Frame
EMAC_TCTRL_CRC = 0x20000000  
# Last Descriptor for TX Frame
EMAC_TCTRL_LAST = 0x40000000  
# Generate TxDone Interrupt
EMAC_TCTRL_INT = 0x80000000 

#  Macro defines for TX Status Information Word
# Collision Count
EMAC_TINFO_COL_CNT = 0x01E00000  
# Packet Deferred (not an error)
EMAC_TINFO_DEFER = 0x02000000  
# Excessive Deferral
EMAC_TINFO_EXCESS_DEF = 0x04000000  
# Excessive Collision
EMAC_TINFO_EXCESS_COL = 0x08000000  
# Late Collision Occured
EMAC_TINFO_LATE_COL = 0x10000000  
# Transmit Underrun
EMAC_TINFO_UNDERRUN = 0x20000000  
# No new Descriptor available
EMAC_TINFO_NO_DESCR = 0x40000000  
# Error Occured (OR of all errors)
EMAC_TINFO_ERR = 0x80000000

# DP83848C PHY definition
# PHY device reset time out definition
EMAC_PHY_RESP_TOUT = 0x100000
# ENET Device Revision ID
# Rev. ID for first rev
EMAC_OLD_EMAC_MODULE_ID = 0x39022000  

# Macro defines for DP83848C PHY Registers      
# Basic Mode Control Register
EMAC_PHY_REG_BMCR = 0x00
# Basic Mode Status Register
EMAC_PHY_REG_BMSR = 0x01        
# PHY Identifier 1
EMAC_PHY_REG_IDR1 = 0x02        
# PHY Identifier 2
EMAC_PHY_REG_IDR2 = 0x03        
# Auto-Negotiation Advertisement
EMAC_PHY_REG_ANAR = 0x04        
# Auto-Neg. Link Partner Abitily
EMAC_PHY_REG_ANLPAR = 0x05        
# Auto-Neg. Expansion Register
EMAC_PHY_REG_ANER = 0x06        
# Auto-Neg. Next Page TX
EMAC_PHY_REG_ANNPTR = 0x07        
# Link Partner Next Page Ability
EMAC_PHY_REG_LPNPA = 0x08

# Macro defines for PHY Extended Registers
# Status Register
EMAC_PHY_REG_STS = 0x10        
# MII Interrupt Control Register
EMAC_PHY_REG_MICR = 0x11        
# MII Interrupt Status Register
EMAC_PHY_REG_MISR = 0x12        
# False Carrier Sense Counter
EMAC_PHY_REG_FCSCR = 0x14        
# Receive Error Counter 
EMAC_PHY_REG_RECR = 0x15        
# PCS Sublayer Config. and Status 
EMAC_PHY_REG_PCSR = 0x16        
# RMII and Bypass Register
EMAC_PHY_REG_RBR = 0x17        
# LED Direct Control Register 
EMAC_PHY_REG_LEDCR = 0x18        
# PHY Control Register
EMAC_PHY_REG_PHYCR = 0x19        
# 10Base-T Status/Control Register
EMAC_PHY_REG_10BTSCR = 0x1A        
# CD Test Control and BIST Extens.
EMAC_PHY_REG_CDCTRL1 = 0x1B        
# Energy Detect Control Register
EMAC_PHY_REG_EDCR = 0x1D

# Macro defines for PHY Basic Mode Control Register     
# Reset bit
EMAC_PHY_BMCR_RESET = (1<<15)    
# Loop back
EMAC_PHY_BMCR_LOOPBACK = (1<<14)    
# Speed selection
EMAC_PHY_BMCR_SPEED_SEL = (1<<13)    
# Auto Negotiation
EMAC_PHY_BMCR_AN = (1<<12)    
# Power down mode
EMAC_PHY_BMCR_POWERDOWN = (1<<11)    
# Isolate
EMAC_PHY_BMCR_ISOLATE = (1<<10)    
# Restart auto negotiation
EMAC_PHY_BMCR_RE_AN = (1<<9)    
# Duplex mode
EMAC_PHY_BMCR_DUPLEX = (1<<8)    

# Macro defines for PHY Basic Mode Status Status Register
# 100 base T4
EMAC_PHY_BMSR_100BE_T4 = (1<<15)    
# 100 base full duplex
EMAC_PHY_BMSR_100TX_FULL = (1<<14)    
# 100 base half duplex
EMAC_PHY_BMSR_100TX_HALF = (1<<13)    
# 10 base T full duplex
EMAC_PHY_BMSR_10BE_FULL = (1<<12)    
# 10 base T half duplex
EMAC_PHY_BMSR_10BE_HALF = (1<<11)    
# MF Preamable Supress
EMAC_PHY_BMSR_NOPREAM = (1<<6)    
# Auto negotiation complete
EMAC_PHY_BMSR_AUTO_DONE = (1<<5)    
# Remote fault
EMAC_PHY_BMSR_REMOTE_FAULT = (1<<4)    
# Auto Negotiation ability
EMAC_PHY_BMSR_NO_AUTO = (1<<3)    
# Link status
EMAC_PHY_BMSR_LINK_ESTABLISHED = (1<<2)

# Macro defines for PHY Status Register 
# Remote Fault
EMAC_PHY_SR_REMOTE_FAULT = (1<<6)    
# Jabber detect
EMAC_PHY_SR_JABBER = (1<<5)    
# Auto Negotiation complete
EMAC_PHY_SR_AUTO_DONE = (1<<4)    
# Loop back status
EMAC_PHY_SR_LOOPBACK = (1<<3)    
# Duplex status
EMAC_PHY_SR_DUP = (1<<2)    
# Speed status
EMAC_PHY_SR_SPEED = (1<<1)    
# Link Status
EMAC_PHY_SR_LINK = (1<<0)    
# Full Duplex 100Mbit
EMAC_PHY_FULLD_100M = 0x2100      
# Half Duplex 100Mbit
EMAC_PHY_HALFD_100M = 0x2000      
# Full Duplex 10Mbit
EMAC_PHY_FULLD_10M = 0x0100      
# Half Duplex 10MBit
EMAC_PHY_HALFD_10M = 0x0000      
# Select Auto Negotiation
EMAC_PHY_AUTO_NEG = 0x3000      
# Default PHY device address
EMAC_DEF_ADR = 0x0100      
# PHY Identifier
EMAC_DP83848C_ID = 0x20005C90  

EMAC_PHY_SR_100_SPEED = ((1<<14)|(1<<13))
EMAC_PHY_SR_FULL_DUP = ((1<<14)|(1<<12))
# Link status
EMAC_PHY_BMSR_LINK_STATUS = (1<<2)

class RX_Stat(cstruct):
  '''RX Status structure type definition.
  
  Info: Receive Information Status
  HashCRC: Receive Hash CRC Status
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class EMAC_CFG_Type(cstruct):
  '''EMAC configuration structure definition.
  
  Mode: Supported EMAC PHY device speed, should be one of the following:
        EMAC_MODE_AUTO
        EMAC_MODE_10M_FULL
        EMAC_MODE_10M_HALF
        EMAC_MODE_100M_FULL
        EMAC_MODE_100M_HALF
  pbEMAC_Addr:  Pointer to EMAC Station address that contains 6-bytes
                of MAC address, it must be sorted in order (bEMAC_Addr[0]..[5])
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
                 
  '''
  pass

class EMAC_PACKETBUF_Type(cstruct):
  '''TX Data Buffer structure definition.
  
  ulDataLen: Data length
  pbDataBuf: A word-align data pointer to data buffer
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class RX_Desc(cstruct):
  '''RX Descriptor structure type definition.
  
  Packet: Receive Packet Descriptor
  Ctrl: Receive Control Descriptor
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class TX_Desc(cstruct):
  '''TX Descriptor structure type definition.
  
  Packet: Transmit Packet Descriptor
  Ctrl: Transmit Control Descriptor
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class TX_Stat(cstruct):
  '''TX Status structure type definition.
  
  Info: Transmit Information Status
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

def EMAC_GetWoLStatus(ulWoLMode):
  '''Get status of Wake On LAN Filter for each specified type in EMAC 
  peripheral, clear this status if it is set.
  
  ulWoLMode:  WoL Filter mode, should be:
              EMAC_WOL_UCAST: unicast frames caused WoL
              EMAC_WOL_UCAST: broadcast frame caused WoL
              EMAC_WOL_MCAST: multicast frame caused WoL
              EMAC_WOL_UCAST_HASH:  unicast frame that passes the imperfect hash
                                    filter caused WoL
              EMAC_WOL_MCAST_HASH:  multicast frame that passes the imperfect 
                                    hash filter caused WoL
              EMAC_WOL_PERFECT:perfect address matching filter caused WoL
              EMAC_WOL_RX_FILTER: the receive filter caused WoL
              EMAC_WOL_MAG_PACKET: the magic packet filter caused WoL
  return: SET/RESET
  
  '''
  return robocaller("EMAC_GetWoLStatus", "FlagStatus", ulWoLMode)

def EMAC_Init(EMAC_ConfigStruct):
  '''Initializes the EMAC peripheral according to the specified parameters in 
  the EMAC_ConfigStruct.
  
  EMAC_ConfigStruct:  Pointer to a EMAC_CFG_Type structure that contains the 
                      configuration information for the specified EMAC
                      peripheral.
                      
  '''
  return robocaller("EMAC_Init", "Status", EMAC_ConfigStruct)

def EMAC_CheckReceiveDataStatus(ulRxStatType):
  '''Get current status value of receive data (due to RxConsumeIndex).
  
  ulRxStatType: Received Status type, should be one of following:
                EMAC_RINFO_CTRL_FRAME: Control Frame
                EMAC_RINFO_VLAN: VLAN Frame
                EMAC_RINFO_FAIL_FILT: RX Filter Failed
                EMAC_RINFO_MCAST: Multicast Frame
                EMAC_RINFO_BCAST: Broadcast Frame
                EMAC_RINFO_CRC_ERR: CRC Error in Frame
                EMAC_RINFO_SYM_ERR: Symbol Error from PHY
                EMAC_RINFO_LEN_ERR: Length Error
                EMAC_RINFO_RANGE_ERR: Range error(exceeded max size)
                EMAC_RINFO_ALIGN_ERR: Alignment error
                EMAC_RINFO_OVERRUN: Receive overrun
                EMAC_RINFO_NO_DESCR: No new Descriptor available
                EMAC_RINFO_LAST_FLAG: last Fragment in Frame
                EMAC_RINFO_ERR: Error Occurred (OR of all error)
  return: Current value of receive data (due to RxConsumeIndex)
                
  '''
  return robocaller("EMAC_CheckReceiveDataStatus", "FlagStatus", ulRxStatType)

def EMAC_CheckTransmitIndex():
  '''Check whether if the current TxProduceIndex is not equal to the current
  RxProduceIndex - 1.
  
  return: TRUE if they're not equal, otherwise return FALSE
  
  '''
  return robocaller("EMAC_CheckTransmitIndex", "Bool")

def EMAC_IntCmd(ulIntType, NewState):
  '''Enable/Disable interrupt for each type in EMAC.
  
  ulIntType:  Interrupt Type, should be:
              EMAC_INT_RX_OVERRUN: Receive Overrun
              EMAC_INT_RX_ERR: Receive Error
              EMAC_INT_RX_FIN: Receive Descriptor Finish
              EMAC_INT_RX_DONE: Receive Done
              EMAC_INT_TX_UNDERRUN: Transmit Under-run
              EMAC_INT_TX_ERR: Transmit Error
              EMAC_INT_TX_FIN: Transmit descriptor finish
              EMAC_INT_TX_DONE: Transmit Done
              EMAC_INT_SOFT_INT: Software interrupt
              EMAC_INT_WAKEUP: Wakeup interrupt
  NewState: New State of this function, should be:
            ENABLE
            DISABLE
            
  '''
  return robocaller("EMAC_IntCmd", "void", ulIntType, NewState)

def EMAC_SetPHYMode(ulPHYMode):
  '''Set specified PHY mode in EMAC peripheral.
  
  ulPHYMode:  Specified PHY mode, should be:
              EMAC_MODE_AUTO
              EMAC_MODE_10M_FULL
              EMAC_MODE_10M_HALF
              EMAC_MODE_100M_FULL
              EMAC_MODE_100M_HALF
  return: 0 if no error, otherwise -1
  '''
  return robocaller("EMAC_SetPHYMode", "int32_t", ulPHYMode)

def EMAC_IntGetStatus(ulIntType):
  ''' Check whether if specified interrupt flag is set or not for each interrupt
  type in EMAC and clear interrupt pending if it is set.
  
  ulIntType:  Interrupt Type, should be:
              EMAC_INT_RX_OVERRUN: Receive Overrun
              EMAC_INT_RX_ERR: Receive Error
              EMAC_INT_RX_FIN: Receive Descriptor Finish
              EMAC_INT_RX_DONE: Receive Done
              EMAC_INT_TX_UNDERRUN: Transmit Under-run
              EMAC_INT_TX_ERR: Transmit Error
              EMAC_INT_TX_FIN: Transmit descriptor finish
              EMAC_INT_TX_DONE: Transmit Done
              EMAC_INT_SOFT_INT: Software interrupt
              EMAC_INT_WAKEUP: Wakeup interrupt
  return: New state of specified interrupt (SET or RESET)
              
  '''
  return robocaller("EMAC_IntGetStatus", "IntStatus", ulIntType)

def EMAC_WritePacketBuffer(pDataStruct):
  '''Write data to Tx packet data buffer at current index due to TxProduceIndex.
  
  pDataStruct:  Pointer to a EMAC_PACKETBUF_Type structure data that contain 
                specified information about Packet data buffer.
                
  '''
  return robocaller("EMAC_WritePacketBuffer", "void", pDataStruct)

def EMAC_SetHashFilter(dstMAC_addr, NewState):
  '''Enable/Disable hash filter functionality for specified destination MAC 
  address in EMAC module.
  
  dstMAC_addr:  Pointer to the first MAC destination address, should be 6-bytes
                length, in order LSB to the MSB
  NewState: New State of this command, should be:
            ENABLE
            DISABLE
  '''
  return robocaller("EMAC_SetHashFilter", "void", dstMAC_addr, NewState)

def EMAC_CheckReceiveIndex():
  '''Check whether the current RxConsumeIndex is not equal to the current
  RxProduceIndex.
  
  return: TRUE if they're not equal, otherwise return FALSE
  '''
  return robocaller("EMAC_CheckReceiveIndex", "Bool")

def EMAC_UpdatePHYStatus():
  '''Auto-Configures value for the EMAC configuration register to match with 
  current PHY mode.
  
  return: 0 if no error, otherwise -1
  '''
  return robocaller("EMAC_UpdatePHYStatus", "int32_t")

def EMAC_CheckPHYStatus(ulPHYState):
  '''Check specified PHY status in EMAC peripheral.
  
  ulPHYState: Specified PHY Status Type, should be:
              EMAC_PHY_STAT_LINK: Link Status
              EMAC_PHY_STAT_SPEED: Speed Status
              EMAC_PHY_STAT_DUP: Duplex Status
  return: Status of specified PHY status (0 or 1).
          -1 if error.
  '''
  return robocaller("EMAC_CheckPHYStatus", "int32_t", ulPHYState)

def EMAC_UpdateTxProduceIndex():
  '''Increase the TxProduceIndex (after writting to the Transmit buffer to
  enable the Transmit buffer) and wrap-around the index if it reaches the
  maximum Transmit Number.
  '''
  return robocaller("EMAC_UpdateTxProduceIndex", "void")

def EMAC_DeInit():
  '''De-initializes the EMAC peripheral registers to their default reset values.
  '''
  return robocaller("EMAC_DeInit", "void")

def EMAC_GetReceiveDataSize():
  '''Get size of current Received data in received buffer (due to 
  RxConsumeIndex).
  
  return: Size of received data
  
  '''
  return robocaller("EMAC_GetReceiveDataSize", "uint32_t", )

def EMAC_UpdateRxConsumeIndex():
  '''Increase the RxConsumeIndex (after reading the Receive buffer to release 
  the Receive buffer) and wrap-around the index if it reaches the maximum
  Receive Number.
  '''
  return robocaller("EMAC_UpdateRxConsumeIndex", "void", )

def EMAC_ReadPacketBuffer(pDataStruct):
  '''Read data from Rx packet data buffer at current index due to 
  RxConsumeIndex.
  
  pDataStruct:  Pointer to a EMAC_PACKETBUF_Type structure data that contain 
                specified information about Packet data buffer.
                
  '''
  return robocaller("EMAC_ReadPacketBuffer", "void", pDataStruct)

def EMAC_SetFilterMode(ulFilterMode, NewState):
  '''Enable/Disable Filter mode for each specified type EMAC peripheral.
  
  ulFilterMode: Filter mode, should be:
                EMAC_RFC_UCAST_EN:  all frames of unicast types will be accepted
                EMAC_RFC_BCAST_EN:  broadcast frame will be accepted
                EMAC_RFC_MCAST_EN:  all frames of multicast types will be
                                    accepted
                EMAC_RFC_UCAST_HASH_EN: The imperfect hash filter will be
                                        applied to unicast addresses
                EMAC_RFC_MCAST_HASH_EN: The imperfect hash filter will be
                                        applied to multicast addresses
                EMAC_RFC_PERFECT_EN:  the destination address will be compared
                                      with the 6 byte station address programmed
                                      in the station address by the filter
                EMAC_RFC_MAGP_WOL_EN: the result of the magic packet filter will 
                                      generate a WoL interrupt when there is a
                                      match
                EMAC_RFC_PFILT_WOL_EN:  the result of the perfect address 
                                        matching filter and the imperfect hash
                                        filter will generate a WoL interrupt 
                                        when there is a match
  NewState: New State of this command, should be:
            ENABLE
            DISABLE
            
  '''
  return robocaller("EMAC_SetFilterMode", "void", ulFilterMode, NewState)

