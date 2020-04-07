$ # 현재위치에서 1 depth 아래 폴더 단위로 사용량 요약
$ du -sh *
$ du -h --max-depth=1

$ # 이런저런 활용
$ du -sh sub/*
$ du -sh PREFIX*
$ du -sh *POSTFIX
$ du -h --max-depth=1 .
$ du -h --max-depth=2 /usr/local

$ #디스크 사용량
$ df -h