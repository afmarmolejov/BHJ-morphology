import os
import shutil
if os.path.exists("/home/andrexfelo/proyecto_amador/SOLAR_CELL/frcmod_basal_zero"):
    shutil.rmtree("/home/andrexfelo/proyecto_amador/SOLAR_CELL/frcmod_basal_zero")
    os.mkdir("/home/andrexfelo/proyecto_amador/SOLAR_CELL/frcmod_basal_zero")
else:
    os.mkdir("/home/andrexfelo/proyecto_amador/SOLAR_CELL/frcmod_basal_zero")
zero="/home/andrexfelo/proyecto_amador/SOLAR_CELL/frcmod_basal_zero/"
indir = '/home/andrexfelo/proyecto_amador/SOLAR_CELL/AMBER_dihedral_new/'
frcdir='/home/andrexfelo/proyecto_amador/SOLAR_CELL/frcmod_basal/'
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        print(n)
        f = open(indir+n, 'r')
        table = [line.rstrip().split(" ") for line in f.readlines()]
        frcmod=open(frcdir+f.name[len(indir):-4]+'.frcmod', 'r')
        table2 = [line.rstrip().split(" ") for line in frcmod.readlines()]
        w=open(zero+n[:-4]+'.frcmod', 'w')
        for line in table2:
            if table[0][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[1][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[2][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[3][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[4][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[5][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[6][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[7][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[8][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break 
        for line in table2:
            if table[9][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[10][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:
            if table[11][0] in line:
                line[9]='0.00000000'              
            if ('IMPROPER') in line:
                break
        for line in table2:           
            w.write(' '.join(line)+'\n')
        w.close()
