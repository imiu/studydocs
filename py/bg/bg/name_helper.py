#!/usr/bin/env python

import json
import codecs

utf_fd = codecs.open('names_right.out', 'w', encoding='utf-8')

with open('names.out') as fd:
    for json_line in fd:
        raw_name = u"%s\n" % json.loads(json_line)['name']
        utf_fd.write(raw_name)

utf_fd.close()
