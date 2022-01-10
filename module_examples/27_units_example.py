from unit_converter.converter import convert
import pint
import scipy.constants as cnst
from molmass import Formula

#simple conversion tool for one time conversion
convert('60 m/s', 'km/h')


#or we can use Pint!
u = pint.UnitRegistry()
Q = u.Quantity

speed = Q(60,'m/seconds')



distance = Q(8,'m')
time = Q(15,'seconds')
speed = distance / time
#print(speed.to('m/seconds'))
speed = speed.to(u.km / u.hour)


c = Q(cnst.c,'m/s')
lightyear = c * Q(1,'year')
print(lightyear.to('m'))


#what is the density of NaCl if the a=0.563nm
formulas_per_cell = 4
NaCl = Formula('NaCl')
mass = formulas_per_cell*Q(NaCl.mass,'g/mole') / Q(cnst.Avogadro, '1/mole')
volume = Q(0.563,'nm')**3
density = mass/volume
print(density.to('grams/cm^3'))


#customs units
u.define('smoot=1.702m=sm')
print(distance.to('sm'))



#electrical conductivity sigma=n*mobility*charge
n = Q(1e17,'cm^-3')
mu = Q(1.5e4,'cm^2/V/s')
e = Q(cnst.e,'coulombs')
sigma = n*mu*e
print(sigma.to('ohms^-1*m^-1'))








