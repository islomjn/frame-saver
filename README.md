# Frame Saver
## This script aims to save video frames for one video file or batch of video files in a directory

## 1. Install depenencies

```
$ pip install -r requirements.txt
```

## 2. To run script

` $ python vid_cap.py --source [filename or folder] --output [output folder]`

Example:

` $ python vid_cap.py --source video.mp4 --output saved_frames`

Output:

```
Namespace(fps=None, output='saved_frames', source='video.mp4')

Processing video 1 out of 1
Starting...
Finished processing video 1 out of 1

Frames are saved in saved_frames/
```
