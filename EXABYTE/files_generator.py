#!/usr/bin/env python

from __future__ import division







def incar_generator(ecut, tsmear):

  input_file_script="""SYSTEM = convergence study

ENCUT = """+str(ecut)+""" eV
ENAUG = """+str(4*ecut)+""" eV

ISMEAR = 1
SIGMA = """+str(tsmear)+"""
PREC= High
NCORE = 2

""" 


  input_file=open('working/INCAR', 'w')
  input_file.write(input_file_script)
  input_file.close()
###################################################################################################################################


def kpoints_generator(kgrid):

  kgrid=int(kgrid)
  shiftk=[[0.25, 0.25, 0.25]]

  input_file_script=str(kgrid)+"""x"""+str(kgrid)+"""x"""+str(kgrid)+""" Monkhorst-Pack grid of k-points
 0
Monkhorst 
 """+str(kgrid)+""" """+str(kgrid)+""" """+str(kgrid)+"""
""" 


  input_file=open('working/KPOINTS', 'w')
  input_file.write(input_file_script)
  for i in range(len(shiftk)):
    print >> input_file, str(shiftk[i][0]*kgrid)+""" """+str(shiftk[i][1]*kgrid)+""" """+str(shiftk[i][2]*kgrid)
  input_file.close()
###################################################################################################################################




##############################################################################################################################
################ POSCAR FILE
##############################################################################################################################

def poscar_generator(a_par, b_par, c_par, primitive_vectors, no_species, position_atoms_PUC):
  input_file_script="""Convergence study
"""+str(a_par)+""" """+str(b_par)+""" """+str(c_par)+""" 
"""+str(primitive_vectors[0][0])+""" """+str(primitive_vectors[0][1])+""" """+str(primitive_vectors[0][2])+"""
"""+str(primitive_vectors[1][0])+""" """+str(primitive_vectors[1][1])+""" """+str(primitive_vectors[1][2])+"""
"""+str(primitive_vectors[2][0])+""" """+str(primitive_vectors[2][1])+""" """+str(primitive_vectors[2][2])+"""
"""+str(no_species).strip('[]').replace(',', ' ')+"""
Direct
"""+str(position_atoms_PUC)+"""
""" 


  input_file=open('working/POSCAR', 'w')
  input_file.write(input_file_script)
  input_file.close()
###################################################################################################################################      
