1//Process conduted in a RPi Zero2 with Bookworm 
//Install the necessary dependencies to work with the bluetooth protocol
$sudo apt install -y pi-bluetooth bluetooth bluez picocom blueman python3-pip

2// Edit Bluetooth service
$ sudo nano /etc/systemd/system/dbus-org.bluez.service

3// Once open search fo the section [Service] and add the following lines
// In RPi5 and RPiz2 with Bookworm the first line was already there. Then just add the -C at the end
ExecStart=/usr/lib/bluetooth/bluetoothd -C
ExecStartPost=/usr/bin/sdptool add SP

4// Reload system units
$ sudo systemctl daemon-reload

5// Enable Bluetooth service
$ sudo systemctl enable --now bluetooth

6// In both RPi5 and RPiz2 with Bookworm I got the following error
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_CTYPE = "UTF-8",
	LANG = "en_GB.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_GB.UTF-8").
// I solved it by adding manually the language and the LC_ALL as follows:
// Edit the following file /etc/default/locale by adding
LANG=en_GB.UTF-8
LC_CTYPE=en_GB.UTF-8
LC_MESSAGES=en_GB.UTF-8
LC_ALL=en_GB.UTF-8

// EXTRA ERROR//
// If it keeps printing the previous error I run the following lines and usually solves the problem
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8

//EXTRA ERROR//
// Another error appeared
Failed to start bluetooth.service: Unit bluetooth.service has a bad unit file setting.
See system logs and 'systemctl status bluetooth.service' for details.
// I found out that I forgot to add the Post in ExecStartPost section 3

7// Enable Bluetooth service
$ sudo systemctl enable --now bluetooth

8// Edit the next file to load rfcomm automatically
$ sudo nano /etc/modules-load.d/modules.conf
// Add the following line
rfcomm

9// Reboot the system

// Pair with the HC-05 Module
10// Turn on the already setup Arduino
11// Access the bluetooth console in the RPi
$ sudo bluetoothctl 

12// Pair with bluetooth module
[bluetooth]# agent on
[bluetooth]# scan on
  Discovery started
  [NEW] Device 98:D3:31:50:4A:C1 98-D3-31-50-4A-C1
  [CHG] Device 98:D3:31:50:4A:C1 LegacyPairing: no
  [CHG] Device 98:D3:31:50:4A:C1 Name: ARDUINOBT
  [CHG] Device 98:D3:31:50:4A:C1 Alias: ARDUINOBT

[bluetooth]# pair 98:D3:31:50:4A:C1
  Attempting to pair with 98:D3:31:50:4A:C1
  [CHG] Device 98:D3:31:50:4A:C1 Connected: yes
  Request PIN code
  [agent] Enter PIN code: 1234
  [CHG] Device 98:D3:31:50:4A:C1 UUIDs: 00001101-0000-1000-8000-00805f9b34fb
  [CHG] Device 98:D3:31:50:4A:C1 ServicesResolved: yes
  [CHG] Device 98:D3:31:50:4A:C1 Paired: yes
  Pairing successful
  [CHG] Device 98:D3:31:50:4A:C1 ServicesResolved: no
  [CHG] Device 98:D3:31:50:4A:C1 Connected: no

[bluetooth]# trust 98:D3:31:50:4A:C1
  [CHG] Device 98:D3:31:50:4A:C1 Trusted: yes
  Changing 98:D3:31:50:4A:C1 trust succeeded

[bluetooth]# exit

13// Create a serial device
$ sudo rfcomm bind rfcomm0 <device's MAC>
