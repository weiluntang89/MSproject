import subprocess

E100 = float(subprocess.getoutput("grep -r TOTEN 100/OUTCAR | tail -1 | awk '{print $5}'"))
E010 = float(subprocess.getoutput("grep -r TOTEN 010/OUTCAR | tail -1 | awk '{print $5}'"))
E001 = float(subprocess.getoutput("grep -r TOTEN 001/OUTCAR | tail -1 | awk '{print $5}'"))

print("E100 - E001 = ", (E100 - E001) * 10**3, "meV")
print("E010 - E001 = ", (E010 - E001) * 10**3, "meV")
print("E100 - E010 = ", (E100 - E010) * 10**3, "meV")

