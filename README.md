##Visuals for Different Genres

**Purpose**

Determine whether there were discernable visual similarities by genre using 
spectrograms and other visuals by cycling through my directory that holds 30 
songs in total, where there are 3 songs from 10 different genres.

**Background**

I wanted to see if there was a distinct difference between genres by investigating
the use of ```specgram``` in ```python```. I got familiar with ```ffmpeg.exe``` so I could convert
 ```mp3``` files to ```wav``` as mono and not speaker. While doing some research for data sets
for different genres, I stumbled upon the [GTZAN Dataset]. Once I downloaded the [GTZAN Genre Dataset Download], 
I realized that their music in all of the genres were in the ```au``` format, and could use ```ffmpeg.exe```
to convert these to ```wav``` files. I selected 30 audio files from the [GTZAN Dataset], 3 from each genre
and wrote code to spin through the directory and convert all the ```au``` audio files to the ```wav``` 
format. The dataset was already in mono, so the conversion from stereo to mono was not required. Once
the conversion was done, I was then able to write code to find all the ```wav``` files in the current
working directory and create spectrogram ```png``` files, two self-similarity matrices for the song's
```timbre``` and ```pitch```, and a 3D plot displaying the ```timbre``` and ```pitches``` by ```segments```.
After I had all of the saved ```specgram``` ```png``` files in the current working directory, I compared the
spectrograms of each genre against each other by pulling 30 ```specgrams``` into a word document, [Comparison.docx].
Due to the size of the file, it says it has been truncated for viewing, but you can download the document
and view it locally. You can also see a subset of the spectrograms for the first 6 genres from the document
here: [genres.png]. This will illustrate the value of downloading the Word document [Comparison.docx]. The
last 4 genres from the document are displayed in a screen shot as well in [genres1.png].

I originally had intended to attempt to use the [Echo Nest Fingerprinting] service to see if I could 
identify the music clips from the [GTZAN Dataset]. The fingerprinting algorithm gets a fingerprint for a song
from the audio clip and the fingerprint can be used to find the song name, artist, year, etc. However, while 
trying to get the codegen portion of this to work, I discovered that the Audio fingerprinting service was recently discontinued in January 2015. Echo Nest states that you can set up your own server (they have the source code 
available to download), however, that appears to be a nontrivial task and beyond the scope of this research project.


**Converting Files**

This snippet of code from [convertAU.py] simply goes through your current working directory, ```cwd``` and finds
all the files that end with ```au``` and converts them into a ```wav``` file assuming you have ```ffmpeg.exe```. 
Make sure that your ```cmdline``` variable holds the correct path to your ```ffmpeg.exe``` program.

 ```python
for filename in os.listdir(cwd):
    if filename.endswith('.au'):
        count=count+1
        cmdline = 'C:\Users\Joe\Anaconda\ffmpeg.exe -i ' + filename + '  ' + filename + '.wav'
        print 'Constructed cmdline =', cmdline
        subprocess.call(cmdline)

 ```
This snippet of code from [genreVisuals.py] gets the ```wav``` file information, which
is the ```sound_info``` and the ```frame_rate```. The ```getframerate()``` function returns
the sampling frequency and the ```fromstring``` function reads the frames of the audio. When
you import ```wave``` you can access all of these functions. Going over the [wav] module will 
explain these functions as well. This function gets the ```frame_rate``` and the data to create
the ```specgrams``` and other visuals you can look at in the code. The data is a one dimensional
array of many values.

```python
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate
```

**Resources**
  
1. [GTZAN Genre Dataset Download]
2. [Echo Nest Fingerprinting]
3. [GTZAN Analysis]
4. [GTZAN Dataset]
5. [wav]
6. [Write WAVE]

[GTZAN Genre Dataset Download]: http://opihi.cs.uvic.ca/sound/genres.tar.gz
[GTZAN Analysis]: https://stevetjoa.com/static/p7.pdf
[GTZAN Dataset]: http://marsyasweb.appspot.com/download/data_sets/
[Echo Nest Fingerprinting]: https://www.ee.columbia.edu/~dpwe/pubs/EllisWJL10-ENfprint.pdf
[convertAU.py]: https://github.com/JoePaxton/genreVisuals/blob/master/convertAU.py
[genreVisuals.py]: https://github.com/JoePaxton/genreVisuals/blob/master/genreVisuals.py
[Comparison.docx]: https://github.com/JoePaxton/GenreVisuals/blob/master/Comparison.docx
[genres.png]: https://github.com/JoePaxton/GenreVisuals/blob/master/genres.png
[genres1.png]: https://github.com/JoePaxton/GenreVisuals/blob/master/genres1.png
[wav]: https://docs.python.org/2/library/wave.html
[Write WAVE]: http://www.mathworks.com/help/matlab/ref/wavwrite.html  
