# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communication.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='communication.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x63ommunication.proto\"\x80\x12\n\rCommunication\x12\x34\n\x0eserver_channel\x18\x01 \x01(\x0b\x32\x1c.Communication.ServerChannel\x12\x1f\n\x03lan\x18\x02 \x01(\x0b\x32\x12.Communication.Lan\x12%\n\x07rs485_1\x18\x03 \x01(\x0b\x32\x14.Communication.RS485\x12%\n\x07rs485_2\x18\x04 \x01(\x0b\x32\x14.Communication.RS485\x12,\n\nmodbus_tcp\x18\t \x01(\x0b\x32\x18.Communication.ModbusTCP\x12!\n\x04wifi\x18\x06 \x01(\x0b\x32\x13.Communication.Wifi\x12!\n\x04gpio\x18\x08 \x01(\x0b\x32\x13.Communication.GPIO\x12\x36\n\x11server_connection\x18\x0b \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x1a)\n\x0c\x42oolKeyValue\x12\r\n\x05value\x18\x01 \x01(\x08\x12\n\n\x02ro\x18\x02 \x01(\x08\x1a*\n\rInt32KeyValue\x12\r\n\x05value\x18\x01 \x01(\x05\x12\n\n\x02ro\x18\x02 \x01(\x08\x1a+\n\x0eStringKeyValue\x12\r\n\x05value\x18\x01 \x01(\t\x12\n\n\x02ro\x18\x02 \x01(\x08\x1a\x9c\x02\n\rServerChannel\x12(\n\x03lan\x18\x01 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12-\n\x08\x63\x65llular\x18\x02 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12,\n\x07rs485_1\x18\x03 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12,\n\x07rs485_2\x18\x04 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12+\n\x06zigbee\x18\x05 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12)\n\x04wifi\x18\x06 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x1a\xed\x02\n\x03Lan\x12)\n\x04\x64hcp\x18\x01 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12!\n\x02ip\x18\x02 \x01(\x0b\x32\x15.Communication.Lan.IP\x12*\n\x03mac\x18\x03 \x01(\x0b\x32\x1d.Communication.StringKeyValue\x12.\n\tconnected\x18\x04 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x1a\xbb\x01\n\x02IP\x12)\n\x02ip\x18\x01 \x01(\x0b\x32\x1d.Communication.StringKeyValue\x12.\n\x07netmask\x18\x02 \x01(\x0b\x32\x1d.Communication.StringKeyValue\x12.\n\x07gateway\x18\x03 \x01(\x0b\x32\x1d.Communication.StringKeyValue\x12*\n\x03\x64ns\x18\x04 \x01(\x0b\x32\x1d.Communication.StringKeyValue\x1a\xe2\x02\n\x05RS485\x12/\n\x08protocol\x18\x01 \x01(\x0b\x32\x1d.Communication.RS485.Protocol\x12/\n\tdevice_id\x18\x07 \x01(\x0b\x32\x1c.Communication.Int32KeyValue\x1a\xf6\x01\n\x08Protocol\x12-\n\x08se_slave\x18\x01 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12.\n\tse_master\x18\x02 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12\x32\n\rmulti_devices\x18\x03 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12,\n\x07sunspec\x18\x04 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12)\n\x04none\x18\x05 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x1a\x65\n\tModbusTCP\x12,\n\x07\x65nabled\x18\x01 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12*\n\x04port\x18\x02 \x01(\x0b\x32\x1c.Communication.Int32KeyValue\x1a\xdc\x02\n\x04Wifi\x12\x0c\n\x04ssid\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x32\n\x0cwps_duration\x18\x04 \x01(\x0b\x32\x1c.Communication.Int32KeyValue\x12\x38\n\rconfiguration\x18\x05 \x01(\x0b\x32!.Communication.Wifi.Configuration\x12\x35\n\x10\x65xternal_antenna\x18\x07 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x1a\x90\x01\n\rConfiguration\x12\'\n\x02hg\x18\x01 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12,\n\x07station\x18\x02 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12(\n\x03wps\x18\x03 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x1a\xdf\x02\n\x04GPIO\x12,\n\x07primary\x18\x01 \x01(\x0b\x32\x1b.Communication.GPIO.Primary\x1a\xa8\x02\n\x07Primary\x12,\n\x07\x64isable\x18\x01 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12)\n\x04rrcr\x18\x02 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12-\n\x08\x61\x63_relay\x18\x03 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12\x32\n\rrrcr_ac_relay\x18\x04 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12(\n\x03\x64rm\x18\x05 \x01(\x0b\x32\x1b.Communication.BoolKeyValue\x12\x37\n\x12\x65xternal_generator\x18\x06 \x01(\x0b\x32\x1b.Communication.BoolKeyValueb\x06proto3')
)




_COMMUNICATION_BOOLKEYVALUE = _descriptor.Descriptor(
  name='BoolKeyValue',
  full_name='Communication.BoolKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Communication.BoolKeyValue.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ro', full_name='Communication.BoolKeyValue.ro', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=419,
)

_COMMUNICATION_INT32KEYVALUE = _descriptor.Descriptor(
  name='Int32KeyValue',
  full_name='Communication.Int32KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Communication.Int32KeyValue.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ro', full_name='Communication.Int32KeyValue.ro', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=463,
)

_COMMUNICATION_STRINGKEYVALUE = _descriptor.Descriptor(
  name='StringKeyValue',
  full_name='Communication.StringKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Communication.StringKeyValue.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ro', full_name='Communication.StringKeyValue.ro', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=508,
)

_COMMUNICATION_SERVERCHANNEL = _descriptor.Descriptor(
  name='ServerChannel',
  full_name='Communication.ServerChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lan', full_name='Communication.ServerChannel.lan', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cellular', full_name='Communication.ServerChannel.cellular', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rs485_1', full_name='Communication.ServerChannel.rs485_1', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rs485_2', full_name='Communication.ServerChannel.rs485_2', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zigbee', full_name='Communication.ServerChannel.zigbee', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wifi', full_name='Communication.ServerChannel.wifi', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=795,
)

_COMMUNICATION_LAN_IP = _descriptor.Descriptor(
  name='IP',
  full_name='Communication.Lan.IP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='Communication.Lan.IP.ip', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netmask', full_name='Communication.Lan.IP.netmask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='Communication.Lan.IP.gateway', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns', full_name='Communication.Lan.IP.dns', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=976,
  serialized_end=1163,
)

_COMMUNICATION_LAN = _descriptor.Descriptor(
  name='Lan',
  full_name='Communication.Lan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dhcp', full_name='Communication.Lan.dhcp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='Communication.Lan.ip', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mac', full_name='Communication.Lan.mac', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='Communication.Lan.connected', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMMUNICATION_LAN_IP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=798,
  serialized_end=1163,
)

_COMMUNICATION_RS485_PROTOCOL = _descriptor.Descriptor(
  name='Protocol',
  full_name='Communication.RS485.Protocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='se_slave', full_name='Communication.RS485.Protocol.se_slave', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='se_master', full_name='Communication.RS485.Protocol.se_master', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi_devices', full_name='Communication.RS485.Protocol.multi_devices', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sunspec', full_name='Communication.RS485.Protocol.sunspec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='none', full_name='Communication.RS485.Protocol.none', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1274,
  serialized_end=1520,
)

_COMMUNICATION_RS485 = _descriptor.Descriptor(
  name='RS485',
  full_name='Communication.RS485',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='Communication.RS485.protocol', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='Communication.RS485.device_id', index=1,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMMUNICATION_RS485_PROTOCOL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1166,
  serialized_end=1520,
)

_COMMUNICATION_MODBUSTCP = _descriptor.Descriptor(
  name='ModbusTCP',
  full_name='Communication.ModbusTCP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='Communication.ModbusTCP.enabled', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='Communication.ModbusTCP.port', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1522,
  serialized_end=1623,
)

_COMMUNICATION_WIFI_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='Communication.Wifi.Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hg', full_name='Communication.Wifi.Configuration.hg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='station', full_name='Communication.Wifi.Configuration.station', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wps', full_name='Communication.Wifi.Configuration.wps', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1830,
  serialized_end=1974,
)

_COMMUNICATION_WIFI = _descriptor.Descriptor(
  name='Wifi',
  full_name='Communication.Wifi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='Communication.Wifi.ssid', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Communication.Wifi.status', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wps_duration', full_name='Communication.Wifi.wps_duration', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configuration', full_name='Communication.Wifi.configuration', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_antenna', full_name='Communication.Wifi.external_antenna', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMMUNICATION_WIFI_CONFIGURATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1626,
  serialized_end=1974,
)

_COMMUNICATION_GPIO_PRIMARY = _descriptor.Descriptor(
  name='Primary',
  full_name='Communication.GPIO.Primary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disable', full_name='Communication.GPIO.Primary.disable', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrcr', full_name='Communication.GPIO.Primary.rrcr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ac_relay', full_name='Communication.GPIO.Primary.ac_relay', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrcr_ac_relay', full_name='Communication.GPIO.Primary.rrcr_ac_relay', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drm', full_name='Communication.GPIO.Primary.drm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_generator', full_name='Communication.GPIO.Primary.external_generator', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2032,
  serialized_end=2328,
)

_COMMUNICATION_GPIO = _descriptor.Descriptor(
  name='GPIO',
  full_name='Communication.GPIO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary', full_name='Communication.GPIO.primary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMMUNICATION_GPIO_PRIMARY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1977,
  serialized_end=2328,
)

_COMMUNICATION = _descriptor.Descriptor(
  name='Communication',
  full_name='Communication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_channel', full_name='Communication.server_channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lan', full_name='Communication.lan', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rs485_1', full_name='Communication.rs485_1', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rs485_2', full_name='Communication.rs485_2', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modbus_tcp', full_name='Communication.modbus_tcp', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wifi', full_name='Communication.wifi', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpio', full_name='Communication.gpio', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_connection', full_name='Communication.server_connection', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMMUNICATION_BOOLKEYVALUE, _COMMUNICATION_INT32KEYVALUE, _COMMUNICATION_STRINGKEYVALUE, _COMMUNICATION_SERVERCHANNEL, _COMMUNICATION_LAN, _COMMUNICATION_RS485, _COMMUNICATION_MODBUSTCP, _COMMUNICATION_WIFI, _COMMUNICATION_GPIO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=2328,
)

_COMMUNICATION_BOOLKEYVALUE.containing_type = _COMMUNICATION
_COMMUNICATION_INT32KEYVALUE.containing_type = _COMMUNICATION
_COMMUNICATION_STRINGKEYVALUE.containing_type = _COMMUNICATION
_COMMUNICATION_SERVERCHANNEL.fields_by_name['lan'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_SERVERCHANNEL.fields_by_name['cellular'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_SERVERCHANNEL.fields_by_name['rs485_1'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_SERVERCHANNEL.fields_by_name['rs485_2'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_SERVERCHANNEL.fields_by_name['zigbee'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_SERVERCHANNEL.fields_by_name['wifi'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_SERVERCHANNEL.containing_type = _COMMUNICATION
_COMMUNICATION_LAN_IP.fields_by_name['ip'].message_type = _COMMUNICATION_STRINGKEYVALUE
_COMMUNICATION_LAN_IP.fields_by_name['netmask'].message_type = _COMMUNICATION_STRINGKEYVALUE
_COMMUNICATION_LAN_IP.fields_by_name['gateway'].message_type = _COMMUNICATION_STRINGKEYVALUE
_COMMUNICATION_LAN_IP.fields_by_name['dns'].message_type = _COMMUNICATION_STRINGKEYVALUE
_COMMUNICATION_LAN_IP.containing_type = _COMMUNICATION_LAN
_COMMUNICATION_LAN.fields_by_name['dhcp'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_LAN.fields_by_name['ip'].message_type = _COMMUNICATION_LAN_IP
_COMMUNICATION_LAN.fields_by_name['mac'].message_type = _COMMUNICATION_STRINGKEYVALUE
_COMMUNICATION_LAN.fields_by_name['connected'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_LAN.containing_type = _COMMUNICATION
_COMMUNICATION_RS485_PROTOCOL.fields_by_name['se_slave'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_RS485_PROTOCOL.fields_by_name['se_master'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_RS485_PROTOCOL.fields_by_name['multi_devices'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_RS485_PROTOCOL.fields_by_name['sunspec'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_RS485_PROTOCOL.fields_by_name['none'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_RS485_PROTOCOL.containing_type = _COMMUNICATION_RS485
_COMMUNICATION_RS485.fields_by_name['protocol'].message_type = _COMMUNICATION_RS485_PROTOCOL
_COMMUNICATION_RS485.fields_by_name['device_id'].message_type = _COMMUNICATION_INT32KEYVALUE
_COMMUNICATION_RS485.containing_type = _COMMUNICATION
_COMMUNICATION_MODBUSTCP.fields_by_name['enabled'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_MODBUSTCP.fields_by_name['port'].message_type = _COMMUNICATION_INT32KEYVALUE
_COMMUNICATION_MODBUSTCP.containing_type = _COMMUNICATION
_COMMUNICATION_WIFI_CONFIGURATION.fields_by_name['hg'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_WIFI_CONFIGURATION.fields_by_name['station'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_WIFI_CONFIGURATION.fields_by_name['wps'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_WIFI_CONFIGURATION.containing_type = _COMMUNICATION_WIFI
_COMMUNICATION_WIFI.fields_by_name['wps_duration'].message_type = _COMMUNICATION_INT32KEYVALUE
_COMMUNICATION_WIFI.fields_by_name['configuration'].message_type = _COMMUNICATION_WIFI_CONFIGURATION
_COMMUNICATION_WIFI.fields_by_name['external_antenna'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_WIFI.containing_type = _COMMUNICATION
_COMMUNICATION_GPIO_PRIMARY.fields_by_name['disable'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_GPIO_PRIMARY.fields_by_name['rrcr'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_GPIO_PRIMARY.fields_by_name['ac_relay'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_GPIO_PRIMARY.fields_by_name['rrcr_ac_relay'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_GPIO_PRIMARY.fields_by_name['drm'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_GPIO_PRIMARY.fields_by_name['external_generator'].message_type = _COMMUNICATION_BOOLKEYVALUE
_COMMUNICATION_GPIO_PRIMARY.containing_type = _COMMUNICATION_GPIO
_COMMUNICATION_GPIO.fields_by_name['primary'].message_type = _COMMUNICATION_GPIO_PRIMARY
_COMMUNICATION_GPIO.containing_type = _COMMUNICATION
_COMMUNICATION.fields_by_name['server_channel'].message_type = _COMMUNICATION_SERVERCHANNEL
_COMMUNICATION.fields_by_name['lan'].message_type = _COMMUNICATION_LAN
_COMMUNICATION.fields_by_name['rs485_1'].message_type = _COMMUNICATION_RS485
_COMMUNICATION.fields_by_name['rs485_2'].message_type = _COMMUNICATION_RS485
_COMMUNICATION.fields_by_name['modbus_tcp'].message_type = _COMMUNICATION_MODBUSTCP
_COMMUNICATION.fields_by_name['wifi'].message_type = _COMMUNICATION_WIFI
_COMMUNICATION.fields_by_name['gpio'].message_type = _COMMUNICATION_GPIO
_COMMUNICATION.fields_by_name['server_connection'].message_type = _COMMUNICATION_BOOLKEYVALUE
DESCRIPTOR.message_types_by_name['Communication'] = _COMMUNICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Communication = _reflection.GeneratedProtocolMessageType('Communication', (_message.Message,), dict(

  BoolKeyValue = _reflection.GeneratedProtocolMessageType('BoolKeyValue', (_message.Message,), dict(
    DESCRIPTOR = _COMMUNICATION_BOOLKEYVALUE,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.BoolKeyValue)
    ))
  ,

  Int32KeyValue = _reflection.GeneratedProtocolMessageType('Int32KeyValue', (_message.Message,), dict(
    DESCRIPTOR = _COMMUNICATION_INT32KEYVALUE,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.Int32KeyValue)
    ))
  ,

  StringKeyValue = _reflection.GeneratedProtocolMessageType('StringKeyValue', (_message.Message,), dict(
    DESCRIPTOR = _COMMUNICATION_STRINGKEYVALUE,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.StringKeyValue)
    ))
  ,

  ServerChannel = _reflection.GeneratedProtocolMessageType('ServerChannel', (_message.Message,), dict(
    DESCRIPTOR = _COMMUNICATION_SERVERCHANNEL,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.ServerChannel)
    ))
  ,

  Lan = _reflection.GeneratedProtocolMessageType('Lan', (_message.Message,), dict(

    IP = _reflection.GeneratedProtocolMessageType('IP', (_message.Message,), dict(
      DESCRIPTOR = _COMMUNICATION_LAN_IP,
      __module__ = 'communication_pb2'
      # @@protoc_insertion_point(class_scope:Communication.Lan.IP)
      ))
    ,
    DESCRIPTOR = _COMMUNICATION_LAN,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.Lan)
    ))
  ,

  RS485 = _reflection.GeneratedProtocolMessageType('RS485', (_message.Message,), dict(

    Protocol = _reflection.GeneratedProtocolMessageType('Protocol', (_message.Message,), dict(
      DESCRIPTOR = _COMMUNICATION_RS485_PROTOCOL,
      __module__ = 'communication_pb2'
      # @@protoc_insertion_point(class_scope:Communication.RS485.Protocol)
      ))
    ,
    DESCRIPTOR = _COMMUNICATION_RS485,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.RS485)
    ))
  ,

  ModbusTCP = _reflection.GeneratedProtocolMessageType('ModbusTCP', (_message.Message,), dict(
    DESCRIPTOR = _COMMUNICATION_MODBUSTCP,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.ModbusTCP)
    ))
  ,

  Wifi = _reflection.GeneratedProtocolMessageType('Wifi', (_message.Message,), dict(

    Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), dict(
      DESCRIPTOR = _COMMUNICATION_WIFI_CONFIGURATION,
      __module__ = 'communication_pb2'
      # @@protoc_insertion_point(class_scope:Communication.Wifi.Configuration)
      ))
    ,
    DESCRIPTOR = _COMMUNICATION_WIFI,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.Wifi)
    ))
  ,

  GPIO = _reflection.GeneratedProtocolMessageType('GPIO', (_message.Message,), dict(

    Primary = _reflection.GeneratedProtocolMessageType('Primary', (_message.Message,), dict(
      DESCRIPTOR = _COMMUNICATION_GPIO_PRIMARY,
      __module__ = 'communication_pb2'
      # @@protoc_insertion_point(class_scope:Communication.GPIO.Primary)
      ))
    ,
    DESCRIPTOR = _COMMUNICATION_GPIO,
    __module__ = 'communication_pb2'
    # @@protoc_insertion_point(class_scope:Communication.GPIO)
    ))
  ,
  DESCRIPTOR = _COMMUNICATION,
  __module__ = 'communication_pb2'
  # @@protoc_insertion_point(class_scope:Communication)
  ))
_sym_db.RegisterMessage(Communication)
_sym_db.RegisterMessage(Communication.BoolKeyValue)
_sym_db.RegisterMessage(Communication.Int32KeyValue)
_sym_db.RegisterMessage(Communication.StringKeyValue)
_sym_db.RegisterMessage(Communication.ServerChannel)
_sym_db.RegisterMessage(Communication.Lan)
_sym_db.RegisterMessage(Communication.Lan.IP)
_sym_db.RegisterMessage(Communication.RS485)
_sym_db.RegisterMessage(Communication.RS485.Protocol)
_sym_db.RegisterMessage(Communication.ModbusTCP)
_sym_db.RegisterMessage(Communication.Wifi)
_sym_db.RegisterMessage(Communication.Wifi.Configuration)
_sym_db.RegisterMessage(Communication.GPIO)
_sym_db.RegisterMessage(Communication.GPIO.Primary)


# @@protoc_insertion_point(module_scope)