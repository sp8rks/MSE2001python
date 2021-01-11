class Bravais_Lattice:
  def __init__(self, name):
    self.name = name

crystal_list = ['Al', 'Cu','W']

def centering():
    c.centering = input('Is there simple (s), body (b), base (c), or face centering (f)? (s/b/c/f):')
    return c.centering

def lattice_params():
    c.a, c.b, c.c = input('Enter lattice parameters').split()
    return c.a, c.b, c.c

def lattice_angles():
    c.alpha, c.beta, c.gamma = input('Enter lattice angles').split()
    c.alpha = int(c.alpha)
    c.beta = int(c.beta)
    c.gamma = int(c.gamma)
    return c.alpha, c.beta, c.gamma

crystals={}

for crystal in crystal_list:
    c = Bravais_Lattice(crystal)
    print(f'Material: {c.name}')
    lattice_params()
    lattice_angles()
    centering()
    
    if (c.a == c.b and c.a == c.c and c.alpha == 90):
        c.crystal_system = 'cubic'
    elif (c.a == c.b and c.a == c.c and c.alpha != 90):
        c.crystal_system = 'trigonal'
    elif (c.a == c.b and c.a != c.c) or (c.b == c.c and c.a != c.c):
        if c.alpha == c.beta and c.alpha == c.gamma:
            c.crystal_system = 'tetragonal'
        else:
            c.crystal_system = 'hexagonal'
    elif c.a != c.b and c.a != c.c and c.b != c.c:
        if c.alpha == c.beta and c.alpha == c.gamma and c.alpha == 90:
             c.crystal_system = 'orthorhombic'
        elif c.alpha != c.beta and c.alpha != c.gamma and c.beta != c.gamma:
            c.crystal_system = 'triclinic'
        else:
            c.crystal_system = 'monoclinic'
    if c.centering == 's':
        c.bravais = f'Simple {c.crystal_system} bravais lattice'
    elif c.centering == 'b':
        c.bravais = f'Body-centered {c.crystal_system} bravais lattice'
    elif c.centering == 'f':
        c.bravais = f'Face-centered {c.crystal_system} bravais lattice'
    elif c.centering == 'c':
        c.bravais = f'Base-centered {c.crystal_system} bravais lattice'
    crystals[c.name] = c

for name in crystal_list:
    print(crystals[name].bravais)



