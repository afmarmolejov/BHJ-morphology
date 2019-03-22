import os
import shutil
if os.path.exists("frcmod_basal_param"):
    shutil.rmtree("frcmod_basal_param")
    os.mkdir("frcmod_basal_param")
else:
    os.mkdir("frcmod_basal_param")

param="frcmod_basal_param/"
indir = 'AMBER_dihedral_new/'
frcdir='frcmod_basal_zero/'
kdir='basal_param/'
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        print(n)
        f = open(indir+n, 'r')
        table = [line.rstrip().split(" ") for line in f.readlines()]
        frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
        table2 = [line.rstrip().split(" ") for line in frcmod.readlines()]
        k_param = open(kdir+n[:-4]+'/param.txt', 'r')
        table3 = [line.rstrip().split(" ") for line in k_param.readlines()]
        for bond in range(0,int(len(table)/4),1):


            for line in table2:
                if table[int(bond*4)][0] in line:

                    if table[int(bond*4+2)][0] == table[int(bond*4)][0]:
                        line[4]=str(round(4))  
                        line[9]=str(float(table3[int(bond*2+1)][0]))
                        line[11]=str(float(table3[int(bond*2+1)][2]))
                        line[14]=str(float(table3[int(bond*2+1)][5]))
                    elif table[int(bond*4+1)][0] == table[int(bond*4)][0]:
                        line[4]=str(round(4))  
                        line[9]=str(table3[int(bond*2+1)][0])
                        line[11]=str(float(table3[int(bond*2+1)][2]))
                        line[14]=str(float(table3[int(bond*2+1)][5]))
                    elif table[int(bond*4)][0] not in [table[int(bond*4+1)][0],table[int(bond*4+2)][0]]:
                        line[4]=str(round(1))  
                        line[9]=str(float(table3[int(bond*2+1)][0])/4)
                        line[11]=str(float(table3[int(bond*2+1)][2]))
                        line[14]=str(float(table3[int(bond*2+1)][5]))
                if ('IMPROPER') in line:
                    break


            q=[]
            for line in table2:
                q.append(line)
                if table[int(bond*4)][0] in line:
                    break
            print(len(q))
            if table[int(bond*4+2)][0] == table[int(bond*4)][0]:
                table2.insert(len(q),[table[int(bond*4)][0],'','','',str(4),'','','','',str(table3[int(bond*2)][0]),'',str(float(table3[int(bond*2)][2])),'','',str(table3[int(bond*2)][5])])
            elif table[int(bond*4+1)][0] == table[int(bond*4)][0]:
                table2.insert(len(q),[table[int(bond*4)][0],'','','',str(4),'','','','',str(table3[int(bond*2)][0]),'',str(float(table3[int(bond*2)][2])),'','',str(table3[int(bond*2)][5])])
            elif table[int(bond*4)][0] not in [table[int(bond*4+1)][0],table[int(bond*4+2)][0]]:
                table2.insert(len(q),[table[int(bond*4)][0],'','','',str(1),'','','','',str(float(table3[int(bond*2)][0])/4),'',str(table3[int(bond*2)][2]),'','',str(table3[int(bond*2)][5])])

            for line in table2:
                if table[int(bond*4+1)][0] in line:
                    if table[int(bond*4+1)][0] not in [table[int(bond*4+3)][0],table[int(bond*4)][0]]:
                        line[4]=str(round(1))  
                        line[9]=str(float(table3[int(bond*2+1)][0])/4)
                        line[11]=str(float(table3[int(bond*2+1)][2])-float(table3[int(bond*2+1)][5])*180)
                        line[14]=str(float(table3[int(bond*2+1)][5]))
                if ('IMPROPER') in line:
                    break
            q=[]
            for line in table2:
                q.append(line)
                if table[int(bond*4+1)][0] in line:
                    break
            print(len(q))
            if table[int(bond*4+1)][0] not in [table[int(bond*4+3)][0],table[int(bond*4)][0]]:
                table2.insert(len(q),[table[int(bond*4+1)][0],'','','',str(1),'','','','',str(float(table3[int(bond*2)][0])/4),'',str(float(table3[int(bond*2)][2])+float(table3[int(bond*2)][5])*180),'','',str(table3[int(bond*2)][5])])

            for line in table2:
                if table[int(bond*4+2)][0] in line:
                    if table[int(bond*4+2)][0] not in [table[int(bond*4+3)][0],table[int(bond*4)][0]]:
                        line[4]=str(round(1))  
                        line[9]=str(float(table3[int(bond*2+1)][0])/4)
                        line[11]=str(float(table3[int(bond*2+1)][2])-float(table3[int(bond*2+1)][5])*180)
                        line[14]=str(float(table3[int(bond*2+1)][5]))

                if ('IMPROPER') in line:
                    break
            q=[]
            for line in table2:
                q.append(line)
                if table[int(bond*4+2)][0] in line:
                    break
            print(len(q))
            if table[int(bond*4+2)][0] not in [table[int(bond*4+3)][0],table[int(bond*4)][0]]:
                table2.insert(len(q),[table[int(bond*4+2)][0],'','','',str(1),'','','','',str(float(table3[int(bond*2)][0])/4),'',str(float(table3[int(bond*2)][2])+180*float(table3[int(bond*2)][5])),'','',str(table3[int(bond*2)][5])])


            for line in table2:
                if table[int(bond*4+3)][0] in line:
                    if table[int(bond*4+3)][0] == table[int(bond*4+1)][0]:
                        line[4]=str(round(4))  
                        line[9]=str(table3[int(bond*2+1)][0])
                        line[11]=str(float(table3[int(bond*2+1)][2]))
                        line[14]=str(table3[int(bond*2+1)][5])
                    elif table[int(bond*4+3)][0] == table[int(bond*4+2)][0]:
                        line[4]=str(round(4))  
                        line[9]=str(table3[int(bond*2+1)][0])
                        line[11]=str(float(table3[int(bond*2+1)][2]))
                        line[14]=str(table3[int(bond*2+1)][5])
                    elif table[int(bond*4+3)][0] not in [table[int(bond*4+1)][0],table[int(bond*4+2)][0]]:
                        line[4]=str(round(1))  
                        line[9]=str(float(table3[int(bond*2+1)][0])/4)
                        line[11]=str(float(table3[int(bond*2+1)][2]))
                        line[14]=str(table3[int(bond*2+1)][5])

                if ('IMPROPER') in line:
                    break
            q=[]
            for line in table2:
                q.append(line)
                if table[int(bond*4+3)][0] in line:
                    break
            print(len(q))
            if table[int(bond*4+3)][0] == table[int(bond*4+1)][0]:
                table2.insert(len(q),[table[int(bond*4+3)][0],'','','',str(4),'','','','',str(table3[int(bond*2)][0]),'',str(float(table3[int(bond*2)][2])),'','',str(table3[int(bond*2)][5])])
            elif table[int(bond*4+3)][0] == table[int(bond*4+2)][0]:
                table2.insert(len(q),[table[int(bond*4+3)][0],'','','',str(4),'','','','',str(table3[int(bond*2)][0]),'',str(float(table3[int(bond*2)][2])),'','',str(table3[int(bond*2)][5])])

            elif table[int(bond*4+3)][0] not in [table[int(bond*4+1)][0],table[int(bond*4+2)][0]]:
                table2.insert(len(q),[table[int(bond*4+3)][0],'','','',str(1),'','','','',str(float(table3[int(bond*2)][0])/4),'',str(float(table3[int(bond*2)][2])),'','',str(table3[int(bond*2)][5])])
        
        w=open(param+n[:-4]+'.frcmod', 'w')
        for line in table2:           
            #print(line)
            w.write(' '.join(line)+'\n')
        w.close()
        
