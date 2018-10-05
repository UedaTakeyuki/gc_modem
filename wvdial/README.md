# wvdial
Config fils of wvdial for making ppp connection with specific SIM card and making systemctl service.

## setup
setup.sh installs depending softwares.

```
pi@raspberrypi:~/gc_modem/wvdial $ ./setup.sh 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
wvdial is already the newest version (1.61-4.1).
0 upgraded, 0 newly installed, 0 to remove and 51 not upgraded.
```

## service setup
The script file ***autostart.sh*** provide the feature to set/reset settings as to start 3G network connection automatically at the system start time.

To set it on and turn the 3G connection on right away, call autostart.sh with ***--on*** option.

```
pi@raspberrypi:~/gc_modem/wvdial $ ./autostart.sh --on
Created symlink /etc/systemd/system/multi-user.target.wants/wvdial.service → /home/pi/gc_modem/wvdial/wvdial.service.
```

You can confirm current status by systemctl command as follows:

```
pi@raspberrypi:~/gc_modem/wvdial $ sudo systemctl status wvdial.service
● wvdial.service - wvdial auto connect
   Loaded: loaded (/home/pi/gc_modem/wvdial/wvdial.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2018-10-05 17:27:44 JST; 13s ago
 Main PID: 1577 (wvdial)
   CGroup: /system.slice/wvdial.service
           ├─1577 /usr/bin/wvdial gosim -C /home/pi/gc_modem/wvdial/wvdial.conf
           └─1581 /usr/sbin/pppd 460800 modem crtscts defaultroute usehostname -detach user mobiledata noipdefault call wvdial usepee

Oct 05 17:27:46 raspberrypi wvdial[1577]: --> Starting pppd at Fri Oct  5 17:27:46 2018
Oct 05 17:27:46 raspberrypi wvdial[1577]: --> Pid of pppd: 1581
Oct 05 17:27:46 raspberrypi pppd[1581]: pppd 2.4.7 started by root, uid 0
Oct 05 17:27:46 raspberrypi pppd[1581]: Using interface ppp0
Oct 05 17:27:46 raspberrypi pppd[1581]: Connect: ppp0 <--> /dev/ttyUSB3
Oct 05 17:27:46 raspberrypi pppd[1581]: CHAP authentication succeeded
Oct 05 17:27:46 raspberrypi pppd[1581]: CHAP authentication succeeded
Oct 05 17:27:46 raspberrypi wvdial[1577]: --> Using interface ppp0
Oct 05 17:27:46 raspberrypi wvdial[1577]: [17B blob data]
Oct 05 17:27:46 raspberrypi wvdial[1577]: [17B blob data]
```

or by ***ifconfig*** command, you must see the ***PPP0:*** section when wvdial working well.

```
pi@raspberrypi:~/gc_modem/wvdial $ ifconfig
eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether b8:27:eb:44:90:3e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ppp0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.66.1.73  netmask 255.255.255.255  destination 10.64.64.64
        ppp  txqueuelen 3  (Point-to-Point Protocol)
        RX packets 10  bytes 214 (214.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11  bytes 301 (301.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 
 ```

To set it off and turn the 3G connection off right away, call autostart.sh with ***--off*** option.
```
pi@raspberrypi:~/gc_modem/wvdial $ ./autostart.sh --off
Removed /etc/systemd/system/multi-user.target.wants/wvdial.service.
Removed /etc/systemd/system/wvdial.service.
```

## SIM card setting
With regards to the several SIM vender which will be described later, necessary settings to make 3G connection is prepared.
What you have got to do is set vendor name to the DIALER1 variable on the wvdial.ini file as follows:

```
pi@raspberrypi:~/gc_modem/wvdial $ cat wvdial.ini
DIALER1=gosim
DIALER2=
```

Above example, SIM vendor name is gosim

Following vendors are abailable:

### International Carrier's
| vendor name | URL | name to set as DIALER1 |
|:---|:---|:---|
|soracom|https://soracom.jp/|soracom|
|TRANSATEL|http://www.transatel.com/|TRANSATEL|
|gosim|https://gosim.com/|gosim|
|hologram|https://hologram.io/|hologram|

### Carrier's in Myanmmer
| vendor name | URL | name to set as DIALER1 |
|:---|:---|:---|
|Myanma Posts and Telecommunications|http://mpt.com.mm/mm/|MTP|
|Ooredoo Myanmar|http://www.ooredoo.com.mm/|Ooredoo|
|Telenor Myanmar|https://www.telenor.com.mm/|TelenorMyanmar|

### Carrier's in Senegal
| vendor name | URL | name to set as DIALER1 |
|:---|:---|:---|
|Orange/Sonatel|https://www.orange.sn|OrangeSonatel|
|Sentel/Tigo|https://www.goafricaonline.com/sn/388680-sentel-tigo-dakar-senegal|SentelTigo|
|Expresso/Sudatel|https://www.expressotelecom.com/|ExpressoSudatel|


