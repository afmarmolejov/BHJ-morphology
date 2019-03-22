import sys
import os
import shutil


######## Canonical and atom numbering 
#
if os.path.exists("babel/"):
   shutil.rmtree("babel/")
   os.mkdir("babel/")
else:
   os.mkdir("babel/")

os.system("babel mols/*smi babel/*.mol2 --canonical -h --gen3D")

###antechamber inputs
if os.path.exists("antechamber/"):
   shutil.rmtree("antechamber/")
   os.mkdir("antechamber/")
else:
   os.mkdir("antechamber/")

if os.path.exists("antechamber_pdb/"):
   shutil.rmtree("antechamber_pdb/")
   os.mkdir("antechamber_pdb/")
else:
   os.mkdir("antechamber_pdb/")

os.system("bash antechamber.bash")


indir="./antechamber/"
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
	os.system("babel antechamber_pdb/"+n[:-5]+".pdb antechamber_pdb/"+n[:-5]+".sdf")
####

######## Rotable bonds id
#
os.system("tar -xvf ComputeRotableAndDihedralAngles.tar")
indir="./antechamber_pdb/"
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        os.system("cp antechamber_pdb/"n" ComputeRotableAndDihedralAngles/dist/")

os.system("cd ComputeRotableAndDihedralAngles/dist/ && java -jar ComputeRotableAndDihedralAngles.jar")
if os.path.exists("dihedral_id/"):
   shutil.rmtree("dihedral_id/")
   os.mkdir("dihedral_id/")
else:
   os.mkdir("dihedral_id/")

indir="antechamber/"
for root, dirs, filenames in os.walk(indir):
    for n in filenames:
        os.system("cp ComputeRotableAndDihedralAngles/dist/"+n[:-5]+".sdf.txt dihedral_id/"+n[:-5]+".txt")
shutil.rmtree("ComputeRotableAndDihedralAngles/")
shutil.rmtree("antechamber_pdb")
###

########## AMBER gaff2 dihedral parameters (.frcmod)
if os.path.exists("frcmod/"):
   shutil.rmtree("frcmod")
   os.mkdir("frcmod")
else:
   os.mkdir("frcmod")

os.system("bash frcmod.bash")

##### numbering and AMBER atom type 
os.system("python numbering_dihedral.py")
os.system("python AMBER_dihedral.py")
##


###### corrected_dihedral_atom_name
os.system("python corrected_dihedral.py")


####### Qchem inputs
####### Charge basal
os.system("python basal_q.py")
##outputs into Hirsfield_iter_basal
############# Charge to .mol2 input
os.system("python antechamber_q.py")


######New atoms assignation


###### frcmod_basal and mol2_basal
os.system("python frcmod_mol2_basal.py")
##### new AMBER atom type basal
os.system("python AMBER_dihedral_new.py")
###### new numbering dihedral_basal
os.system("python numbering_dihedral_basal.py")
###### new corrected_dihedral_atom_name_basal
os.system("python corrected_dihedral_basal.py")


####scan sander (turn_off AMBER parameters)
os.system("python frcmod_basal_zero.py")
os.system("python mol2_basal_0.py")
os.system("python scan_sander_basal.py")
##wait for outputs in scan_sander_basal ### visualize the .sd with pymol

####scan QM (QChem)
os.system("python scan_qchem_basal.py")
os.system("python scan_qchem_miztli.py")
#wait for outputs to save into out_scan_qchem_basal
os.system("python video_qchem_basal.py")
#visualize the .sd extension by pymol


##parameter optimization
os.system("python basal_param.py")

##Final parameters frcmod
os.system("python frcmod_basal_param.py")

####scan sander verification (turn_on new AMBER parameters)
os.system("python scan_sander_basal_param.py")
##wait for outputs into scan_sander_basal_param ### visualize the .sd with pymol












