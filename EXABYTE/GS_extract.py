#!/usr/bin/env python

from __future__ import division 
from numpy import *
from pylab import *
import os





def plot_conv(conv_selection, Material, diffE_target):


  if conv_selection == 1:
    conv_param='ecut'
  elif conv_selection == 2:
    conv_param='kgrid'





  list_files=os.listdir('GS_Plots/'+Material+'/conv_test')
  range_param=[]
  for i in range(len(list_files)):
   if list_files[i].split('_')[0]=='OUTCAR':
     range_param.append(float(list_files[i].split('_')[1]))

  range_param.sort()


  #list of ecut parameter across datasets (x axis)
  param_lower_bound=[None]*(len(range_param)-1)
  for k in range(len(param_lower_bound)):
    param_lower_bound[k]=range_param[k]

  

  #extract etot values from output file 
  etot=[None]*len(range_param)
  for n in range(len(range_param)):
          output_file=open('GS_Plots/'+Material+'/conv_test/OSZICAR_'+str(range_param[n]))
          output_file_lines=output_file.readlines()
          for i in range(len(output_file_lines)):
            if 'E0' in output_file_lines[i]:
              etot[n]=float(output_file_lines[i].split()[4])
              break



  #extract pressure values from output file 
  ptot=[None]*len(range_param)
  for n in range(len(range_param)):
       stress_tensor=empty((3,3))
       output_file=open('GS_Plots/'+Material+'/conv_test/OUTCAR_'+str(range_param[n]))
       list_lines=output_file.readlines()

       for i in range(len(list_lines)-1, 0, -1): 
         if 'in kB' in list_lines[i]:
          for j in range(3):
            stress_tensor[j,j]=-float(list_lines[i].split()[j+2])            
          stress_tensor[2,1]=stress_tensor[1,2]=-float(list_lines[i].split()[6])
          stress_tensor[2,0]=stress_tensor[0,2]=-float(list_lines[i].split()[7])
          stress_tensor[1,0]=stress_tensor[0,1]=-float(list_lines[i].split()[5])

          ptot[n]=-(stress_tensor.trace())/3
          break




  delta_etot=[None]*(len(range_param)-1)
  for k in range(len(delta_etot)):
     delta_etot[k]=abs(etot[k+1]-etot[k])


  m=0
  for k in range(len(delta_etot)):
   if delta_etot[k] < diffE_target:
    m=m+1
    if m==2:
      if conv_param=='kgrid':
        print 'First kgrid parameter to satisfy convergence criterion is: '+str(int(param_lower_bound[k-1]))+'X'+str(int(param_lower_bound[k-1]))+'X'+str(int(param_lower_bound[k-1]))+' Monkhorst-Pack grid of k-points'
        break
      elif conv_param=='ecut':
        print 'First ecut parameter to satisfy convergence criterion is: '+str(param_lower_bound[k-1])+' eV'
        break
   else:
    m=0 
  else:
    print 'Convergence criterion not satisfied yet....'

      
     

  #write data to file
  diff_file=open('GS_Plots/'+Material+'/conv_test/diff_E.dat','w')
  for n in range(len(range_param)-1):
      print >> diff_file, str(range_param[n])+'   '+str(delta_etot[n])
  diff_file.close()

  #write data to file
  diff_file=open('GS_Plots/'+Material+'/conv_test/E.dat','w')
  for n in range(len(range_param)):
       print >> diff_file, str(range_param[n])+'   '+str(etot[n])   
  diff_file.close()







  #plot using matplotlib
  fig = figure()
  ax1 = fig.add_subplot(111)

  if conv_param=='kgrid': 
   xlabel('kgrid')
  elif conv_param=='ecut': 
   xlabel('ecut (eV)')

  ylabel(r'$\Delta$'+'E (eV)')


  semilogy(param_lower_bound, delta_etot)
  scatter(param_lower_bound, delta_etot)


  xlimits=list(linspace(ax1.get_xlim()[0], ax1.get_xlim()[1], 100))
  plot(xlimits, [diffE_target]*len(xlimits), 'k-', label='target')  
  legend()
  savefig('GS_Plots/'+Material+'/'+conv_param+'.png')
  close(fig)
  return param_lower_bound, delta_etot






  





  




