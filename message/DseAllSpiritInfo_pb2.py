# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseAllSpiritInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import DseSingleSpiritInfo_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DseAllSpiritInfo.proto',
  package='',
  serialized_pb=_b('\n\x16\x44seAllSpiritInfo.proto\x1a\x19\x44seSingleSpiritInfo.proto\":\n\x10\x44seAllSpiritInfo\x12&\n\x08soldiers\x18\x01 \x03(\x0b\x32\x14.DseSingleSpiritInfo')
  ,
  dependencies=[DseSingleSpiritInfo_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSEALLSPIRITINFO = _descriptor.Descriptor(
  name='DseAllSpiritInfo',
  full_name='DseAllSpiritInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='soldiers', full_name='DseAllSpiritInfo.soldiers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=53,
  serialized_end=111,
)

_DSEALLSPIRITINFO.fields_by_name['soldiers'].message_type = DseSingleSpiritInfo_pb2._DSESINGLESPIRITINFO
DESCRIPTOR.message_types_by_name['DseAllSpiritInfo'] = _DSEALLSPIRITINFO

DseAllSpiritInfo = _reflection.GeneratedProtocolMessageType('DseAllSpiritInfo', (_message.Message,), dict(
  DESCRIPTOR = _DSEALLSPIRITINFO,
  __module__ = 'DseAllSpiritInfo_pb2'
  # @@protoc_insertion_point(class_scope:DseAllSpiritInfo)
  ))
_sym_db.RegisterMessage(DseAllSpiritInfo)


# @@protoc_insertion_point(module_scope)
