import numpy as np
import math
from scipy import signal as sg # to do convolution
import scipy.io.wavfile 
import os.path 

"""
Crop .wav files and rename them
Input:  start = the starting time of the sinal (seconds) 
		sound = the .wav file to be cropped
Output: soundOut = cropped .wav file

###### below is explination for algorithum that selects point to crop ####
1000 is a number b/c the first few seconds or so data points are 
zero and so any number is going to be infinitly higher then the moving average
7.4 is the ratio that works with 1000, nn is the length in seconds of the 
window for which the moving average is taken

""" 
def autoCropper(lrate, sound, o, posno, startRn, endRn, positions):
	print "sound looks like:"
	print sound
	soundMatt= sound[1]  
	lenSound=len(soundMatt) 
	soundMat=abs(soundMatt) #this takes the absulute value
	lenSound=len(soundMat)
	print lenSound

		# text file with recording settings:
	with open (".../settings.txt", "r") as myfile:
		daset = myfile.readlines()

	def Convert(string):
		li = list(string.split(", ")) 
		return li

	pi = Convert(daset[0])
	ma = Convert(daset[1])
	he = Convert(daset[2])

	
	nn = 1 # nn = 0.5
	oo = 44100 * nn
	mm = int(oo)
	crDictionary = {}
	n=0
	j=0
	p=0
	qq=0  #
	for r in range (startRn+1, endRn+1):  # loops through each round  # for r in range (1, 5):
		print "  "  #
		print "(j) last break at:{0}".format(j) # j is iteration of loop 2 that trigers break 
		print "(p) take up at:{0}".format(p) #
		p = p*qq #  
		print "(p after 1 iteration) take up at:{0}".format(p)  #
		print '2nd loop r={0}, j={1}, p={2}'.format(r,j,p)
		for j in range(p, lenSound-mm): 
			moAv = np.mean(soundMat[j:j+mm-1]) #mean of nn second long moving interval
			if soundMat[j+mm-1] > 7.4*(moAv+1000): #
				qq = 1  
				p = j 
				print "the {0}th break is at:{1}".format(r, j) #
				k = j+22049  # sets k as the end point of the 1/2 sec interval from which the mean was taken
				crMat = soundMatt[k:k+88200] # creates a takes a 2 second long window
				scipy.io.wavfile.write('mi{0}pi{1}ma{2}he{3}ta{4}.wav'.format(o, pi[r-1], ma[r-1], he[r-1], r),44100,crMat)  
				p = j + 88200 # this should make the loop skip the next 2 seconds 
				print "should take up at:{0}".format(p)	
				break
