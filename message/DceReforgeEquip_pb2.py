# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DceReforgeEquip.proto

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
  name='DceReforgeEquip.proto',
  package='',
  serialized_pb=_b('\n\x15\x44\x63\x65ReforgeEquip.proto\".\n\x0f\x44\x63\x65ReforgeEquip\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\x05\x12\x0b\n\x03tid\x18\x02 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DCEREFORGEEQUIP = _descriptor.Descriptor(
  name='DceReforgeEquip',
  full_name='DceReforgeEquip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='DceReforgeEquip.action', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tid', full_name='DceReforgeEquip.tid', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=25,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['DceReforgeEquip'] = _DCEREFORGEEQUIP

DceReforgeEquip = _reflection.GeneratedProtocolMessageType('DceReforgeEquip', (_message.Message,), dict(
  DESCRIPTOR = _DCEREFORGEEQUIP,
  __module__ = 'DceReforgeEquip_pb2'
  # @@protoc_insertion_point(class_scope:DceReforgeEquip)
  ))
_sym_db.RegisterMessage(DceReforgeEquip)


# @@protoc_insertion_point(module_scope)