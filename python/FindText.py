# -*- coding:utf-8 -*-

import glob
import re


class Ftext:

    def exeCore(self, sword, sdir=''):
        p = re.compile(sword)
        arr = list()
        cnt = 0

        for i in glob.glob(r'D:\YSY\LMS\건강나라\www\*.php'):
            with open(i, 'r', encoding='utf-8') as f:
                for x, y in enumerate(f.readlines(), start=1):
                    m = p.findall(y)
                    if m:
                        arr.append('File ' + str(i) + ' [ ' + str(x) + ' ] Line Searching : ' + str(m))
                        arr.append('Full Line Text : ' + str(y))

        return arr

    def exeUi(self):
        s = str(input('Text: '))
        p = re.compile(s)

        for i in glob.glob(r'D:\YSY\LMS\건강나라\www\*.php'):
            with open(i, 'r', encoding='utf-8') as f:
                for x, y in enumerate(f.readlines(), start=1):
                    m = p.findall(y)
                    if m:
                        print('File %s [ %d ] Line Searching : %s' % (i, x, m))
                        print('Full Line Text : %s' % y)

    def exeConsole(self):
        sword = str(input('Text: '))
        dir = str(input('Directory: '))

        carr = self.exeCore(sword, dir)
        for i in carr:
            print(i)


if __name__ == "__main__":
    ft = Ftext()
    ft.exeConsole()

    """
    rarr = ft.exeCore('과정삭제', 'dir')
    for i in rarr:
        print(i)
    """