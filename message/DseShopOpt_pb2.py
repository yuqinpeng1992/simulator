# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseShopOpt.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ShopUnit_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DseShopOpt.proto',
  package='',
  serialized_pb=_b('\n\x10\x44seShopOpt.proto\x1a\x0eShopUnit.proto\"b\n\nDseShopOpt\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0e\n\x06shopid\x18\x02 \x01(\x05\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\x0b\n\x03res\x18\x04 \x01(\x05\x12\x1a\n\x07\x62uylist\x18\x05 \x03(\x0b\x32\t.ShopUnit')
  ,
  dependencies=[ShopUnit_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSESHOPOPT = _descriptor.Descriptor(
  name='DseShopOpt',
  full_name='DseShopOpt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DseShopOpt.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shopid', full_name='DseShopOpt.shopid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='DseShopOpt.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res', full_name='DseShopOpt.res', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buylist', full_name='DseShopOpt.buylist', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=36,
  serialized_end=134,
)

_DSESHOPOPT.fields_by_name['buylist'].message_type = ShopUnit_pb2._SHOPUNIT
DESCRIPTOR.message_types_by_name['DseShopOpt'] = _DSESHOPOPT

DseShopOpt = _reflection.GeneratedProtocolMessageType('DseShopOpt', (_message.Message,), dict(
  DESCRIPTOR = _DSESHOPOPT,
  __module__ = 'DseShopOpt_pb2'
  # @@protoc_insertion_point(class_scope:DseShopOpt)
  ))
_sym_db.RegisterMessage(DseShopOpt)


# @@protoc_insertion_point(module_scope)