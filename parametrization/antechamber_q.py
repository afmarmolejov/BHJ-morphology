import cclib
import os
import shutil

if os.path.exists("antechamber_q/"):
    shutil.rmtree("antechamber_q/")
    os.mkdir("antechamber_q/")
else:
    os.mkdir("antechamber_q/")     

indir = 'Hirshfeld_iter_basal/'
for root, dirs, filenames in os.walk(indir):
       for n in filenames:
            print(n)
            cmd="sed"+" "+"'/Running Job 1/,/Running Job 2/d'"+" "+indir+n+" "+">"+indir+n+"_q"
            os.system(cmd)
            cmd2=indir+n+"_q"
            doc=open(cmd2,'r')
            cmd3=indir+n+"q"
            docc=open(cmd3,'w')
            for line in doc: 
                docc.write(line.replace("READ", "0 1"))    
            docc.close()
            mol=cclib.parser.QChem(indir+n+"q")
            data=mol.parse()
            charge=data.atomcharges
            del charge['mulliken']
            hirshfeld=charge.get('hirshfeld')
            q=open(indir+"q.dat", 'w')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            for y in hirshfeld:
                m=str(y)
                q.write(m.ljust(0)+'\n')
            q.close()
            q=open(indir+"q.dat", 'r')
            table = [line.rstrip().split("\n") for line in q.readlines()]
            table=table[6:]
            print('Initial charge') 
            def sumar_lista(table):
                suma=0
                for item in table:
                    suma=suma+float(item[0])
                return suma
            Q1=round(float(table[-1][0]), 6)       	    
            Q2=round(float(sumar_lista(table)), 6)
       	    print(Q2)
            table[-1]=[str(round(Q1-Q2, 6))]
            def sumar_lista(table):
                suma=0
                for item in table:
                    suma=suma+float(item[0])
                return suma
            print('Final charge')       
            print(sumar_lista(table))
            cmd4="rm"+" "+indir+"q.dat"
            os.system(cmd4)
            q=open(indir+'q.dat', 'w')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            q.write(' '+'\n')
            for item in table:
                    q.write(str(item[0])+'\n')
            q.close()
            antedir='antechamber/'
            T=open(indir+n,'r')
            cmd5="awk "+"'{print $1,$2,$3,$4,$5,$6,$7,$8}' "+antedir+T.name[len(indir):-6]+".mol2"+" "+"|"+"column"+" "+"-t"+" "+">"+" "+indir+"q2.dat"
            os.system(cmd5)
            cmd6="paste "+indir+"q2.dat "+indir+"q.dat | awk '{print $1,$2,$3,$4,$5,$6,$7,$8,$9}' > "+indir+"q3.dat"
            os.system(cmd6)
            anteqdir='antechamber_q/'
            cmd7="antechamber -i "+indir+"q3.dat -fi mol2 -fo mol2 -o "+anteqdir+T.name[len(indir):-6]+".mol2 -at gaff2"
            os.system(cmd7)
            os.system('rm ANTECHAMBER_AC.AC')
            os.system('rm ANTECHAMBER_AC.AC0')
            os.system('rm ANTECHAMBER_BOND_TYPE.AC')
            os.system('rm ANTECHAMBER_BOND_TYPE.AC0')
            os.system('rm ATOMTYPE.INF')
            cmd8="rm "+indir+n+"q "+indir+n+"_q"
            os.system(cmd8)
            cmd9="rm "+indir+"q.dat "+indir+"q2.dat "+indir+"q3.dat"
            os.system(cmd9)

