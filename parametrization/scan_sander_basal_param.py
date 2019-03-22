from __future__ import print_function
from rdkit import Chem
from rdkit.Chem.AtomPairs import Torsions
from rdkit import Chem
from rdkit.Chem import AllChem, rdMolTransforms
import os
import shutil
  

if os.path.exists("scan_sander_basal_param"):
    shutil.rmtree("scan_sander_basal_param")
    os.mkdir("scan_sander_basal_param")
else:
    os.mkdir("scan_sander_basal_param")

xyzindir='min_basal_xyz/'
moldir='min_basal_mol/'
dihedir='numbering_dihedral_basal/'

for root, dirs, filenames in os.walk(xyzindir):
       for n in filenames:
        print(n)
        os.system('babel '+xyzindir+n+' '+moldir+n[:-4]+'.mol')
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
        
        resta13=int(table[1][0])-int(1)
        resta14=int(table[1][1])-int(1)
        resta15=int(table[1][2])-int(1)
        resta16=int(table[1][3])-int(1)
        resta17=int(table[5][0])-int(1)
        resta18=int(table[5][1])-int(1)
        resta19=int(table[5][2])-int(1)
        resta20=int(table[5][3])-int(1)
        resta21=int(table[9][0])-int(1)
        resta22=int(table[9][1])-int(1)
        resta23=int(table[9][2])-int(1)
        resta24=int(table[9][3])-int(1)
        
        resta25=int(table[2][0])-int(1)
        resta26=int(table[2][1])-int(1)
        resta27=int(table[2][2])-int(1)
        resta28=int(table[2][3])-int(1)
        resta29=int(table[6][0])-int(1)
        resta30=int(table[6][1])-int(1)
        resta31=int(table[6][2])-int(1)
        resta32=int(table[6][3])-int(1)
        resta33=int(table[10][0])-int(1)
        resta34=int(table[10][1])-int(1)
        resta35=int(table[10][2])-int(1)
        resta36=int(table[10][3])-int(1)

        resta37=int(table[3][0])-int(1)
        resta38=int(table[3][1])-int(1)
        resta39=int(table[3][2])-int(1)
        resta40=int(table[3][3])-int(1)
        resta41=int(table[7][0])-int(1)
        resta42=int(table[7][1])-int(1)
        resta43=int(table[7][2])-int(1)
        resta44=int(table[7][3])-int(1)
        resta45=int(table[11][0])-int(1)
        resta46=int(table[11][1])-int(1)
        resta47=int(table[11][2])-int(1)
        resta48=int(table[11][3])-int(1)
        
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
            
            resta13=int(table[1][0])-int(2)
            resta14=int(table[1][1])-int(2)
            resta15=int(table[1][2])-int(2)
            resta16=int(table[1][3])-int(2)
            resta17=int(table[5][0])-int(2)
            resta18=int(table[5][1])-int(2)
            resta19=int(table[5][2])-int(2)
            resta20=int(table[5][3])-int(2)
            resta21=int(table[9][0])-int(2)
            resta22=int(table[9][1])-int(2)
            resta23=int(table[9][2])-int(2)
            resta24=int(table[9][3])-int(2)
        
            resta25=int(table[2][0])-int(2)
            resta26=int(table[2][1])-int(2)
            resta27=int(table[2][2])-int(2)
            resta28=int(table[2][3])-int(2)
            resta29=int(table[6][0])-int(2)
            resta30=int(table[6][1])-int(2)
            resta31=int(table[6][2])-int(2)
            resta32=int(table[6][3])-int(2)
            resta33=int(table[10][0])-int(2)
            resta34=int(table[10][1])-int(2)
            resta35=int(table[10][2])-int(2)
            resta36=int(table[10][3])-int(2)

            resta37=int(table[3][0])-int(2)
            resta38=int(table[3][1])-int(2)
            resta39=int(table[3][2])-int(2)
            resta40=int(table[3][3])-int(2)
            resta41=int(table[7][0])-int(2)
            resta42=int(table[7][1])-int(2)
            resta43=int(table[7][2])-int(2)
            resta44=int(table[7][3])-int(2)
            resta45=int(table[11][0])-int(2)
            resta46=int(table[11][1])-int(2)
            resta47=int(table[11][2])-int(2)
            resta48=int(table[11][3])-int(2)
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
            
            resta13=int(table[1][0])-int(2)
            resta14=int(table[1][1])-int(2)
            resta15=int(table[1][2])-int(2)
            resta16=int(table[1][3])-int(2)
            resta17=int(table[5][0])-int(2)
            resta18=int(table[5][1])-int(2)
            resta19=int(table[5][2])-int(2)
            resta20=int(table[5][3])-int(2)
            resta21=int(table[9][0])-int(2)
            resta22=int(table[9][1])-int(2)
            resta23=int(table[9][2])-int(2)
            resta24=int(table[9][3])-int(2)
        
            resta25=int(table[2][0])-int(2)
            resta26=int(table[2][1])-int(2)
            resta27=int(table[2][2])-int(2)
            resta28=int(table[2][3])-int(2)
            resta29=int(table[6][0])-int(2)
            resta30=int(table[6][1])-int(2)
            resta31=int(table[6][2])-int(2)
            resta32=int(table[6][3])-int(2)
            resta33=int(table[10][0])-int(2)
            resta34=int(table[10][1])-int(2)
            resta35=int(table[10][2])-int(2)
            resta36=int(table[10][3])-int(2)

            resta37=int(table[3][0])-int(2)
            resta38=int(table[3][1])-int(2)
            resta39=int(table[3][2])-int(2)
            resta40=int(table[3][3])-int(2)
            resta41=int(table[7][0])-int(2)
            resta42=int(table[7][1])-int(2)
            resta43=int(table[7][2])-int(2)
            resta44=int(table[7][3])-int(2)
            resta45=int(table[11][0])-int(2)
            resta46=int(table[11][1])-int(2)
            resta47=int(table[11][2])-int(2)
            resta48=int(table[11][3])-int(2)

        t1=round(rdMolTransforms.GetDihedralDeg(c, resta1,resta2,resta3,resta4),2)
        if 180<=t1<=360:
            a=t1
            print(a)
        if 0<=t1<=180:
            a=t1
            print(a)
        if  t1<0:
            a=t1+360
            print(a)
        t2=round(rdMolTransforms.GetDihedralDeg(c, resta5,resta6,resta7,resta8),2)
        if 180<=t2<=360:
            b=t2
            print(b)
        if 0<=t2<=180:
            b=t2
            print(b)
        if t2<0:
            b=t2+360
            print(b)
        t3=round(rdMolTransforms.GetDihedralDeg(c, resta9,resta10,resta11,resta12),2)
        if 180<=t3<=360:
            z=t3
            print(z)
        if 0<=t3<=180:
            z=t3
            print(z)
        if t3<0:
            z=t3+360
            print(z)
        #####
        t4=round(rdMolTransforms.GetDihedralDeg(c, resta13,resta14,resta15,resta16),2)
        if 180<=t4<=360:
            d=t4
            print(d)
        if 0<=t4<=180:
            d=t4
            print(d)
        if  t4<0:
            d=t4+360
            print(d)
        t5=round(rdMolTransforms.GetDihedralDeg(c, resta17,resta18,resta19,resta20),2)
        if 180<=t5<=360:
            e=t5
            print(e)
        if 0<=t5<=180:
            e=t5
            print(e)
        if t5<0:
            e=t5+360
            print(e)
        t6=round(rdMolTransforms.GetDihedralDeg(c, resta21,resta22,resta23,resta24),2)
        if 180<=t6<=360:
            f=t6
            print(f)
        if 0<=t6<=180:
            f=t6
            print(f)
        if t6<0:
            f=t6+360
            print(f)
        ###
        t7=round(rdMolTransforms.GetDihedralDeg(c, resta25,resta26,resta27,resta28),2)
        if 180<=t7<=360:
            g=t7
            print(g)
        if 0<=t7<=180:
            g=t7
            print(g)
        if  t7<0:
            g=t7+360
            print(g)
        t8=round(rdMolTransforms.GetDihedralDeg(c, resta29,resta30,resta31,resta32),2)
        if 180<=t8<=360:
            h=t8
            print(h)
        if 0<=t8<=180:
            h=t8
            print(h)
        if t8<0:
            h=t8+360
            print(h)
        t9=round(rdMolTransforms.GetDihedralDeg(c, resta33,resta34,resta35,resta36),2)
        if 180<=t9<=360:
            l=t9
            print(l)
        if 0<=t9<=180:
            l=t9
            print(l)
        if t9<0:
            l=t9+360
            print(l)
        
        ####
        t10=round(rdMolTransforms.GetDihedralDeg(c, resta37,resta38,resta39,resta40),2)
        if 180<=t10<=360:
            x=t10
            print(x)
        if 0<=t10<=180:
            x=t10
            print(x)
        if  t10<0:
            x=t10+360
            print(x)
        t11=round(rdMolTransforms.GetDihedralDeg(c, resta41,resta42,resta43,resta44),2)
        if 180<=t11<=360:
            y=t11
            print(y)
        if 0<=t11<=180:
            y=t11
            print(y)
        if t11<0:
            y=t11+360
            print(y)
        t12=round(rdMolTransforms.GetDihedralDeg(c, resta45,resta46,resta47,resta48),2)
        if 180<=t12<=360:
            o=t12
            print(o)
        if 0<=t12<=180:
            o=t12
            print(o)
        if t12<0:
            o=t12+360
            print(o)
        ####


        #### scan dihedrals
        rootname=n[:-4]
        print(rootname)
        
        cmd='cd ./ '+'&& '+'sh sander_angle_1_param.sh '+str(int(resta1)+int(1))+' '+str(int(resta2)+int(1))+' '+str(int(resta3)+int(1))+' '+str(int(resta4)+int(1))+' '+str(int(resta5)+int(1))+' '+str(int(resta6)+int(1))+' '+str(int(resta7)+int(1))+' '+str(int(resta8)+int(1))+' '+str(int(resta9)+int(1))+' '+str(int(resta10)+int(1))+' '+str(int(resta11)+int(1))+' '+str(int(resta12)+int(1))+' '+str(int(resta13)+int(1))+' '+str(int(resta14)+int(1))+' '+str(int(resta15)+int(1))+' '+str(int(resta16)+int(1))+' '+str(int(resta17)+int(1))+' '+str(int(resta18)+int(1))+' '+str(int(resta19)+int(1))+' '+str(int(resta20)+int(1))+' '+str(int(resta21)+int(1))+' '+str(int(resta22)+int(1))+' '+str(int(resta23)+int(1))+' '+str(int(resta24)+int(1))+' '+str(int(resta25)+int(1))+' '+str(int(resta26)+int(1))+' '+str(int(resta27)+int(1))+' '+str(int(resta28)+int(1))+' '+str(int(resta29)+int(1))+' '+str(int(resta30)+int(1))+' '+str(int(resta31)+int(1))+' '+str(int(resta32)+int(1))+' '+str(int(resta33)+int(1))+' '+str(int(resta34)+int(1))+' '+str(int(resta35)+int(1))+' '+str(int(resta36)+int(1))+' '+str(int(resta37)+int(1))+' '+str(int(resta38)+int(1))+' '+str(int(resta39)+int(1))+' '+str(int(resta40)+int(1))+' '+str(int(resta41)+int(1))+' '+str(int(resta42)+int(1))+' '+str(int(resta43)+int(1))+' '+str(int(resta44)+int(1))+' '+str(int(resta45)+int(1))+' '+str(int(resta46)+int(1))+' '+str(int(resta47)+int(1))+' '+str(int(resta48)+int(1))+' '+rootname+' '+str(b)+' '+str(z)+' '+str(e)+' '+str(f)+' '+str(h)+' '+str(l)+' '+str(y)+' '+str(o)
        os.system(cmd)
        print(cmd)
        cmd2='cd ./ '+'&& '+'sh sander_angle_2_param.sh '+str(int(resta1)+int(1))+' '+str(int(resta2)+int(1))+' '+str(int(resta3)+int(1))+' '+str(int(resta4)+int(1))+' '+str(int(resta5)+int(1))+' '+str(int(resta6)+int(1))+' '+str(int(resta7)+int(1))+' '+str(int(resta8)+int(1))+' '+str(int(resta9)+int(1))+' '+str(int(resta10)+int(1))+' '+str(int(resta11)+int(1))+' '+str(int(resta12)+int(1))+' '+str(int(resta13)+int(1))+' '+str(int(resta14)+int(1))+' '+str(int(resta15)+int(1))+' '+str(int(resta16)+int(1))+' '+str(int(resta17)+int(1))+' '+str(int(resta18)+int(1))+' '+str(int(resta19)+int(1))+' '+str(int(resta20)+int(1))+' '+str(int(resta21)+int(1))+' '+str(int(resta22)+int(1))+' '+str(int(resta23)+int(1))+' '+str(int(resta24)+int(1))+' '+str(int(resta25)+int(1))+' '+str(int(resta26)+int(1))+' '+str(int(resta27)+int(1))+' '+str(int(resta28)+int(1))+' '+str(int(resta29)+int(1))+' '+str(int(resta30)+int(1))+' '+str(int(resta31)+int(1))+' '+str(int(resta32)+int(1))+' '+str(int(resta33)+int(1))+' '+str(int(resta34)+int(1))+' '+str(int(resta35)+int(1))+' '+str(int(resta36)+int(1))+' '+str(int(resta37)+int(1))+' '+str(int(resta38)+int(1))+' '+str(int(resta39)+int(1))+' '+str(int(resta40)+int(1))+' '+str(int(resta41)+int(1))+' '+str(int(resta42)+int(1))+' '+str(int(resta43)+int(1))+' '+str(int(resta44)+int(1))+' '+str(int(resta45)+int(1))+' '+str(int(resta46)+int(1))+' '+str(int(resta47)+int(1))+' '+str(int(resta48)+int(1))+' '+rootname+' '+str(a)+' '+str(z)+' '+str(d)+' '+str(f)+' '+str(g)+' '+str(l)+' '+str(x)+' '+str(o)
        os.system(cmd2)
        cmd3='cd ./ '+'&& '+'sh sander_angle_3_param.sh '+str(int(resta1)+int(1))+' '+str(int(resta2)+int(1))+' '+str(int(resta3)+int(1))+' '+str(int(resta4)+int(1))+' '+str(int(resta5)+int(1))+' '+str(int(resta6)+int(1))+' '+str(int(resta7)+int(1))+' '+str(int(resta8)+int(1))+' '+str(int(resta9)+int(1))+' '+str(int(resta10)+int(1))+' '+str(int(resta11)+int(1))+' '+str(int(resta12)+int(1))+' '+str(int(resta13)+int(1))+' '+str(int(resta14)+int(1))+' '+str(int(resta15)+int(1))+' '+str(int(resta16)+int(1))+' '+str(int(resta17)+int(1))+' '+str(int(resta18)+int(1))+' '+str(int(resta19)+int(1))+' '+str(int(resta20)+int(1))+' '+str(int(resta21)+int(1))+' '+str(int(resta22)+int(1))+' '+str(int(resta23)+int(1))+' '+str(int(resta24)+int(1))+' '+str(int(resta25)+int(1))+' '+str(int(resta26)+int(1))+' '+str(int(resta27)+int(1))+' '+str(int(resta28)+int(1))+' '+str(int(resta29)+int(1))+' '+str(int(resta30)+int(1))+' '+str(int(resta31)+int(1))+' '+str(int(resta32)+int(1))+' '+str(int(resta33)+int(1))+' '+str(int(resta34)+int(1))+' '+str(int(resta35)+int(1))+' '+str(int(resta36)+int(1))+' '+str(int(resta37)+int(1))+' '+str(int(resta38)+int(1))+' '+str(int(resta39)+int(1))+' '+str(int(resta40)+int(1))+' '+str(int(resta41)+int(1))+' '+str(int(resta42)+int(1))+' '+str(int(resta43)+int(1))+' '+str(int(resta44)+int(1))+' '+str(int(resta45)+int(1))+' '+str(int(resta46)+int(1))+' '+str(int(resta47)+int(1))+' '+str(int(resta48)+int(1))+' '+rootname+' '+str(b)+' '+str(a)+' '+str(e)+' '+str(d)+' '+str(h)+' '+str(g)+' '+str(y)+' '+str(x)
        os.system(cmd3)
        if n=='C342.xyz':
            cmd='cd ./ '+'&& '+'sh sander_angle_1_param.sh '+str(int(resta1)+int(2))+' '+str(int(resta2)+int(2))+' '+str(int(resta3)+int(2))+' '+str(int(resta4)+int(2))+' '+str(int(resta5)+int(2))+' '+str(int(resta6)+int(2))+' '+str(int(resta7)+int(2))+' '+str(int(resta8)+int(2))+' '+str(int(resta9)+int(2))+' '+str(int(resta10)+int(2))+' '+str(int(resta11)+int(2))+' '+str(int(resta12)+int(2))+' '+str(int(resta13)+int(2))+' '+str(int(resta14)+int(2))+' '+str(int(resta15)+int(2))+' '+str(int(resta16)+int(2))+' '+str(int(resta17)+int(2))+' '+str(int(resta18)+int(2))+' '+str(int(resta19)+int(2))+' '+str(int(resta20)+int(2))+' '+str(int(resta21)+int(2))+' '+str(int(resta22)+int(2))+' '+str(int(resta23)+int(2))+' '+str(int(resta24)+int(2))+' '+str(int(resta25)+int(2))+' '+str(int(resta26)+int(2))+' '+str(int(resta27)+int(2))+' '+str(int(resta28)+int(2))+' '+str(int(resta29)+int(2))+' '+str(int(resta30)+int(2))+' '+str(int(resta31)+int(2))+' '+str(int(resta32)+int(2))+' '+str(int(resta33)+int(2))+' '+str(int(resta34)+int(2))+' '+str(int(resta35)+int(2))+' '+str(int(resta36)+int(2))+' '+str(int(resta37)+int(2))+' '+str(int(resta38)+int(2))+' '+str(int(resta39)+int(2))+' '+str(int(resta40)+int(2))+' '+str(int(resta41)+int(2))+' '+str(int(resta42)+int(2))+' '+str(int(resta43)+int(2))+' '+str(int(resta44)+int(2))+' '+str(int(resta45)+int(2))+' '+str(int(resta46)+int(2))+' '+str(int(resta47)+int(2))+' '+str(int(resta48)+int(2))+' '+rootname+' '+str(b)+' '+str(z)+' '+str(e)+' '+str(f)+' '+str(h)+' '+str(l)+' '+str(y)+' '+str(o)
            os.system(cmd)
            cmd2='cd ./ '+'&& '+'sh sander_angle_2_param.sh '+str(int(resta1)+int(2))+' '+str(int(resta2)+int(2))+' '+str(int(resta3)+int(2))+' '+str(int(resta4)+int(2))+' '+str(int(resta5)+int(2))+' '+str(int(resta6)+int(2))+' '+str(int(resta7)+int(2))+' '+str(int(resta8)+int(2))+' '+str(int(resta9)+int(2))+' '+str(int(resta10)+int(2))+' '+str(int(resta11)+int(2))+' '+str(int(resta12)+int(2))+' '+str(int(resta13)+int(2))+' '+str(int(resta14)+int(2))+' '+str(int(resta15)+int(2))+' '+str(int(resta16)+int(2))+' '+str(int(resta17)+int(2))+' '+str(int(resta18)+int(2))+' '+str(int(resta19)+int(2))+' '+str(int(resta20)+int(2))+' '+str(int(resta21)+int(2))+' '+str(int(resta22)+int(2))+' '+str(int(resta23)+int(2))+' '+str(int(resta24)+int(2))+' '+str(int(resta25)+int(2))+' '+str(int(resta26)+int(2))+' '+str(int(resta27)+int(2))+' '+str(int(resta28)+int(2))+' '+str(int(resta29)+int(2))+' '+str(int(resta30)+int(2))+' '+str(int(resta31)+int(2))+' '+str(int(resta32)+int(2))+' '+str(int(resta33)+int(2))+' '+str(int(resta34)+int(2))+' '+str(int(resta35)+int(2))+' '+str(int(resta36)+int(2))+' '+str(int(resta37)+int(2))+' '+str(int(resta38)+int(2))+' '+str(int(resta39)+int(2))+' '+str(int(resta40)+int(2))+' '+str(int(resta41)+int(2))+' '+str(int(resta42)+int(2))+' '+str(int(resta43)+int(2))+' '+str(int(resta44)+int(2))+' '+str(int(resta45)+int(2))+' '+str(int(resta46)+int(2))+' '+str(int(resta47)+int(2))+' '+str(int(resta48)+int(2))+' '+rootname+' '+str(a)+' '+str(z)+' '+str(d)+' '+str(f)+' '+str(g)+' '+str(l)+' '+str(x)+' '+str(o)
            os.system(cmd2)
            cmd3='cd ./ '+'&& '+'sh sander_angle_3_param.sh '+str(int(resta1)+int(2))+' '+str(int(resta2)+int(2))+' '+str(int(resta3)+int(2))+' '+str(int(resta4)+int(2))+' '+str(int(resta5)+int(2))+' '+str(int(resta6)+int(2))+' '+str(int(resta7)+int(2))+' '+str(int(resta8)+int(2))+' '+str(int(resta9)+int(2))+' '+str(int(resta10)+int(2))+' '+str(int(resta11)+int(2))+' '+str(int(resta12)+int(2))+' '+str(int(resta13)+int(2))+' '+str(int(resta14)+int(2))+' '+str(int(resta15)+int(2))+' '+str(int(resta16)+int(2))+' '+str(int(resta17)+int(2))+' '+str(int(resta18)+int(2))+' '+str(int(resta19)+int(2))+' '+str(int(resta20)+int(2))+' '+str(int(resta21)+int(2))+' '+str(int(resta22)+int(2))+' '+str(int(resta23)+int(2))+' '+str(int(resta24)+int(2))+' '+str(int(resta25)+int(2))+' '+str(int(resta26)+int(2))+' '+str(int(resta27)+int(2))+' '+str(int(resta28)+int(2))+' '+str(int(resta29)+int(2))+' '+str(int(resta30)+int(2))+' '+str(int(resta31)+int(2))+' '+str(int(resta32)+int(2))+' '+str(int(resta33)+int(2))+' '+str(int(resta34)+int(2))+' '+str(int(resta35)+int(2))+' '+str(int(resta36)+int(2))+' '+str(int(resta37)+int(2))+' '+str(int(resta38)+int(2))+' '+str(int(resta39)+int(2))+' '+str(int(resta40)+int(2))+' '+str(int(resta41)+int(2))+' '+str(int(resta42)+int(2))+' '+str(int(resta43)+int(2))+' '+str(int(resta44)+int(2))+' '+str(int(resta45)+int(2))+' '+str(int(resta46)+int(2))+' '+str(int(resta47)+int(2))+' '+str(int(resta48)+int(2))+' '+rootname+' '+str(b)+' '+str(a)+' '+str(e)+' '+str(d)+' '+str(h)+' '+str(g)+' '+str(y)+' '+str(x)
            os.system(cmd3)
        if n=='C385.xyz':
            cmd='cd ./ '+'&& '+'sh sander_angle_1_param.sh '+str(int(resta1)+int(2))+' '+str(int(resta2)+int(2))+' '+str(int(resta3)+int(2))+' '+str(int(resta4)+int(2))+' '+str(int(resta5)+int(2))+' '+str(int(resta6)+int(2))+' '+str(int(resta7)+int(2))+' '+str(int(resta8)+int(2))+' '+str(int(resta9)+int(2))+' '+str(int(resta10)+int(2))+' '+str(int(resta11)+int(2))+' '+str(int(resta12)+int(2))+' '+str(int(resta13)+int(2))+' '+str(int(resta14)+int(2))+' '+str(int(resta15)+int(2))+' '+str(int(resta16)+int(2))+' '+str(int(resta17)+int(2))+' '+str(int(resta18)+int(2))+' '+str(int(resta19)+int(2))+' '+str(int(resta20)+int(2))+' '+str(int(resta21)+int(2))+' '+str(int(resta22)+int(2))+' '+str(int(resta23)+int(2))+' '+str(int(resta24)+int(2))+' '+str(int(resta25)+int(2))+' '+str(int(resta26)+int(2))+' '+str(int(resta27)+int(2))+' '+str(int(resta28)+int(2))+' '+str(int(resta29)+int(2))+' '+str(int(resta30)+int(2))+' '+str(int(resta31)+int(2))+' '+str(int(resta32)+int(2))+' '+str(int(resta33)+int(2))+' '+str(int(resta34)+int(2))+' '+str(int(resta35)+int(2))+' '+str(int(resta36)+int(2))+' '+str(int(resta37)+int(2))+' '+str(int(resta38)+int(2))+' '+str(int(resta39)+int(2))+' '+str(int(resta40)+int(2))+' '+str(int(resta41)+int(2))+' '+str(int(resta42)+int(2))+' '+str(int(resta43)+int(2))+' '+str(int(resta44)+int(2))+' '+str(int(resta45)+int(2))+' '+str(int(resta46)+int(2))+' '+str(int(resta47)+int(2))+' '+str(int(resta48)+int(2))+' '+rootname+' '+str(b)+' '+str(z)+' '+str(e)+' '+str(f)+' '+str(h)+' '+str(l)+' '+str(y)+' '+str(o)
            os.system(cmd)
            cmd2='cd ./ '+'&& '+'sh sander_angle_2_param.sh '+str(int(resta1)+int(2))+' '+str(int(resta2)+int(2))+' '+str(int(resta3)+int(2))+' '+str(int(resta4)+int(2))+' '+str(int(resta5)+int(2))+' '+str(int(resta6)+int(2))+' '+str(int(resta7)+int(2))+' '+str(int(resta8)+int(2))+' '+str(int(resta9)+int(2))+' '+str(int(resta10)+int(2))+' '+str(int(resta11)+int(2))+' '+str(int(resta12)+int(2))+' '+str(int(resta13)+int(2))+' '+str(int(resta14)+int(2))+' '+str(int(resta15)+int(2))+' '+str(int(resta16)+int(2))+' '+str(int(resta17)+int(2))+' '+str(int(resta18)+int(2))+' '+str(int(resta19)+int(2))+' '+str(int(resta20)+int(2))+' '+str(int(resta21)+int(2))+' '+str(int(resta22)+int(2))+' '+str(int(resta23)+int(2))+' '+str(int(resta24)+int(2))+' '+str(int(resta25)+int(2))+' '+str(int(resta26)+int(2))+' '+str(int(resta27)+int(2))+' '+str(int(resta28)+int(2))+' '+str(int(resta29)+int(2))+' '+str(int(resta30)+int(2))+' '+str(int(resta31)+int(2))+' '+str(int(resta32)+int(2))+' '+str(int(resta33)+int(2))+' '+str(int(resta34)+int(2))+' '+str(int(resta35)+int(2))+' '+str(int(resta36)+int(2))+' '+str(int(resta37)+int(2))+' '+str(int(resta38)+int(2))+' '+str(int(resta39)+int(2))+' '+str(int(resta40)+int(2))+' '+str(int(resta41)+int(2))+' '+str(int(resta42)+int(2))+' '+str(int(resta43)+int(2))+' '+str(int(resta44)+int(2))+' '+str(int(resta45)+int(2))+' '+str(int(resta46)+int(2))+' '+str(int(resta47)+int(2))+' '+str(int(resta48)+int(2))+' '+rootname+' '+str(a)+' '+str(z)+' '+str(d)+' '+str(f)+' '+str(g)+' '+str(l)+' '+str(x)+' '+str(o)
            os.system(cmd2)
            cmd3='cd ./ '+'&& '+'sh sander_angle_3_param.sh '+str(int(resta1)+int(2))+' '+str(int(resta2)+int(2))+' '+str(int(resta3)+int(2))+' '+str(int(resta4)+int(2))+' '+str(int(resta5)+int(2))+' '+str(int(resta6)+int(2))+' '+str(int(resta7)+int(2))+' '+str(int(resta8)+int(2))+' '+str(int(resta9)+int(2))+' '+str(int(resta10)+int(2))+' '+str(int(resta11)+int(2))+' '+str(int(resta12)+int(2))+' '+str(int(resta13)+int(2))+' '+str(int(resta14)+int(2))+' '+str(int(resta15)+int(2))+' '+str(int(resta16)+int(2))+' '+str(int(resta17)+int(2))+' '+str(int(resta18)+int(2))+' '+str(int(resta19)+int(2))+' '+str(int(resta20)+int(2))+' '+str(int(resta21)+int(2))+' '+str(int(resta22)+int(2))+' '+str(int(resta23)+int(2))+' '+str(int(resta24)+int(2))+' '+str(int(resta25)+int(2))+' '+str(int(resta26)+int(2))+' '+str(int(resta27)+int(2))+' '+str(int(resta28)+int(2))+' '+str(int(resta29)+int(2))+' '+str(int(resta30)+int(2))+' '+str(int(resta31)+int(2))+' '+str(int(resta32)+int(2))+' '+str(int(resta33)+int(2))+' '+str(int(resta34)+int(2))+' '+str(int(resta35)+int(2))+' '+str(int(resta36)+int(2))+' '+str(int(resta37)+int(2))+' '+str(int(resta38)+int(2))+' '+str(int(resta39)+int(2))+' '+str(int(resta40)+int(2))+' '+str(int(resta41)+int(2))+' '+str(int(resta42)+int(2))+' '+str(int(resta43)+int(2))+' '+str(int(resta44)+int(2))+' '+str(int(resta45)+int(2))+' '+str(int(resta46)+int(2))+' '+str(int(resta47)+int(2))+' '+str(int(resta48)+int(2))+' '+rootname+' '+str(b)+' '+str(a)+' '+str(e)+' '+str(d)+' '+str(h)+' '+str(g)+' '+str(y)+' '+str(x)
            os.system(cmd3)

xyzindir='min_basal_xyz/'
dihedir='scan_sander_basal_param/'

for root, dirs, filenames in os.walk(xyzindir):
       for n in filenames:
        print('\n')
        print(n[:-4]+'\n')
        w=open(dihedir+'out_1_'+n[:-4]+'/sander_1_'+n[:-4]+'.txt','r')
        table = [line.rstrip().split("\n") for line in w.readlines()]
        x=[]
        for i in range(0,25,1):
            a=float(table[i][0])/1.
            x.append(a)
        y=[]
        for i in range(0,25,1):
            
            y.append(round(x[i]-min(x),4))
        w=open(dihedir+'out_1_'+n[:-4]+'/sander_1_'+n[:-4]+'.txt','w')
        for i in range(0,25,1):
            print(y[i])
            w.write(str(y[i])+'\n')
        w.close()
        
        print('\n')
        p=open(dihedir+'out_2_'+n[:-4]+'/sander_2_'+n[:-4]+'.txt','r')
        table = [line.rstrip().split("\n") for line in p.readlines()]
        x=[]
        for i in range(0,25,1):
            a=float(table[i][0])/1.
            x.append(a)
        y=[]
        for i in range(0,25,1):
            
            y.append(round(x[i]-min(x),4))
        p=open(dihedir+'out_2_'+n[:-4]+'/sander_2_'+n[:-4]+'.txt','w')
        for i in range(0,25,1):
            print(y[i])
            p.write(str(y[i])+'\n')
        p.close()
        
        print('\n')
        q=open(dihedir+'out_3_'+n[:-4]+'/sander_3_'+n[:-4]+'.txt','r')
        table = [line.rstrip().split("\n") for line in q.readlines()]
        x=[]
        for i in range(0,25,1):
            a=float(table[i][0])/1.
            x.append(a)
        y=[]
        for i in range(0,25,1):
            
            y.append(round(x[i]-min(x),4))
        q=open(dihedir+'out_3_'+n[:-4]+'/sander_3_'+n[:-4]+'.txt','w')
        for i in range(0,25,1):
            print(y[i])
            q.write(str(y[i])+'\n')
        q.close()

