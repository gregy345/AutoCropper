import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import wave
import sys   
from scipy.io.wavfile import read  
import scipy.io.wavfile
import math
import cmath
import pylab
import os 
import os.path
import glob 
from autocropper import autoCropper
from transferFile import transfer
"""
Crop .wav files and rename them
Input:  roundno = the number of the round of recording 
		startP = the position in the round to start on
		endP = the position in the round to end on
""" 
def main():
	
	print "number of positions?, 1, 2, ... 10 (type 4) "
	posno = 4 #input()    
	startR = 1
	print "number of rounds?, 1, 2, 3, ... (type 3)"  
	endR = 3 #input()  

	startRn = startR -1
	endRn = endR

	################
	basepath='.../DataBefore'
	nbr=len([name for name in os.listdir(basepath) 
		if os.path.isfile(os.path.join(basepath, name))])
	os.chdir('..../DataBefore')
	fillist =  os.listdir(basepath) 

	rounds = {}
	for x in range(1,10):
		rounds['r{0}'.format(x)]=[k for k in fillist if 'r{0}'.format(x) in k]

	# creates fillist of files in raw data folder
	nbr=len([name for name in os.listdir(basepath) 
		if os.path.isfile(os.path.join(basepath, name))])  # 
	os.chdir(basepath) #
	fillist =  os.listdir(basepath) 

	# text file with recording settings:
	with open ("..../settings.txt", "r") as myfile:
		daset = myfile.readlines()

	def Convert(string):
		li = list(string.split(", ")) 
		return li

	pi = Convert(daset[0])
	ma = Convert(daset[1])
	he = Convert(daset[2])

	positions = {}
	for x in range(1,5):
		positions[x]=[k for k in fillist if 'p{0}'.format(x) in k] #sub = positions[posno]
	
	print "the number of files in the full directory is: {0}".format(nbr)
	print 'the names of files in full directory are:'
	print fillist
	print 'the contense of the dictionary positions:'
	print positions
		
	# reads the raw files into a dictionary named "lfile1"
	lfile1 = {}
	for k in range(0, posno): # loops through positions (pXseries.wav files in folder) # for k in range(0, 4):
		print "the file is:" 
		print fillist[k]
		lfile1['log{0}'.format(k+1)] = scipy.io.wavfile.read(fillist[k]) 
	print " the fillist is:"
	print fillist

	# creates cropped versions of the raw files and puts them in same folder
	fs = 44100
	for o in range(0, posno): # loop through positions   
		autoCropper(fs, lfile1['log{0}'.format(o+1)], (o+1), posno, startRn, endRn, positions) 
	print '  '
	print 'new files created in:{0}'.format(basepath)  
	
	#transfers the cropped files to new folder
	for s in range(0, posno): #loop through possitions 
		for q in range(startRn+1, endRn+1): # loop through rounds 
			transfer('mi{0}pi{1}ma{2}he{3}ta{4}.wav'.format(s+1, pi[q-1], ma[q-1], he[q-1], q), basepath)
			 

if __name__ == '__main__':
	main()


