# Crow IP 8/16 Module using HACS for Home Assistant

all credits to @febalci [LINK](https://github.com/febalci) for his great work.

His thread in HA community is: [Links to HA community](https://community.home-assistant.io/t/custom-component-crow-runner-arrowhead-aap-8-16-alarm-ip-module/130588?u=febalci)

For Crow Runner 8/16 with IP Module and special Firmware running via SSH Running in Home Assistant Version 2024.1.2 and higher (Python 3.11.6)
Ensure that your Crow Runner IP Module is running the correct firmware. The standard firmware from Crow or AAP will NOT work with this version!!

In order to get that module running you must ensure that the preconditions are fulfilled:
=========================================================================================

- running a Alarm System as Runner 8/16 Connected to that an IP Module
- The firmware version required for this component is **Ver 2.10.3628 2017 Oct 20 09:48:43** and it is specifically written for telnet connection to home automation software. You will need to contact AAP from their email address in that web page and request this firmware.
- not having ANY SSH connection active to that IP Module (Firmware support just a single connection ) to SSH standardport 5002.
- WebUi can be reached with IP adress that is given in the first Bootup via DHCP Server.
- set the IP adress to static in order to keep a fixed IP adress at any time.
- running home assistant higher then release version 2024.1.2 (lower once are not support)

An setup example is given below:
================================
In order to get that module running you must ensure that the preconditions are fulfilled.

- Base system is a Alarm System as Crow Runner 8/16
- Connected to that bases system is an IP Module running Firmware Ver 2.10.3628 2017 Oct 20 09:48:43
- Not connected ANY SSH connection (Firmware support just a single connection ) to SSH standard port is 5002
- WebUi can be reached with IP adress that is given in the first Bootup via DHCP Server
- Password should be 12345678 if not changed by your installer company.


Add customer repo to your HA HACS installation:
===============================================


[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?repository=ha_pycrowipmodule&category=Integration&owner=acdcnow)



Config Code:
============

```
crowipmodule:
  host: xxx.xxx.xxx.xxx ( any IP adress it is recommanted to set a static IP adress)
  port: 5002
  keepalive_interval: 60
  timeout: 20
  areas:
    1:
      name: 'Home'  (Name it like you want)
      code: '1234'  (Keypad Arm and Disarm Code (User code))
    2:
      name: 'None' (Name it like you want)
      code: '1234'  (Keypad Arm and Disarm Code (User code))
  outputs:
    3:
      name: 'Main Router' (Name it like you want)
    4:
      name: 'USV Restart' (Name it like you want)
  zones:
    1: --> depends on your installation how many zones you have and the type of your base system and 8 or 16 zone system
      name: 'Entrance' (Name it like you want)
      type: 'motion' (support type are motion, door, window)
    2:
      name: 'Terrace'
      type: 'door'
    3:
      name: 'Kitchen Window'
      type: 'window'
    4:
      name: 'Kitchen Door'
      type: 'door'
    5:
      name: 'Kitchen Motion'
      type: 'motion'
    6:
      name: 'Bedroom Motion'
      type: 'motion'
    7:
      name: 'Child Room'
      type: 'door'
    8:
      name: 'Child Window Wireless'
      type: 'window'
    9:
      name: 'Child PIR'
      type: 'motion'
    10:
      name: 'Den Motion'
      type: 'motion'
    11:
      name: 'Guest Motion'
      type: 'motion'
    12:
      name: 'Hall Motion'
      type: 'motion'
    13:
      name: 'Hobby Motion'
      type: 'motion'
    14:
      name: 'Bedroom Door'
      type: 'door'
    15:
      name: 'Guest Door'
      type: 'door'
    16:
      name: 'Exit Wireless'
      type: 'door'
```

Changelog:
==========
Core2024.01:
- HACS asjustments and prepair for config_flow.py setup
Core2023.08:
- tryfix on python 3.11 and fix the update error on binary sensors
- requirements V0.28 to adjust the need on python 3.10
- state attribute update for 2021.12.0 release
- When HA restarts; update all entities just after the connection is established.
- Check network disconnects real-time.
- ESA waits until STATUS request
- Added RL1 and RL2 Relays
- Corrected HA 110 breaking changes
- SwitchDevice, BinarySensorDevice and AlarmControlPanel is deprecated,
- modify to extend SwitchEntity, BinarySensorEntity and AlarmControlPanelEntity
- Add the respository to HACS
- Corrected HA 103 breaking changes made on alarm_control_panel.
- Outputs controlling and status corrected.
- Removed sensor.area_a_keypad and added sensor.crow_alarm_system; this new sensor has all system related attributes only.
- Handle trigger based disconnection issue.
- Corrected some issues.
- Corrected deepcopy dict, which results area_keypad device attributes to be the same as alarm_control_panel.
- Corrected alarm trigger updates of both area_keypad and alarm_control_panel.
- System binary sensors are converted to alarm control panel device attributes.
- If 'code' configuration is missing in configuration.yaml, then keypad is on in Alarm Panel.
- 'code' configuration is moved to 'areas' section for area specific code.
- Corrected some errors.
