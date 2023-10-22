# !/usr/bin/python
# -*- coding:utf-8 -*-

import argparse
from moviepy.editor import *

def combine_video(files, name):
    L = []
    if name == '':
        name = files[0]
    for file in files:
        video = VideoFileClip(file)
        L.append(video)
    final_clip = concatenate_videoclips(L)
    final_clip.write_videofile(name + ".mp4", fps=24, codec="libx264", remove_temp=True)
    print('[影片合併完成]' + name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', action='append', help='input video files to be combined', default=[])
    parser.add_argument('-n', '--name', type=str, help='new file name for combined video', default="")

    args = parser.parse_args()

    files = args.input
    name = args.name

    combine_video(files, name)