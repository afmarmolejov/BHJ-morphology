import os
import shutil
if os.path.exists("basal_param"):
    shutil.rmtree("basal_param")
    os.mkdir("basal_param")
else:
    os.mkdir("basal_param")

indir = 'min_basal_xyz/'
qchemdir='out_scan_qchem_basal/'
amberdir='scan_sander_basal/'
solardir='./'
paramdir='basal_param/'
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        print(n[:-4])
        os.mkdir(paramdir+n[:-4]+'/')
        cmd='python '+solardir+'GA_minimum.py '+qchemdir+n[:-4]+'_1/qchem_1_'+n[:-4]+'.txt '+amberdir+'out_1_'+n[:-4]+'/sander_1_'+n[:-4]+'.txt > '+solardir+'parametro.txt'
        os.system(cmd)
        r=open(solardir+'parametro.txt','r')
        table = [line.rstrip().split(" ") for line in r.readlines()]
        w=open(paramdir+n[:-4]+'/'+'param.txt','w')
        w.write(str(table[15][0])+'  '+str(table[15][2])+'   '+str(table[15][5])+'\n')
        w.write(str(table[18][0])+'  '+str(table[18][2])+'   '+str(table[18][5])+'\n')
        
        cmd='python '+solardir+'GA_minimum.py '+qchemdir+n[:-4]+'_2/qchem_2_'+n[:-4]+'.txt '+amberdir+'out_2_'+n[:-4]+'/sander_2_'+n[:-4]+'.txt > '+solardir+'parametro.txt'
        os.system(cmd)
        r=open(solardir+'parametro.txt','r')
        table = [line.rstrip().split(" ") for line in r.readlines()]
        w.write(str(table[15][0])+'  '+str(table[15][2])+'   '+str(table[15][5])+'\n')
        w.write(str(table[18][0])+'  '+str(table[18][2])+'   '+str(table[18][5])+'\n')
        
        cmd='python '+solardir+'GA_minimum.py '+qchemdir+n[:-4]+'_3/qchem_3_'+n[:-4]+'.txt '+amberdir+'out_3_'+n[:-4]+'/sander_3_'+n[:-4]+'.txt > '+solardir+'parametro.txt'
        os.system(cmd)
        r=open(solardir+'parametro.txt','r')
        table = [line.rstrip().split(" ") for line in r.readlines()]
        w.write(str(table[15][0])+'  '+str(table[15][2])+'   '+str(table[15][5])+'\n')
        w.write(str(table[18][0])+'  '+str(table[18][2])+'   '+str(table[18][5])+'\n')
        w.close()
        cmd2='cd '+solardir+' && rm parametro.txt'
        os.system(cmd2)
