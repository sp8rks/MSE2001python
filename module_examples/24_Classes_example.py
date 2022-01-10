class Bravais_Lattice:
    ''' here is where we write the help
    This class defines all the structural info for a material'''
    def __init__(self,crystal_system, centering):
        self.crystal_system=crystal_system
        self.centering_type = centering
        self.crystal_structure = crystal_system+' ' +centering
        if self.crystal_system == 'cubic':
            self.alpha = 90
            self.beta=90
            self.gamma=90


Cu = Bravais_Lattice('cubic','face')
Mg = Bravais_Lattice('hexagonal','base')
Cu.lattice_parameter = 3.615
Cu.color = 'copper'

Cu_lattice_parameter = 3.615


def atoms_in_the_unit_cell(self):
    if self.crystal_system == 'cubic' and self.centering_type == 'face':
        atoms_per_cell = 4
        return atoms_per_cell

atoms_per_cell = atoms_in_the_unit_cell(Cu)
