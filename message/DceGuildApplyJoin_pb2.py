# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DceGuildApplyJoin.proto

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
  name='DceGuildApplyJoin.proto',
  package='',
  serialized_pb=_b('\n\x17\x44\x63\x65GuildApplyJoin.proto\"$\n\x11\x44\x63\x65GuildApplyJoin\x12\x0f\n\x07guildid\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DCEGUILDAPPLYJOIN = _descriptor.Descriptor(
  name='DceGuildApplyJoin',
  full_name='DceGuildApplyJoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guildid', full_name='DceGuildApplyJoin.guildid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=27,
  serialized_end=63,
)

DESCRIPTOR.message_types_by_name['DceGuildApplyJoin'] = _DCEGUILDAPPLYJOIN

DceGuildApplyJoin = _reflection.GeneratedProtocolMessageType('DceGuildApplyJoin', (_message.Message,), dict(
  DESCRIPTOR = _DCEGUILDAPPLYJOIN,
  __module__ = 'DceGuildApplyJoin_pb2'
  # @@protoc_insertion_point(class_scope:DceGuildApplyJoin)
  ))
_sym_db.RegisterMessage(DceGuildApplyJoin)


# @@protoc_insertion_point(module_scope)