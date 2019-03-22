#!/bin/sh

#######################
# to run execute: sh run_all_sander_param.sh <dihedral atom 1> <dihedral atom 2> <dihedral atom 3> <dihedral atom 4> <root name of all files>
#######################

#degrees, from 0 to 360 15 by 15
number=`seq 0 15 360`
rank=10000 #used in dihedral restraint (force)
rest2=2500
an_r1=${50}  #angle 1_1
an_r2=${51}  # angle 2_1
a_r1_1=`echo $an_r1-0.1 | bc | awk '{printf "%f", $0}'`
a_r1_2=`echo $an_r1+0.1 | bc | awk '{printf "%f", $0}'`
a_r2_1=`echo $an_r2-0.1 | bc | awk '{printf "%f", $0}'`
a_r2_2=`echo $an_r2+0.1 | bc`



an_r3=${52}  #angle 1_2
an_r4=${53}  # angle 2_2
a_r3_1=`echo $an_r3-0.1 | bc | awk '{printf "%f", $0}'`
a_r3_2=`echo $an_r3+0.1 | bc | awk '{printf "%f", $0}'`
a_r4_1=`echo $an_r4-0.1 | bc | awk '{printf "%f", $0}'`
a_r4_2=`echo $an_r4+0.1 | bc | awk '{printf "%f", $0}'`



an_r5=${54}  #angle 1_3
an_r6=${55}  # angle 2_3
a_r5_1=`echo $an_r5-0.1 | bc | awk '{printf "%f", $0}'`
a_r5_2=`echo $an_r5+0.1 | bc | awk '{printf "%f", $0}'`
a_r6_1=`echo $an_r6-0.1 | bc | awk '{printf "%f", $0}'`
a_r6_2=`echo $an_r6+0.1 | bc | awk '{printf "%f", $0}'`


an_r7=${56}  #angle 1_4
an_r8=${57}  # angle 2_4
a_r7_1=`echo $an_r7-0.1 | bc | awk '{printf "%f", $0}'`
a_r7_2=`echo $an_r7+0.1 | bc | awk '{printf "%f", $0}'`
a_r8_1=`echo $an_r8-0.1 | bc | awk '{printf "%f", $0}'`
a_r8_2=`echo $an_r8+0.1 | bc | awk '{printf "%f", $0}'`


#define dihedral atoms to scan
dihedral_atom1=$1
dihedral_atom2=$2
dihedral_atom3=$3
dihedral_atom4=$4
#dihedral_atom5=${13}
#dihedral_atom6=${14}
#dihedral_atom7=${15}
#dihedral_atom8=${16} 
#dihedral_atom9=${25}
#dihedral_atom10=${26}
#dihedral_atom11=${27}
#dihedral_atom12=${28}
dihedral_atom13=${37}
dihedral_atom14=${38}
dihedral_atom15=${39}
dihedral_atom16=${40} 
 
#define dihedral atoms to restrain
#dihedral1
dihedral_atom17=$5
dihedral_atom18=$6
dihedral_atom19=$7
dihedral_atom20=$8
dihedral_atom21=${17}
dihedral_atom22=${18}
dihedral_atom23=${19}
dihedral_atom24=${20}
dihedral_atom25=${29}
dihedral_atom26=${30}
dihedral_atom27=${31}
dihedral_atom28=${32}
dihedral_atom29=${41}
dihedral_atom30=${42}
dihedral_atom31=${43}
dihedral_atom32=${44}

#dihedral2
 
dihedral_atom33=$9
dihedral_atom34=${10}
dihedral_atom35=${11}
dihedral_atom36=${12}
dihedral_atom37=${21}
dihedral_atom38=${22}
dihedral_atom39=${23}
dihedral_atom40=${24}
dihedral_atom41=${33}
dihedral_atom42=${34}
dihedral_atom43=${35}
dihedral_atom44=${36}
dihedral_atom45=${45}
dihedral_atom46=${46}
dihedral_atom47=${47}
dihedral_atom48=${48}

#define root name for all files
rootname=${49}

#first, run tleap!
#template for tleap file, will write $rootname.tleap
tleapfile="
loadAmberParams frcmod_basal_zero/$rootname.frcmod\n
LIG = loadmol2 mol2_basal_0/$rootname.mol2\n
check LIG\n
charge LIG\n
saveamberparm LIG scan_sander_basal/$rootname.prmtop scan_sander_basal/$rootname.inpcrd\n
saveOff LIG scan_sander_basal/$rootname.lib\n
quit\n";
echo $tleapfile > $rootname.tleap;

#run tleap as defined above
tleap -f $rootname.tleap;

#template for dihedral restraints file, save it in $dih_file
dih_file="&rst iat= DIH_1, DIH_2, DIH_3, DIH_4,\n
r1=AN_PREV00000, r2=ANG.000000, r3=ANG.000000, r4=ANG.100000, rk2=RANK.0, rk3=RANK.0, &end \n



\n
&rst iat= DIHI_13, DIHI_14, DIHI_15, DIHI_16,\n
r1=AN_PREV00000, r2=ANG.000000, r3=ANG.000000, r4=ANG.100000, rk2=REST.0, rk3=REST.0, &end \n 
\n

&rst iat= DIHR_1, DIHR_2, DIHR_3, DIHR_4,\n
r1=A_R1_1, r2=AN_R1, r3=AN_R1, r4=A_R1_2, rk2=RANK.0, rk3=RANK.0, &end \n

\n
&rst iat= DIHR_5, DIHR_6, DIHR_7, DIHR_8,\n
r1=A_R3_1, r2=AN_R3, r3=AN_R3, r4=A_R3_2, rk2=RANK.0, rk3=RANK.0, &end \n
\n
&rst iat= DIHR_9, DIHS_10, DIHS_11, DIHS_12,\n
r1=A_R5_1, r2=AN_R5, r3=AN_R5, r4=A_R5_2, rk2=RANK.0, rk3=RANK.0, &end \n
\n
&rst iat= DIHS_13, DIHS_14, DIHS_15, DIHS_16,\n
r1=A_R7_1, r2=AN_R7, r3=AN_R7, r4=A_R7_2, rk2=RANK.0, rk3=RANK.0, &end \n

\n
&rst iat= DIHU_1, DIHU_2, DIHU_3, DIHU_4,\n
r1=A_R2_1, r2=AN_R2, r3=AN_R2, r4=A_R2_2, rk2=RANK.0, rk3=RANK.0, &end \n

\n
&rst iat= DIHU_5, DIHU_6, DIHU_7, DIHU_8,\n
r1=A_R4_1, r2=AN_R4, r3=AN_R4, r4=A_R4_2, rk2=RANK.0, rk3=RANK.0, &end \n
\n
&rst iat= DIHU_9, DIHV_10, DIHV_11, DIHV_12,\n
r1=A_R6_1, r2=AN_R6, r3=AN_R6, r4=A_R6_2, rk2=RANK.0, rk3=RANK.0, &end \n
\n
&rst iat= DIHV_13, DIHV_14, DIHV_15, DIHV_16,\n
r1=A_R8_1, r2=AN_R8, r3=AN_R8, r4=A_R8_2, rk2=RANK.0, rk3=RANK.0, &end \n"


#\n
#&rst iat= DIHI_13, DIHI_14, DIHI_15, DIHI_16,\n
#r1=AN_PREV00000, r2=ANG.000000, r3=ANG.000000, r4=ANG.100000, rk2=RANK.0, rk3=RANK.0, &end \n 
#\n

#&rst iat= DIH_9, DIHI_10, DIHI_11, DIHI_12,\n
#r1=AG_PREV00000, r2=AGN.000000, r3=AGN.000000, r4=AGN.100000, rk2=RANK.0, rk3=RANK.0, &end \n 
#\n

#\n
#&rst iat= DIH_5, DIH_6, DIH_7, DIH_8,\n
#r1=AG_PREV00000, r2=AGN.000000, r3=AGN.000000, r4=AGN.100000, rk2=REST.0, rk3=REST.0, &end \n





echo $dih_file > dihedral_TEMPLATE.f;

#for each angle, use dihedral_TEMPLATE.f to create the restraint files for sander
if [ -e dih_tmp ]; then rm dih_tmp/*; else mkdir dih_tmp; fi
for N in $number;
do
        angprev_num=`echo $N-1 | bc`

        
        if [ $N = 0 ]; then 
	       M=`echo $N+180 | bc`
               ang_prev=-0.1
               ag_prev=179.9

        else 
	       M=`echo $N+180 | bc`
	       angprev_nun2=`echo $M-1 | bc`
               ang_prev=$angprev_num.9
               ag_prev=$angprev_nun2.9
               
        fi

        sed 's/DIH_1/'$dihedral_atom1'/g' dihedral_TEMPLATE.f | sed 's/DIH_2/'$dihedral_atom2'/g' | sed 's/DIH_3/'$dihedral_atom3'/g' | sed 's/DIH_4/'$dihedral_atom4'/g' | sed 's/AN_PREV/'$ang_prev'/g' | sed 's/ANG/'$N'/g' | sed 's/RANK/'$rank'/g' | sed 's/DIHI_13/'$dihedral_atom13'/g' | sed 's/DIHI_14/'$dihedral_atom14'/g' | sed 's/DIHI_15/'$dihedral_atom15'/g' | sed 's/DIHI_16/'$dihedral_atom16'/g' | sed 's/REST/'$rest2'/g' | sed 's/DIHR_1/'$dihedral_atom17'/g' | sed 's/DIHR_2/'$dihedral_atom18'/g' | sed 's/DIHR_3/'$dihedral_atom19'/g' | sed 's/DIHR_4/'$dihedral_atom20'/g' | sed 's/AN_R1/'$an_r1'/g' | sed 's/A_R1_1/'$a_r1_1'/g' | sed 's/A_R1_2/'$a_r1_2'/g' | sed 's/DIHR_5/'$dihedral_atom21'/g' | sed 's/DIHR_6/'$dihedral_atom22'/g' | sed 's/DIHR_7/'$dihedral_atom23'/g' | sed 's/DIHR_8/'$dihedral_atom24'/g' | sed 's/AN_R3/'$an_r3'/g' | sed 's/A_R3_1/'$a_r3_1'/g' | sed 's/A_R3_2/'$a_r3_2'/g' | sed 's/DIHR_9/'$dihedral_atom25'/g' | sed 's/DIHS_10/'$dihedral_atom26'/g' | sed 's/DIHS_11/'$dihedral_atom27'/g' | sed 's/DIHS_12/'$dihedral_atom28'/g' | sed 's/AN_R5/'$an_r5'/g' | sed 's/A_R5_1/'$a_r5_1'/g' | sed 's/A_R5_2/'$a_r5_2'/g' | sed 's/DIHS_13/'$dihedral_atom29'/g' | sed 's/DIHS_14/'$dihedral_atom30'/g' | sed 's/DIHS_15/'$dihedral_atom31'/g' | sed 's/DIHS_16/'$dihedral_atom32'/g' | sed 's/AN_R7/'$an_r7'/g' | sed 's/A_R7_1/'$a_r7_1'/g' | sed 's/A_R7_2/'$a_r7_2'/g' | sed 's/DIHU_1/'$dihedral_atom33'/g' | sed 's/DIHU_2/'$dihedral_atom34'/g' | sed 's/DIHU_3/'$dihedral_atom35'/g' | sed 's/DIHU_4/'$dihedral_atom36'/g' | sed 's/AN_R2/'$an_r2'/g' | sed 's/A_R2_1/'$a_r2_1'/g' | sed 's/A_R2_2/'$a_r2_2'/g' | sed 's/DIHU_5/'$dihedral_atom37'/g' | sed 's/DIHU_6/'$dihedral_atom38'/g' | sed 's/DIHU_7/'$dihedral_atom39'/g' | sed 's/DIHU_8/'$dihedral_atom40'/g' | sed 's/AN_R4/'$an_r4'/g' | sed 's/A_R4_1/'$a_r4_1'/g' | sed 's/A_R4_2/'$a_r4_2'/g' | sed 's/DIHU_9/'$dihedral_atom41'/g' | sed 's/DIHV_10/'$dihedral_atom42'/g' | sed 's/DIHV_11/'$dihedral_atom43'/g' | sed 's/DIHV_12/'$dihedral_atom44'/g' | sed 's/AN_R6/'$an_r6'/g' | sed 's/A_R6_1/'$a_r6_1'/g' | sed 's/A_R6_2/'$a_r6_2'/g' | sed 's/DIHV_13/'$dihedral_atom45'/g' | sed 's/DIHV_14/'$dihedral_atom46'/g' | sed 's/DIHV_15/'$dihedral_atom47'/g' | sed 's/DIHV_16/'$dihedral_atom48'/g' | sed 's/AN_R8/'$an_r8'/g' | sed 's/A_R8_1/'$a_r8_1'/g' | sed 's/A_R8_2/'$a_r8_2'/g' > dih_tmp/dihedral_$N.f 



#| sed 's/DIH_9/'$dihedral_atom9'/g' | sed 's/DIHI_10/'$dihedral_atom10'/g' | sed 's/DIHI_11/'$dihedral_atom11'/g' | sed 's/DIHI_12/'$dihedral_atom12'/g' 

#| sed 's/DIH_5/'$dihedral_atom5'/g' | sed 's/DIH_6/'$dihedral_atom6'/g' | sed 's/DIH_7/'$dihedral_atom7'/g' | sed 's/DIH_8/'$dihedral_atom8'/g' | sed 's/AG_PREV/'$ag_prev'/g' | sed 's/AGN/'$M'/g'

#





done

echo "New restraints"

#run minimisations
#template file for min.in (will be changed for each minimisation step)
min_file="Minimization of IPR with dihedral constraints\n
&cntrl\n
imin=1,\n
ntb=0,\n
cut=999.,\n
maxcyc=30000,\n 
ntpr=1,\n
nmropt=1\n
/\n
&wt type='END'\n
/\n
DISANG=dih_tmp/dihedral_XXANGLEXX.f\n"
echo $min_file > min.in;

#for each angle, create input.in with correct dihedral restraint file, and run sander to minimize the structure
if [ -e scan_sander_basal/out_1_$rootname  ]; then rm scan_sander_basal/out_1_$rootname/*; else mkdir scan_sander_basal/out_1_$rootname; fi
for N in $number;
do
 sed -e 's/XXANGLEXX/'$N'/g' min.in > input.in
 if [ $N -lt 10 ]; then N=00$N; fi
 if [ $N -lt 100 -a $N -gt 9 ]; then N=0$N; fi
sanderexe=`which sander` 
 #$AMBERHOME/exe/sander -O -i input.in -o out_1_$rootname/${rootname}_$N.out -p ${rootname}.prmtop -c ${rootname}.inpcrd -r out_1_$rootname/${rootname}_$N.rst
 $sanderexe -O -i input.in -o scan_sander_basal/out_1_$rootname/${rootname}_$N.out -p scan_sander_basal/${rootname}.prmtop -c scan_sander_basal/${rootname}.inpcrd -r scan_sander_basal/out_1_$rootname/${rootname}_$N.inpcrd
done

echo "Run finished"
#remove sander_energies if exists
if [ -e sander_energies.txt ]; then rm sander_energies.txt; fi
#get FINAL RESULTS line and retrieve last step energies
for file in scan_sander_basal/out_1_$rootname/*.out;
do
	echo -n $file >> sander_energies.txt;
	sed -n $(echo `grep -n " FINAL " $file | awk '{print $1}' | sed 's/://'`+5 | bc )p $file >> sander_energies.txt
done
#save energies in a proper format (1 column with the energies sorted by angle)
awk '{printf "%.7f\n",$3}' sander_energies.txt > scan_sander_basal/out_1_$rootname/sander_1_$rootname.txt

#########OPTIONAL################
#create a sd file for visualization of all sander process in min_pdbs
if [ -e scan_sander_basal/min_pdbs ]; then rm scan_sander_basal/min_pdbs/*; else mkdir scan_sander_basal/min_pdbs; fi
for N in $number;
do
	if [ $N -lt 10 ]; then N=00$N; fi
	if [ $N -lt 100 -a $N -gt 9 ]; then N=0$N; fi
	ambpdb -p scan_sander_basal/${rootname}.prmtop -c scan_sander_basal/out_1_$rootname/${rootname}_$N.inpcrd > scan_sander_basal/min_pdbs/min_pdb_${rootname}_$N.pdb 2> /dev/null
	babel -ipdb scan_sander_basal/min_pdbs/min_pdb_${rootname}_$N.pdb -osd scan_sander_basal/min_pdbs/min_pdb_${rootname}_$N.sd 2> /dev/null
	cat scan_sander_basal/min_pdbs/min_pdb_${rootname}_$N.sd >> scan_sander_basal/out_1_$rootname/min_pdb_all_1.sd
done

##########CLEAN FILES#######
rm mdinfo
rm sander_energies.txt
rm dihedral_TEMPLATE.f
rm min.in
rm input.in
rm $rootname.tleap
rm leap.log
rm scan_sander_basal/out_1_$rootname/${rootname}*.inpcrd
rm scan_sander_basal/out_1_$rootname/${rootname}*.out
rm scan_sander_basal/$rootname.lib
rm scan_sander_basal/$rootname.inpcrd
rm scan_sander_basal/$rootname.prmtop
rm -r scan_sander_basal/min_pdbs/
#rm -r dih_temp/
############################

#################################

