# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.MiddleCoverV3.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto.com.bapis.bilibili.app.card.v1 import Base_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import ReasonStyle_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.MiddleCoverV3.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:pyproto/com.bapis.bilibili.app.card.v1.MiddleCoverV3.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\x1a\x31pyproto/com.bapis.bilibili.app.card.v1.Base.proto\x1a\x38pyproto/com.bapis.bilibili.app.card.v1.ReasonStyle.proto\"\xb4\x01\n\rMiddleCoverV3\x12\x37\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32$.com.bapis.bilibili.app.card.v1.BaseH\x00\x88\x01\x01\x12K\n\x11\x63over_badge_style\x18\x04 \x01(\x0b\x32+.com.bapis.bilibili.app.card.v1.ReasonStyleH\x01\x88\x01\x01\x42\x07\n\x05_baseB\x14\n\x12_cover_badge_styleb\x06proto3'
  ,
  dependencies=[pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2.DESCRIPTOR,])




_MIDDLECOVERV3 = _descriptor.Descriptor(
  name='MiddleCoverV3',
  full_name='com.bapis.bilibili.app.card.v1.MiddleCoverV3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='com.bapis.bilibili.app.card.v1.MiddleCoverV3.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cover_badge_style', full_name='com.bapis.bilibili.app.card.v1.MiddleCoverV3.cover_badge_style', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='_base', full_name='com.bapis.bilibili.app.card.v1.MiddleCoverV3._base',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cover_badge_style', full_name='com.bapis.bilibili.app.card.v1.MiddleCoverV3._cover_badge_style',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=204,
  serialized_end=384,
)

_MIDDLECOVERV3.fields_by_name['base'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2._BASE
_MIDDLECOVERV3.fields_by_name['cover_badge_style'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2._REASONSTYLE
_MIDDLECOVERV3.oneofs_by_name['_base'].fields.append(
  _MIDDLECOVERV3.fields_by_name['base'])
_MIDDLECOVERV3.fields_by_name['base'].containing_oneof = _MIDDLECOVERV3.oneofs_by_name['_base']
_MIDDLECOVERV3.oneofs_by_name['_cover_badge_style'].fields.append(
  _MIDDLECOVERV3.fields_by_name['cover_badge_style'])
_MIDDLECOVERV3.fields_by_name['cover_badge_style'].containing_oneof = _MIDDLECOVERV3.oneofs_by_name['_cover_badge_style']
DESCRIPTOR.message_types_by_name['MiddleCoverV3'] = _MIDDLECOVERV3
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MiddleCoverV3 = _reflection.GeneratedProtocolMessageType('MiddleCoverV3', (_message.Message,), {
  'DESCRIPTOR' : _MIDDLECOVERV3,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.MiddleCoverV3_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.MiddleCoverV3)
  })
_sym_db.RegisterMessage(MiddleCoverV3)


# @@protoc_insertion_point(module_scope)
