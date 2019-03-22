import os
import shutil


basdir='./'

if os.path.exists(basdir+"scan_qchem_miztli/"):
    shutil.rmtree(basdir+"scan_qchem_miztli/")
    os.mkdir(basdir+"scan_qchem_miztli/")
else:
    os.mkdir(basdir+"scan_qchem_miztli/")     

mizdir=basdir+"scan_qchem_miztli/"

indir='min_basal_xyz/'


for root, dirs,filnames in os.walk(indir):
    for n in filnames:
        w=open(mizdir+'runqc_'+n[:-4]+'_1'+'.lsf', 'w')
        w.write('#!/bin/bash'+'\n')
        w.write('#BSUB -q q_hpc'+'\n')
        w.write('#BSUB -eo error'+'\n')
        w.write('#BSUB -oo sal'+'\n')
        w.write('#BSUB -R "span[hosts=1]"'+'\n')
        w.write('#BSUB -n 16'+'\n')
        w.write('\n')
        w.write('module load qchem/4.4-serial-multicore'+'\n')
        w.write('export QCSCRATCH=/tmpu/cab_g/afmv_a/scratch_qchem'+'\n')
        for Root, Dirs,Filnames in os.walk(basdir+'scan_qchem_basal/'+n[:-4]+'_1'):
            for m in Filnames:
                w.write('qchem -nt 16 '+n[:-4]+'_1'+'/'+m+' '+n[:-4]+'_1'+'/'+m[:-2]+'out'+'\n')
            w.close()
        
        p=open(mizdir+'runqc_'+n[:-4]+'_2'+'.lsf', 'w')
        p.write('#!/bin/bash'+'\n')
        p.write('#BSUB -q q_htc'+'\n')
        p.write('#BSUB -eo error'+'\n')
        p.write('#BSUB -oo sal'+'\n')
        p.write('#BSUB -R "span[hosts=1]"'+'\n')
        p.write('#BSUB -n 16'+'\n')
        p.write('\n')
        p.write('module load qchem/4.4-serial-multicore'+'\n')
        p.write('export QCSCRATCH=/tmpu/cab_g/afmv_a/scratch_qchem'+'\n')
        for Root, Dirs,Filnames in os.walk(basdir+'scan_qchem_basal/'+n[:-4]+'_2'):
            for m in Filnames:
                p.write('qchem -nt 16 '+n[:-4]+'_2'+'/'+m+' '+n[:-4]+'_2'+'/'+m[:-2]+'out'+'\n')
            p.close()
        x=open(mizdir+'runqc_'+n[:-4]+'_3'+'.lsf', 'w')
        x.write('#!/bin/bash'+'\n')
        x.write('#BSUB -q q_htc'+'\n')
        x.write('#BSUB -eo error'+'\n')
        x.write('#BSUB -oo sal'+'\n')
        x.write('#BSUB -R "span[hosts=1]"'+'\n')
        x.write('#BSUB -n 16'+'\n')
        x.write('\n')
        x.write('module load qchem/4.4-serial-multicore'+'\n')
        x.write('export QCSCRATCH=/tmpu/cab_g/afmv_a/scratch_qchem'+'\n')
        for Root, Dirs,Filnames in os.walk(basdir+'scan_qchem_basal/'+n[:-4]+'_3'):
            for m in Filnames:
                x.write('qchem -nt 16 '+n[:-4]+'_3'+'/'+m+' '+n[:-4]+'_3'+'/'+m[:-2]+'out'+'\n')
            x.close()
