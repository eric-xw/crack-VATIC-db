# Crack the mysql database of VATIC 

given a video name <video_name>, this program is able to make all boxes of that video a same box(x1, y1, x2, y2), and VATIC will show the changes on the webpage.

First, clone the project to somewhere on kalabaw: 
  git clone https://github.com/littlekobe/crack-VATIC-db.git

Then run the following commands to see
  cd crack-VATIC-db
  python crack_db.py --video_slug <video_name> --x1 <x1> --y1 <y1> --x2 <x2> --y2 <y2>
  or python crack_db.py (default values: video_name)
  

