# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DceGuildChangeApplyRule.proto

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
  name='DceGuildChangeApplyRule.proto',
  package='',
  serialized_pb=_b('\n\x1d\x44\x63\x65GuildChangeApplyRule.proto\"6\n\x17\x44\x63\x65GuildChangeApplyRule\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\r\n\x05param\x18\x02 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DCEGUILDCHANGEAPPLYRULE = _descriptor.Descriptor(
  name='DceGuildChangeApplyRule',
  full_name='DceGuildChangeApplyRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DceGuildChangeApplyRule.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param', full_name='DceGuildChangeApplyRule.param', index=1,
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
  serialized_start=33,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['DceGuildChangeApplyRule'] = _DCEGUILDCHANGEAPPLYRULE

DceGuildChangeApplyRule = _reflection.GeneratedProtocolMessageType('DceGuildChangeApplyRule', (_message.Message,), dict(
  DESCRIPTOR = _DCEGUILDCHANGEAPPLYRULE,
  __module__ = 'DceGuildChangeApplyRule_pb2'
  # @@protoc_insertion_point(class_scope:DceGuildChangeApplyRule)
  ))
_sym_db.RegisterMessage(DceGuildChangeApplyRule)


# @@protoc_insertion_point(module_scope)