# solaredge_setapp

solaredge_setapp is a python library that parses inverter and power optimizer data from a compatible SolarEdge PV inverter. Only those models which support SetApp commissioning are supported.

This project is built on the efforts of others: for Home Assistant users, see drobtravels' <a href="https://github.com/drobtravels/solaredge-local">solaredge_local</a>, and jbuehl's <a href="https://github.com/jbuehl/solaredge">solaredge</a> for all non-SetApp power inverters.

Developed and tested on a European SE3500H-RW000BNN4 SolarEdge Inverter -- CPU versions 4.8.19. It may work on newer versions of SetApp.

## Installation

To install, either clone this project and install using `distutils`:

```python3 setup.py install```

### Working on protobuf messages

Clone the project if you want to modify the protocol buffer messages.

In order to use `compile-proto.sh` to (re)compile the protocol buffer `.proto` message definitions you will need `protoc`, which is provided, for example, by Ubuntu's package `protobuf-compiler`. *(Re-)compiling the protobuf messages is only necessary if you have made changes to them.*

## Usage

**Note:** more recent firmware versions have firewalled access to the SetApp interface over *ethernet*. It should still be possible to access your inverter on port 80 via *wifi*.

Basic usage of the **status** API endpoint:



import solaredge_setapp<br>
import requests<br>
import json<br>

inverter_ip = "<your inverter IP address>"<br>
for example:<br>
inverter_ip = "10.0.0.152"<br>

status_request = requests.get(f"http://{inverter_ip}/web/v1/status").content<br>
status = solaredge_setapp.status.Status().parse_protobuf(status_request)<br>

print(f"Inverter {status['serial']} is {status['status']} at {status['power_ac']:.2f}W")<br>

#or write status as json to file:<br>

f = open("/tmp/FileName", "w")<br>
f.write(json.dumps(status))<br>
f.close()<br>




See the `status.proto` file for all possible fields, and `solaredge_setapp/status.py`  for all fields that are parsed for this endpoint.

The following API endpoints are available:

* **app_configs** - web/v1/app_configs - language and functionality
* **communication** - web/v1/communication - ethernet, wifi and RS485 settings
* **device_manager** - web/v1/device_manager - unknown
* **grid_protection** - web/v1/grid_protection - grid protection settings
* **information** - web/v1/information - CPU and DSP versions, error logging
* **maintenance** - web/v1/maintenance - power optimizer telemetry
* **power_control** - web/v1/power_control - grid power settings
* **region** - web/v1/region - language and country settings
* **status** - web/v1/status - inverter and energy statistics

## Limitations

The SetApp API does not (yet) provide real-time power optimizer data. Initial results suggest the data is 5-15 minutes old. Inverter production and voltage information is near real-time, however. Basically, the entire information set visible on the inverter's SetApp web interface is available through this library, in addition to per optimizer voltages and temperatures.

Rate limiting will kick in if you have the SetApp web interface open while also polling using this library.

The SetApp API is new, and therefore likely to change. Variable naming and distribution is likely to change.

## Contributing

Contributions are more than welcome, especially to the protocol buffer message definitions.
