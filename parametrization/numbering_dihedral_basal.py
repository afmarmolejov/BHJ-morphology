import os
import shutil
if os.path.exists("numbering_dihedral_basal/"):
    shutil.rmtree("numbering_dihedral_basal/")
    os.mkdir("numbering_dihedral_basal/")
else:
    os.mkdir("numbering_dihedral_basal/")
indir = 'dihedral_id/'
antedir='mol2_basal/'
frcdir='frcmod_basal/'
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open("numbering_dihedral_basal/"+f.name[len(indir):-4]+'.dat', 'w')
        searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
        frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
        print (f.name)
        print (searchfile.name)
        print (frcmod.name)
        for bond in range(0,int(len(table)/5),1):
            for line in searchfile:
                if (" "+table[int(bond*5+1)][0]+" ") in line:  
                    a1=[line.rstrip().split(" ") for line in line]
                if (" "+table[int(bond*5+1)][1]+" ") in line:  
                    a2=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+1)][2]+" ") in line:  
                    a3=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+1)][3]+" ") in line:  
                    a4=[line.rstrip().split(' ') for line in line]
                    a=a1[50][0]+a1[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a4[50][0]+a4[51][0]
                    aT=a4[50][0]+a4[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a1[50][0]+a1[51][0]
                    b=a1[5][0]+a1[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a4[5][0]+a4[6][0]
                    bT=a4[5][0]+a4[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a1[5][0]+a1[6][0]
            for line in frcmod:
                if line.startswith('IMPROPER'):
                            break
                if (a) in line:  
                    w.write(b+'\n')
                else:
                    if (aT) in line:  
                        w.write(bT+'\n')
            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            for line in searchfile:
                if (" "+table[int(bond*5+2)][0]+" ") in line:  
                    a1=[line.rstrip().split(" ") for line in line]
                if (" "+table[int(bond*5+2)][1]+" ") in line:  
                    a2=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+2)][2]+" ") in line:  
                    a3=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+2)][3]+" ") in line:  
                    a4=[line.rstrip().split(' ') for line in line]
                    a=a1[50][0]+a1[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a4[50][0]+a4[51][0]
                    aT=a4[50][0]+a4[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a1[50][0]+a1[51][0]
                    b=a1[5][0]+a1[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a4[5][0]+a4[6][0]
                    bT=a4[5][0]+a4[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a1[5][0]+a1[6][0]
            for line in frcmod:
                if line.startswith('IMPROPER'):
                            break
                if (a) in line:  
                    w.write(b+'\n')
                else:
                    if (aT) in line:  
                        w.write(bT+'\n') 

            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            for line in searchfile:
                if (" "+table[int(bond*5+3)][0]+" ") in line:  
                    a1=[line.rstrip().split(" ") for line in line]
                if (" "+table[int(bond*5+3)][1]+" ") in line:  
                    a2=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+3)][2]+" ") in line:  
                    a3=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+3)][3]+" ") in line:  
                    a4=[line.rstrip().split(' ') for line in line]
                    a=a1[50][0]+a1[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a4[50][0]+a4[51][0]
                    aT=a4[50][0]+a4[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a1[50][0]+a1[51][0]
                    b=a1[5][0]+a1[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a4[5][0]+a4[6][0]
                    bT=a4[5][0]+a4[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a1[5][0]+a1[6][0]
            for line in frcmod:
                if line.startswith('IMPROPER'):
                            break
                if (a) in line:  
                    w.write(b+'\n')
                else:
                    if (aT) in line:  
                        w.write(bT+'\n') 

            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            for line in searchfile:
                if (" "+table[int(bond*5+4)][0]+" ") in line:  
                    a1=[line.rstrip().split(" ") for line in line]
                if (" "+table[int(bond*5+4)][1]+" ") in line:  
                    a2=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+4)][2]+" ") in line:  
                    a3=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+4)][3]+" ") in line:  
                    a4=[line.rstrip().split(' ') for line in line]
                    a=a1[50][0]+a1[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a4[50][0]+a4[51][0]
                    aT=a4[50][0]+a4[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a1[50][0]+a1[51][0]
                    b=a1[5][0]+a1[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a4[5][0]+a4[6][0]
                    bT=a4[5][0]+a4[6][0]+'-'+a3[5][0]+a3[6][0]+'-'+a2[5][0]+a2[6][0]+'-'+a1[5][0]+a1[6][0]
            for line in frcmod:
                if line.startswith('IMPROPER'):
                            break
                if (a) in line:  
                    w.write(b+'\n')
                else:
                    if (aT) in line:  
                        w.write(bT+'\n') 

            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')


        w.close()
