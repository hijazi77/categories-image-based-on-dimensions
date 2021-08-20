import os
import shutil
import  cv2
import numpy as np


current = f'{os.getcwd()}'

dst = f'{current}\landscape' #move to path if landscape
portriat = f'{current}\portriat' #move to path if portrait
files = os.listdir(current) #move from path
files.sort() #sorting files

count = 1
count2 = 1

for f in files: #inherting all files
  if f.endswith('.jpg'): #get only jpg files ---> change it if you need

      im = cv2.imread(f)
      h, w, _ = im.shape #read the img dimensions
      if w > h: #get img which width bigger than height
        source = f'{current}\{f}' #declare the old file path 
        loc = f'{dst}\{f}' #declare the new file path
        shutil.move(source,loc) #moving files
        print(f'file {f} is landscape')
        count += 1
      if h > w:
        source2 = f'{current}\{f}' #declare the old file path
        loc2 = f'{portriat}\{f}' #declare the new file path
        shutil.move(source2,loc2) #moving files
        print(f'file {f} is portrait')
        count2 += 1
