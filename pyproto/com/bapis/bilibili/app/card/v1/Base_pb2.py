# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.Base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto.com.bapis.bilibili.app.card.v1 import Args_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Args__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import Button_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Button__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import ThreePoint_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ThreePoint__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import Mask_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Mask__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import AdInfo_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_AdInfo__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import PlayerArgs_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_PlayerArgs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.Base.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1pyproto/com.bapis.bilibili.app.card.v1.Base.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\x1a\x31pyproto/com.bapis.bilibili.app.card.v1.Args.proto\x1a\x33pyproto/com.bapis.bilibili.app.card.v1.Button.proto\x1a\x37pyproto/com.bapis.bilibili.app.card.v1.ThreePoint.proto\x1a\x31pyproto/com.bapis.bilibili.app.card.v1.Mask.proto\x1a\x33pyproto/com.bapis.bilibili.app.card.v1.AdInfo.proto\x1a\x37pyproto/com.bapis.bilibili.app.card.v1.PlayerArgs.proto\"\xee\x05\n\x04\x42\x61se\x12\x16\n\tcard_type\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tcard_goto\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04goto\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05param\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x12\n\x05\x63over\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x12\n\x05title\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x10\n\x03uri\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x44\n\x0bthree_point\x18\x08 \x01(\x0b\x32*.com.bapis.bilibili.app.card.v1.ThreePointH\x07\x88\x01\x01\x12\x37\n\x04\x61rgs\x18\t \x01(\x0b\x32$.com.bapis.bilibili.app.card.v1.ArgsH\x08\x88\x01\x01\x12\x44\n\x0bplayer_args\x18\n \x01(\x0b\x32*.com.bapis.bilibili.app.card.v1.PlayerArgsH\t\x88\x01\x01\x12\x10\n\x03idx\x18\x0b \x01(\x03H\n\x88\x01\x01\x12<\n\x07\x61\x64_info\x18\x0c \x01(\x0b\x32&.com.bapis.bilibili.app.card.v1.AdInfoH\x0b\x88\x01\x01\x12\x37\n\x04mask\x18\r \x01(\x0b\x32$.com.bapis.bilibili.app.card.v1.MaskH\x0c\x88\x01\x01\x12\x16\n\tfrom_type\x18\x0e \x01(\tH\r\x88\x01\x01\x12@\n\x0b\x64\x65sc_button\x18\x11 \x01(\x0b\x32&.com.bapis.bilibili.app.card.v1.ButtonH\x0e\x88\x01\x01\x42\x0c\n\n_card_typeB\x0c\n\n_card_gotoB\x07\n\x05_gotoB\x08\n\x06_paramB\x08\n\x06_coverB\x08\n\x06_titleB\x06\n\x04_uriB\x0e\n\x0c_three_pointB\x07\n\x05_argsB\x0e\n\x0c_player_argsB\x06\n\x04_idxB\n\n\x08_ad_infoB\x07\n\x05_maskB\x0c\n\n_from_typeB\x0e\n\x0c_desc_buttonb\x06proto3'
  ,
  dependencies=[pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Args__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Button__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ThreePoint__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Mask__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_AdInfo__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_PlayerArgs__pb2.DESCRIPTOR,])




_BASE = _descriptor.Descriptor(
  name='Base',
  full_name='com.bapis.bilibili.app.card.v1.Base',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='card_type', full_name='com.bapis.bilibili.app.card.v1.Base.card_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='card_goto', full_name='com.bapis.bilibili.app.card.v1.Base.card_goto', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goto', full_name='com.bapis.bilibili.app.card.v1.Base.goto', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='param', full_name='com.bapis.bilibili.app.card.v1.Base.param', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cover', full_name='com.bapis.bilibili.app.card.v1.Base.cover', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='com.bapis.bilibili.app.card.v1.Base.title', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='com.bapis.bilibili.app.card.v1.Base.uri', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='three_point', full_name='com.bapis.bilibili.app.card.v1.Base.three_point', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='com.bapis.bilibili.app.card.v1.Base.args', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_args', full_name='com.bapis.bilibili.app.card.v1.Base.player_args', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idx', full_name='com.bapis.bilibili.app.card.v1.Base.idx', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_info', full_name='com.bapis.bilibili.app.card.v1.Base.ad_info', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='com.bapis.bilibili.app.card.v1.Base.mask', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_type', full_name='com.bapis.bilibili.app.card.v1.Base.from_type', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc_button', full_name='com.bapis.bilibili.app.card.v1.Base.desc_button', index=14,
      number=17, type=11, cpp_type=10, label=1,
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
      name='_card_type', full_name='com.bapis.bilibili.app.card.v1.Base._card_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_card_goto', full_name='com.bapis.bilibili.app.card.v1.Base._card_goto',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_goto', full_name='com.bapis.bilibili.app.card.v1.Base._goto',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_param', full_name='com.bapis.bilibili.app.card.v1.Base._param',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cover', full_name='com.bapis.bilibili.app.card.v1.Base._cover',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_title', full_name='com.bapis.bilibili.app.card.v1.Base._title',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_uri', full_name='com.bapis.bilibili.app.card.v1.Base._uri',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_three_point', full_name='com.bapis.bilibili.app.card.v1.Base._three_point',
      index=7, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_args', full_name='com.bapis.bilibili.app.card.v1.Base._args',
      index=8, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_player_args', full_name='com.bapis.bilibili.app.card.v1.Base._player_args',
      index=9, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_idx', full_name='com.bapis.bilibili.app.card.v1.Base._idx',
      index=10, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ad_info', full_name='com.bapis.bilibili.app.card.v1.Base._ad_info',
      index=11, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_mask', full_name='com.bapis.bilibili.app.card.v1.Base._mask',
      index=12, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_from_type', full_name='com.bapis.bilibili.app.card.v1.Base._from_type',
      index=13, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_desc_button', full_name='com.bapis.bilibili.app.card.v1.Base._desc_button',
      index=14, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=408,
  serialized_end=1158,
)

_BASE.fields_by_name['three_point'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ThreePoint__pb2._THREEPOINT
_BASE.fields_by_name['args'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Args__pb2._ARGS
_BASE.fields_by_name['player_args'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_PlayerArgs__pb2._PLAYERARGS
_BASE.fields_by_name['ad_info'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_AdInfo__pb2._ADINFO
_BASE.fields_by_name['mask'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Mask__pb2._MASK
_BASE.fields_by_name['desc_button'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Button__pb2._BUTTON
_BASE.oneofs_by_name['_card_type'].fields.append(
  _BASE.fields_by_name['card_type'])
_BASE.fields_by_name['card_type'].containing_oneof = _BASE.oneofs_by_name['_card_type']
_BASE.oneofs_by_name['_card_goto'].fields.append(
  _BASE.fields_by_name['card_goto'])
_BASE.fields_by_name['card_goto'].containing_oneof = _BASE.oneofs_by_name['_card_goto']
_BASE.oneofs_by_name['_goto'].fields.append(
  _BASE.fields_by_name['goto'])
_BASE.fields_by_name['goto'].containing_oneof = _BASE.oneofs_by_name['_goto']
_BASE.oneofs_by_name['_param'].fields.append(
  _BASE.fields_by_name['param'])
_BASE.fields_by_name['param'].containing_oneof = _BASE.oneofs_by_name['_param']
_BASE.oneofs_by_name['_cover'].fields.append(
  _BASE.fields_by_name['cover'])
_BASE.fields_by_name['cover'].containing_oneof = _BASE.oneofs_by_name['_cover']
_BASE.oneofs_by_name['_title'].fields.append(
  _BASE.fields_by_name['title'])
_BASE.fields_by_name['title'].containing_oneof = _BASE.oneofs_by_name['_title']
_BASE.oneofs_by_name['_uri'].fields.append(
  _BASE.fields_by_name['uri'])
_BASE.fields_by_name['uri'].containing_oneof = _BASE.oneofs_by_name['_uri']
_BASE.oneofs_by_name['_three_point'].fields.append(
  _BASE.fields_by_name['three_point'])
_BASE.fields_by_name['three_point'].containing_oneof = _BASE.oneofs_by_name['_three_point']
_BASE.oneofs_by_name['_args'].fields.append(
  _BASE.fields_by_name['args'])
_BASE.fields_by_name['args'].containing_oneof = _BASE.oneofs_by_name['_args']
_BASE.oneofs_by_name['_player_args'].fields.append(
  _BASE.fields_by_name['player_args'])
_BASE.fields_by_name['player_args'].containing_oneof = _BASE.oneofs_by_name['_player_args']
_BASE.oneofs_by_name['_idx'].fields.append(
  _BASE.fields_by_name['idx'])
_BASE.fields_by_name['idx'].containing_oneof = _BASE.oneofs_by_name['_idx']
_BASE.oneofs_by_name['_ad_info'].fields.append(
  _BASE.fields_by_name['ad_info'])
_BASE.fields_by_name['ad_info'].containing_oneof = _BASE.oneofs_by_name['_ad_info']
_BASE.oneofs_by_name['_mask'].fields.append(
  _BASE.fields_by_name['mask'])
_BASE.fields_by_name['mask'].containing_oneof = _BASE.oneofs_by_name['_mask']
_BASE.oneofs_by_name['_from_type'].fields.append(
  _BASE.fields_by_name['from_type'])
_BASE.fields_by_name['from_type'].containing_oneof = _BASE.oneofs_by_name['_from_type']
_BASE.oneofs_by_name['_desc_button'].fields.append(
  _BASE.fields_by_name['desc_button'])
_BASE.fields_by_name['desc_button'].containing_oneof = _BASE.oneofs_by_name['_desc_button']
DESCRIPTOR.message_types_by_name['Base'] = _BASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Base = _reflection.GeneratedProtocolMessageType('Base', (_message.Message,), {
  'DESCRIPTOR' : _BASE,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.Base_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.Base)
  })
_sym_db.RegisterMessage(Base)


# @@protoc_insertion_point(module_scope)
