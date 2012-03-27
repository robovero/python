"""
"""

from internals import robocaller, cstruct

__author__ =      "Danny Chan"
__credits__ =     ["Danny Chan", "NXP MCU SW Application Team"]
__maintainer__ =  "Danny Chan"
__email__ =       "danny@gumstix.com"
__copyright__ =   "Copyright 2012, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

class tS_ResonatorStateCoeff(cstruct):
  '''  
  '''
  pass
  
def vF_dspl_resonator(psi_Output, pS_ResonatorStateCoeff, i_NSamples):
  '''
  '''
  return robocaller("vF_dspl_resonator", "void", psi_Output, pS_ResonatorStateCoeff, i_NSamples)

class tS_blockfir32_Coeff(cstruct):
  '''  
  '''
  pass
  
def vF_dspl_blockfir32(pi_y, pi_x, pS_Coeff, i_nsamples):
  '''
  '''
  return robocaller("vF_dspl_blockfir32", "void", pi_y, pi_x, pS_Coeff, i_nsamples)

class tS_biquad32_StateCoeff(cstruct):
  ''' Biquad filter state coefficient class
  
  short int pi_Coeff: '2.14' format fractional values
  pi_Coeff0: a1
  pi_Coeff1: a2
  pi_Coeff2: b0
  pi_Coeff3: b1
  pi_Coeff4: b2
  short int pi_State[2]: '2.14' format fractional values that can be
  zero initialized for the first call but are updated by the routine to 
  allow repeated calling of the filter with a stream of data
  ptr: LPC1769 memory address where structure is stored. Use this in place of
      the C reference operator (&).

  '''
  pass

def vF_dspl_biquad32(pi_Output, pi_Input, pS_StateCoeff, i_NSamples):
  '''The biquad is a commonly used 2nd order filter section that can be 
  cascaded to build any order of filter
  
  pi_Output, pi_Input: pointers to integer arrays in '4.28' format fractional values
  pS_StateCoeff: pointer to tS_biquad32_StateCoeff
  i_NSamples: integer number of samples
  
  '''
  return robocaller("vF_dspl_biquad32", "void", pi_Output, pi_Input, pS_StateCoeff, i_NSamples)
  
class tS_pid_Coeff(cstruct):
  '''
  
  short int Kp
  short int Ki
  short int Kd
  short int IntegratedError
  short int LastError
  ptr: LPC1769 memory address where structure is stored. Use this in place of
    the C reference operator (&).

  '''
  pass

def vF_dspl_pid(si_Error, pS_Coeff):
  '''PID Controller
  
  si_Error: short int
  pS_Coeff: pointer to tS_pid_Coeff
  return:
  
  '''
  return robocaller("vF_dspl_pid", "int", si_Error, pS_Coeff)

def iF_dspl_dotproduct32(pi_x, pi_y, i_VectorLen):
  '''Performs pi_x dot pi_y
  
  pi_x, pi_y: pointers to integer arrays
  i_VectorLen: length of vectors
  return: integer dot product of pi_x and pi_y
  
  '''
  return robocaller("iF_dspl_dotproduct32", "int", pi_x, pi_y, i_VectorLen)

def iF_RandomNumber(i_Seed):
  '''Returns a random number given an integer i_Seed
  
  i_Seed: integer input
  return: integer
  
  '''
  return robocaller("iF_RandomNumber", "int", i_Seed)

def iF_dspl_vectsumofsquares32(pi_x, i_VectorLen):
  ''' Calculates the sum of the squares of 32 bit elements in pi_x
  
  pi_x: pointer to 32 bit integer array
  i_VectorLen: length of vector
  return: integer
  
  '''
  return robocaller("iF_dspl_vectsumofsquares32", "int", pi_x, i_VectorLen)

def iF_dspl_vectsumofsquares16(psi_x, i_VectorLen):
  ''' Calculates the sum of the squares of 32 bit signed elements in pi_x
  
  psi_x: pointer to signed integer array
  i_VectorLen: length of vector
  return: integer
  
  '''
  return robocaller("iF_dspl_vectsumofsquares16", "int", psi_x, i_VectorLen)

def vF_dspl_vectmulconst32(pi_y, pi_x, i_c, i_VectorLen):
  '''Multiplies each element in pi_x by i_c and returns in pi_y
  
  pi_x, pi_y: pointers to 32 bit integer arrays
  i_c: integer
  i_VectorLen: length of vector
  
  '''
  return robocaller("vF_dspl_vectmulconst32", "void", pi_y, pi_x, i_c, i_VectorLen)

def vF_dspl_vectmulconst16(psi_y, psi_x, si_c, i_VectorLen):
  '''Multiplies each element in psi_x by si_c and returns in psi_y
  
  psi_x, psi_y: pointers to signed integer arrays
  si_c: integer
  i_VectorLen: length of vector
  
  TODO: deref on psi_y doesn't work
  '''
  return robocaller("vF_dspl_vectmulconst16", "void", psi_y, psi_x, si_c, i_VectorLen)

def vF_dspl_vectmulelement32(pi_z, pi_x, pi_y, i_VectorLen):
  '''(Doesn't work?) Element by element multiplication of unsigned vectors
  
  pi_x, pi_y: pointers to integer arrays
  i_VectorLen: length of vector
  pi_z: result of element by element multiplication
  
  '''
  return robocaller("vF_dspl_vectmulelement32", "void", pi_z, pi_x, pi_y, i_VectorLen)

def vF_dspl_vectmulelement16(psi_z, psi_x, psi_y, i_VectorLen):
  '''(Doesn't work?) Element by element multiplication of unsigned vectors
  
  pi_x, pi_y: pointers to integer arrays
  i_VectorLen: length of vector
  pi_z: result of element by element multiplication
  
  '''
  return robocaller("vF_dspl_vectmulelement16", "void", psi_z, psi_x, psi_y, i_VectorLen)

def vF_dspl_vectaddconst32(pi_y, pi_x, i_c, i_VectorLen):
  '''Adds a constant integer i_c to each element in vector pi_x and outputs in pi_y
  
  pi_x, pi_y: pointer to 32bit integer arrays
  i_c: integer
  i_VectorLen: length of vector
  
  '''
  return robocaller("vF_dspl_vectaddconst32", "void", pi_y, pi_x, i_c, i_VectorLen)
  
def vF_dspl_vectaddconst16(psi_y, psi_x, si_c, i_VectorLen):
  '''Adds a constant integer i_c to each element in vector pi_x and outputs in pi_y
  
  psi_x, psi_y: pointer to signed integer arrays
  si_c: signed integer
  i_VectorLen: length of vector
  
  '''
  return robocaller("vF_dspl_vectaddconst16", "void", psi_y, psi_x, si_c, i_VectorLen)

def vF_dspl_vectsub32(pi_z, pi_x, pi_y, i_VectorLen):
  '''Subtracts two unsigned 32 bit integer vectors and returns in pi_z
  
  pi_z: pi_x - pi_y
  pi_x, pi_y, pi_z: pointers to 32bit integer arrays
  i_VectorLen: length of vector
  
  '''
  return robocaller("vF_dspl_vectsub32", "void", pi_z, pi_x, pi_y, i_VectorLen)

def vF_dspl_vectsub16(psi_z, psi_x, psi_y, i_VectorLen):
  '''Subtracts two unsigned 32 bit integer vectors and returns in psi_z
  
  psi_z: psi_x - psi_y
  psi_x, psi_y, psi_z: pointers to signed integer arrays
  i_VectorLen: length of vector
  
  
  TODO: Find out why using deref on psi_z doesn't work
  '''
  return robocaller("vF_dspl_vectsub16", "void", psi_z, psi_x, psi_y, i_VectorLen)

def vF_dspl_vectadd32(pi_z, pi_x, pi_y, i_VectorLen):
  '''Adds two unsigned 32 bit integer vectors and returns in pi_z
  
  pi_z: pi_x + pi_y
  pi_x, pi_y, pi_z: pointers to 32bit integer arrays
  i_VectorLen: length of vector
  
  '''
  return robocaller("vF_dspl_vectadd32", "void", pi_z, pi_x, pi_y, i_VectorLen)

def vF_dspl_vectadd16(psi_z, psi_x, psi_y, i_VectorLen):
  '''Adds two unsigned 16 bit integer vectors
  
  psi_z: psi_x + psi_y
  psi_x, psi_y, psi_z: pointers to signed integer arrays
  i_VectorLen: length of vector
  
  NOTE: this function is supposed to be signed, but problems with Python
  cause it to be unsigned
  '''
  return robocaller("vF_dspl_vectadd16", "void", psi_z, psi_x, psi_y, i_VectorLen)
  
def vF_dspl_fftR4b16N64(psi_Y, psi_x):
  ''' Perform Fast Fourier Transform with 64 data points
  
  psi_x: ptr to short int array. Used for input
  psi_Y: ptr to short int array. Used for output
  
  '''
  return robocaller("vF_dspl_fftR4b16N64", "void", psi_Y, psi_x)

def vF_dspl_fftR4b16N256(psi_Y, psi_x):
  '''Perform Fast Fourier Transform with 256 data points
  
  psi_x: ptr to short int array. Used for input
  psi_Y: ptr to short int array. Used for output
  
  '''
  return robocaller("vF_dspl_fftR4b16N256", "void", psi_Y, psi_x)

def vF_dspl_fftR4b16N1024(psi_Y, psi_x):
  '''Perform Fast Fourier Transform with 1024 data points
  
  psi_x: ptr to short int array. Used for input
  psi_Y: ptr to short int array. Used for output
  
  '''
  return robocaller("vF_dspl_fftR4b16N1024", "void", psi_Y, psi_x)

def vF_dspl_fftR4b16N4096(psi_Y, psi_x):
  '''Perform Fast Fourier Transform with 4096 data points
  
  psi_x: ptr to short int array. Used for input
  psi_Y: ptr to short int array. Used for output
  
  '''
  return robocaller("vF_dspl_fftR4b16N4096", "void", psi_Y, psi_x)
