# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseChangeSpiritSkin.proto

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
  name='DseChangeSpiritSkin.proto',
  package='',
  serialized_pb=_b('\n\x19\x44seChangeSpiritSkin.proto\"A\n\x13\x44seChangeSpiritSkin\x12\x0b\n\x03tid\x18\x01 \x01(\x05\x12\x0f\n\x07skin_id\x18\x02 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSECHANGESPIRITSKIN = _descriptor.Descriptor(
  name='DseChangeSpiritSkin',
  full_name='DseChangeSpiritSkin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='DseChangeSpiritSkin.tid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skin_id', full_name='DseChangeSpiritSkin.skin_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='DseChangeSpiritSkin.code', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=29,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['DseChangeSpiritSkin'] = _DSECHANGESPIRITSKIN

DseChangeSpiritSkin = _reflection.GeneratedProtocolMessageType('DseChangeSpiritSkin', (_message.Message,), dict(
  DESCRIPTOR = _DSECHANGESPIRITSKIN,
  __module__ = 'DseChangeSpiritSkin_pb2'
  # @@protoc_insertion_point(class_scope:DseChangeSpiritSkin)
  ))
_sym_db.RegisterMessage(DseChangeSpiritSkin)


# @@protoc_insertion_point(module_scope)
