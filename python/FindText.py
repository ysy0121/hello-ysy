#-*- coding:utf-8 -*-

import sys
import glob
import re

s = str(input('Text: '))
p = re.compile(s)

for i in glob.glob('D:\YSY\LMS\건강나라\www\*.php'):
    with open(i, 'r', encoding='utf-8') as f:
        for x, y in enumerate(f.readlines(), start=1):
            m = p.findall(y)
            if m:
                print('File %s [ %d ] Line Searching : %s' %(i,x,m))
                print('Full Line Text : %s' % y)
