import ase, ase.io
import numpy as np

df = pd.read_csv('tmp/springer_database.csv')

wyckoff = np.zeros([8,3])

#wyckoff[0][0], wyckoff[0][1], wyckoff[0][2] = cr_x, cr_y, cr_z
#wyckoff[1][0], wyckoff[1][1], wyckoff[1][2] = 2/3, 1/3, -cr_z + 1/3
#wyckoff[2][0], wyckoff[2][1], wyckoff[2][2] = i_x, i_y, i_z
#wyckoff[3][0], wyckoff[3][1], wyckoff[3][2] = -i_y, i_x - i_y, i_z
#wyckoff[4][0], wyckoff[4][1], wyckoff[4][2] = -i_x + i_y, -i_x, i_z
#wyckoff[5][0], wyckoff[5][1], wyckoff[5][2] = -i_x + 2/3, -i_y + 1/3, -i_z + 1/3
#wyckoff[6][0], wyckoff[6][1], wyckoff[6][2] = i_y + 2/3, -i_x+i_y + 1/3, -i_z + 1/3
#wyckoff[7][0], wyckoff[7][1], wyckoff[7][2] = i_x-i_y+2/3, i_x+1/3, -i_z+1/3


for i in range(len(df)):
    i_x, i_y, i_z = df.iloc[i]['Ix'], df.iloc[i]['Iy'], df.iloc[i]['Iz']
    cr_x , cr_y, cr_z = 0, 0, df.iloc[i]['Crz']
    name = df.iloc[i]['Compound']
    poscar = ase.io.read('CrI3_7_monolayer.vasp', format='vasp') #generic poscar file

    wyckoff[0][0], wyckoff[0][1], wyckoff[0][2] = cr_x, cr_y, cr_z
    wyckoff[1][0], wyckoff[1][1], wyckoff[1][2] = 2/3, 1/3, -cr_z + 1/3
    wyckoff[2][0], wyckoff[2][1], wyckoff[2][2] = i_x, i_y, i_z
    wyckoff[3][0], wyckoff[3][1], wyckoff[3][2] = -i_y, i_x - i_y, i_z
    wyckoff[4][0], wyckoff[4][1], wyckoff[4][2] = -i_x + i_y, -i_x, i_z
    wyckoff[5][0], wyckoff[5][1], wyckoff[5][2] = -i_x + 2/3, -i_y + 1/3, -i_z + 1/3
    wyckoff[6][0], wyckoff[6][1], wyckoff[6][2] = i_y + 2/3, -i_x+i_y + 1/3, -i_z + 1/3
    wyckoff[7][0], wyckoff[7][1], wyckoff[7][2] = i_x-i_y+2/3, i_x+1/3, -i_z+1/3
    for i in range(len(poscar.positions)):
        for j in range(3):
            poscar.positions[i][j] = wyckoff[i][j]

    ase.io.write(f"{name}.vasp", poscar, format="vasp")

    fin = open(f"{name}.vasp", "rt")
    data = fin.read()
    data = data.replace('Cartesian', 'direct')
    fin.close()
    fin = open(f"{name}.vasp", "wt")
    fin.write(data)
    fin.close()


#ase.io.vasp.write_vasp("poscar_new2.vasp", poscar, direct=False)
