my_word = 'cat'

import pandas as pd

df = pd.DataFrame({'names':['taylor','kai','andrew']})


class BravaisLattice:
    '''doc string info here'''
    def __init__(self,crystal_system,centering):
        self.crystal_system = crystal_system
        self.centering = centering
    def atoms_in_the_unit_cell(self):
        if self.crystal_system == 'cubic' and self.centering == 'face':
            atoms_per_cell = 4
            return atoms_per_cell

Cu = BravaisLattice('cubic','face')
Mg = BravaisLattice('hexagonal','base')

number = Cu.atoms_in_the_unit_cell()

Cu.density = 5

# %%

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length*self.width
        return area
    def perimeter(self):
        perimeter = self.length*2+self.width*2
        return perimeter

shape1 = Rectangle(10,5)
shape1.area()
shape1.perimeter()

# class Square:
#     def __init__(self,length):
#         self.length = length
#     def area(self):
#         return self.length*self.length
#     def perimeter(self):
#         return self.length*4

# shape2 = Square(5)
# shape2.area()
# shape2.perimeter()


#now for the shorter option

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)

shape3 = Square(5)
shape3.area()
shape3.perimeter


# %%
class GlassFiber:
    def __init__(self,glass_type,glass_modulus):
        self.glass_type = glass_type
        self.glass_modulus = glass_modulus

class Matrix:
    def __init__(self,epoxy_type,epoxy_modulus):
        self.epoxy_type = epoxy_type
        self.epoxy_modulus = epoxy_modulus


glass1 = GlassFiber('SiO2',100)
epoxy1 = Matrix('asdf',3)


class Composite(GlassFiber,Matrix):
    def __init__(self,epoxy_type,epoxy_modulus,glass_type,glass_modulus):
        GlassFiber.__init__(self,glass_type,glass_modulus)
        Matrix.__init__(self,epoxy_type,epoxy_modulus)

composite1 = Composite('resinA',3,'SiO2',100)

