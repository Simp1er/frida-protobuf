# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/VideoIdKeyValueSet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto import VideoIdKeyValueSetKey_pb2 as pyproto_dot_VideoIdKeyValueSetKey__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/VideoIdKeyValueSet.proto',
  package='com.tencent.qqlive.protocol.pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n pyproto/VideoIdKeyValueSet.proto\x12\x1e\x63om.tencent.qqlive.protocol.pb\x1a#pyproto/VideoIdKeyValueSetKey.proto\"\xcb\x03\n\x12VideoIdKeyValueSet\x12P\n\x0citem_id_type\x18\x01 \x01(\x0e\x32\x35.com.tencent.qqlive.protocol.pb.VideoIdKeyValueSetKeyH\x00\x88\x01\x01\x12\x14\n\x07item_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12T\n\x10sub_item_id_type\x18\x03 \x01(\x0e\x32\x35.com.tencent.qqlive.protocol.pb.VideoIdKeyValueSetKeyH\x02\x88\x01\x01\x12\x18\n\x0bsub_item_id\x18\x04 \x01(\tH\x03\x88\x01\x01\x12V\n\x12third_item_id_type\x18\x05 \x01(\x0e\x32\x35.com.tencent.qqlive.protocol.pb.VideoIdKeyValueSetKeyH\x04\x88\x01\x01\x12\x1a\n\rthird_item_id\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x0f\n\r_item_id_typeB\n\n\x08_item_idB\x13\n\x11_sub_item_id_typeB\x0e\n\x0c_sub_item_idB\x15\n\x13_third_item_id_typeB\x10\n\x0e_third_item_idb\x06proto3'
  ,
  dependencies=[pyproto_dot_VideoIdKeyValueSetKey__pb2.DESCRIPTOR,])




_VIDEOIDKEYVALUESET = _descriptor.Descriptor(
  name='VideoIdKeyValueSet',
  full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id_type', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet.item_id_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet.item_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_item_id_type', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet.sub_item_id_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_item_id', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet.sub_item_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='third_item_id_type', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet.third_item_id_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='third_item_id', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet.third_item_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
      name='_item_id_type', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet._item_id_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_item_id', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet._item_id',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_sub_item_id_type', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet._sub_item_id_type',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_sub_item_id', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet._sub_item_id',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_third_item_id_type', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet._third_item_id_type',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_third_item_id', full_name='com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet._third_item_id',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=106,
  serialized_end=565,
)

_VIDEOIDKEYVALUESET.fields_by_name['item_id_type'].enum_type = pyproto_dot_VideoIdKeyValueSetKey__pb2._VIDEOIDKEYVALUESETKEY
_VIDEOIDKEYVALUESET.fields_by_name['sub_item_id_type'].enum_type = pyproto_dot_VideoIdKeyValueSetKey__pb2._VIDEOIDKEYVALUESETKEY
_VIDEOIDKEYVALUESET.fields_by_name['third_item_id_type'].enum_type = pyproto_dot_VideoIdKeyValueSetKey__pb2._VIDEOIDKEYVALUESETKEY
_VIDEOIDKEYVALUESET.oneofs_by_name['_item_id_type'].fields.append(
  _VIDEOIDKEYVALUESET.fields_by_name['item_id_type'])
_VIDEOIDKEYVALUESET.fields_by_name['item_id_type'].containing_oneof = _VIDEOIDKEYVALUESET.oneofs_by_name['_item_id_type']
_VIDEOIDKEYVALUESET.oneofs_by_name['_item_id'].fields.append(
  _VIDEOIDKEYVALUESET.fields_by_name['item_id'])
_VIDEOIDKEYVALUESET.fields_by_name['item_id'].containing_oneof = _VIDEOIDKEYVALUESET.oneofs_by_name['_item_id']
_VIDEOIDKEYVALUESET.oneofs_by_name['_sub_item_id_type'].fields.append(
  _VIDEOIDKEYVALUESET.fields_by_name['sub_item_id_type'])
_VIDEOIDKEYVALUESET.fields_by_name['sub_item_id_type'].containing_oneof = _VIDEOIDKEYVALUESET.oneofs_by_name['_sub_item_id_type']
_VIDEOIDKEYVALUESET.oneofs_by_name['_sub_item_id'].fields.append(
  _VIDEOIDKEYVALUESET.fields_by_name['sub_item_id'])
_VIDEOIDKEYVALUESET.fields_by_name['sub_item_id'].containing_oneof = _VIDEOIDKEYVALUESET.oneofs_by_name['_sub_item_id']
_VIDEOIDKEYVALUESET.oneofs_by_name['_third_item_id_type'].fields.append(
  _VIDEOIDKEYVALUESET.fields_by_name['third_item_id_type'])
_VIDEOIDKEYVALUESET.fields_by_name['third_item_id_type'].containing_oneof = _VIDEOIDKEYVALUESET.oneofs_by_name['_third_item_id_type']
_VIDEOIDKEYVALUESET.oneofs_by_name['_third_item_id'].fields.append(
  _VIDEOIDKEYVALUESET.fields_by_name['third_item_id'])
_VIDEOIDKEYVALUESET.fields_by_name['third_item_id'].containing_oneof = _VIDEOIDKEYVALUESET.oneofs_by_name['_third_item_id']
DESCRIPTOR.message_types_by_name['VideoIdKeyValueSet'] = _VIDEOIDKEYVALUESET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoIdKeyValueSet = _reflection.GeneratedProtocolMessageType('VideoIdKeyValueSet', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOIDKEYVALUESET,
  '__module__' : 'pyproto.VideoIdKeyValueSet_pb2'
  # @@protoc_insertion_point(class_scope:com.tencent.qqlive.protocol.pb.VideoIdKeyValueSet)
  })
_sym_db.RegisterMessage(VideoIdKeyValueSet)


# @@protoc_insertion_point(module_scope)