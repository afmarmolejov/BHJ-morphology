import cclib
import os
import shutil

if os.path.exists("video_qchem_basal"):
    shutil.rmtree("video_qchem_basal")
    os.mkdir("video_qchem_basal")
else:
    os.mkdir("video_qchem_basal")

indir = 'out_scan_qchem_basal/'
bas="min_basal_xyz/"
outdir="video_qchem_basal/"

for root, dirs, filenames in os.walk(bas):
    for n in filenames:
        print(n[:-4])
        os.mkdir(outdir+n[:-4])
        for i in range(0,360,15):
            mol=cclib.parser.QChem(indir+n[:-4]+'_1/'+n[:-4]+'_'+str(i)+'.qcout')
            data=mol.parse()
            di=data.writexyz()    
            d=open(outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.xyz', 'w')
            d.write(di)
            d.close()
        mol=cclib.parser.QChem(indir+n[:-4]+'_1/'+n[:-4]+'_0.qcout')
        data=mol.parse()
        di=data.writexyz()    
        d=open(outdir+n[:-4]+'/'+n[:-4]+'_360.xyz', 'w')
        d.write(di)
        d.close()
        for i in range(0,375,15):
            os.system('babel '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.xyz '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.pdb')
            os.system('babel -ipdb '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.pdb -osd '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.sd')
        for i in range(0,375,15):
            cmd='cat '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.sd  >> '+outdir+n[:-4]+'/scan_1.sd'
            os.system(cmd)
        os.system('babel '+outdir+n[:-4]+'/'+'scan_1.sd '+outdir+n[:-4]+'/'+'scan_1.sd --align')
        cmd='rm '+outdir+n[:-4]+'/'+n[:-4]+'*.sd '+outdir+n[:-4]+'/'+n[:-4]+'*.xyz '+outdir+n[:-4]+'/'+n[:-4]+'*.pdb '
        os.system(cmd)

        for i in range(0,360,15):
            mol=cclib.parser.QChem(indir+n[:-4]+'_2/'+n[:-4]+'_'+str(i)+'.qcout')
            data=mol.parse()
            di=data.writexyz()    
            d=open(outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.xyz', 'w')
            d.write(di)
            d.close()
        mol=cclib.parser.QChem(indir+n[:-4]+'_2/'+n[:-4]+'_0.qcout')
        data=mol.parse()
        di=data.writexyz()    
        d=open(outdir+n[:-4]+'/'+n[:-4]+'_360.xyz', 'w')
        d.write(di)
        d.close()
        for i in range(0,375,15):
            os.system('babel '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.xyz '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.pdb')
            os.system('babel -ipdb '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.pdb -osd '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.sd')
        for i in range(0,375,15):
            cmd='cat '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.sd  >> '+outdir+n[:-4]+'/scan_2.sd'
            os.system(cmd)
        os.system('babel '+outdir+n[:-4]+'/'+'scan_2.sd '+outdir+n[:-4]+'/'+'scan_2.sd --align')
        cmd='rm '+outdir+n[:-4]+'/'+n[:-4]+'*.sd '+outdir+n[:-4]+'/'+n[:-4]+'*.xyz '+outdir+n[:-4]+'/'+n[:-4]+'*.pdb '
        os.system(cmd)

        for i in range(0,360,15):
            mol=cclib.parser.QChem(indir+n[:-4]+'_3/'+n[:-4]+'_'+str(i)+'.qcout')
            data=mol.parse()
            di=data.writexyz()    
            d=open(outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.xyz', 'w')
            d.write(di)
            d.close()
        mol=cclib.parser.QChem(indir+n[:-4]+'_3/'+n[:-4]+'_0.qcout')
        data=mol.parse()
        di=data.writexyz()    
        d=open(outdir+n[:-4]+'/'+n[:-4]+'_360.xyz', 'w')
        d.write(di)
        d.close()
        for i in range(0,375,15):
            os.system('babel '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.xyz '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.pdb')
            os.system('babel -ipdb '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.pdb -osd '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.sd')
        for i in range(0,375,15):
            cmd='cat '+outdir+n[:-4]+'/'+n[:-4]+'_'+str(i)+'.sd  >> '+outdir+n[:-4]+'/scan_3.sd'
            os.system(cmd)
        os.system('babel '+outdir+n[:-4]+'/'+'scan_3.sd '+outdir+n[:-4]+'/'+'scan_3.sd --align')
        cmd='rm '+outdir+n[:-4]+'/'+n[:-4]+'*.sd '+outdir+n[:-4]+'/'+n[:-4]+'*.xyz '+outdir+n[:-4]+'/'+n[:-4]+'*.pdb '
        os.system(cmd)
