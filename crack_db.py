import os
import sys
import math
import argparse
import config
import shutil
from database import session
import sqlalchemy
import random
import models
from models import *
import cStringIO
from PIL import Image, ImageDraw, ImageFont

def make_same_boxes(video_slug, x1, y1, x2, y2):
    video = session.query(Video).filter(Video.slug == video_slug)
    if video.count() == 0:
        print "Video {0} does not exist!".format(video_id)
        raise SystemExit()
    video = video.one()
    
    for segment in video.segments:
        for job in segment.jobs:
            for path in job.paths:
                for box in path.boxes:
                    box.xtl = x1
                    box.ytl = y1
                    box.xbr = x2
                    box.ybr = y2
    session.commit()
    
if __name__=='__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_slug", default='video3_00104', type=str)
    parser.add_argument("--x1", default='50', type=int)
    parser.add_argument("--y1", default='50', type=int)
    parser.add_argument("--x2", default='200', type=int)
    parser.add_argument("--y2", default='200', type=int)
    args = parser.parse_args()
    
    make_same_boxes(args.video_slug, args.x1, args.y1, args.x2, args.y2)
    