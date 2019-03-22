import os
import shutil
if os.path.exists('/home/andrexfelo/proyecto_amador/SOLAR_CELL/mol2_basal_0/'):
    shutil.rmtree('/home/andrexfelo/proyecto_amador/SOLAR_CELL/mol2_basal_0/')
    os.mkdir('/home/andrexfelo/proyecto_amador/SOLAR_CELL/mol2_basal_0/')
else:
    os.mkdir('/home/andrexfelo/proyecto_amador/SOLAR_CELL/mol2_basal_0/')
indir = '/home/andrexfelo/proyecto_amador/SOLAR_CELL/mol2_basal/'
seqdir='/home/andrexfelo/proyecto_amador/SOLAR_CELL/corrected_dihedral_basal/'
outdir='/home/andrexfelo/proyecto_amador/SOLAR_CELL/mol2_basal_0/'
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        print(n)
        f = open(seqdir+n[:-5]+'.dat', 'r')
        table = [line.rstrip().split("-") for line in f.readlines()]
        leap=open(indir+n[:-5]+'.leap', 'w')    
        leap.write('LIG = loadmol2 '+n+'\n')
        leap.write('impose LIG {1}, { {"'+table[0][0]+'" "'+table[0][1]+'" "'+table[0][2]+'" "'+table[0][3]+'" 45 } }'+'\n')    
        leap.write('impose LIG {1}, { {"'+table[4][0]+'" "'+table[4][1]+'" "'+table[4][2]+'" "'+table[4][3]+'" 145 } }'+'\n')    
        leap.write('impose LIG {1}, { {"'+table[8][0]+'" "'+table[8][1]+'" "'+table[8][2]+'" "'+table[8][3]+'" 270 } }'+'\n')    
        leap.write('charge LIG'+'\n')
        leap.write('savemol2 LIG ../mol2_basal_0/'+n+' 1'+'\n')
        leap.write('quit'+'\n')
        leap.close()
        cmd='cd '+indir+' && tleap -f '+n[:-5]+'.leap'
        cmd2='cd '+indir+' && rm '+n[:-5]+'.leap'
        os.system(cmd)
        os.system(cmd2)
