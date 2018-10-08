# gc_modem
USB 3G dongle utils

## at.py

### USAGE
```
pi@raspberrypi:~/gc_modem/scripts $ python -m at --help
usage: at.py [-h] [-d D] [-timeout TIMEOUT] at_command

AT command interface

positional arguments:
  at_command        AT command string.

optional arguments:
  -h, --help        show this help message and exit
  -d D              modem device like "/dev/ttyUSB0". Default is
                    "/dev/gc_modem"
  -timeout TIMEOUT  timeout time with modem. Default is 1
```

### Example
```
pi@raspberrypi:~/gc_modem/scripts $ python -m at ati
ati
/dev/gc_modem
1
['ati\r\r\n', 'Manufacturer: ZTE CORPORATION\r\n', 'Model: MF190\r\n', 'Revision: BD_MF190V1.0.0B02\r\n', 'IMEI: 359728033653091\r\n', '+GCAP: +CGSM,+DS,+ES\r\n', '\r\n', 'OK\r\n']
```
