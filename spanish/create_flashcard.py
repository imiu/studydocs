#!/usr/bin/env python
from __future__ import with_statement
import codecs
import re
from datetime import date


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


f_path = '/Users/alexander/Desktop/%s-spanish.txt' % date.today()

flash_lines = []
with codecs.open('./words.txt', 'r', 'utf-8') as f_in:
    for line in nonblank_lines(f_in):
        p = re.compile('\s+\-\s+')
        flash_lines.append(p.sub('\t', line))

with codecs.open(f_path, 'w', 'utf-8') as f_out:
    for line in flash_lines:
        f_out.write(line + '\n')
