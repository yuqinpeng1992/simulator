# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseRankList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import RankPlayer_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DseRankList.proto',
  package='',
  serialized_pb=_b('\n\x11\x44seRankList.proto\x1a\x10RankPlayer.proto\">\n\x0b\x44seRankList\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12!\n\x08ranklist\x18\x02 \x01(\x0b\x32\x0f.RankPlayerList')
  ,
  dependencies=[RankPlayer_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSERANKLIST = _descriptor.Descriptor(
  name='DseRankList',
  full_name='DseRankList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DseRankList.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ranklist', full_name='DseRankList.ranklist', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=39,
  serialized_end=101,
)

_DSERANKLIST.fields_by_name['ranklist'].message_type = RankPlayer_pb2._RANKPLAYERLIST
DESCRIPTOR.message_types_by_name['DseRankList'] = _DSERANKLIST

DseRankList = _reflection.GeneratedProtocolMessageType('DseRankList', (_message.Message,), dict(
  DESCRIPTOR = _DSERANKLIST,
  __module__ = 'DseRankList_pb2'
  # @@protoc_insertion_point(class_scope:DseRankList)
  ))
_sym_db.RegisterMessage(DseRankList)


# @@protoc_insertion_point(module_scope)
