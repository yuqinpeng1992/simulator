# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseSpiritDebrisList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MItem_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DseSpiritDebrisList.proto',
  package='',
  serialized_pb=_b('\n\x19\x44seSpiritDebrisList.proto\x1a\x0bMItem.proto\",\n\x13\x44seSpiritDebrisList\x12\x15\n\x05items\x18\x01 \x03(\x0b\x32\x06.MItem')
  ,
  dependencies=[MItem_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSESPIRITDEBRISLIST = _descriptor.Descriptor(
  name='DseSpiritDebrisList',
  full_name='DseSpiritDebrisList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='DseSpiritDebrisList.items', index=0,
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
  serialized_start=42,
  serialized_end=86,
)

_DSESPIRITDEBRISLIST.fields_by_name['items'].message_type = MItem_pb2._MITEM
DESCRIPTOR.message_types_by_name['DseSpiritDebrisList'] = _DSESPIRITDEBRISLIST

DseSpiritDebrisList = _reflection.GeneratedProtocolMessageType('DseSpiritDebrisList', (_message.Message,), dict(
  DESCRIPTOR = _DSESPIRITDEBRISLIST,
  __module__ = 'DseSpiritDebrisList_pb2'
  # @@protoc_insertion_point(class_scope:DseSpiritDebrisList)
  ))
_sym_db.RegisterMessage(DseSpiritDebrisList)


# @@protoc_insertion_point(module_scope)