# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseGuildLeaveMessage.proto

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
  name='DseGuildLeaveMessage.proto',
  package='',
  serialized_pb=_b('\n\x1a\x44seGuildLeaveMessage.proto\"#\n\x14\x44seGuildLeaveMessage\x12\x0b\n\x03res\x18\x01 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSEGUILDLEAVEMESSAGE = _descriptor.Descriptor(
  name='DseGuildLeaveMessage',
  full_name='DseGuildLeaveMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='DseGuildLeaveMessage.res', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=30,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['DseGuildLeaveMessage'] = _DSEGUILDLEAVEMESSAGE

DseGuildLeaveMessage = _reflection.GeneratedProtocolMessageType('DseGuildLeaveMessage', (_message.Message,), dict(
  DESCRIPTOR = _DSEGUILDLEAVEMESSAGE,
  __module__ = 'DseGuildLeaveMessage_pb2'
  # @@protoc_insertion_point(class_scope:DseGuildLeaveMessage)
  ))
_sym_db.RegisterMessage(DseGuildLeaveMessage)


# @@protoc_insertion_point(module_scope)