# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.DislikeReason.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.DislikeReason.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:pyproto/com.bapis.bilibili.app.card.v1.DislikeReason.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\"C\n\rDislikeReason\x12\x0f\n\x02id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameb\x06proto3'
)




_DISLIKEREASON = _descriptor.Descriptor(
  name='DislikeReason',
  full_name='com.bapis.bilibili.app.card.v1.DislikeReason',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.bapis.bilibili.app.card.v1.DislikeReason.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.bapis.bilibili.app.card.v1.DislikeReason.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_id', full_name='com.bapis.bilibili.app.card.v1.DislikeReason._id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='com.bapis.bilibili.app.card.v1.DislikeReason._name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=94,
  serialized_end=161,
)

_DISLIKEREASON.oneofs_by_name['_id'].fields.append(
  _DISLIKEREASON.fields_by_name['id'])
_DISLIKEREASON.fields_by_name['id'].containing_oneof = _DISLIKEREASON.oneofs_by_name['_id']
_DISLIKEREASON.oneofs_by_name['_name'].fields.append(
  _DISLIKEREASON.fields_by_name['name'])
_DISLIKEREASON.fields_by_name['name'].containing_oneof = _DISLIKEREASON.oneofs_by_name['_name']
DESCRIPTOR.message_types_by_name['DislikeReason'] = _DISLIKEREASON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DislikeReason = _reflection.GeneratedProtocolMessageType('DislikeReason', (_message.Message,), {
  'DESCRIPTOR' : _DISLIKEREASON,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.DislikeReason_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.DislikeReason)
  })
_sym_db.RegisterMessage(DislikeReason)


# @@protoc_insertion_point(module_scope)
