"""Examples demonstrating use of DSP functions.
"""

from robovero.cr_dsplib import *
from robovero.extras import Array
from math import cos,pi
from time import sleep

__author__ =			"Danny Chan"
__email__ =				"danny@gumstix.com"
__copyright__ = 	"Copyright 2012, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

"""# Matrix operations

x=Array(3,4,[2,5,12])
y=Array(3,4,[1,10,5])
z=Array(3,4,0)
i_s=12
s=7

print 'x =', x[0], x[1], x[2]
print 'y =', y[0], y[1], y[2]

vF_dspl_vectadd32(z.ptr, x.ptr, y.ptr, 3)
print 'vF_dspl_vectadd32:'
print 'x + y =', z[0], z[1], z[2]

vF_dspl_vectsub32(z.ptr, x.ptr, y.ptr, 3)
print 'vF_dspl_vectsub32:'
print 'x - y =', z[0], z[1], z[2]

vF_dspl_vectaddconst32(z.ptr, x.ptr, i_s, 3)
print 'vF_dspl_vectaddconst32:'
print 'x +',i_s,'=', z[0], z[1], z[2]

vF_dspl_vectmulconst32(z.ptr, x.ptr, i_s, 3)
print 'vF_dspl_vectmulconst32:'
print 'x *',i_s,'=', z[0], z[1], z[2]

vF_dspl_vectmulelement32(z.ptr, x.ptr, y.ptr, 3)
print 'vF_dspl_vectmulelement32:'
print 'x * y =', z[0], z[1], z[2]

print 'iF_dspl_vectsumofsquares32:'
print '|x|^2 =', iF_dspl_vectsumofsquares32(x.ptr,3)

print 'iF_dspl_dotproduct32:'
print 'x dot y =', iF_dspl_dotproduct32(x.ptr,y.ptr,3)

print 'iF_RandomNumber:'
for i in range(10):
  s = iF_RandomNumber(s)
  print s
"""

"""# Biquad filter
print 'Biquad filter'
TESTSIZE=8
pi_Input=Array(TESTSIZE,4,0)
pi_Output=Array(TESTSIZE,4,0)

S_StateCoeff=tS_biquad32_StateCoeff()

S_StateCoeff.pi_Coeff0= 1.91119706742607360000 * (2**14) #a1
S_StateCoeff.pi_Coeff1= -0.91497583480143418000 * (2**14) #a2
S_StateCoeff.pi_Coeff2= 0.00094547653094439164 * (2**14) #b0
S_StateCoeff.pi_Coeff3= 0.00189095306188878330 * (2**14) #b1
S_StateCoeff.pi_Coeff4= 0.00094547653094439164 * (2**14) #b2
S_StateCoeff.pi_State0=0
S_StateCoeff.pi_State1=0

# Step input
for j in range(TESTSIZE):
  pi_Input[j] = 1*(2**28)

vF_dspl_biquad32(pi_Output.ptr, pi_Input.ptr, S_StateCoeff.ptr, TESTSIZE)

for j in range(TESTSIZE):
  print j, pi_Output[j]/(2.**28)"""

"""# Normalized Radix-4 Fast Fourier transform, Fixed-point number representation
print '\nfft'
NPOINTS=1024
psi_Input=Array(NPOINTS*2,2)  #Real and imaginary parts, needing twice the buffer
psi_Output=Array(NPOINTS*2,2)

print 'allocate done'

# Define input data
for j in range(NPOINTS):
  # Real part - sinusoidal input
  # Since psi_Input is a short int, we will need to use fixed-point number representation
  # See AN10934.pdf for details
  psi_Input[2*j] = int((1*2**14) * cos((pi*4/NPOINTS*j)))
  # Real part - DC Input
  #psi_Input[2*j] = int(1.*2**14)
  # Imaginary part 
  psi_Input[(2*j)+1] = 0

print 'write done'

vF_dspl_fftR4b16N1024(psi_Output.ptr, psi_Input.ptr)

for j in range(NPOINTS):
  print j, ((psi_Input[2*j] + 2**15) % 2**16 - 2**15)/2.**14, ((psi_Input[2*j+1] + 2**15) % 2**16 - 2**15)/2.**14, ((psi_Output[2*j] + 2**15) % 2**16 - 2**15)/2.**14, ((psi_Output[(2*j)+1] + 2**15) % 2**16 - 2**15)/2.**14
"""

# PID
print '\nPID:'
# Be sure to avoid overflow. All values are short int (-32768 to 32768)
pS_Coeff=tS_pid_Coeff()

pS_Coeff.Kp = 10
pS_Coeff.Ki = 1
pS_Coeff.Kd = 2
pS_Coeff.IntegratedError = 0
pS_Coeff.LastError = 0

target = 1000
current = 2000

print 'Target Current Speed'
print target, current

for i in range(50):
  si_Error = current-target
  newSpeed = ((vF_dspl_pid(si_Error,pS_Coeff.ptr) + 2**15) % 2**16 - 2**15) #Convert to signed
  print target, current, newSpeed
  current = (newSpeed * -0.05) + current
  
exit()
