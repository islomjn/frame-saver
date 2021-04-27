# @author: Islomjon Shukhratov
# extended from: https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames

import os
import sys, argparse
from os import listdir
from os.path import isfile, join
import cv2

vid_formats = ['mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv']

video_formats = ['mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv']

def frame_saver(source, output, fps=500):
    isFile = os.path.isfile(source)
    if not os.path.exists(output):
        os.makedirs(output)
    
    if isFile:
        for i in range(1):
            print(f'Processing video {i+1} out of {1}')
            vidcap = cv2.VideoCapture(source)
            success, image = vidcap.read()
            count = 0
            print('Starting...')
            while success:
                vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*fps))
                cv2.imwrite(f'{output}/frame_0{i}_{count}.jpg', image)
                success, image = vidcap.read()
                count += 1
            print(f'Finished processing video {i+1} out of {1}\n')
        
        
    else:
        vids = []
        for file in os.listdir(source):
            if file.endswith('.mp4'):
                vids.append(os.path.join(file))
        for i in range(len(vids)):
            print(f'Processing video {i+1} out of {len(vids)}')
            vidcap = cv2.VideoCapture(vids[i])

            success, image = vidcap.read()
            count = 0
            print('Starting...')
            while success:
                vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*fps))
                cv2.imwrite(f'{output}/frame_0{i}_{count}.jpg', image)
                success, image = vidcap.read()
                count += 1
            print(f'Finished processing video {i+1} out of {len(vids)}\n')
    
    print(f'Frames are saved in {output}/')
    

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--source', help='Path to a video, default current directory', default=os.getcwd())
    args.add_argument('--output', help='Path the frames will be saved, by default it creates "saved_frames" folder', default='saved_frames')
    args.add_argument('--fps', help='Set frames per second, default two frames per second', required=False)

    opt = args.parse_args()
    print(opt, '\n')

    frame_saver(opt.source, opt.output)

# TODO:
# Add progress bar
# Add ability to use not only .mp4 files
# Add function that will handle video processing
# Add more customized arguments
# Add timer (every video, all videos)