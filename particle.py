"""
#===========================================================================#
	AxiMeta
		-- This file generates particle matrix arrays
		-- 1. Input box dimension (boundary)
		-- 2. Input array (lines and rows)
		-- 3. Generates coordinaries in file particlePositions
#===========================================================================#
"""

import os

#===========================Input Section===================================#
# Particle diameter
diameter = 5e-3

# Particle distance
delta = 0.0005

# Box dimension
x = 0.1
y = 0.5
z = 0.004

# Matrix dimension
xArray = 80
yArray = 500
zArray = 1
#===========================End Input Section===============================#


 # Total particle number
particleNumber = xArray * yArray * zArray

# Print particle number
print('>>> AxiMeta: Particle number -> %d'%particleNumber)


with open('particlePositions', 'w') as file:
	# particle distance
	xDistance = x/(xArray+1)
	yDistance = y/(yArray+1)
	zDistance = z/(zArray+1)

	Count = 0
	for i in range(0, xArray):
		for j in range(0, yArray):
			for k in range(0, zArray):
				Count += 1
				print('>>> AxiMeta: Current writing particle %d\r'%Count)
				file.write('\n(' + str(xDistance*(i+1)) + '\t'+ str(yDistance*(j+1)) + '\t' + str(zDistance*(k+1)) + ')')
	print('>>> AxiMeta: Done writing. Now exit...')
	file.close()


















