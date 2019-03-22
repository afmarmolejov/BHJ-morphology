import os
import shutil
if os.path.exists("AMBER_dihedral_new/"):
    shutil.rmtree("AMBER_dihedral_new/")
    os.mkdir("AMBER_dihedral_new/")
else:
    os.mkdir("AMBER_dihedral_new/")
indir = 'dihedral_id/'
antedir='mol2_basal/'
frcdir='frcmod_basal/'
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open("AMBER_dihedral_new/"+f.name[len(indir):-4]+'.dat', 'w')
        searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
        frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
        print (f.name)
        print (searchfile.name)
        print (frcmod.name)
        
        
        for bond in range(0,int(len(table)/5),1):
            print(bond*5+1)
            for line in searchfile:
                if (" "+table[int(bond*5+1)][0]+" ") in line:  
                    a1=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+1)][1]+" ") in line:  
                    a2=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+1)][2]+" ") in line:  
                    a3=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+1)][3]+" ") in line:  
                    a4=[line.rstrip().split() for line in line]
            a=a1[50][0]+a1[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a4[50][0]+a4[51][0]
            aT=a4[50][0]+a4[51][0]+'-'+a3[50][0]+a3[51][0]+'-'+a2[50][0]+a2[51][0]+'-'+a1[50][0]+a1[51][0]

            for line in frcmod:
                if line.startswith('IMPROPER'):
                    break
                if (a) in line:  
                    print(a)
                    w.write(a+'\n')
                else:
                    if (aT) in line:  
                        print(aT)
                        w.write(aT+'\n')
            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            for line in searchfile:
                if (" "+table[int(bond*5+2)][0]+" ") in line:  
                    b1=[line.rstrip().split(" ") for line in line]
                if (" "+table[int(bond*5+2)][1]+" ") in line:  
                    b2=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+2)][2]+" ") in line:  
                    b3=[line.rstrip().split(' ') for line in line]
                if (" "+table[int(bond*5+2)][3]+" ") in line:  
                    b4=[line.rstrip().split(' ') for line in line]
            b=b1[50][0]+b1[51][0]+'-'+b2[50][0]+b2[51][0]+'-'+b3[50][0]+b3[51][0]+'-'+b4[50][0]+b4[51][0]
            bT=b4[50][0]+b4[51][0]+'-'+b3[50][0]+b3[51][0]+'-'+b2[50][0]+b2[51][0]+'-'+b1[50][0]+b1[51][0]
            for line in frcmod:
                if line.startswith('IMPROPER'):
                    break
                if (b) in line:  
                    print(b)
                    w.write(b+'\n')
                else:
                    if (bT) in line:  
                        print(bT)
                        w.write(bT+'\n')
            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            for line in searchfile:
                if (" "+table[int(bond*5+3)][0]+" ") in line:  
                    c1=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+3)][1]+" ") in line:  
                    c2=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+3)][2]+" ") in line:  
                    c3=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+3)][3]+" ") in line:  
                    c4=[line.rstrip().split() for line in line]
            c=c1[50][0]+c1[51][0]+'-'+c2[50][0]+c2[51][0]+'-'+c3[50][0]+c3[51][0]+'-'+c4[50][0]+c4[51][0]
            cT=c4[50][0]+c4[51][0]+'-'+c3[50][0]+c3[51][0]+'-'+c2[50][0]+c2[51][0]+'-'+c1[50][0]+c1[51][0]

            for line in frcmod:
                if line.startswith('IMPROPER'):
                    break
                if (c) in line:  
                    print(c)
                    w.write(c+'\n')
                else:
                    if (cT) in line:  
                        print(cT)
                        w.write(cT+'\n')
            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            for line in searchfile:
                if (" "+table[int(bond*5+4)][0]+" ") in line:  
                    d1=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+4)][1]+" ") in line:  
                    d2=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+4)][2]+" ") in line:  
                    d3=[line.rstrip().split() for line in line]
                if (" "+table[int(bond*5+4)][3]+" ") in line:  
                    d4=[line.rstrip().split() for line in line]
            d=d1[50][0]+d1[51][0]+'-'+d2[50][0]+a2[51][0]+'-'+d3[50][0]+a3[51][0]+'-'+d4[50][0]+d4[51][0]
            dT=d4[50][0]+d4[51][0]+'-'+d3[50][0]+a3[51][0]+'-'+d2[50][0]+a2[51][0]+'-'+d1[50][0]+d1[51][0]

            for line in frcmod:
                if line.startswith('IMPROPER'):
                    break
                if (d) in line:  
                    print(d)
                    w.write(d+'\n')
                else:
                    if (dT) in line:  
                        print(dT)
                        w.write(dT+'\n')
            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')


        w.close()
