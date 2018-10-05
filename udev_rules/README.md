# udev_rules
Udev rules for usb 3G & 4G modem recognition.

## setup
***set.sh*** set a specified rule active and install dependencies.
```
pi@raspberrypi:~/gc_modem/udev_rules $ ./set.sh 99-ZTE_mf190.rules 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
eject is already the newest version (2.1.5+deb1+cvs20081104-13.2).
0 upgraded, 0 newly installed, 0 to remove and 51 not upgraded.
```

***reset.sh*** set a specified rule iactive.
```
pi@raspberrypi:~/gc_modem/udev_rules $ ./reset.sh 99-ZTE_mf190.rules 
```

## /dev/gc_modem
Regarding 3G modem which is designed to provide network connection by ***SERIAL***, the name of tty which is related to modem is depend on not only model of modem, but also situation. For example, ZTE-mf190 tend to create ***ttyUSB3*** even Huawai-E3276 tend to create ***ttyUSB0***. Also, in case ttyUSB3 is already busy of used by other device, ZTE-mf190 create other tty like ***ttyUSB4*** or ***ttyUSB5*** and so on.

For avoiding at this ambiguity of tty name, the udev_rules of 3G modem in this project make symbolic link ***gc_modem*** to the created tty by modem. So all you have got to do is just use tty named ***gc_modem*** under /dev folder.

Note that 4G modem which is designed to connect by ***NDIS***, of cource these rules don't make ***gc_modem*** becauae they don't use tty which gc_modem related to.

## available modem

### [L02-a](https://amzn.to/2QxxlkF)
