import sys
import string
import subprocess as subp
import matplotlib.pyplot as plt
import vplot as vpl
import numpy as np

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

nsemi=30
necc=30
semi=[0 for j in range(nsemi)]
ecc=[0 for j in range(necc)]
periq=[[0 for j in range(necc)] for k in range(nsemi)]

result = subp.run("ls -d data/40Eri*", shell=True, stdout=subp.PIPE).stdout.decode('utf-8')
dirs=result.split()

iSemi=0
iEcc=0


for dir in dirs:
    if dir != "0":
        cmd = "cd "+dir+"; vplanet vpl.in >& output"
        subp.call(cmd, shell=True)
         At this point the log file has been generated

        print(dir)
        sys.stdout.flush()
        sys.stderr.flush()
        # Now search for parameters
        found=0

        data = np.loadtxt('./data/grid_list.dat', skiprows=1, dtype=str, delimiter=' ',usecols=(1,2))
        semi_data =data[::nsemi,0]
        semi[iSemi]=float(semi_data[iSemi])
        ecc_data =data[:necc,1]
        ecc[iEcc] = float(ecc_data[iEcc])

        data = np.loadtxt(dir+'/40Eri.comp.forward', dtype=float, delimiter=' ',usecols=(3))
        periq[iEcc][iSemi]=float(min(data))
        print("semi")
        print(semi)
        print("ecc")
        print(ecc)
        print("periq")
        print(periq)

        iSemi += 1
        if (iSemi == nsemi):
        # New line in ecc
            iEcc += 1
            iSemi = 0


CS = plt.contourf(ecc,semi, periq,50)
plt.ylabel('SemiMajorAxis',fontsize=20)
plt.xlabel('Eccentricity',fontsize=20)
plt.tick_params(axis='both', labelsize=20)
plt.colorbar(CS)

#plt.yscale('log')
plt.xlim(0,0.9)
plt.ylim(200,8000)


x=[0,0.9]
y=[418,418]
plt.plot(x,y,linestyle='dotted',color='black',linewidth=3)

plt.tight_layout()


if (sys.argv[1] == 'pdf'):
    plt.savefig('GalaxyEffects.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('GalaxyEffects.png')
