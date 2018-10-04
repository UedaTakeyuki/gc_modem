
################################################################
# 
# set rule on /etc/udev/rules.d/
# 
# usage: ./setup.sh rule_name
#
#
# @author Dr. Takeyuki UEDA
# @copyright Copyright© Atelier UEDA 2018 - All rights reserved.
#
SCRIPT_DIR=$(cd $(dirname $0); pwd)

usage_exit(){
	echo "Usage: $0 rule_name" 1>&2
  exit 1
}

if [ $# -ne 1 ]; then
	usage_exit
fi
if [ -e $1 ]; then
	sudo ln -s $SCRIPT_DIR/$1 /etc/udev/rules.d/$1
fi

sudo apt-get install eject
