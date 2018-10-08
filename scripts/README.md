# gc_modem
USB 3G dongle utils

## at.py
Send AT command and return AT command response as an array.

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

## getcsq.py 

Send AT+CSQ for get signal strength of the device.

### USAGE
```
pi@raspberrypi:~/gc_modem/scripts $ python -m getcsq --help
usage: getcsq.py [-h] [-d D] [-timeout TIMEOUT]

3g signal quality

optional arguments:
  -h, --help        show this help message and exit
  -d D              modem device like "/dev/ttyUSB0". Default is
                    "/dev/gc_modem"
  -timeout TIMEOUT  timeout time with modem. Default is 1

result: [csq, rssi, condition]
```
### Example
```
pi@raspberrypi:~/gc_modem/scripts $ python -m getcsq
['13', '-87', 'OK']
```

### definition of csq value, rssi, and condition.
[origina](http://m2msupport.net/m2msupport/atcsq-signal-quality/)

| Value of csq | RSSI dBm | Condition |
|:---|:---:|:---:|
|0	|-113 or less	|Marginal|
|1	|-111	|Marginal|
|2	|-109	|Marginal|
|3	|-107	|Marginal|
|4	|-105	|Marginal|
|5	|-103	|Marginal|
|6	|-101	|Marginal|
|7	|-99	|Marginal|
|8	|-97	|Marginal|
|9	|-95	|Marginal|
|10	|-93	|OK|
|11	|-91	|OK|
|12	|-89	|OK|
|13	|-87	|OK|
|14	|-85	|OK|
|15	|-83	|Good|
|16	|-81	|Good|
|17	|-79	|Good|
|18	|-77	|Good|
|19	|-75	|Good|
|20	|-73	|Excellent|
|21	|-71	|Excellent|
|22	|-69	|Excellent|
|23	|-67	|Excellent|
|24	|-65	|Excellent|
|25	|-63	|Excellent|
|26	|-61	|Excellent|
|27	|-59	|Excellent|
|28	|-57	|Excellent|
|29	|-55	|Excellent|
|30	|-53	|Excellent|
