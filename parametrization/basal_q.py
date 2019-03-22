import os
import shutil


indir='./'

header_basal=open(indir+'qchem.header_charge_basal', 'w')
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

footer_basal=open(indir+'qchem.footer_charge_basal', 'w')
footer_basal.write('$end'+'\n')
footer_basal.write('\n')
footer_basal.write('@@@'+'\n')
footer_basal.write('\n')
footer_basal.write('$comment'+'\n')
footer_basal.write('   HIRSHFELD_BASAL'+'\n')
footer_basal.write('$end'+'\n')
footer_basal.write('\n')
footer_basal.write('$rem'+'\n')
footer_basal.write('   SYM_IGNORE TRUE'+'\n')
footer_basal.write('   JOBTYPE SP'+'\n')
footer_basal.write('   EXCHANGE omegaB97X-D'+'\n')
footer_basal.write('   BASIS cc-pVTZ'+'\n')
footer_basal.write('   HIRSHITER TRUE'+'\n')
footer_basal.write('   MEM_STATIC 5000'+'\n')
footer_basal.write('   MEM_TOTAL 20000'+'\n')
footer_basal.write('$end'+'\n')
footer_basal.write('\n')
footer_basal.write('$molecule'+'\n')
footer_basal.write('   READ'+'\n')
footer_basal.write('$end'+'\n')
footer_basal.close()

os.mkdir(indir+"charge")
os.mkdir(indir+"charge2")

if os.path.exists(indir+"basal_q/"):
    shutil.rmtree(indir+"basal_q")
    os.mkdir(indir+"basal_q")
else:
    os.mkdir(indir+"basal_q")
    
os.system("babel "+indir+"babel/*.mol2 "+indir+"charge/*.xyz")
os.system("cd "+indir+"&& bash basal_q.bash")
os.system("rm "+indir+'qchem.footer_charge_basal '+indir+'qchem.header_charge_basal')
shutil.rmtree(indir+"charge/")
shutil.rmtree(indir+"charge2/")
