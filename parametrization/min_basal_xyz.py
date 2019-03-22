import cclib
import os
import shutil

if os.path.exists("min_basal_xyz"):
    shutil.rmtree("min_basal_xyz")
    os.mkdir("min_basal_xyz")
else:
    os.mkdir("min_basal_xyz")

indir = 'Hirshfeld_iter_basal/'
outdir="min_basal_xyz/"

for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        print(n[:-6])
        mol=cclib.parser.QChem(indir+n)
        data=mol.parse()
        di=data.writexyz()
        print(di)
        d=open(outdir+n[:-6]+'.xyz', 'w')
        d.write(di)
        d.close()
        os.system('babel '+outdir+n[:-6]+'.xyz '+outdir+n[:-6]+'.xyz')
