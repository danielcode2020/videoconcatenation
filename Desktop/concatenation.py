from moviepy.editor import *
import os
import time
import sys


clear = lambda: os.system('cls') #function to clear the console

path = "" # the path to your file , ex : C/User ....

path_save = "" # the path to save the final video

L = [] #empty list where the name of files will be added

string ="" #.mp4 or any string which is only specific to the name of file
#, ex: "video"  for video1.mp4, video2.mp4, video3.mp4

#this string will be searched in the name of file 

arr = os.listdir(path)

for x in arr:
    if string in x:
         video = VideoFileClip(path+ x)
         L.append(video) # adds the video to the list
         
print("Files received ")

time.sleep(2)

print(" Working on editing ... ")

final_clip = concatenate_videoclips(L,method = 'compose')

# concatenates the files, this method avoids
#the glitches caused by different quality resolution between videos



final_clip.write_videofile(path_save, fps=24, remove_temp=False)
# saves the file


clear()

print("Videos concatenated ! ")

time.sleep(2)


print("Removing files...")

# this block deletes the files used if needed
# __________________________________


print("Delete the source files ? : (y/n) ")
a=input("")
if a =='y' :
    
    try:
        for x in arr:
            if string in x:
                os.remove(path +  x)
        
        print("Files removed ...")
        time.sleep(2)
    except:
        print("Files not found ...")

# ___________________________________


print("Done ! ")

print("Press c to exit ")

s=""
while s!='c':
    s=input("")
sys.exit(0)
