##Visuals for Different Genres

**Purpose**

Determine whether there were visual similarities by genre in spectrograms and other
visuals by cycling through my directory that holds 30 songs in total, where there
are 3 songs for 10 different genres.

**Background**

I wanted to see if there was a distinct difference between genres by investigating
the use of ```specgram``` in ```python```. I got familiar with ```ffmpeg.exe``` so I could convert
 ```mp3``` files to ```wav``` as mono and not speaker. While doing some research for data sets
for different genres, I stumbled upon the [GTZAN Dataset]. Once I downloaded the [GTZAN Genre Dataset Download], 
I realized that their music in all of the genres were in the ```au``` format. In the [GTZAN Dataset],
there are 10 genres with 100 songs each having an elapsed time of 30 seconds. In the [GTZAN Analysis],
the [GTZAN Dataset] used the Echo Nest Musical Fingerprinter, which queries a database of about 30,000,000
songs. The Audio fingerprinting service discontinued in January 2015. You could set up your own server
with their old data if you wanted to. The fingerprinting algorithm gets a *fingerprint* for a song from 
an audio clip and the *fingerprint* can be used to find the song name, artist, year, and etc. I selected 30 audio 
files from the [GTZAN Dataset], 3 from each genre and wrote code to spin through the directory and convert
all the ```au``` audio files to the ```wav``` format. The dataset was already in mono conversion as opposed
to the stereo sound. Once the conversion was done, I was then able to write code to find all the ```wav``` 
files in the current working directory and create spectrogram ```png``` files, two self similarity matrices
for the song's ```timbre```  and ```pitch```, and a 3D plot displaying the ```timbre``` and ```pitch``` by 
 ```segments```. After I had all of the saved ```specgram``` ```png``` files in the current working directory,
I compared the frequency of each genre against each other by pulling the 30 ```specgrams``` into a ```word``` document, 
[Comparison.docx]. Since, this file was too big and got truncated, you can view two seperate ```png``` files that
are screen shots of the ```word``` document. You can see the spectrograms for the first 6 genres here: [genres.png].
The last 4 genres are displayed in a screen shot as well in [genres1.png].


**Code Explanation**


**Resources**
  
1. [GTZAN Genre Dataset Download]
2. [Echo Nest Fingerprinting]
3. [GTZAN Analysis]
4. [GTZAN Dataset]

[GTZAN Genre Dataset Download]: http://opihi.cs.uvic.ca/sound/genres.tar.gz
[GTZAN Analysis]: https://stevetjoa.com/static/p7.pdf
[GTZAN Dataset]: http://marsyasweb.appspot.com/download/data_sets/
[Echo Nest Fingerprinting]: https://www.ee.columbia.edu/~dpwe/pubs/EllisWJL10-ENfprint.pdf
[convertAU.py]: https://github.com/JoePaxton/genreVisuals/blob/master/_convertAU.py
[spectograms.py]: https://github.com/JoePaxton/genreVisuals/blob/master/_spectrograms.py
[Comparison.docx]: https://github.com/JoePaxton/GenreVisuals/blob/master/Comparison.docx
[genres.png]: https://github.com/JoePaxton/GenreVisuals/blob/master/genres.png
[genres1.png]: https://github.com/JoePaxton/GenreVisuals/blob/master/genres1.png
