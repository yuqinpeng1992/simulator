# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DceHeartbeat.proto

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
  name='DceHeartbeat.proto',
  package='',
  serialized_pb=_b('\n\x12\x44\x63\x65Heartbeat.proto\"\x0e\n\x0c\x44\x63\x65Heartbeat')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DCEHEARTBEAT = _descriptor.Descriptor(
  name='DceHeartbeat',
  full_name='DceHeartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=22,
  serialized_end=36,
)

DESCRIPTOR.message_types_by_name['DceHeartbeat'] = _DCEHEARTBEAT

DceHeartbeat = _reflection.GeneratedProtocolMessageType('DceHeartbeat', (_message.Message,), dict(
  DESCRIPTOR = _DCEHEARTBEAT,
  __module__ = 'DceHeartbeat_pb2'
  # @@protoc_insertion_point(class_scope:DceHeartbeat)
  ))
_sym_db.RegisterMessage(DceHeartbeat)


# @@protoc_insertion_point(module_scope)