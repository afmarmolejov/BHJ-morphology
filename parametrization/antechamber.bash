#! /bin/bash
for file in `ls babel/*mol2`; do
     echo $file
     antechamber -i $file -fi mol2 -fo mol2 -o ${file/babel/antechamber} -at gaff2
done
rm ANTECHAMBER_AC.AC
rm ANTECHAMBER_AC.AC0
rm ANTECHAMBER_BOND_TYPE.AC
rm ANTECHAMBER_BOND_TYPE.AC0
rm ATOMTYPE.INF

for i in `ls babel/*mol2`; do
     echo $i
     antechamber -i $i -fi mol2 -fo pdb -o ${i/babel/antechamber_pdb} -at gaff2
done
rm ANTECHAMBER_AC.AC
rm ANTECHAMBER_AC.AC0
rm ANTECHAMBER_BOND_TYPE.AC
rm ANTECHAMBER_BOND_TYPE.AC0
rm ATOMTYPE.INF

for j in `ls antechamber_pdb/*.mol2`; do
     echo $j
     mv $j ${j/mol2/pdb}
done
