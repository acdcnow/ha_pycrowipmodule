Home Assistant Crow IP Module
For Crow Runner 8/16 with IP Module and special Firmware running via SSH Running in Home Assistant Version 2023.08.0 and higer

Ensure that your Crow Runner IP Module is running the correct firmware. The standard firmware from Crow or AAP will NOT work with this version!!

In order to get that module running you must ensure that the deconditions are fulfilled: That will be:

running a Alarm System as Runner 8/16 Connected to that an IP Module
running Firmware Ver 2.10.3628 2017 Oct 20 09:48:43
not having ANY SSH connection active to that IP Module (Firmware support just a single connection ) to SSH port 5002.
WebUi can be reached with IP adress that is given in the first Bootup via DHCP Server.
set the IP adress to static in order to keep a fixed IP adress at any time.
running home assistant higher then release version 2023.08.0 (lower once are not support)
An setup example is given below:

In order to get that module running you must ensure that the preconditions are fulfilled.

1: Base system is a Alarm System as Crow Runner 8/16
2: Connected to that bases system is an IP Module running Firmware Ver 2.10.3628 2017 Oct 20 09:48:43
3: Not connected ANY SSH connection (Firmware support just a single connection ) to SSH standard port is 5002
4: WebUi can be reached with IP adress that is given in the first Bootup via DHCP Server
   Password should be 12345678 if not changed by your installer company. 


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
Changelog

V2023.08: 
- requirements V0.31 to adjust the need on python 3.11 and fix the timeout error on code adjustments
- state attribute update
- When HA restarts; update all entities just after the connection is established. 
- Check network disconnects real-time. 
- ESA waits until STATUS request 
- Added RL1 and RL2 Relays 
- SwitchDevice, BinarySensorDevice and AlarmControlPanel is deprecated, 
- modify to extend SwitchEntity, BinarySensorEntity and AlarmControlPanelEntity 
- Add the respository to HACS 
- update arm and home based on the different used case from my system
