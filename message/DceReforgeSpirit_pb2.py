# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DceReforgeSpirit.proto

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
  name='DceReforgeSpirit.proto',
  package='',
  serialized_pb=_b('\n\x16\x44\x63\x65ReforgeSpirit.proto\"/\n\x10\x44\x63\x65ReforgeSpirit\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\x05\x12\x0b\n\x03tid\x18\x02 \x03(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DCEREFORGESPIRIT = _descriptor.Descriptor(
  name='DceReforgeSpirit',
  full_name='DceReforgeSpirit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='DceReforgeSpirit.action', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tid', full_name='DceReforgeSpirit.tid', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=26,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['DceReforgeSpirit'] = _DCEREFORGESPIRIT

DceReforgeSpirit = _reflection.GeneratedProtocolMessageType('DceReforgeSpirit', (_message.Message,), dict(
  DESCRIPTOR = _DCEREFORGESPIRIT,
  __module__ = 'DceReforgeSpirit_pb2'
  # @@protoc_insertion_point(class_scope:DceReforgeSpirit)
  ))
_sym_db.RegisterMessage(DceReforgeSpirit)


# @@protoc_insertion_point(module_scope)