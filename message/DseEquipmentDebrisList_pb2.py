# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseEquipmentDebrisList.proto

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
  name='DseEquipmentDebrisList.proto',
  package='',
  serialized_pb=_b('\n\x1c\x44seEquipmentDebrisList.proto\x1a\x0bMItem.proto\"/\n\x16\x44seEquipmentDebrisList\x12\x15\n\x05items\x18\x01 \x03(\x0b\x32\x06.MItem')
  ,
  dependencies=[MItem_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSEEQUIPMENTDEBRISLIST = _descriptor.Descriptor(
  name='DseEquipmentDebrisList',
  full_name='DseEquipmentDebrisList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='DseEquipmentDebrisList.items', index=0,
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
  serialized_start=45,
  serialized_end=92,
)

_DSEEQUIPMENTDEBRISLIST.fields_by_name['items'].message_type = MItem_pb2._MITEM
DESCRIPTOR.message_types_by_name['DseEquipmentDebrisList'] = _DSEEQUIPMENTDEBRISLIST

DseEquipmentDebrisList = _reflection.GeneratedProtocolMessageType('DseEquipmentDebrisList', (_message.Message,), dict(
  DESCRIPTOR = _DSEEQUIPMENTDEBRISLIST,
  __module__ = 'DseEquipmentDebrisList_pb2'
  # @@protoc_insertion_point(class_scope:DseEquipmentDebrisList)
  ))
_sym_db.RegisterMessage(DseEquipmentDebrisList)


# @@protoc_insertion_point(module_scope)
