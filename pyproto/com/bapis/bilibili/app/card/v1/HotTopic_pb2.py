# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.HotTopic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto.com.bapis.bilibili.app.card.v1 import Base_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import HotTopicItem_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_HotTopicItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.HotTopic.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5pyproto/com.bapis.bilibili.app.card.v1.HotTopic.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\x1a\x31pyproto/com.bapis.bilibili.app.card.v1.Base.proto\x1a\x39pyproto/com.bapis.bilibili.app.card.v1.HotTopicItem.proto\"\xa5\x01\n\x08HotTopic\x12\x37\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32$.com.bapis.bilibili.app.card.v1.BaseH\x00\x88\x01\x01\x12\x11\n\x04\x64\x65sc\x18\x02 \x01(\tH\x01\x88\x01\x01\x12;\n\x05items\x18\x03 \x03(\x0b\x32,.com.bapis.bilibili.app.card.v1.HotTopicItemB\x07\n\x05_baseB\x07\n\x05_descb\x06proto3'
  ,
  dependencies=[pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_HotTopicItem__pb2.DESCRIPTOR,])




_HOTTOPIC = _descriptor.Descriptor(
  name='HotTopic',
  full_name='com.bapis.bilibili.app.card.v1.HotTopic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='com.bapis.bilibili.app.card.v1.HotTopic.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc', full_name='com.bapis.bilibili.app.card.v1.HotTopic.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='com.bapis.bilibili.app.card.v1.HotTopic.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
      name='_base', full_name='com.bapis.bilibili.app.card.v1.HotTopic._base',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_desc', full_name='com.bapis.bilibili.app.card.v1.HotTopic._desc',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=200,
  serialized_end=365,
)

_HOTTOPIC.fields_by_name['base'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2._BASE
_HOTTOPIC.fields_by_name['items'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_HotTopicItem__pb2._HOTTOPICITEM
_HOTTOPIC.oneofs_by_name['_base'].fields.append(
  _HOTTOPIC.fields_by_name['base'])
_HOTTOPIC.fields_by_name['base'].containing_oneof = _HOTTOPIC.oneofs_by_name['_base']
_HOTTOPIC.oneofs_by_name['_desc'].fields.append(
  _HOTTOPIC.fields_by_name['desc'])
_HOTTOPIC.fields_by_name['desc'].containing_oneof = _HOTTOPIC.oneofs_by_name['_desc']
DESCRIPTOR.message_types_by_name['HotTopic'] = _HOTTOPIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotTopic = _reflection.GeneratedProtocolMessageType('HotTopic', (_message.Message,), {
  'DESCRIPTOR' : _HOTTOPIC,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.HotTopic_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.HotTopic)
  })
_sym_db.RegisterMessage(HotTopic)


# @@protoc_insertion_point(module_scope)
