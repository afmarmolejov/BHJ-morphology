#! /bin/bash
for file in `ls charge/*xyz`; do
     echo $file
     sed '1,2d' $file > ${file/charge/charge2}
done

for i in `ls charge2/*xyz`; do
     echo $i
     cat qchem.header_charge_basal $i qchem.footer_charge_basal > ${i/charge2/basal_q}
done

for j in `ls basal_q/*xyz`; do
     echo $j
     mv $j ${j/xyz/qcin}
done

