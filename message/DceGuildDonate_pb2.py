# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DceGuildDonate.proto

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
  name='DceGuildDonate.proto',
  package='',
  serialized_pb=_b('\n\x14\x44\x63\x65GuildDonate.proto\"*\n\x0e\x44\x63\x65GuildDonate\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DCEGUILDDONATE = _descriptor.Descriptor(
  name='DceGuildDonate',
  full_name='DceGuildDonate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DceGuildDonate.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='DceGuildDonate.id', index=1,
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
  serialized_start=24,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['DceGuildDonate'] = _DCEGUILDDONATE

DceGuildDonate = _reflection.GeneratedProtocolMessageType('DceGuildDonate', (_message.Message,), dict(
  DESCRIPTOR = _DCEGUILDDONATE,
  __module__ = 'DceGuildDonate_pb2'
  # @@protoc_insertion_point(class_scope:DceGuildDonate)
  ))
_sym_db.RegisterMessage(DceGuildDonate)


# @@protoc_insertion_point(module_scope)
