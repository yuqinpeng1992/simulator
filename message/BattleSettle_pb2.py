# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattleSettle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MDropList_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='BattleSettle.proto',
  package='',
  serialized_pb=_b('\n\x12\x42\x61ttleSettle.proto\x1a\x0fMDropList.proto\"h\n\x0c\x42\x61ttleSettle\x12\x0c\n\x04star\x18\x01 \x01(\x05\x12\x0c\n\x04gold\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\x12\x11\n\tfirstpass\x18\x04 \x01(\x08\x12\x1c\n\x08\x64roplist\x18\x05 \x01(\x0b\x32\n.MDropList')
  ,
  dependencies=[MDropList_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLESETTLE = _descriptor.Descriptor(
  name='BattleSettle',
  full_name='BattleSettle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='star', full_name='BattleSettle.star', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='BattleSettle.gold', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='BattleSettle.exp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firstpass', full_name='BattleSettle.firstpass', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='droplist', full_name='BattleSettle.droplist', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_end=143,
)

_BATTLESETTLE.fields_by_name['droplist'].message_type = MDropList_pb2._MDROPLIST
DESCRIPTOR.message_types_by_name['BattleSettle'] = _BATTLESETTLE

BattleSettle = _reflection.GeneratedProtocolMessageType('BattleSettle', (_message.Message,), dict(
  DESCRIPTOR = _BATTLESETTLE,
  __module__ = 'BattleSettle_pb2'
  # @@protoc_insertion_point(class_scope:BattleSettle)
  ))
_sym_db.RegisterMessage(BattleSettle)


# @@protoc_insertion_point(module_scope)
