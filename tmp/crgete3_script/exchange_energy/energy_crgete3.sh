# Calculate energy of different magnetic configuratio

modelist=(1 2 3 4) # 1-fm, 2-neel, 3-zigzag, 4-stripy

for mode in ${modelist[@]}
do
	if [ "$mode" -eq 1 ]; then
		dirname="fm"
		if [ ! -d "$dirname" ]; then
			mkdir $dirname
		fi
		cp INCAR POTCAR KPOINTS POSCAR slurm.vasp $dirname
		cd $dirname
		sbatch slurm.vasp
		cd ..
		continue

	elif [ "$mode" -eq 2 ]; then
		dirname="neel"
		if [ ! -d "$dirname" ]; then
			mkdir $dirname
		fi
		cp POSCAR INCAR POTCAR KPOINTS slurm.vasp $dirname
		cd $dirname
		sed -i "s/MAGMOM = 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0/MAGMOM = -3 3 3 -3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0/g" INCAR
		sbatch slurm.vasp	
		cd ..

	elif [ "$mode" -eq 3 ]; then
		dirname="zigzag"
		if [ ! -d "$dirname" ]; then
			mkdir $dirname
		fi
		cp POSCAR INCAR POTCAR KPOINTS slurm.vasp $dirname
		cd $dirname
		sed -i "s/MAGMOM = 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0/MAGMOM = -3 3 -3 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0/g" INCAR
		sbatch slurm.vasp	
		cd ..


	elif [ "$mode" -eq 4 ]; then
		dirname="stripy"
		if [ ! -d "$dirname" ]; then
			mkdir $dirname
		fi
		cp POSCAR INCAR POTCAR KPOINTS slurm.vasp $dirname
		cd $dirname
		sed -i "s/MAGMOM = 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0/MAGMOM = 3 3 -3 -3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0/g" INCAR
		sbatch slurm.vasp	
		cd ..
	fi

done
