# Crack the mysql database of VATIC 

given a video name <video_name>, this program is able to make all boxes of that video a same box(x1, y1, x2, y2), and VATIC will show the changes on the webpage.

First, clone the project to somewhere on kalabaw: <br>
  _git clone https://github.com/littlekobe/crack-VATIC-db.git_ <br>
  <br>

Then run the following commands to see <br>
  _cd crack-VATIC-db_ <br>
  __python crack_db.py --video_slug <video_name> --x1 <x1> --y1 <y1> --x2 <x2> --y2 <y2>__ <br>
  
Here are two examples: <br>
  __python crack_db.py --video_slug 'video3_00104' --x1 50 --y1 50 --x2 200 --y2 200__ <br>
  or __python crack_db.py__ (the default values are same as the above command) <br>
  then you can visit here(http://dragonox.cs.ucsb.edu/?id=12383&hitId=offline) see the change.
  

