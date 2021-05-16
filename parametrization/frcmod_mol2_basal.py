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





for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        print('\n')
        
        count=0
        letters=[]
        for char in string.ascii_uppercase:
            for i in string.ascii_uppercase:
                letters.append(str(char+i))
              
        
        
        
        f = open(indir+n, 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        
        for bond in range(0,int(len(table)/4),1):
            print(bond)
           
            if bond==0:
                antedir='antechamber_q/'
                frcdir='frcmod/'
                frcmod=open(frcdir+n[:-4]+'.frcmod', 'r')
            else:
                antedir='dihe'+str(int(bond-1))+'/'+n[:-4]+'/'
                frcdir='dihe'+str(int(bond-1))+'/'+n[:-4]+'/'
                frcmod=open(frcdir+n[:-4]+'.frcmod', 'r')
            
            
            if os.path.exists('dihe'+str(bond)+'/'):
                shutil.rmtree('dihe'+str(bond)+'/')
                os.mkdir('dihe'+str(bond)+'/')
            else:
                os.mkdir('dihe'+str(bond)+'/')
            dih1='dihe'+str(bond)+'/'
            
            w=open(dih1+n,"w")
            
            for line in frcmod:
                a1=table[bond*4][3]
                if str("remark goes here") in line:
                        w.write('  remark goes here'+'\n')   
                if str("MASS") in line:
                        w.write('  MASS'+'\n')
                if str("BOND") in line:
                        w.write("\n"+"  BOND"+'\n')
                if str("ANGLE") in line:
                        w.write('\n'+'  ANGLE'+'\n')
                if str("DIHE") in line:
                        w.write('\n'+'  DIHE'+'\n')
                if str("IMPROPER") in line:
                        w.write('\n'+'  IMPROPER'+'\n')
                if str("NONB") in line:
                        w.write('\n'+'  NONB'+'\n')
                if (a1) in line:
                    w.write(line)
            w.close()
            indir = 'AMBER_dihedral/'
            changedir='dihe'+str(bond)+'/'
            
            if os.path.exists('dihe'+str(bond)+'/'+n[:-4]+'/'):
                shutil.rmtree('dihe'+str(bond)+'/'+n[:-4]+'/')
                os.mkdir('dihe'+str(bond)+'/'+n[:-4]+'/')
            else:
                os.mkdir('dihe'+str(bond)+'/'+n[:-4]+'/')
            
            changedir='dihe'+str(bond)+'/'
            w=open(changedir+n,"r")
            
            dihe1='dihe'+str(bond)+'/'+n[:-4]+'/'
            AA=open(dihe1+n[:-4]+'_1.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print(n)
            AA.write('dihe1remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][:2]:
                    line[0]=str(letters[count])+line[0][2:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            split[-1][0]=str(letters[count])+split[-1][0][4:]
            AA.write(' '.join(split[-1])+"\n")
            AA.close()
            
            
            
            w=open(changedir+n,"r")
            dihe2='dihe'+str(bond)+'/'+n[:-4]+'/'
            AA=open(dihe2+n[:-4]+'_2.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (n)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][3:5]:
                    line[0]=line[0][:3]+str(letters[count])+line[0][5:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            AA.close()
            
            w=open(changedir+n,"r")
            dihe3='dihe'+str(bond)+'/'+n[:-4]+'/'
            AA=open(dihe3+n[:-4]+'_3.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (n)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][6:8]:
                    line[0]=line[0][:6]+str(letters[count])+line[0][8:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            AA.close()

            
            w=open(changedir+n,"r")
            dihe4='dihe'+str(bond)+'/'+n[:-4]+'/'
            AA=open(dihe4+n[:-4]+'_4.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (n)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][3]
                if (a1) in line[0][9:11]:
                    line[0]=line[0][:9]+str(letters[count])+line[0][11:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            AA.close()
            
            
            
            
            
            searchfile=open(antedir+n[:-4]+'.mol2', "r")
            
            correctdir = 'corrected_dihedral/'
            C = open(correctdir+n[:-4]+'.dat', 'r')
            table3 = [line.rstrip().split("-") for line in C.readlines()]
            w=open(dihe1+n[:-4]+'.mol2', 'w')
            
            table2 = [re.split('|\n',line2) for line2 in searchfile.readlines()]
            for line2 in table2:
                    a1=table3[bond*4][3]
                    #print(a1)
                    if (a1+' ') in line2[0][8:14]:
                        #print(a1+' ')
                        line2[0]=line2[0][0:50]+str(letters[count])+line2[0][52:]
                    w.write(''.join(line2))
            w.close()
            
            
            shutil.copy2(frcdir+n[:-4]+'.frcmod',dihe1+n[:-4]+'.frcmod')            
            tleap1=open(dihe1+n[:-4]+'.leap', 'w')
            tleap1.write('loadamberparams '+n[:-4]+'.frcmod'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_1.dat'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_2.dat'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_3.dat'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_4.dat'+'\n')
            tleap1.write('LIG = loadmol2 '+n[:-4]+'.mol2'+'\n')
            tleap1.write('check LIG'+'\n')
            tleap1.write('saveamberparm LIG '+n[:-4]+'.prmtop '+n[:-4]+'.inpcrd'+'\n')
            tleap1.write('quit'+'\n')
            tleap1.close()
            os.system('cd '+dihe1+' && tleap -f '+n[:-4]+'.leap')
            os.system('cd '+dihe1+' && rm '+n[:-4]+'.frcmod '+n[:-4]+'.inpcrd '+n[:-4]+'.leap '+n[:-4]+'_*.dat ')
            
            parmedin=open(dihe1+f.name[len(indir):-4]+'.parmed', 'w')
            parmedin.write('writeFrcmod '+f.name[len(indir):-4]+'.frcmod'+'\n')
            parmedin.write('quit'+'\n')
            parmedin.close()
            os.system('cd '+dihe1+' && parmed -i '+f.name[len(indir):-4]+'.parmed -p '+f.name[len(indir):-4]+'.prmtop')
            os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.parmed '+f.name[len(indir):-4]+'.prmtop')
            count=count+1
            
            
            
            ##########
        for bond in range(0,int(len(table)/4),1):
            print(bond)
            print(str(int(bond)+int(len(table)/4-1)))
            antedir='dihe'+str(int(bond)+int(len(table)/4-1))+'/'+n[:-4]+'/'
            frcdir='dihe'+str(int(bond)+int(len(table)/4-1))+'/'+n[:-4]+'/'
            frcmod=open(frcdir+n[:-4]+'.frcmod', 'r')
            
            
            if os.path.exists('dihe'+str(int(bond)+int(len(table)/4))+'/'):
                shutil.rmtree('dihe'+str(int(bond)+int(len(table)/4))+'/')
                os.mkdir('dihe'+str(int(bond)+int(len(table)/4))+'/')
            else:
                os.mkdir('dihe'+str(int(bond)+int(len(table)/4))+'/')
            dih1='dihe'+str(int(bond)+int(len(table)/4))+'/'
            
            w=open(dih1+n,"w")
            
            for line in frcmod:
                a1=table[bond*4][1]
                if str("remark goes here") in line:
                        w.write('  remark goes here'+'\n')   
                if str("MASS") in line:
                        w.write('  MASS'+'\n')
                if str("BOND") in line:
                        w.write("\n"+"  BOND"+'\n')
                if str("ANGLE") in line:
                        w.write('\n'+'  ANGLE'+'\n')
                if str("DIHE") in line:
                        w.write('\n'+'  DIHE'+'\n')
                if str("IMPROPER") in line:
                        w.write('\n'+'  IMPROPER'+'\n')
                if str("NONB") in line:
                        w.write('\n'+'  NONB'+'\n')
                if (a1) in line:
                    w.write(line)
            w.close()
            indir = 'AMBER_dihedral/'
            changedir='dihe'+str(int(bond)+int(len(table)/4))+'/'
            
            if os.path.exists('dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/'):
                shutil.rmtree('dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/')
                os.mkdir('dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/')
            else:
                os.mkdir('dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/')
            
            changedir='dihe'+str(int(bond)+int(len(table)/4))+'/'
            w=open(changedir+n,"r")
            
            dihe1='dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/'
            AA=open(dihe1+n[:-4]+'_1.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print(n)
            AA.write('dihe1remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][:2]:
                    line[0]=str(letters[count])+line[0][2:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            split[-1][0]=str(letters[count])+split[-1][0][4:]
            AA.write(' '.join(split[-1])+"\n")
            AA.close()
            
            
            
            w=open(changedir+n,"r")
            dihe2='dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/'
            AA=open(dihe2+n[:-4]+'_2.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (n)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][3:5]:
                    line[0]=line[0][:3]+str(letters[count])+line[0][5:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            AA.close()
            
            w=open(changedir+n,"r")
            dihe3='dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/'
            AA=open(dihe3+n[:-4]+'_3.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (n)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][6:8]:
                    line[0]=line[0][:6]+str(letters[count])+line[0][8:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            AA.close()

            
            w=open(changedir+n,"r")
            dihe4='dihe'+str(int(bond)+int(len(table)/4))+'/'+n[:-4]+'/'
            AA=open(dihe4+n[:-4]+'_4.dat',"w")
            split = [line.rstrip().split('\n') for line in w.readlines()]
            print (n)
            AA.write('remark goes here'+'\n')
            AA.write('MASS'+'\n')
            for line in split:
                a1=table[bond*4][1]
                if (a1) in line[0][9:11]:
                    line[0]=line[0][:9]+str(letters[count])+line[0][11:]
                    AA.write(' '.join(line)+'\n')
                if ('  BOND') in line:
                    AA.write('\n'+'BOND'+'\n')
                if ('  ANGLE') in line:
                    AA.write('\n'+'ANGLE'+'\n')
                if ('  DIHE') in line:
                    AA.write('\n'+'DIHE'+'\n')
                if ('  IMPROPER') in line:
                    AA.write('\n'+'IMPROPER'+'\n')
                if ('  NONB') in line:
                    AA.write('\n'+'NONBON'+'\n')
            AA.close()
            
            
            
            
            
            searchfile=open(antedir+n[:-4]+'.mol2', "r")
            
            correctdir = 'corrected_dihedral/'
            C = open(correctdir+n[:-4]+'.dat', 'r')
            table3 = [line.rstrip().split("-") for line in C.readlines()]
            w=open(dihe1+n[:-4]+'.mol2', 'w')
            
            table2 = [re.split('|\n',line2) for line2 in searchfile.readlines()]
            for line2 in table2:
                    a1=table3[bond*4][1]
                    #print(a1)
                    if (a1+' ') in line2[0][8:14]:
                        #print(a1+' ')
                        line2[0]=line2[0][0:50]+str(letters[count])+line2[0][52:]
                    w.write(''.join(line2))
            w.close()
            
            
            shutil.copy2(frcdir+n[:-4]+'.frcmod',dihe1+n[:-4]+'.frcmod')            
            tleap1=open(dihe1+n[:-4]+'.leap', 'w')
            tleap1.write('loadamberparams '+n[:-4]+'.frcmod'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_1.dat'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_2.dat'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_3.dat'+'\n')
            tleap1.write('loadamberparams '+n[:-4]+'_4.dat'+'\n')
            tleap1.write('LIG = loadmol2 '+n[:-4]+'.mol2'+'\n')
            tleap1.write('check LIG'+'\n')
            tleap1.write('saveamberparm LIG '+n[:-4]+'.prmtop '+n[:-4]+'.inpcrd'+'\n')
            tleap1.write('quit'+'\n')
            tleap1.close()
            os.system('cd '+dihe1+' && tleap -f '+n[:-4]+'.leap')
            os.system('cd '+dihe1+' && rm '+n[:-4]+'.frcmod '+n[:-4]+'.inpcrd '+n[:-4]+'.leap '+n[:-4]+'_*.dat ')
            
            parmedin=open(dihe1+f.name[len(indir):-4]+'.parmed', 'w')
            parmedin.write('writeFrcmod '+f.name[len(indir):-4]+'.frcmod'+'\n')
            parmedin.write('quit'+'\n')
            parmedin.close()
            os.system('cd '+dihe1+' && parmed -i '+f.name[len(indir):-4]+'.parmed -p '+f.name[len(indir):-4]+'.prmtop')
            os.system('cd '+dihe1+' && rm '+f.name[len(indir):-4]+'.parmed '+f.name[len(indir):-4]+'.prmtop')
            count=count+1
            
            os.system('cp '+dihe1+n[:-4]+'.frcmod '+new+n[:-4]+'.frcmod')
            os.system('cp '+dihe1+n[:-4]+'.mol2 '+mol2+n[:-4]+'.mol2')
    for i in range(0,int(len(table)/4),1):
        shutil.rmtree('dihe'+str(i)+'/')
        shutil.rmtree('dihe'+str(int(i)+int(len(table)/4))+'/')
        

                
            
