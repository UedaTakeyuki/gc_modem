# udev_rules
Collection of udev rules for usb 3G & 4G modem and setup script.

## install
download from [release](https://github.com/UedaTakeyuki/gc_modem/releases)

or 

```
git clone https://github.com/UedaTakeyuki/gc_modem.git
```

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
Regarding the 3G modem, which is designed to provide network connection via ***serial***, the name of the tty which is related to the modem depends not only on the model of the modem, but also on the situation. For example, ZTE-mf190 tend to create ***ttyUSB3***, even Huawei-E3276 tends to create ***ttyUSB0***. Also, in case ttyUSB3 is already busy of used by other device, ZTE-mf190 create other tty devices like ***ttyUSB4*** or ***ttyUSB5*** and so on.

To avoid this ambiguity of tty name, the udev_rules of the 3G modem in this project make a symbolic link ***gc_modem*** to the created tty by the modem. So all you have to do is only use the tty named ***gc_modem*** under ```/dev``` folder.

Note that the 4G modem which is designed to connect by ***NDIS***, of cource these rules don't make ***gc_modem*** because they don't use tty, which gc_modem is related to.

## modems which are prepared rule

### Huawei E173
Inexpensive 3G modem.

### Huawei E303C
No rules are necessary because this device supports Huawei ***HiLink*** that provides ***ether** device. For setup of the HiLink, connect to 192.168.1.1 (or 192.168.8.1 for some devices) by web browser and set APN.

### ZTE-mf190
Inexpensive 3G modem. This model has several model IDs

### ZTE-MF821
Inexpensive 4G(LTE) modem, but ***gc_modem*** link available due to its serial connection support. This device also supports ***QMI***, refer to the qmi-network.conf of this device.

### Qualcomm_Siemens-SG75
4G modem. The connection interface is ***NDIS***. 

### Huawei w04
4G modem. The connection interface is ***NDIS***. 

### [NTT DoCoMo L02-a](https://amzn.to/2QxxlkF)
Japanese inexpensive 3G modem. This device adapts the Japanese wireless regulation called 技適(giteki).
### [NTT DoCoMo L05-a](https://amzn.to/2NoD9L3)
Japanese inexpensive 3G modem. This device adapts the Japanese wireless regulation called 技適(giteki).

## Request to add rule file
Add rule file request is welcome, both pull requests and just [issue](https://github.com/UedaTakeyuki/gc_modem/issues) with a sample 3G modem device.

## QA
Any questions, suggestions, or reports are welcome! Please make [issue](https://github.com/UedaTakeyuki/gc_modem/issues) without hesitation! 
