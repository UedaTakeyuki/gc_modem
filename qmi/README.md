# QMI (Qualcomm MSM Interface)
Here are the chips needed to use an LTE communication dongle with QMI from Linux.

## qmi-network
A command tool to manage QMI devices.

### installation

The install script of the qmi tool is available as [here](https://github.com/UedaTakeyuki/gc_setups/blob/master/libqmi-utils.setup.sh).

### usage
```
qmi-network [OPTIONS] [DEVICE] [COMMAND]
```

- OPTIONS:
  - --profile=[PATH] Use the profile in the specified path
  - --help Show help options
  - --version Show version

```
sudo qmi-network --profile=./soracom.conf /dev/cdc-wdm0 start
```

```
sudo qmi-network --profile=./soracom.conf /dev/cdc-wdm0 stop
```

Without --profile option, ```/etc/qmi-network.conf``` is used as the profile. So, you can copy one of the .conf files of this to the ```/etc/qmi-network.conf```.

## documents
- [manpage of the qmi-network](https://www.freedesktop.org/software/libqmi/man/latest/qmi-network.1.html?__goaway_challenge=meta-refresh&__goaway_id=507928b5219e97d47446903227df0ad5&__goaway_referer=https%3A%2F%2Fwww.google.com%2F)
