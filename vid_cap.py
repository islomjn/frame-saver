import os
from os import listdir
from os.path import isfile, join

dir = os.getcwd()
vids = [v for v in listdir(dir) if isfile(v)]
vids = []

for file in os.listdir(dir):
    if file.endswith(".mp4"):
        vids.append(os.path.join(file))

import cv2
for i in range(len(vids)):
    print(f'Processing video {i} out of {len(vids)}')
    vidcap = cv2.VideoCapture(vids[i])
    
    sucess, image = vidcap.read()
    count = 0
    print('Starting...')
    while sucess:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))
        cv2.imwrite(f'frames/frame_0{i}_{count}.jpg', image)
        sucess, image = vidcap.read()
        count += 1
    print(f'Finished processing video {i} out of {len(vids)}')