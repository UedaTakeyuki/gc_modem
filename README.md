# gc_modem
USB 3G dongle utils

- [udev_rules](udev_rules/udev_rules.md) : Udev rules for usb 3G modem recognition.
- [wvdial](wvdial/wvdial.md) : Settings for ppp connection with SIM cards.
- [scripts](scripts/scripts.md) : utils to get information of 3G Dongle. 

# General Design

A tty device which used by 3G modem (like /dev/ttyUSB0) is linked to the ***/dev/gc_modem*** file by udev rules provided on the project, to avoid confusion which tty (ttyUSB0, ttyUSB1, ttyUSB2, ttyUSB3 and so on) is used.

The [wvdial configration](wvdial/wvdial.conf) use ***/dev/gc_modem***.

Scripts files also use ***/dev/gc_modem***.
