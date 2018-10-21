# gc_modem
USB 3G dongle and Data SIM card utilities

- [udev_rules](udev_rules/README.md) : Udev rules for usb 3G modem recognition.
- [wvdial](wvdial/README.md) : Settings for ppp connection with SIM cards.
- [scripts](scripts/README.md) : utils to get information of 3G Dongle. 

## install
download from [release](https://github.com/UedaTakeyuki/gc_modem/releases)

or 

```
git clone https://github.com/UedaTakeyuki/gc_modem.git
```


## gc_modem symlink to appropriate tty for 3G modem

To avoid ambiguity of which tty device is relating with 3G modem, a udev_rules of this project make symbolic link ***/dev/gc_modem***  to the appropriate tty device.
The [wvdial configration](wvdial/wvdial.conf) and script files in this project also use ***/dev/gc_modem***.
