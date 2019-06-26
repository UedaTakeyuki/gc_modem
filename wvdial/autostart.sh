#!/bin/bash

################################################################
# 
# Autostart setting
# 
# usage: ./autostart.sh --on/--off
#
#
# @author Dr. Takeyuki UEDA
# @copyright Copyright© Atelier UEDA 2018 - All rights reserved.
#
CMD=wvdial
SCRIPT_DIR=$(cd $(dirname $0); pwd)
#echo $cwd

usage_exit(){
	echo "Usage: $0 [--on]/[--off]" 1>&2
  echo "  [--on]:               Set autostart as ON. " 			1>&2
  echo "  [--off]:              Set autostart as OFF. " 		1>&2
  exit 1
}

on(){
	sed -i -e "s@^ExecStart=.*@ExecStart=/usr/bin/wvdial "'$DIALER1 $DIALER2'" -C ${SCRIPT_DIR}/${CMD}.conf@" -e "s@^EnvironmentFile=.*@EnvironmentFile=${SCRIPT_DIR}/${CMD}.ini@" ${SCRIPT_DIR}/${CMD}.service
#	sudo ln -s ${SCRIPT_DIR}/${CMD}.service /etc/systemd/system/${CMD}.service
	sudo cp ${SCRIPT_DIR}/${CMD}.service /etc/systemd/system/${CMD}.service
	sudo systemctl daemon-reload
	sudo systemctl enable ${CMD}.service
	sudo systemctl start ${CMD}.service
}

off(){
	sudo systemctl stop ${CMD}.service
	sudo systemctl disable ${CMD}.service
}

while getopts ":-:" OPT
do
  case $OPT in
    -)
				case "${OPTARG}" in
					on)
								on
								;;
					off)
								off
								;;
				esac
				;;
    \?) usage_exit
        ;;
  esac
done
