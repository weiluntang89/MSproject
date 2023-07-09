from pyxtal import pyxtal
from pyxtal.lattice import Lattice
import pandas as pd
import numpy as np

df = pd.read_csv('tmp/springer_database.csv')

struc = pyxtal()
spg = 148
composition = [6,6,18]
α = 90
β = 90
γ = 120

#for i in range(1):
ix = df.iloc[6]['Ix']
iy = df.iloc[6]['Iy']
iz = df.iloc[6]['Iz']
Crz = df.iloc[6]['Crz']
Bz = df.iloc[6]['Bz']
a = df.iloc[6]['a']
c = df.iloc[6]['c']
name = df.iloc[6]['Compound']

cell = Lattice.from_para(a, a, c, α, β, γ, ltype = 'Hexagonal')
sites = [{"6c": [0, 0, Crz]},{"6c": [0, 0, Bz]}, {"18f": [ix, iy, iz]}]

df_to_array = np.array(df)
element = df_to_array[6][1].split()
print(element)
struc.from_random(3, spg, element, composition, lattice=cell, sites=sites)
print(struc)
    #print(struc)
    #struc.resort_species(element)
    #print(struc.atom_sites)
    #print(struc)
struc.to_file(f"{name}_crgete3.poscar", fmt='poscar', sym_num=1)
#print(len(df))
