# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TacticInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BattleSpirits_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TacticInfo.proto',
  package='',
  serialized_pb=_b('\n\x10TacticInfo.proto\x1a\x13\x42\x61ttleSpirits.proto\"\xab\x01\n\nTacticInfo\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05power\x18\x03 \x01(\x05\x12\x0c\n\x04head\x18\x04 \x01(\x05\x12\x13\n\x08leaderid\x18\x05 \x01(\t:\x01\x30\x12#\n\x0bspiritslist\x18\x06 \x03(\x0b\x32\x0e.BattleSpirits\x12+\n\x13reserverspiritslist\x18\x07 \x03(\x0b\x32\x0e.BattleSpirits')
  ,
  dependencies=[BattleSpirits_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TACTICINFO = _descriptor.Descriptor(
  name='TacticInfo',
  full_name='TacticInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='TacticInfo.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='TacticInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='TacticInfo.power', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head', full_name='TacticInfo.head', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leaderid', full_name='TacticInfo.leaderid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("0").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spiritslist', full_name='TacticInfo.spiritslist', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reserverspiritslist', full_name='TacticInfo.reserverspiritslist', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_end=213,
)

_TACTICINFO.fields_by_name['spiritslist'].message_type = BattleSpirits_pb2._BATTLESPIRITS
_TACTICINFO.fields_by_name['reserverspiritslist'].message_type = BattleSpirits_pb2._BATTLESPIRITS
DESCRIPTOR.message_types_by_name['TacticInfo'] = _TACTICINFO

TacticInfo = _reflection.GeneratedProtocolMessageType('TacticInfo', (_message.Message,), dict(
  DESCRIPTOR = _TACTICINFO,
  __module__ = 'TacticInfo_pb2'
  # @@protoc_insertion_point(class_scope:TacticInfo)
  ))
_sym_db.RegisterMessage(TacticInfo)


# @@protoc_insertion_point(module_scope)