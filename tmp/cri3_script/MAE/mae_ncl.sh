modelist=(1 2 3) # 1 - 001, 2 - 010, 3 -100

for mode in ${modelist[@]}
do
	if [ "$mode" -eq 1 ]; then
		dirname="001"
		if [ ! -d "$dirname" ]; then
			mkdir $dirname
		fi
		
		cp POSCAR INCAR POTCAR KPOINTS CHGCAR $dirname
		cp /home/weilunt/crgete3/crgete3_fm/crgete3_fm_mae/crgete3_fm_mae_010/crgete3_fm_mae_010_12/crgete3_001/slurm.vasp $dirname

		cd $dirname
		sed -i "s/!SAXIS = 0 1 0/SAXIS = 0 0 1/g" INCAR
		sed -i "s/!LSORBIT = .True./LSORBIT = .True./g" INCAR
		sed -i "s/ICHARG = 1/ICHARG = 11/g" INCAR

		sed -i "s/8 8 1/16 16 1/g" KPOINTS

		#sed -i "s/mpirun -np 36 ~/vasp.5.4.4/bin/vasp_std >out/mpirun -np 36 ~/vasp.5.4.4/bin/vasp_ncl >out/g" slurm.vasp
		sbatch slurm.vasp
		cd ..
	fi

	if [ "$mode" -eq 2 ]; then
		dirname="010"
		if [ ! -d "$dirname" ]; then
			mkdir $dirname
		fi

		cp POSCAR INCAR POTCAR KPOINTS CHGCAR $dirname
		cp /home/weilunt/crgete3/crgete3_fm/crgete3_fm_mae/crgete3_fm_mae_010/crgete3_fm_mae_010_12/crgete3_001/slurm.vasp $dirname

		cd $dirname

		sed -i "s/!SAXIS = 0 1 0/SAXIS = 0 1 0/g" INCAR
		sed -i "s/!LSORBIT = .True./LSORBIT = .True./g" INCAR
		sed -i "s/ICHARG = 1/ICHARG = 11/g" INCAR

		sed -i "s/8 8 1/16 16 1/g" KPOINTS

		sbatch slurm.vasp
		cd ..
	fi


	if [ "$mode" -eq 3 ]; then

		dirname="100"

		if [ ! -d "$dirname" ]; then
			mkdir $dirname
		fi

		cp POSCAR INCAR POTCAR KPOINTS CHGCAR $dirname
		cp /home/weilunt/crgete3/crgete3_fm/crgete3_fm_mae/crgete3_fm_mae_010/crgete3_fm_mae_010_12/crgete3_001/slurm.vasp $dirname

		cd $dirname

		sed -i "s/!SAXIS = 0 1 0/SAXIS = 1 0 0/g" INCAR
		sed -i "s/!LSORBIT = .True./LSORBIT = .True./g" INCAR
		sed -i "s/ICHARG = 1/ICHARG = 11/g" INCAR

		sed -i "s/8 8 1/16 16 1/g" KPOINTS

		sbatch slurm.vasp
		cd ..
	fi
done
