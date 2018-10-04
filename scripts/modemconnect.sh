#!/bin/bash -e

# http://qiita.com/bsdhack/items/29400b9ed989cd67b1db
cwd=`dirname "${0}"`
# ${0} が 相対パスの場合は cd して pwd を取得
expr "${0}" : "/.*" > /dev/null || cwd=`(cd "${cwd}" && pwd)`

wvdial `python ${cwd}/getimsi.py -carrier` &
#/usr/bin/wvdial `python /home/pi/modem/getimsi.py -carrier` &

# wait ppp0 is made
${cwd}/wait_ppp0.sh
