# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_configs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app_configs.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x61pp_configs.proto\"\xbd\x02\n\rWebAppConfigs\x12)\n\x08mainmenu\x18\x01 \x01(\x0b\x32\x17.WebAppConfigs.MainMenu\x12\x10\n\x08language\x18\x02 \x01(\x05\x1a\xee\x01\n\x08MainMenu\x12\x1c\n\x14\x63ountry_and_language\x18\x01 \x01(\x08\x12\x0f\n\x07pairing\x18\x02 \x01(\x08\x12\x15\n\rcommunication\x18\x03 \x01(\x08\x12\x15\n\rpower_control\x18\x04 \x01(\x08\x12\x16\n\x0e\x64\x65vice_manager\x18\x05 \x01(\x08\x12\x13\n\x0bmaintenance\x18\x06 \x01(\x08\x12\x13\n\x0binformation\x18\x07 \x01(\x08\x12\x1a\n\x12site_configuration\x18\x08 \x01(\x08\x12\x0e\n\x06status\x18\t \x01(\x08\x12\x17\n\x0fgrid_protection\x18\n \x01(\x08\x62\x06proto3')
)




_WEBAPPCONFIGS_MAINMENU = _descriptor.Descriptor(
  name='MainMenu',
  full_name='WebAppConfigs.MainMenu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_and_language', full_name='WebAppConfigs.MainMenu.country_and_language', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pairing', full_name='WebAppConfigs.MainMenu.pairing', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='communication', full_name='WebAppConfigs.MainMenu.communication', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='power_control', full_name='WebAppConfigs.MainMenu.power_control', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_manager', full_name='WebAppConfigs.MainMenu.device_manager', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maintenance', full_name='WebAppConfigs.MainMenu.maintenance', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='information', full_name='WebAppConfigs.MainMenu.information', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_configuration', full_name='WebAppConfigs.MainMenu.site_configuration', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='WebAppConfigs.MainMenu.status', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grid_protection', full_name='WebAppConfigs.MainMenu.grid_protection', index=9,
      number=10, type=8, cpp_type=7, label=1,
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
  serialized_start=101,
  serialized_end=339,
)

_WEBAPPCONFIGS = _descriptor.Descriptor(
  name='WebAppConfigs',
  full_name='WebAppConfigs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mainmenu', full_name='WebAppConfigs.mainmenu', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='WebAppConfigs.language', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WEBAPPCONFIGS_MAINMENU, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=339,
)

_WEBAPPCONFIGS_MAINMENU.containing_type = _WEBAPPCONFIGS
_WEBAPPCONFIGS.fields_by_name['mainmenu'].message_type = _WEBAPPCONFIGS_MAINMENU
DESCRIPTOR.message_types_by_name['WebAppConfigs'] = _WEBAPPCONFIGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebAppConfigs = _reflection.GeneratedProtocolMessageType('WebAppConfigs', (_message.Message,), dict(

  MainMenu = _reflection.GeneratedProtocolMessageType('MainMenu', (_message.Message,), dict(
    DESCRIPTOR = _WEBAPPCONFIGS_MAINMENU,
    __module__ = 'app_configs_pb2'
    # @@protoc_insertion_point(class_scope:WebAppConfigs.MainMenu)
    ))
  ,
  DESCRIPTOR = _WEBAPPCONFIGS,
  __module__ = 'app_configs_pb2'
  # @@protoc_insertion_point(class_scope:WebAppConfigs)
  ))
_sym_db.RegisterMessage(WebAppConfigs)
_sym_db.RegisterMessage(WebAppConfigs.MainMenu)


# @@protoc_insertion_point(module_scope)