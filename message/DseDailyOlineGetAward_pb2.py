# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseDailyOlineGetAward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DseDailyOlineGetAward.proto',
  package='',
  serialized_pb=_b('\n\x1b\x44seDailyOlineGetAward.proto\"3\n\x15\x44seDailyOlineGetAward\x12\x0b\n\x03res\x18\x01 \x01(\x05\x12\r\n\x05\x62oxid\x18\x02 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSEDAILYOLINEGETAWARD = _descriptor.Descriptor(
  name='DseDailyOlineGetAward',
  full_name='DseDailyOlineGetAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='DseDailyOlineGetAward.res', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boxid', full_name='DseDailyOlineGetAward.boxid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['DseDailyOlineGetAward'] = _DSEDAILYOLINEGETAWARD

DseDailyOlineGetAward = _reflection.GeneratedProtocolMessageType('DseDailyOlineGetAward', (_message.Message,), dict(
  DESCRIPTOR = _DSEDAILYOLINEGETAWARD,
  __module__ = 'DseDailyOlineGetAward_pb2'
  # @@protoc_insertion_point(class_scope:DseDailyOlineGetAward)
  ))
_sym_db.RegisterMessage(DseDailyOlineGetAward)


# @@protoc_insertion_point(module_scope)