import os
import re
import shutil
import string
indir = 'AMBER_dihedral/'


if os.path.exists('frcmod_basal/'):
    shutil.rmtree('frcmod_basal/')
    os.mkdir('frcmod_basal/')
else:
    os.mkdir('frcmod_basal/')
new='frcmod_basal/'

if os.path.exists('mol2_basal/'):
    shutil.rmtree('mol2_basal/')
    os.mkdir('mol2_basal/')
else:
    os.mkdir('mol2_basal/')
mol2='mol2_basal/'

letters=[]
for char in string.ascii_uppercase:
    for i in string.ascii_uppercase:
        letters.append(str(char+i))
#print(lista)

count=0

for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        print('\n')
        bond=0
        
        
        antedir='antechamber_q/'
        f = open(indir+n, 'r')    
        frcdir='frcmod/'
        frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            
        if os.path.exists('dihe'+str(bond)+'/'):
            shutil.rmtree('dihe'+str(bond)+'/')
            os.mkdir('dihe'+str(bond)+'/')
        else:
            os.mkdir('dihe'+str(bond)+'/')
        dih1='dihe'+str(bond)+'/'
            

            

        w=open(dih1+n,"w") 
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
            
        for line in frcmod:
            a1=table[bond*4][3]
            if str("remark goes here") in line:
                    w.write('remark goes here'+'\n')   
            if str("MASS") in line:
                    w.write('MASS'+'\n')
            if str("BOND") in line:
                    w.write("\n"+"BOND"+'\n')
            if str("ANGLE") in line:
                    w.write('\n'+'ANGLE'+'\n')
            if str("DIHE") in line:
                    w.write('\n'+'DIHE'+'\n')
            if str("IMPROPER") in line:
                    w.write('\n'+'IMPROPER'+'\n')
            if str("NONBON") in line:
                    w.write('\n'+'NONBON'+'\n')
            if (a1) in line:
                    w.write(line)
        w.close()

        indir = 'AMBER_dihedral/'
        changedir='dihe'+str(bond)+'/'
        
        antedir='antechamber_q'
        
            


            
        if os.path.exists('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'):
            shutil.rmtree('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
            os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
        else:
            os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe1='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe1+f.name[len(indir):-4]+'_1.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('dihe1remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][3]
            if (a1) in line[0][:2]:
                line[0]=str(letters[count])+line[0][2:]
                AA.write(' '.join(line)+'\n')
    
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONBON') in line:
                AA.write('\n'+'NONBON'+'\n')
        split[-1]=str(letters[count])+line[0][4:]
        AA.write(''.join(split[-1]))
        AA.close()
            
            
            
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe2='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe2+f.name[len(indir):-4]+'_2.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][3]
            if (a1) in line[0][3:5]:
                line[0]=line[0][:3]+str(letters[count])+line[0][5:]
                AA.write(' '.join(line)+'\n')
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONBON') in line:
                AA.write('\n'+'NONBON'+'\n')
        AA.close()
            
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe3='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe3+f.name[len(indir):-4]+'_3.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][3]
            if (a1) in line[0][6:8]:
                line[0]=line[0][:6]+str(letters[count])+line[0][8:]
                AA.write(' '.join(line)+'\n')
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONBON') in line:
                AA.write('\n'+'NONBON'+'\n')
        AA.close()

        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe4='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe4+f.name[len(indir):-4]+'_4.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][3]
            if (a1) in line[0][9:11]:
                line[0]=line[0][:9]+str(letters[count])+line[0][11:]
                AA.write(' '.join(line)+'\n')
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONBON') in line:
                AA.write('\n'+'NONBON'+'\n')
        AA.close()
         
        f = open(indir+n, 'r')
        antedir='antechamber_q/'
        searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            
        
            
        correctdir = 'corrected_dihedral/'
        C = open(correctdir+f.name[len(indir):-4]+'.dat', 'r')
        table = [line.rstrip().split("-") for line in C.readlines()]
        w=open(dihe1+f.name[len(indir):-4]+'.mol2', 'w')
            
        table2 = [re.split('|\n',line2) for line2 in searchfile.readlines()]
        for line2 in table2:
                a1=table[bond*4][3]
                #print(a1)
                if (a1+' ') in line2[0][8:14]:
                    #print(a1+' ')
                    line2[0]=line2[0][0:50]+str(letters[count])+line2[0][52:]
                w.write(''.join(line2))
        w.close()
        
        f = open(indir+n, 'r')
        frcdir='frcmod/'
        shutil.copy2(frcdir+f.name[len(indir):-4]+'.frcmod',dihe1+f.name[len(indir):-4]+'.frcmod')
        tleap1=open(dihe1+f.name[len(indir):-4]+'.leap', 'w')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'.frcmod'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_1.dat'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_2.dat'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_3.dat'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_4.dat'+'\n')
        tleap1.write('LIG = loadmol2 '+f.name[len(indir):-4]+'.mol2'+'\n')
        tleap1.write('check LIG'+'\n')
        tleap1.write('saveamberparm LIG '+f.name[len(indir):-4]+'.prmtop '+f.name[len(indir):-4]+'.inpcrd'+'\n')
        tleap1.write('quit'+'\n')
        tleap1.close()
        os.system('cd '+dihe1+' && tleap -f '+f.name[len(indir):-4]+'.leap')
        os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.frcmod '+f.name[len(indir):-4]+'.inpcrd '+f.name[len(indir):-4]+'.leap '+f.name[len(indir):-4]+'_*.dat ')
    
        parmedin=open(dihe1+f.name[len(indir):-4]+'.parmed', 'w')
        parmedin.write('writeFrcmod '+f.name[len(indir):-4]+'.frcmod'+'\n')
        parmedin.write('quit'+'\n')
        parmedin.close()
        os.system('cd '+dihe1+' && parmed -i '+f.name[len(indir):-4]+'.parmed -p '+f.name[len(indir):-4]+'.prmtop')
        os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.parmed '+f.name[len(indir):-4]+'.prmtop')

            
        count=count+1
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        
        for bond in range(1,int(len(table)/4),1):
            print(bond)
            antedir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            
            frcdir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            
            
            if os.path.exists('dihe'+str(bond)+'/'):
                shutil.rmtree('dihe'+str(bond)+'/')
                os.mkdir('dihe'+str(bond)+'/')
            else:
                os.mkdir('dihe'+str(bond)+'/')
            dih1='dihe'+str(bond)+'/'
            

            
            
            w=open(dih1+n,"w")
            #w2=open(dih1+n[:-4]+'_1',"w")
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            antedir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            
            
            
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            
            for line in frcmod:
                a1=table[bond*4][3]
                if str("remark goes here") in line:
                        w.write('remark goes here'+'\n')   
                if str("MASS") in line:
                        w.write('MASS'+'\n')
                if str("BOND") in line:
                        w.write("\n"+"BOND"+'\n')
                if str("ANGLE") in line:
                        w.write('\n'+'ANGLE'+'\n')
                if str("DIHE") in line:
                        w.write('\n'+'DIHE'+'\n')
                if str("IMPROPER") in line:
                        w.write('\n'+'IMPROPER'+'\n')
                if str("NONB") in line:
                        w.write('\n'+'NONB'+'\n')
                if (a1) in line:
                    w.write(line)
            w.close()
            indir = 'AMBER_dihedral/'
            changedir='dihe'+str(bond)+'/'
            
            antedir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            if os.path.exists('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'):
                shutil.rmtree('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
                os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
            else:
                os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            
            changedir='dihe'+str(bond)+'/'
            w=open(changedir+n,"r")
            dihe1='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe1+f.name[len(indir):-4]+'_1.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('dihe1remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][:2]:
                    line[0]=str(letters[count])+line[0][2:]
                    AA.write(' '.join(line)+'\n')
    
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            #split[-1]=str(letters[count])+line[0][4:]
            #AA.write(''.join(split[-1]))
            AA.close()
            
            
            
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            w=open(changedir+n,"r")
            dihe2='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe2+f.name[len(indir):-4]+'_2.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][3:5]:
                    line[0]=line[0][:3]+str(letters[count])+line[0][5:]
                    AA.write(' '.join(line)+'\n')
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            AA.close()
            
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            w=open(changedir+n,"r")
            dihe3='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe3+f.name[len(indir):-4]+'_3.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][6:8]:
                    line[0]=line[0][:6]+str(letters[count])+line[0][8:]
                    AA.write(' '.join(line)+'\n')
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            AA.close()

            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            w=open(changedir+n,"r")
            dihe4='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe4+f.name[len(indir):-4]+'_4.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][9:11]:
                    line[0]=line[0][:9]+str(letters[count])+line[0][11:]
                    AA.write(' '.join(line)+'\n')
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            AA.close()
            
            
            
            
            antedir='dihe'+str(int(int(bond-1)))+'/'+f.name[len(indir):-4]+'/'
            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            
            correctdir = 'corrected_dihedral/'
            C = open(correctdir+f.name[len(indir):-4]+'.dat', 'r')
            table = [line.rstrip().split("-") for line in C.readlines()]
            w=open(dihe1+f.name[len(indir):-4]+'.mol2', 'w')
            
            table2 = [re.split('|\n',line2) for line2 in searchfile.readlines()]
            for line2 in table2:
                    a1=table[bond*4][3]
                    #print(a1)
                    if (a1+' ') in line2[0][8:14]:
                        #print(a1+' ')
                        line2[0]=line2[0][0:50]+str(letters[count])+line2[0][52:]
                    w.write(''.join(line2))
            w.close()
            
            
            
            frcdir='dihe'+str(count-1)+'/'+f.name[len(indir):-4]+'/'
            shutil.copy2(frcdir+f.name[len(indir):-4]+'.frcmod',dihe1+f.name[len(indir):-4]+'.frcmod')            
            tleap1=open(dihe1+f.name[len(indir):-4]+'.leap', 'w')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'.frcmod'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_1.dat'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_2.dat'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_3.dat'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_4.dat'+'\n')
            tleap1.write('LIG = loadmol2 '+f.name[len(indir):-4]+'.mol2'+'\n')
            tleap1.write('check LIG'+'\n')
            tleap1.write('saveamberparm LIG '+f.name[len(indir):-4]+'.prmtop '+f.name[len(indir):-4]+'.inpcrd'+'\n')
            tleap1.write('quit'+'\n')
            tleap1.close()
            os.system('cd '+dihe1+' && tleap -f '+f.name[len(indir):-4]+'.leap')
            os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.frcmod '+f.name[len(indir):-4]+'.inpcrd '+f.name[len(indir):-4]+'.leap '+f.name[len(indir):-4]+'_*.dat ')
    
            parmedin=open(dihe1+f.name[len(indir):-4]+'.parmed', 'w')
            parmedin.write('writeFrcmod '+f.name[len(indir):-4]+'.frcmod'+'\n')
            parmedin.write('quit'+'\n')
            parmedin.close()
            os.system('cd '+dihe1+' && parmed -i '+f.name[len(indir):-4]+'.parmed -p '+f.name[len(indir):-4]+'.prmtop')
            os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.parmed '+f.name[len(indir):-4]+'.prmtop')

            
            count=count+1
        letters=[]
        for char in string.ascii_uppercase:
            for i in string.ascii_uppercase:
                letters.append(str(char+i))
        let2=[]
        for i,j in enumerate(letters):
            if i > (count-1):
                let2.append(j)
        letters=let2

        count=0


        print('\n')
        bond=0
        f = open(indir+n, 'r')    
        table = [line.rstrip().split("-") for line in f.readlines()]
        
        antedir='dihe'+str(int(len(table)/4-1))+'/'+f.name[len(indir):-4]+'/'
        f = open(indir+n, 'r')    
        frcdir='dihe'+str(int(len(table)/4-1))+'/'+f.name[len(indir):-4]+'/'
        frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            
        if os.path.exists('dihe'+str(bond)+'/'):
            shutil.rmtree('dihe'+str(bond)+'/')
            os.mkdir('dihe'+str(bond)+'/')
        else:
            os.mkdir('dihe'+str(bond)+'/')
        dih1='dihe'+str(bond)+'/'
            

            

        w=open(dih1+n,"w") 
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
            
        for line in frcmod:
            a1=table[bond*4][1]
            if str("remark goes here") in line:
                    w.write('remark goes here'+'\n')   
            if str("MASS") in line:
                    w.write('MASS'+'\n')
            if str("BOND") in line:
                    w.write("\n"+"BOND"+'\n')
            if str("ANGLE") in line:
                    w.write('\n'+'ANGLE'+'\n')
            if str("DIHE") in line:
                    w.write('\n'+'DIHE'+'\n')
            if str("IMPROPER") in line:
                    w.write('\n'+'IMPROPER'+'\n')
            if str("NONB") in line:
                    w.write('\n'+'NONB'+'\n')
            if (a1) in line:
                    w.write(line)
        w.close()

        indir = 'AMBER_dihedral/'
        changedir='dihe'+str(bond)+'/'
        
        antedir='dihe'+str(int(len(table)/4-1))+'/'+f.name[len(indir):-4]+'/'
        
            


            
        if os.path.exists('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'):
            shutil.rmtree('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
            os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
        else:
            os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe1='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe1+f.name[len(indir):-4]+'_1.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('dihe1remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][1]
            if (a1) in line[0][:2]:
                line[0]=str(letters[count])+line[0][2:]
                AA.write(' '.join(line)+'\n')
    
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONB') in line:
                AA.write('\n'+'NONB'+'\n')
        #split[-1][2]=str(letters[count])
        #AA.write('\n')
        AA.close()
            
            
            
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe2='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe2+f.name[len(indir):-4]+'_2.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][1]
            if (a1) in line[0][3:5]:
                line[0]=line[0][:3]+str(letters[count])+line[0][5:]
                AA.write(' '.join(line)+'\n')
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONB') in line:
                AA.write('\n'+'NONB'+'\n')
        #AA.write('\n')
        AA.close()
            
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe3='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe3+f.name[len(indir):-4]+'_3.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][1]
            if (a1) in line[0][6:8]:
                line[0]=line[0][:6]+str(letters[count])+line[0][8:]
                AA.write(' '.join(line)+'\n')
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONB') in line:
                AA.write('\n'+'NONB'+'\n')
        #AA.write('\n')
        AA.close()

        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        w=open(changedir+n,"r")
        dihe4='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
        AA=open(dihe4+f.name[len(indir):-4]+'_4.dat',"w")
        split = [line.rstrip().split('\n') for line in w.readlines()]
        print (f.name)
        AA.write('remark goes here'+'\n')
        AA.write('MASS'+'\n')
        for line in split:
            a1=table[bond*4][1]
            if (a1) in line[0][9:11]:
                line[0]=line[0][:9]+str(letters[count])+line[0][11:]
                AA.write(' '.join(line)+'\n')
            if ('BOND') in line:
                AA.write('\n'+'BOND'+'\n')
            if ('ANGLE') in line:
                AA.write('\n'+'ANGLE'+'\n')
            if ('DIHE') in line:
                AA.write('\n'+'DIHE'+'\n')
            if ('IMPROPER') in line:
                AA.write('\n'+'IMPROPER'+'\n')
            if ('NONB') in line:
                AA.write('\n'+'NONB'+'\n')
        #AA.write('\n')
        AA.close()
         
        f = open(indir+n, 'r')
        antedir='dihe'+str(int(len(table)/4-1))+'/'+f.name[len(indir):-4]+'/'
        searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            
        
            
        correctdir = 'corrected_dihedral/'
        C = open(correctdir+f.name[len(indir):-4]+'.dat', 'r')
        table = [line.rstrip().split("-") for line in C.readlines()]
        w=open(dihe1+f.name[len(indir):-4]+'.mol2', 'w')
            
        table2 = [re.split('|\n',line2) for line2 in searchfile.readlines()]
        for line2 in table2:
                a1=table[bond*4][1]
                #print(a1)
                if (a1+' ') in line2[0][8:14]:
                    #print(a1+' ')
                    line2[0]=line2[0][0:50]+str(letters[count])+line2[0][52:]
                w.write(''.join(line2))
        w.close()
        
        f = open(indir+n, 'r')
        frcdir='dihe'+str(int(len(table)/4-1))+'/'+f.name[len(indir):-4]+'/'
        print(frcdir)
        shutil.copy2(frcdir+f.name[len(indir):-4]+'.frcmod',dihe1+f.name[len(indir):-4]+'.frcmod')
        tleap1=open(dihe1+f.name[len(indir):-4]+'.leap', 'w')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'.frcmod'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_1.dat'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_2.dat'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_3.dat'+'\n')
        tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_4.dat'+'\n')
        tleap1.write('LIG = loadmol2 '+f.name[len(indir):-4]+'.mol2'+'\n')
        tleap1.write('check LIG'+'\n')
        tleap1.write('saveamberparm LIG '+f.name[len(indir):-4]+'.prmtop '+f.name[len(indir):-4]+'.inpcrd'+'\n')
        tleap1.write('quit'+'\n')
        tleap1.close()
        os.system('cd '+dihe1+' && tleap -f '+f.name[len(indir):-4]+'.leap')
        os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.frcmod '+f.name[len(indir):-4]+'.inpcrd '+f.name[len(indir):-4]+'.leap '+f.name[len(indir):-4]+'_*.dat ')
    
        parmedin=open(dihe1+f.name[len(indir):-4]+'.parmed', 'w')
        parmedin.write('writeFrcmod '+f.name[len(indir):-4]+'.frcmod'+'\n')
        parmedin.write('quit'+'\n')
        parmedin.close()
        os.system('cd '+dihe1+' && parmed -i '+f.name[len(indir):-4]+'.parmed -p '+f.name[len(indir):-4]+'.prmtop')
        os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.parmed '+f.name[len(indir):-4]+'.prmtop')

            
        count=count+1
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        
        for bond in range(1,int(len(table)/4),1):
            print(bond)
            antedir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            
            frcdir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            frcdir2='frcmod/'
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            frcmod2=open(frcdir2+f.name[len(indir):-4]+'.frcmod', 'r')
            
            if os.path.exists('dihe'+str(bond)+'/'):
                shutil.rmtree('dihe'+str(bond)+'/')
                os.mkdir('dihe'+str(bond)+'/')
            else:
                os.mkdir('dihe'+str(bond)+'/')
            dih1='dihe'+str(bond)+'/'
            

            
            
            w=open(dih1+n,"w")
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            antedir='dihe'+str(int(bond-2))+'/'+f.name[len(indir):-4]+'/'
            
            
            
            frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
            for line in frcmod:
                a1=table[bond*4][1]
                if str("remark goes here") in line:
                        w.write('remark goes here'+'\n')   
                if str("MASS") in line:
                        w.write('MASS'+'\n')
                if str("BOND") in line:
                        w.write("\n"+"BOND"+'\n')
                if str("ANGLE") in line:
                        w.write('\n'+'ANGLE'+'\n')
                if str("DIHE") in line:
                        w.write('\n'+'DIHE'+'\n')
                if str("IMPROPER") in line:
                        w.write('\n'+'IMPROPER'+'\n')
                if str("NONB") in line:
                        w.write('\n'+'NONB'+'\n')
                if (a1) in line:
                    w.write(line)
            w.close()
            indir = 'AMBER_dihedral/'
            changedir='dihe'+str(bond)+'/'
            
            antedir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            if os.path.exists('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'):
                shutil.rmtree('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
                os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
            else:
                os.mkdir('dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/')
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            
            changedir='dihe'+str(bond)+'/'
            w=open(changedir+n,"r")
            dihe1='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe1+f.name[len(indir):-4]+'_1.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('dihe1remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][:2]:
                    line[0]=str(letters[count])+line[0][2:]
                    AA.write(' '.join(line)+'\n')
    
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            #split[-1][2]=str(letters[count])
            #AA.write(' '.join(split[-1]))
            AA.write('\n')
            AA.close()
            
            
            
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            w=open(changedir+n,"r")
            dihe2='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe2+f.name[len(indir):-4]+'_2.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][3:5]:
                    line[0]=line[0][:3]+str(letters[count])+line[0][5:]
                    AA.write(' '.join(line)+'\n')
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            AA.write('\n')
            AA.close()
            
            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            w=open(changedir+n,"r")
            dihe3='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe3+f.name[len(indir):-4]+'_3.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][6:8]:
                    line[0]=line[0][:6]+str(letters[count])+line[0][8:]
                    AA.write(' '.join(line)+'\n')
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            AA.write('\n')
            AA.close()

            f = open(indir+n, 'r')
            table = [line.rstrip().split("-") for line in f.readlines()]
            w=open(changedir+n,"r")
            dihe4='dihe'+str(bond)+'/'+f.name[len(indir):-4]+'/'
            AA=open(dihe4+f.name[len(indir):-4]+'_4.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (f.name)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][9:11]:
                    line[0]=line[0][:9]+str(letters[count])+line[0][11:]
                    AA.write(' '.join(line)+'\n')
                if ('BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('NONB') in line:
                    AA.write('\n'+'NONB'+'\n')
            AA.write('\n')
            AA.close()
            
            
            
            
            antedir='dihe'+str(int(bond-1))+'/'+f.name[len(indir):-4]+'/'
            searchfile=open(antedir+f.name[len(indir):-4]+'.mol2', "r")
            
            correctdir = 'corrected_dihedral/'
            C = open(correctdir+f.name[len(indir):-4]+'.dat', 'r')
            table = [line.rstrip().split("-") for line in C.readlines()]
            w=open(dihe1+f.name[len(indir):-4]+'.mol2', 'w')
            
            table2 = [re.split('|\n',line2) for line2 in searchfile.readlines()]
            for line2 in table2:
                    a1=table[bond*4][1]
                    #print(a1)
                    if (a1+' ') in line2[0][8:14]:
                        #print(a1+' ')
                        line2[0]=line2[0][0:50]+str(letters[count])+line2[0][52:]
                    w.write(''.join(line2))
            w.close()
            
            
            
            frcdir='dihe'+str(bond-1)+'/'+f.name[len(indir):-4]+'/'
            shutil.copy2(frcdir+f.name[len(indir):-4]+'.frcmod',dihe1+f.name[len(indir):-4]+'.frcmod')            
            tleap1=open(dihe1+f.name[len(indir):-4]+'.leap', 'w')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'.frcmod'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_1.dat'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_2.dat'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_3.dat'+'\n')
            tleap1.write('loadamberparams '+f.name[len(indir):-4]+'_4.dat'+'\n')
            tleap1.write('LIG = loadmol2 '+f.name[len(indir):-4]+'.mol2'+'\n')
            tleap1.write('check LIG'+'\n')
            tleap1.write('saveamberparm LIG '+f.name[len(indir):-4]+'.prmtop '+f.name[len(indir):-4]+'.inpcrd'+'\n')
            tleap1.write('quit'+'\n')
            tleap1.close()
            os.system('cd '+dihe1+' && tleap -f '+f.name[len(indir):-4]+'.leap')
            os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.frcmod '+f.name[len(indir):-4]+'.inpcrd '+f.name[len(indir):-4]+'.leap '+f.name[len(indir):-4]+'_*.dat ')
    
            parmedin=open(dihe1+f.name[len(indir):-4]+'.parmed', 'w')
            parmedin.write('writeFrcmod '+f.name[len(indir):-4]+'.frcmod'+'\n')
            parmedin.write('quit'+'\n')
            parmedin.close()
            os.system('cd '+dihe1+' && parmed -i '+f.name[len(indir):-4]+'.parmed -p '+f.name[len(indir):-4]+'.prmtop')
            os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.parmed '+f.name[len(indir):-4]+'.prmtop')

            
            count=count+1
   

        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        frcdir='dihe'+str(int(len(table)/4-1))+'/'+f.name[len(indir):-4]+'/'
        moldir='dihe'+str(int(len(table)/4-1))+'/'+f.name[len(indir):-4]+'/'
        os.system('cp '+frcdir+f.name[len(indir):-4]+'.frcmod '+new+f.name[len(indir):-4]+'.frcmod')
        os.system('cp '+moldir+f.name[len(indir):-4]+'.mol2 '+mol2+f.name[len(indir):-4]+'.mol2')


        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        for i in range(0,int(len(table)/4)):
               shutil.rmtree('dihe'+str(i)+'/')
