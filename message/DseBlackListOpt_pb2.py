# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseBlackListOpt.proto

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
  name='DseBlackListOpt.proto',
  package='',
  serialized_pb=_b('\n\x15\x44seBlackListOpt.proto\"9\n\x0f\x44seBlackListOpt\x12\x0b\n\x03res\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0b\n\x03uid\x18\x03 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSEBLACKLISTOPT = _descriptor.Descriptor(
  name='DseBlackListOpt',
  full_name='DseBlackListOpt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='DseBlackListOpt.res', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='DseBlackListOpt.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='DseBlackListOpt.uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=25,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['DseBlackListOpt'] = _DSEBLACKLISTOPT

DseBlackListOpt = _reflection.GeneratedProtocolMessageType('DseBlackListOpt', (_message.Message,), dict(
  DESCRIPTOR = _DSEBLACKLISTOPT,
  __module__ = 'DseBlackListOpt_pb2'
  # @@protoc_insertion_point(class_scope:DseBlackListOpt)
  ))
_sym_db.RegisterMessage(DseBlackListOpt)


# @@protoc_insertion_point(module_scope)
