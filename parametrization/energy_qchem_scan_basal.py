import os
import shutil
import cclib

indir = '/home/andrexfelo/proyecto_amador/SOLAR_CELL/min_basal_xyz/'
outscandir='/home/andrexfelo/proyecto_amador/SOLAR_CELL/out_scan_qchem_basal/'
for root, dirs, filenames in os.walk(indir):
    for m in filenames:
        print(m[:-4])
        x=[]
        for n in range(0,360,15):
            mol=cclib.parser.QChem(outscandir+m[:-4]+'_1/'+m[:-4]+'_'+str(n)+'.qcout')
            data=mol.parse()
            energy=data.scfenergies[-1]
            x.append(energy/27.21138505*627.509391)
        mol=cclib.parser.QChem(outscandir+m[:-4]+'_1/'+m[:-4]+'_0.qcout')
        data=mol.parse()
        energy=data.scfenergies[-1]                   
        x.append(energy/27.21138505*627.509391)
        w=open(outscandir+m[:-4]+'_1/qchem_1_'+m[:-4]+'.txt','w')
        for j in range(0,25,1):
            w.write(str(x[j]-min(x))+'\n')
        w.close()
        x=[]
        for n in range(0,360,15):
            mol=cclib.parser.QChem(outscandir+m[:-4]+'_2/'+m[:-4]+'_'+str(n)+'.qcout')
            data=mol.parse()
            energy=data.scfenergies[-1]
            x.append(energy/27.21138505*627.509391)
        mol=cclib.parser.QChem(outscandir+m[:-4]+'_2/'+m[:-4]+'_0.qcout')
        data=mol.parse()
        energy=data.scfenergies[-1]                   
        x.append(energy/27.21138505*627.509391)
        w=open(outscandir+m[:-4]+'_2/qchem_2_'+m[:-4]+'.txt','w')
        for j in range(0,25,1):
            w.write(str(x[j]-min(x))+'\n')
        w.close()
        x=[]
        for n in range(0,360,15):
            mol=cclib.parser.QChem(outscandir+m[:-4]+'_3/'+m[:-4]+'_'+str(n)+'.qcout')
            data=mol.parse()
            energy=data.scfenergies[-1]
            x.append(energy/27.21138505*627.509391)
        mol=cclib.parser.QChem(outscandir+m[:-4]+'_3/'+m[:-4]+'_0.qcout')
        data=mol.parse()
        energy=data.scfenergies[-1]                   
        x.append(energy/27.21138505*627.509391)
        w=open(outscandir+m[:-4]+'_3/qchem_3_'+m[:-4]+'.txt','w')
        for j in range(0,25,1):
            w.write(str(x[j]-min(x))+'\n')
        w.close()
