__author__ = 'Joe Paxton'

"""
This program runs through your current working directory and displays 
different graphs based on the music's attributes.

Go to my README.md for more detail.
"""

import os
import subprocess
import pylab
import numpy as n
import matplotlib.pyplot as plt
import scipy.io.wavfile
import wave
import echonest.remix.audio as audio
from matplotlib.pyplot import specgram
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import distance

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate
   
def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.title('Spectrogram of %r' % wav_file)
    pylab.xlabel("Seconds")
    pylab.ylabel("Frequency")
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig(wav_file + '_' + 'spectrogram.png')

def graph_timbre_pitches(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    segments = audio.AudioAnalysis(wav_file).segments
    collect = audio.AudioQuantumList()
    collect_p = audio.AudioQuantumList()
	
    for seg in segments:
        collect.append(seg.timbre)
        collect_p.append(seg.pitches)
        
    points = n.zeros((len(segments), 3),dtype=float)
    
    for i in range(len(segments)):
	points[i] = ( (i, n.mean(collect[i]), n.mean(collect_p[i])) )
		
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_xlabel('Segments')
    ax.set_ylabel('Timbre')
    ax.set_zlabel('Pitches')
    ax.set_title('3D Timbre and Pitches for ' + wav_file)
    ax.scatter(points[:,0], points[:,1], points[:,2], zdir = 'z', c = '.5')
    plt.savefig(wav_file + '_' + '3D.png', dpi=600)
    plt.show()
    
def selfSim(wav_file):
	dist = 0.0
	sound_info, frame_rate = get_wav_info(wav_file)
	segments = audio.AudioAnalysis(wav_file).segments
	segs = len(segments),len(segments)
	timbreMatrix = n.zeros(segs)
	pitchMatrix = n.zeros(segs)
	
	for i in range(len(segments)):
		for j in range(len(segments)):
			dist = distance.euclidean(segments[i].pitches, segments[j].pitches)
			pitchMatrix[i][j] = dist
	
	for i in range(len(segments)):
		for j in range(len(segments)):
			dist = distance.euclidean(segments[i].timbre, segments[j].timbre)
			timbreMatrix[i][j] = dist
			
	return pitchMatrix, timbreMatrix
	
def showSelfSim(filename, m):
	plot = plt.imshow(m, origin = 'lower')
	plot.set_cmap('hot')
	
	plot2 = plt.imshow(m, origin = 'lower')
	plot2.set_cmap('hot')
	
	plt.show()
	
def main():
    cwd = os.getcwd() # Get and verify the current working director (cwd)
    print "Creating a spectogram for every .wav file in the directory: ", cwd
    print "Make sure you exit out of the first two images in order to see the self similiarity matrices"

    count = 0
    for filename in os.listdir(cwd):
	    if filename.endswith('.wav'):
	        count= count + 1
	        print count, '- Using song file: ', filename
	        graph_spectrogram(filename)
	        graph_timbre_pitches(filename)
	        t,p = selfSim(filename)
	        showSelfSim(filename, t)
	        showSelfSim(filename, p)
            print '\nNumber of wave files processed = ',count
			
if __name__ == '__main__':
    main()
