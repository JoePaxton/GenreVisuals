__author__= 'Joe Paxton'
import os
import subprocess
 
cwd = os.getcwd() # Verify the current working director (cwd) otherwise change cwd to point to location of wav files
print cwd
print os.listdir(cwd)
 
count = 0
 
for filename in os.listdir(cwd):
	if filename.endswith('.au'):
		count=count+1
		#The following command assume that ffmpeg.exe is on your path, if not change the cmdline string
		cmdline = 'C:\Users\Joe\Anaconda\ffmpeg.exe -i ' + filename + '  ' + filename + '.wav'
		print 'Constructed cmdline =', cmdline
		subprocess.call(cmdline)
                               
print 'au files found = ',count
