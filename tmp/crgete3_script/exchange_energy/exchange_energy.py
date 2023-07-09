import subprocess

FM = float(subprocess.getoutput("grep -r TOTEN fm/OUTCAR | tail -1 | awk '{print $5}'"))
NEEL = float(subprocess.getoutput("grep -r TOTEN neel/OUTCAR | tail -1 | awk '{print $5}'"))
ZIGZAG = float(subprocess.getoutput("grep -r TOTEN zigzag/OUTCAR | tail -1 | awk '{print $5}'"))
STRIPY = float(subprocess.getoutput("grep -r TOTEN stripy/OUTCAR | tail -1 | awk '{print $5}'"))


def exchange_energy(FM, NEEL, ZIGZAG, STRIPY):
	FM, NEEL, ZIGZAG, STRIPY = FM/4, NEEL/4, ZIGZAG/4, STRIPY/4
	dFM_NEEL = FM - NEEL
	dFM_ZIGZAG = FM - ZIGZAG
	dFM_STRIPY = FM - STRIPY
	J1 = 1/8 * dFM_NEEL - 1/8 * dFM_ZIGZAG + 1/8 * dFM_STRIPY
	J2 = -1/16 * dFM_NEEL + 1/16 * dFM_ZIGZAG + 1/16 * dFM_STRIPY
	J3 = 1/24 * dFM_NEEL + 1/8 * dFM_ZIGZAG - 1/8 * dFM_STRIPY

	print("J1: ", J1 * 10**3, "meV")
	print("J2: ", J2 * 10**3, "meV")
	print("J3: ", J3 * 10**3, "meV")
	
exchange_energy(FM, NEEL, ZIGZAG, STRIPY)
	
