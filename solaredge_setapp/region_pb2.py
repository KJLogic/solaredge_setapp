# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: region.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='region.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cregion.proto\"\xaa\x01\n\x06Region\x12 \n\x07\x63ountry\x18\x01 \x01(\x0b\x32\x0f.Region.Country\x12\"\n\x08language\x18\x02 \x01(\x0b\x32\x10.Region.Language\x1a+\n\x07\x43ountry\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\x05\x12\x0f\n\x07options\x18\x02 \x03(\x05\x1a-\n\x08Language\x12\x10\n\x08language\x18\x01 \x01(\x05\x12\x0f\n\x07options\x18\x02 \x03(\x05\x62\x06proto3')
)




_REGION_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='Region.Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country', full_name='Region.Country.country', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='Region.Country.options', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=97,
  serialized_end=140,
)

_REGION_LANGUAGE = _descriptor.Descriptor(
  name='Language',
  full_name='Region.Language',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='Region.Language.language', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='Region.Language.options', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=142,
  serialized_end=187,
)

_REGION = _descriptor.Descriptor(
  name='Region',
  full_name='Region',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country', full_name='Region.country', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='Region.language', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REGION_COUNTRY, _REGION_LANGUAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=187,
)

_REGION_COUNTRY.containing_type = _REGION
_REGION_LANGUAGE.containing_type = _REGION
_REGION.fields_by_name['country'].message_type = _REGION_COUNTRY
_REGION.fields_by_name['language'].message_type = _REGION_LANGUAGE
DESCRIPTOR.message_types_by_name['Region'] = _REGION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Region = _reflection.GeneratedProtocolMessageType('Region', (_message.Message,), dict(

  Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), dict(
    DESCRIPTOR = _REGION_COUNTRY,
    __module__ = 'region_pb2'
    # @@protoc_insertion_point(class_scope:Region.Country)
    ))
  ,

  Language = _reflection.GeneratedProtocolMessageType('Language', (_message.Message,), dict(
    DESCRIPTOR = _REGION_LANGUAGE,
    __module__ = 'region_pb2'
    # @@protoc_insertion_point(class_scope:Region.Language)
    ))
  ,
  DESCRIPTOR = _REGION,
  __module__ = 'region_pb2'
  # @@protoc_insertion_point(class_scope:Region)
  ))
_sym_db.RegisterMessage(Region)
_sym_db.RegisterMessage(Region.Country)
_sym_db.RegisterMessage(Region.Language)


# @@protoc_insertion_point(module_scope)
