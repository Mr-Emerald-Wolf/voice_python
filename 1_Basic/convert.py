#pydub
from pydub import AudioSegment

audio = AudioSegment.from_wav("test.wav")
n = len(audio)
counter = 1
interval = 5 * 1000
overlap = 1.5 * 1000
start = 0
end = 0
flag = 0
for i in range(0, 2 * n, interval):
     if i == 0: 
        start = 0
        end = interval

     else: 
        start = end - overlap 
        end = start + interval

     if end >= n: 
        end = n 
        flag = 1
chunk = audio[start:end]

filename = 'chunk'+str(counter)+'.wav'

chunk.export(filename, format ="wav")

print("Processing chunk "+str(counter)+". Start = " +str(start)+" end = "+str(end))
counter = counter + 1
                        
