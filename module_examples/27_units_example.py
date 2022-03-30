from unit_converter.converter import convert
import pint
import scipy.constants as cnst
from molmass import Formula

#simple conversion tool for one time conversion
convert('60 m/s', 'km/h')
convert('100 mile/h','km/h')


#or we can use Pint!
u = pint.UnitRegistry()
Q = u.Quantity

speed = Q(60,'m/seconds')



distance = Q(8,'m')
time = Q(15,'seconds')
speed = distance / time
#print(speed.to('km/hr'))
speed = speed.to(u.km / u.hour)


c = Q(cnst.c,'m/s')
lightyear = c * Q(12,'month')
print(lightyear.to('m'))


#what is the density of NaCl if the a=0.563nm
formulas_per_cell = 4
NaCl = Formula('NaCl')
mass = formulas_per_cell*Q(NaCl.mass,'g/mole') / Q(cnst.Avogadro, '1/mole')
volume = Q(0.563,'nm')**3
density = mass/volume
#print(density.to('grams/cm^3'))
print(density.to('grams/nm^3'))

#customs units
u.define('smoot=1.702m=sm')
print(distance.to('sm'))



#electrical conductivity sigma=n*mobility*charge
n = Q(1e17,'cm^-3')
mu = Q(1.5e4,'cm^2/V/s')
e = Q(cnst.e,'coulombs')
sigma = n*mu*e
print(sigma.to('ohms^-1*m^-1'))

#to check your current units you can use .units attribute
sigma.units


# %% 
#how about an example!
from unit_converter.converter import convert
import pint
import scipy.constants as cnst
from molmass import Formula

#methane combustion
#CH4+2O2 ->2H2O+CO2

#how many grams of water are produced for every liter of methane?
#PV=nRT
#n_methane=PV/RT
#assume 1atm, 300K

#first get pints classes ready
u = pint.UnitRegistry()
Q = u.Quantity

n_methane = Q(1,'atm')*Q(1,'L')/(Q(cnst.R,'J/mol/K')*Q(300,'K'))
#print(n_methane.to('mol'))

#for every 1 mol of CH4, we make 2 moles of H2O
n_H2O = 2*n_methane
H2O = Formula('H2O')
m_H2O = n_H2O*Q(H2O.mass,'g/mol')
print(m_H2O.to('g'))





