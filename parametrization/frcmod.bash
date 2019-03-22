#! /bin/bash
for file in `ls antechamber/*mol2`; do
     echo $file
     parmchk -i $file -f mol2 -o ${file/antechamber/frcmod} -s 2 -a Y
     rm ANTECHAMBER.FRCMOD
done

for j in `ls frcmod/*.mol2`; do
     echo $j
     mv $j ${j/mol2/frcmod}
done
