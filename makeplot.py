import numpy as np
import matplotlib.pyplot as plt
import vplot
import sys
import scipy.signal as sig

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

out = vplot.GetOutput()

fig = plt.figure(figsize=(8.5,6))
plt.subplot(2,2,1)
plt.plot(out.b.Time/1e9,out.b.RotPer,'k-')
plt.ylabel('Rotation Period (days)')
plt.xscale('log')

plt.subplot(2,2,2)
plt.plot(out.b.Time/1e9,out.b.EnvelopeMass,'k-')
plt.ylabel('Envelope Mass (M$_\oplus$)')
plt.xscale('log')

plt.subplot(2,2,3)
plt.plot(out.b.Time/1e9,out.b.SurfWaterMass,'k-')
plt.xlabel('Time (Gyr)')
plt.ylabel('Water Mass (Earth Oceans)')
plt.xscale('log')

plt.subplot(2,2,4)
plt.plot(out.b.Time/1e9,out.b.TidalQ,'k-')
plt.xlabel('Time (Gyr)')
plt.ylabel('TidalQ')
plt.xscale('log')
plt.yscale('log')

vplot.make_pretty(fig)
if (sys.argv[1] == 'pdf'):
    fig.savefig('HD26965.pdf')
if (sys.argv[1] == 'png'):
    fig.savefig('HD26965.png')
plt.close()
