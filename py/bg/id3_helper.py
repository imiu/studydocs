#!/usr/bin/env python
from pprint import pprint
import re
import codecs
import os
import glob
from mutagen.easyid3 import EasyID3

mp3_dir = r'/Volumes/FS/iTunes/iTunes Music/Music/Boris Grebenshchikov/Aerostat 8/'
names_file = codecs.open('./names_right.out', encoding="utf-8")
names_dict = {}
for name in names_file:
    ep_number = name.split(" - ")[0]
    names_dict[ep_number] = name.strip()

os.chdir(mp3_dir)
ep_number = ''
re_ep_number = re.compile(r'^(\d*)\ ')
for mp3_file in glob.glob("*.mp3"):
    ep_number = re_ep_number.search(mp3_file).group(1)
    # pprint(mp3_file)
    # pprint(names_dict[ep_number])
    mfile = EasyID3(mp3_dir + mp3_file)
    mfile["title"] = names_dict[ep_number]
    mfile.save()

pprint("Done")
