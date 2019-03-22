import numpy as npy
import sys
from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators
from pyevolve import Initializators
from pyevolve import GAllele
#import pyevolve
import math

gaussian_file=sys.argv[1]
sander_file=sys.argv[2]

gaussian=map(float,open(gaussian_file).read().split())
sander=map(float,open(sander_file).read().split())
angles=[0,	15,	30,	45,	60,	75,	90,	105,	120,	135,	150,	165,	180,	195,	210,	225,	240,	255,	270,	285,	300,	315,	330,	345,	360]


###########################################################
##  TWO CURVE FITTING
###########################################################
def calc_fitted_2graphs(PKIDVF1,PN1,PHASE1,PKIDVF2,PN2,PHASE2):
	values=[]
	for i,ANGLE in enumerate(angles):
		EDIHEDRAL1=PKIDVF1*(1+math.cos(math.radians(PN1*ANGLE-PHASE1)))
		EDIHEDRAL2=PKIDVF2*(1+math.cos(math.radians(PN2*ANGLE-PHASE2)))
		values.append(EDIHEDRAL1+EDIHEDRAL2+sander[i])
	values=npy.array(values)
	values=values-min(values)
	err=[]
	for i,value in enumerate(values):
		err.append(value-gaussian[i])
	err=npy.array(err)
	rmsd=npy.sqrt(npy.sum(err**2)/len(err))
	return rmsd


#function for ranking chromosomes
def eval_func_2graphs(chromosome):
	score=0.0
	rmsd=calc_fitted_2graphs(chromosome[0],chromosome[1],chromosome[2],chromosome[6]*chromosome[3],chromosome[4],chromosome[5])
	if chromosome[1] == chromosome[4] and chromosome[2] == chromosome[5] and chromosome[6] == 1:
		rmsd=rmsd*2	
	score=1/rmsd
	return score

#initialize alleles	
setOfAlleles=GAllele.GAlleles()

#first variable
pkidvf=npy.arange(0.1,30.1,0.1)
setOfAlleles.add(GAllele.GAlleleList(pkidvf))
#second variable
pn=npy.arange(1,8.1,1)
setOfAlleles.add(GAllele.GAlleleList(pn))
#third variable
phase=npy.arange(0,360.1,10)
setOfAlleles.add(GAllele.GAlleleList(phase))

#repeat assignment of variables for second curve
setOfAlleles.add(GAllele.GAlleleList(pkidvf))
setOfAlleles.add(GAllele.GAlleleList(pn))
setOfAlleles.add(GAllele.GAlleleList(phase))

#binary value for using 1 or 2 functions
func1or2=[0,1]
setOfAlleles.add(GAllele.GAlleleList(func1or2))

#initialize genome with defined alleles
genome = G1DList.G1DList(7)
genome.setParams(allele=setOfAlleles)

#define evaluator function
genome.evaluator.set(eval_func_2graphs)
genome.mutator.set(Mutators.G1DListMutatorAllele)
genome.initializator.set(Initializators.G1DListInitializatorAllele)

ga = GSimpleGA.GSimpleGA(genome)
ga.selector.set(Selectors.GTournamentSelector)
ga.setCrossoverRate(0.7)
ga.setElitism(False)
ga.setGenerations(30000)
ga.evolve(freq_stats=3000)

best=ga.bestIndividual()
############################################################
#GET values

#only one plot for optimization

print ("The optimized values for 2 functions are:")
print ("Function 1:")
print ("PK/IDIVF    PHASE    PN")
print(str(best[0])+'0000000'+'  '+str(best[2])+'00'+'   '+str(best[1]))
print ("Function 2:")
print ("PK/IDIVF    PHASE    PN")
print(str(best[3])+'0000000'+'  '+str(best[5])+'00'+'   '+'-'+str(best[4]))
	
	
###########################
# Script created for Parametrization tutorial
# Date: 31/05/2013
# Author: Sergio Ruiz
# Mail: sruizcarmona@gmail.com
# Summary:
# Optimization of dihedral parameters to fit a reference profile using a genetic algorithm.
# Arguments: 1.- reference energies (Gaussian) 2.- energies to fit (Sander)
###########################
