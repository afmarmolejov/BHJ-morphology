from __future__ import print_function
from rdkit import Chem
from rdkit.Chem.AtomPairs import Torsions
from rdkit import Chem
from rdkit.Chem import AllChem, rdMolTransforms
import os
import shutil


indir='./'

if os.path.exists(indir+"scan_qchem_basal/"):
    shutil.rmtree(indir+"scan_qchem_basal/")
    os.mkdir(indir+"scan_qchem_basal/")
else:
    os.mkdir(indir+"scan_qchem_basal/")     

scandir='scan_qchem_basal/'
xyzindir='min_basal_xyz/'
moldir='min_basal_mol/'
dihedir='numbering_dihedral_basal/'

for root, dirs, filenames in os.walk(xyzindir):
    for n in filenames:
        print(n)
        m = Chem.MolFromMolFile(moldir+n[:-4]+'.mol')
        c = m.GetConformer()
        ##numbering less one
        f=open(dihedir+n[:-4]+'.dat', 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        resta1=int(table[0][0])-int(1)
        resta2=int(table[0][1])-int(1)
        resta3=int(table[0][2])-int(1)
        resta4=int(table[0][3])-int(1)
        resta5=int(table[4][0])-int(1)
        resta6=int(table[4][1])-int(1)
        resta7=int(table[4][2])-int(1)
        resta8=int(table[4][3])-int(1)
        resta9=int(table[8][0])-int(1)
        resta10=int(table[8][1])-int(1)
        resta11=int(table[8][2])-int(1)
        resta12=int(table[8][3])-int(1)
	if n=='C342.xyz':
		resta1=int(table[0][0])-int(2)
		resta2=int(table[0][1])-int(2)
		resta3=int(table[0][2])-int(2)
		resta4=int(table[0][3])-int(2)
		resta5=int(table[4][0])-int(2)
		resta6=int(table[4][1])-int(2)
		resta7=int(table[4][2])-int(2)
		resta8=int(table[4][3])-int(2)
		resta9=int(table[8][0])-int(2)
		resta10=int(table[8][1])-int(2)
		resta11=int(table[8][2])-int(2)
		resta12=int(table[8][3])-int(2)
	if n=='C385.xyz':
		resta1=int(table[0][0])-int(2)
		resta2=int(table[0][1])-int(2)
		resta3=int(table[0][2])-int(2)
		resta4=int(table[0][3])-int(2)
		resta5=int(table[4][0])-int(2)
		resta6=int(table[4][1])-int(2)
		resta7=int(table[4][2])-int(2)
		resta8=int(table[4][3])-int(2)
		resta9=int(table[8][0])-int(2)
		resta10=int(table[8][1])-int(2)
		resta11=int(table[8][2])-int(2)
		resta12=int(table[8][3])-int(2)
        

        t1=rdMolTransforms.GetDihedralDeg(c, resta1,resta2,resta3,resta4)
        print(t1)
        t2=rdMolTransforms.GetDihedralDeg(c, resta5,resta6,resta7,resta8)
        print(t2)
        t3=rdMolTransforms.GetDihedralDeg(c, resta9,resta10,resta11,resta12)
        print(t3)
        os.mkdir(scandir+n[:-4]+'_1')
        savedir=scandir+n[:-4]+"_1/"
        name=open(indir+'corrected_dihedral_basal/'+n[:-3]+'dat', 'r')
        table2 = [line.rstrip().split("-") for line in name.readlines()]
        
        for i in range(0,360,15):
            impose=open(indir+'impose.leap','w')
            os.system('babel '+xyzindir+n+' '+indir+n[:-3]+'mol2')
            os.system('antechamber -i '+indir+n[:-3]+'mol2 -fi mol2 -o '+indir+'cambio.mol2 -fo mol2')
            #os.system('cd '+indir+' && parmchk -i cambio.mol2 -f mol2 -o frcmod.frcmod -a Y -s 2')
            #impose.write('loadamberparams '+'frcmod.frcmod'+'\n')
            impose.write('LIG = loadmol2 '+'cambio.mol2'+'\n')
            #impose.write('check LIG'+'\n')
            cmd='impose LIG {1}, {{"'+str(table2[0][0])+'" "'+str(table2[0][1])+'" "'+str(table2[0][2])+'" "'+str(table2[0][3])+'" '+str(i)+'.0000'+'}}'
            impose.write(cmd+'\n')
            impose.write('savemol2 LIG LIG.mol2 0'+'\n')
            impose.write('quit'+'\n')
            impose.close()
            os.system('cd '+indir+' && tleap -f impose.leap')
            os.system('babel '+indir+'LIG.mol2 '+indir+'LIG.xyz')
            
            
            
            write=open(savedir+n[:-4]+"_"+str(i)+".qcin","w")
            if i>180:
                i=i-360
            header_basal=open(indir+'qchem.header_scan_basal', 'w')
            header_basal.write('$comment'+'\n')
            header_basal.write('   OPTIMIZATION'+'\n')
            header_basal.write('$end'+'\n')
            header_basal.write('\n')
            header_basal.write('$rem'+'\n')
            header_basal.write('   JOBTYPE OPT'+'\n')
            header_basal.write('   EXCHANGE omegaB97X-D'+'\n')
            header_basal.write('   BASIS cc-pVTZ'+'\n')
            header_basal.write('$end'+'\n')
            header_basal.write('\n')
            header_basal.write('$molecule'+'\n')
            header_basal.write('   0 1'+'\n')
            header_basal.close()
            footer_basal=open(indir+'qchem.footer_scan_basal', 'w')
            footer_basal.write('$end'+'\n')
            footer_basal.write('\n')
            footer_basal.write('$opt'+'\n')
            footer_basal.write('CONSTRAINT'+'\n')
            footer_basal.write('tors '+str(int(table[0][0]))+' '+str(int(table[0][1]))+' '+str(int(table[0][2]))+' '+str(int(table[0][3]))+' '+str(int(i))+'.00000'+'\n')           
            footer_basal.write('tors '+str(int(table[4][0]))+' '+str(int(table[4][1]))+' '+str(int(table[4][2]))+' '+str(int(table[4][3]))+' '+str(round(float(t2), 5))+'\n')         
            footer_basal.write('tors '+str(int(table[8][0]))+' '+str(int(table[8][1]))+' '+str(int(table[8][2]))+' '+str(int(table[8][3]))+' '+str(round(float(t3), 5))+'\n')            
            footer_basal.write('ENDCONSTRAINT'+'\n')
            footer_basal.write('$end'+'\n')
            footer_basal.close()
            head=open(indir+'qchem.header_scan_basal','r')
            for line in head:
                write.write(line)
            read=open(indir+'LIG.xyz','r')
            number=len(read.readline())
            for line2 in read:
                if ("Geometry") in line2:
                    continue
                write.write(line2)
            foot=open(indir+'qchem.footer_scan_basal','r')
            for line3 in foot:
                write.write(line3)
            write.close()
            os.system('cd '+indir+' && rm cambio.mol2 impose.leap LIG.xyz LIG.mol2')
            
        os.mkdir(scandir+n[:-4]+'_2')
        savedir=scandir+n[:-4]+"_2/"
        for i in range(0,360,15):
            impose=open(indir+'impose.leap','w')
            os.system('babel '+xyzindir+n+' '+indir+n[:-3]+'mol2')
            os.system('antechamber -i '+indir+n[:-3]+'mol2 -fi mol2 -o '+indir+'cambio.mol2 -fo mol2')
            #os.system('cd '+indir+' && parmchk -i cambio.mol2 -f mol2 -o frcmod.frcmod -a Y -s 2')
            #impose.write('loadamberparams '+'frcmod.frcmod'+'\n')
            impose.write('LIG = loadmol2 '+'cambio.mol2'+'\n')
            #impose.write('check LIG'+'\n')
            cmd='impose LIG {1}, {{"'+str(table2[4][0])+'" "'+str(table2[4][1])+'" "'+str(table2[4][2])+'" "'+str(table2[4][3])+'" '+str(i)+'.0000'+'}}'
            impose.write(cmd+'\n')
            impose.write('savemol2 LIG LIG.mol2 0'+'\n')
            impose.write('quit'+'\n')
            impose.close()
            os.system('cd '+indir+' && tleap -f impose.leap')
            os.system('babel '+indir+'LIG.mol2 '+indir+'LIG.xyz')

            
            
            
            write=open(savedir+n[:-4]+"_"+str(i)+".qcin","w")
            if i>180:
                i=i-360
            header_basal=open(indir+'qchem.header_scan_basal', 'w')
            header_basal.write('$comment'+'\n')
            header_basal.write('   OPTIMIZATION'+'\n')
            header_basal.write('$end'+'\n')
            header_basal.write('\n')
            header_basal.write('$rem'+'\n')
            header_basal.write('   JOBTYPE OPT'+'\n')
            header_basal.write('   EXCHANGE omegaB97X-D'+'\n')
            header_basal.write('   BASIS cc-pVTZ'+'\n')
            header_basal.write('   MEM_STATIC 5000'+'\n') 
            header_basal.write('   MEM_TOTAL 20000'+'\n')
            header_basal.write('$end'+'\n')
            header_basal.write('\n')
            header_basal.write('$molecule'+'\n')
            header_basal.write('   0 1'+'\n')
            header_basal.close()
            footer_basal=open(indir+'qchem.footer_scan_basal', 'w')
            footer_basal.write('$end'+'\n')
            footer_basal.write('\n')
            footer_basal.write('$opt'+'\n')
            footer_basal.write('CONSTRAINT'+'\n')
            footer_basal.write('tors '+str(int(table[0][0]))+' '+str(int(table[0][1]))+' '+str(int(table[0][2]))+' '+str(int(table[0][3]))+' '+str(round(float(t1), 5))+'\n')           
            footer_basal.write('tors '+str(int(table[4][0]))+' '+str(int(table[4][1]))+' '+str(int(table[4][2]))+' '+str(int(table[4][3]))+' '+str(int(i))+'.00000'+'\n')         
            footer_basal.write('tors '+str(int(table[8][0]))+' '+str(int(table[8][1]))+' '+str(int(table[8][2]))+' '+str(int(table[8][3]))+' '+str(round(float(t3), 5))+'\n')            
            footer_basal.write('ENDCONSTRAINT'+'\n')
            footer_basal.write('$end'+'\n')
            footer_basal.close()
            head=open(indir+'qchem.header_scan_basal','r')
            for line in head:
                write.write(line)
            read=open(indir+'LIG.xyz','r')
            number=len(read.readline())
            for line2 in read:
                if ("Geometry") in line2:
                    continue
                write.write(line2)
            foot=open(indir+'qchem.footer_scan_basal','r')
            for line3 in foot:
                write.write(line3)
            
            write.close()
            os.system('cd '+indir+' && rm cambio.mol2 impose.leap LIG.xyz LIG.mol2')
            
        os.mkdir(scandir+n[:-4]+'_3')
        savedir=scandir+n[:-4]+"_3/"
        for i in range(0,360,15):
            impose=open(indir+'impose.leap','w')
            os.system('babel '+xyzindir+n+' '+indir+n[:-3]+'mol2')
            os.system('antechamber -i '+indir+n[:-3]+'mol2 -fi mol2 -o '+indir+'cambio.mol2 -fo mol2')
            #os.system('cd '+indir+' && parmchk -i cambio.mol2 -f mol2 -o frcmod.frcmod -a Y -s 2')
            #impose.write('loadamberparams '+'frcmod.frcmod'+'\n')
            impose.write('LIG = loadmol2 '+'cambio.mol2'+'\n')
            #impose.write('check LIG'+'\n')
            cmd='impose LIG {1}, {{"'+str(table2[8][0])+'" "'+str(table2[8][1])+'" "'+str(table2[8][2])+'" "'+str(table2[8][3])+'" '+str(i)+'.0000'+'}}'
            impose.write(cmd+'\n')
            impose.write('savemol2 LIG LIG.mol2 0'+'\n')
            impose.write('quit'+'\n')
            impose.close()
            os.system('cd '+indir+' && tleap -f impose.leap')
            os.system('babel '+indir+'LIG.mol2 '+indir+'LIG.xyz')

            write=open(savedir+n[:-4]+"_"+str(i)+".qcin","w")
            if i>180:
                i=i-360
            header_basal=open(indir+'qchem.header_scan_basal', 'w')
            header_basal.write('$comment'+'\n')
            header_basal.write('   OPTIMIZATION'+'\n')
            header_basal.write('$end'+'\n')
            header_basal.write('\n')
            header_basal.write('$rem'+'\n')
            header_basal.write('   JOBTYPE OPT'+'\n')
            header_basal.write('   EXCHANGE omegaB97X-D'+'\n')
            header_basal.write('   BASIS cc-pVTZ'+'\n')
            header_basal.write('$end'+'\n')
            header_basal.write('\n')
            header_basal.write('$molecule'+'\n')
            header_basal.write('   0 1'+'\n')
            header_basal.close()
            footer_basal=open(indir+'qchem.footer_scan_basal', 'w')
            footer_basal.write('$end'+'\n')
            footer_basal.write('\n')
            footer_basal.write('$opt'+'\n')
            footer_basal.write('CONSTRAINT'+'\n')
            footer_basal.write('tors '+str(int(table[0][0]))+' '+str(int(table[0][1]))+' '+str(int(table[0][2]))+' '+str(int(table[0][3]))+' '+str(round(float(t1), 5))+'\n')           
            footer_basal.write('tors '+str(int(table[4][0]))+' '+str(int(table[4][1]))+' '+str(int(table[4][2]))+' '+str(int(table[4][3]))+' '+str(round(float(t2), 5))+'\n')         
            footer_basal.write('tors '+str(int(table[8][0]))+' '+str(int(table[8][1]))+' '+str(int(table[8][2]))+' '+str(int(table[8][3]))+' '+str(int(i))+'.00000'+'\n')            
            footer_basal.write('ENDCONSTRAINT'+'\n')
            footer_basal.write('$end'+'\n')
            footer_basal.close()
            head=open(indir+'qchem.header_scan_basal','r')
            for line in head:
                write.write(line)
            read=open(indir+'LIG.xyz','r')
            number=len(read.readline())
            for line2 in read:
                if ("Geometry") in line2:
                    continue
                write.write(line2)
            foot=open(indir+'qchem.footer_scan_basal','r')
            for line3 in foot:
                write.write(line3)
            
            write.close()
            os.system('cd '+indir+' && rm cambio.mol2 impose.leap LIG.xyz LIG.mol2 '+n[:-3]+'mol2')
os.system('cd '+indir+' && rm qchem.footer_scan_basal qchem.header_scan_basal')
