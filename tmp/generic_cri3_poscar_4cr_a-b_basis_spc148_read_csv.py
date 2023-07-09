# CrI3 supercell new basis read csv

import ase, ase.io
import numpy as np
#poscar = ase.io.read('CrI3_a+b_supercell_local_function_cut.vasp', format='vasp')
wyckoff = np.zeros([16,3])


for i in ([0,1,2, 10,11]):
    cr_x , cr_y, cr_z = 0, 0, df.iloc[i]['Crz']
    i_x, i_y, i_z = df.iloc[i]['Ix'], df.iloc[i]['Iy'], df.iloc[i]['Iz']
    name = df.iloc[i]['Compound']
    poscar = ase.io.read('CrI3_a+b_supercell_local_function_cut.vasp', format='vasp')


    wyckoff[0][0], wyckoff[0][1], wyckoff[0][2] = 1/2*cr_x+1/2*cr_y, 1/2*cr_x-1/2*cr_y, cr_z
    wyckoff[1][0], wyckoff[1][1], wyckoff[1][2] = 0, 2/3, -cr_z + 1/3
    wyckoff[2][0], wyckoff[2][1], wyckoff[2][2] = 1/2, 1/6, -cr_z+1/3
    wyckoff[3][0], wyckoff[3][1], wyckoff[3][2] = 1/2*cr_x+1/2*cr_y+1/2, 1/2*cr_x-1/2*cr_y+1/2, cr_z

    wyckoff[4][0], wyckoff[4][1], wyckoff[4][2] = 1/2*i_x+1/2*i_y+1/2, 1/2*i_x-1/2*i_y+1/2, i_z
    wyckoff[5][0], wyckoff[5][1], wyckoff[5][2] = -i_x+1/2*i_y+1/2, 1/2*i_y+1/2, i_z
    wyckoff[6][0], wyckoff[6][1], wyckoff[6][2] = 1/2*i_x-i_y, -1/2*i_x+1, i_z
    wyckoff[7][0], wyckoff[7][1], wyckoff[7][2] = 1/2*i_x-i_y+1/2, -1/2*i_x+1/2, i_z
    wyckoff[8][0], wyckoff[8][1], wyckoff[8][2] = 1/2*i_x+1/2*i_y, 1/2*i_x-1/2*i_y, i_z
    wyckoff[9][0], wyckoff[9][1], wyckoff[9][2] = -i_x+1/2*i_y+1, 1/2*i_y, i_z
    wyckoff[10][0], wyckoff[10][1], wyckoff[10][2] = -1/2*i_x+i_y+1, 1/2*i_x+2/3, -i_z+1/3
    wyckoff[11][0], wyckoff[11][1], wyckoff[11][2] = i_x-1/2*i_y+1/2, 1/6-1/2*i_y, -i_z+1/3
    wyckoff[12][0], wyckoff[12][1], wyckoff[12][2] = i_x-1/2*i_y, 2/3-1/2*i_y, -i_z+1/3
    wyckoff[13][0], wyckoff[13][1], wyckoff[13][2] = -1/2*i_x+i_y+1/2, 1/2*i_x+1/6, -i_z+1/3
    wyckoff[14][0], wyckoff[14][1], wyckoff[14][2] = -1/2*i_x-1/2*i_y+1/2, -1/2*i_x+1/2*i_y+1/6, -i_z+1/3
    wyckoff[15][0], wyckoff[15][1], wyckoff[15][2] = -1/2*i_x-1/2*i_y+1, -1/2*i_x+1/2*i_y+2/3, -i_z+1/3


#print(wyckoff)

#print(poscar.positions)
    for i in range(len(poscar.positions)):
        for j in range(3):
            poscar.positions[i][j] = wyckoff[i][j]

    poscar.positions[:, [1, 0]] = poscar.positions[:, [0, 1]]
    poscar.cell[[1, 0]] = poscar.cell[[0, 1]]
#print(poscar.positions)
#print(poscar.positions)
#print(poscar.cell)
#print(type(poscar))


#x = 2
#poscar.positions[0][0] = x
#print(poscar.positions[0])
#print(type(poscar.positions))
    ase.io.write(f"{name}_supercell.vasp", poscar, format="vasp")
#filename = "poscar_new1.vasp"
#myfile = open(filename, 'w')
#myfile.write(label + '\n')


    fin = open(f"{name}_supercell.vasp", "rt")
    data = fin.read()
    data = data.replace('Cartesian', 'direct')
    fin.close()
    fin = open(f"{name}_supercell.vasp", "wt")
    fin.write(data)
    fin.close()


#ase.io.vasp.write_vasp("poscar_supercell_new2.vasp", poscar, direct=False)
