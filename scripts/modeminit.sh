#!/bin/bash -e

# http://qiita.com/bsdhack/items/29400b9ed989cd67b1db
cwd=`dirname "${0}"`
# ${0} が 相対パスの場合は cd して pwd を取得
expr "${0}" : "/.*" > /dev/null || cwd=`(cd "${cwd}" && pwd)`

${cwd}/modeminfos.sh || true
${cwd}/settimezonebymodem.sh || true
${cwd}/getkcell.sh || true
