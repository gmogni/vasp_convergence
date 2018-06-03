#!/usr/bin/env python

from __future__ import division
import matplotlib
matplotlib.use("Agg")

import wx
import wx.xrc
import wx.grid
import csv
from numpy import *
from math import *
import os
import commands
from files_generator import *
from GS_extract import *
import time
import threading
from pylab import *
import multiprocessing

from matplotlib.backends.backend_wxagg import FigureCanvas

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


elements_file=open('elementlist.csv', 'rb')
reader = list(csv.reader(elements_file))




###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame):
	
	def __init__( self, parent ):
                global gSizer333, m_gauge1

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'Convergence tests', pos = wx.DefaultPosition, size = wx.DisplaySize(),   style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )


		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer1 = wx.FlexGridSizer( 3, 1, 0, 0 )
		gSizer1.AddGrowableRow( 1,2 )
		gSizer1.AddGrowableCol( 0 )
		gSizer1.SetFlexibleDirection( wx.BOTH )
		gSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Atomic info" ), wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 2, 4, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Element 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer3.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		m_choice1Choices = [str(reader[i][0])+"  "+str(str(reader[i][1]))+"  "+str(str(reader[i][2])) for i in range(len(reader))]
		self.m_choice1 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		gSizer3.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )





		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer3.Add( self.m_spinCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Positions atoms", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		gSizer3.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		gSizer111 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Element 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer111.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_checkBox1 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer111.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		gSizer3.Add( gSizer111, 1, wx.EXPAND, 5 )
		
		m_choice2Choices = [str(reader[i][0])+"  "+str(str(reader[i][1]))+"  "+str(str(reader[i][2])) for i in range(len(reader))]
		self.m_choice2 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		gSizer3.Add( self.m_choice2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )




		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer3.Add( self.m_spinCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Positions atoms", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		gSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( gSizer3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer2.Add( sbSizer1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Crystal structure info" ), wx.VERTICAL )
		
		gSizer13 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_grid1 = wx.grid.Grid( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 3, 3 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"X" )
		self.m_grid1.SetColLabelValue( 1, u"Y" )
		self.m_grid1.SetColLabelValue( 2, u"Z" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelValue( 0, u"v1" )
		self.m_grid1.SetRowLabelValue( 1, u"v2" )
		self.m_grid1.SetRowLabelValue( 2, u"v3" )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer13.Add( self.m_grid1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		gSizer12 = wx.GridSizer( 3, 1, 0, 0 )
		
		self.m_textCtrl5 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"a", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"b", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"c", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		gSizer13.Add( gSizer12, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( gSizer13, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer2.Add( sbSizer2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Convergence parameters" ), wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 2, 1, 0, 0 )
		
		gSizer10 = wx.GridSizer( 1, 4, 0, 0 )
		
		m_choice3Choices = [ u"ecut (eV)", u"kgrid" ]
		self.m_choice3 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		gSizer10.Add( self.m_choice3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Initial Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_textCtrl14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Final Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_textCtrl15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl16 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Step", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_textCtrl16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		gSizer6.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		gSizer11 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_textCtrl17 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Delta E precision (eV)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_textCtrl17, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
		
		
		gSizer6.Add( gSizer11, 1, wx.EXPAND, 5 )
		
		
		sbSizer3.Add( gSizer6, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer2.Add( sbSizer3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Other input parameters" ), wx.VERTICAL )
		
		gSizer8 = wx.GridSizer( 2, 3, 0, 0 )
		
		self.m_textCtrl18 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, u"ecut (eV)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl19 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, u"kgrid", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrl20 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, u"tsmear (eV)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		sbSizer4.Add( gSizer8, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer2.Add( sbSizer4, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( gSizer2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )



		gSizer333 = wx.GridSizer( 1, 1, 0, 0 )
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer333.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		gSizer1.Add( gSizer333, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )




		gSizer113 = wx.GridSizer( 1, 1, 0, 0 )

		
		m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		m_gauge1.SetValue( 0 ) 
		gSizer113.Add( m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		gSizer1.Add( gSizer113, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )






		


		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )


                self.m_choice2.Disable()
                self.m_spinCtrl2.Disable()
                self.m_textCtrl2.Disable()
                self.m_textCtrl18.Disable()

                global yes_2, conv_quant#,element_1,no_atoms_1,positions_atoms_1,v1,v2,v3,a,b,c,init_value, final_value, step_value, delta_E_value,kgrid_value,tsmear_value
                yes_2=False
                conv_quant=0

                #Default Values
                #element_1='Si'
                #no_atoms_1=2
                #positions_atoms_1=['0 0 0 \n 0.25 0.25 0.25']
                #v1=[0.5,0.5,0.0]
                #v2=[0.0,0.5,0.5]
                #v3=[0.5,0.0,0.5]
                #a,b,c=5.431,5.431,5.431
                #init_value, final_value, step_value=200,350,10
                #delta_E_value=1e-3
                #kgrid_value,tsmear_value=18,0.2


		# Connect Events
		self.m_choice1.Bind( wx.EVT_CHOICE, self.element_1_choice )
		self.m_spinCtrl1.Bind( wx.EVT_SPINCTRL, self.atoms_1 )
		self.m_spinCtrl1.Bind( wx.EVT_TEXT, self.atoms_1_txt )
		self.m_textCtrl1.Bind( wx.EVT_TEXT, self.positions_1 )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.check_2 )
		self.m_choice2.Bind( wx.EVT_CHOICE, self.element_2_choice )
		self.m_spinCtrl2.Bind( wx.EVT_SPINCTRL, self.atoms_2 )
		self.m_spinCtrl2.Bind( wx.EVT_TEXT, self.atoms_2_txt )
		self.m_textCtrl2.Bind( wx.EVT_TEXT, self.positions_2 )
		self.m_grid1.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.grid_prim )
		self.m_textCtrl5.Bind( wx.EVT_TEXT, self.a_param )
		self.m_textCtrl6.Bind( wx.EVT_TEXT, self.b_param )
		self.m_textCtrl7.Bind( wx.EVT_TEXT, self.c_param )
		self.m_choice3.Bind( wx.EVT_CHOICE, self.conv_param )
		self.m_textCtrl14.Bind( wx.EVT_TEXT, self.init )
		self.m_textCtrl15.Bind( wx.EVT_TEXT, self.final )
		self.m_textCtrl16.Bind( wx.EVT_TEXT, self.step )
		self.m_textCtrl17.Bind( wx.EVT_TEXT, self.delta_E )
		self.m_textCtrl18.Bind( wx.EVT_TEXT, self.ecut )
		self.m_textCtrl19.Bind( wx.EVT_TEXT, self.kgrid )
		self.m_textCtrl20.Bind( wx.EVT_TEXT, self.tsmear )
		self.m_button1.Bind( wx.EVT_BUTTON, self.Calculate_button )
	
	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def element_1_choice( self, event ):
          global element_1
          element_1=str((reader[self.m_choice1.GetSelection( )])[1])

	def atoms_1( self, event ):
          global no_atoms_1
          no_atoms_1=(self.m_spinCtrl1.GetValue( ))


	def atoms_1_txt( self, event ):
          global no_atoms_1
          no_atoms_1=(self.m_spinCtrl1.GetValue( ))

	def positions_1( self, event ):
          global positions_atoms_1
          positions_atoms_1=self.m_textCtrl1.GetValue( )


	def check_2( self, event ):
          global yes_2
          yes_2=self.m_checkBox1.GetValue( )
          if yes_2==True:
             self.m_choice2.Enable()
             self.m_spinCtrl2.Enable()
             self.m_textCtrl2.Enable()
          elif yes_2==False:
             self.m_choice2.Disable()
             self.m_spinCtrl2.Disable()
             self.m_textCtrl2.Disable()



	def element_2_choice( self, event ):
          global element_2
          element_2=str((reader[self.m_choice2.GetSelection( )])[1])

	def atoms_2( self, event ):
          global no_atoms_2
          no_atoms_2=(self.m_spinCtrl2.GetValue( ))


	def atoms_2_txt( self, event ):
          global no_atoms_2
          no_atoms_2=(self.m_spinCtrl2.GetValue( ))

	def positions_2( self, event ):
          global positions_atoms_2
          positions_atoms_2=self.m_textCtrl2.GetValue( )


	def grid_prim( self, event ):
          global v1,v2,v3
          v1=[(self.m_grid1.GetCellValue(0,n)) for n in range(3)]
          v2=[(self.m_grid1.GetCellValue(1,n)) for n in range(3)]
          v3=[(self.m_grid1.GetCellValue(2,n)) for n in range(3)]

	def a_param( self, event ):
          global a
          a=(self.m_textCtrl5.GetValue( ))

	def b_param( self, event ):
          global b
          b=(self.m_textCtrl6.GetValue( ))

	def c_param( self, event ):
          global c
          c=(self.m_textCtrl7.GetValue( ))

	def conv_param( self, event ):
          global conv_quant
          conv_quant=self.m_choice3.GetSelection( )
          if conv_quant==0:
            self.m_textCtrl19.Enable()
            self.m_textCtrl18.Disable()
          elif conv_quant==1:
            self.m_textCtrl19.Disable()
            self.m_textCtrl18.Enable()
          

	def init( self, event ):
          global init_value
          init_value=(self.m_textCtrl14.GetValue( ))

	def final( self, event ):
          global final_value
          final_value=(self.m_textCtrl15.GetValue( ))


	def step( self, event ):
          global step_value
          step_value=(self.m_textCtrl16.GetValue( ))


	def delta_E( self, event ):
          global delta_E_value
          delta_E_value=(self.m_textCtrl17.GetValue( ))

	def ecut( self, event ):
          global ecut_value
          ecut_value=(self.m_textCtrl18.GetValue( ))

	def kgrid( self, event ):
          global kgrid_value
          kgrid_value=(self.m_textCtrl19.GetValue( ))

	def tsmear( self, event ):
          global tsmear_value
          tsmear_value=(self.m_textCtrl20.GetValue( ))

	def Calculate_button( self, event ):
           global figure, yes_2, conv_quant,element_1,no_atoms_1,positions_atoms_1,v1,v2,v3,a,b,c,init_value, final_value, step_value, delta_E_value,kgrid_value,tsmear_value, looper, conv_param, m , ecut_value

           latt_param=[float(a), float(b), float(c)]
           lattice_vectors=[[float(v1[i]) for i in range(3)], [float(v2[i]) for i in range(3)], [float(v3[i]) for i in range(3)]]


           commands.getoutput('cd working; rm *') #start from scratch every time
     
           species=[]
           no_species=[]  



           species.append(element_1)
           no_species.append(int(no_atoms_1))
           position_atoms_PUC=positions_atoms_1
           Material=element_1+str(no_atoms_1)
           if yes_2==True:
             species.append(element_2)
             no_species.append(int(no_atoms_2))
             position_atoms_PUC=position_atoms_PUC+'\n'+positions_atoms_2
             Material=Material+(element_2+str(no_atoms_2))


        

           range_param=list(arange(float(init_value), float(final_value)+float(step_value), float(step_value)))

           for i in range(len(species)):
              commands.getoutput('cat Potentials/POTCAR_'+species[i]+' >> working/POTCAR')

           conv_selection=conv_quant+1



           commands.getoutput('mkdir GS_Plots/'+Material)
           commands.getoutput('cd GS_Plots/'+Material+'; rm -r conv_test')
           commands.getoutput('cd GS_Plots/'+Material+'; mkdir conv_test')

           def looper():
            global conv_param,m,ecut_value,kgrid_value,tsmear_value
            m=0
            for conv_param in range_param:
             if conv_selection == 1:
               ecut=float(conv_param)
               kgrid=float(kgrid_value)
               tsmear=float(tsmear_value)
               print 'Processing STEP '+str(m+1)+' of '+str(len(range_param))+': ecut = '+str(ecut)+' eV..........'
             elif conv_selection == 2:
               kgrid=float(conv_param)
               tsmear=float(tsmear_value)
               ecut=float(ecut_value)
               print 'Processing STEP '+str(m+1)+' of '+str(len(range_param))+': kgrid = '+str(int(kgrid))+'X'+str(int(kgrid))+'X'+str(int(kgrid))+'..........'

             incar_generator(ecut, tsmear)    
             kpoints_generator(kgrid)
             poscar_generator(latt_param[0], latt_param[1], latt_param[2], lattice_vectors, no_species, position_atoms_PUC)  

             commands.getoutput('cd working; mpirun -np '+str(multiprocessing.cpu_count()-2)+' vasp')  #run vasp
             commands.getoutput('cd working; mv OSZICAR ../GS_Plots/'+Material+'/conv_test/OSZICAR_'+str(conv_param)) #cut output file 
             commands.getoutput('cd working; mv OUTCAR ../GS_Plots/'+Material+'/conv_test/OUTCAR_'+str(conv_param)) #cut output file 
             commands.getoutput('cd working; find . ! -name "POTCAR" -type f -exec rm -f {} +') #start from scratch every time
               
             if m>=1:
               param_lower_bound, delta_etot=plot_conv(conv_selection, Material, float(delta_E_value)) #extract energy data from output file and write it to file for plotting
               gSizer333.Clear()
                

               self.figure = figure()
               self.axes = self.figure.add_subplot(111)

              
               if conv_selection == 1:
                  self.axes.set_xlabel('ecut (eV)')
               elif conv_selection == 2:
                  self.axes.set_xlabel('kgrid')
               self.axes.set_ylabel(r'$\Delta$'+'E (eV)')
               self.axes.semilogy(param_lower_bound, delta_etot)
               self.axes.scatter(param_lower_bound, delta_etot)
               xlimits=list(linspace(self.axes.get_xlim()[0], self.axes.get_xlim()[1], 100))
               self.axes.plot(xlimits, [float(delta_E_value)]*len(xlimits), 'k-', label='target')  
               self.axes.legend()

               self.canvas = FigureCanvas(self, -1, self.figure)
               self.canvas.draw()
               self.canvas.Refresh()
               gSizer333.Add(  self.canvas, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5  )
	       w, h = self.GetClientSize()
               if m%2==0:
                 self.SetSize((w,h+1 ))
               else:
                 self.SetSize((w,h-1 ))
               time.sleep (0.5)               
               close(self.figure)               






             m=m+1     
             m_gauge1.SetValue(m/len(range_param)*100)
             if m == len(range_param):
                print 'JOB FINISHED :)'  









           th = threading.Thread(target=looper, args=())
           th.daemon = True
           th.start()     

             


              

if __name__ == "__main__":
  app = wx.App()
  frame = MyFrame1(None).Show()
  app.MainLoop()

	











