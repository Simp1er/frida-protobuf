# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.CreativeContent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.CreativeContent.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<pyproto/com.bapis.bilibili.app.card.v1.CreativeContent.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\"\xcd\x02\n\x0f\x43reativeContent\x12\x12\n\x05title\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08video_id\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12\x15\n\x08username\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x16\n\timage_url\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07log_url\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x10\n\x03url\x18\t \x01(\tH\x06\x88\x01\x01\x12\x16\n\tclick_url\x18\n \x01(\tH\x07\x88\x01\x01\x12\x15\n\x08show_url\x18\x0b \x01(\tH\x08\x88\x01\x01\x42\x08\n\x06_titleB\x0e\n\x0c_descriptionB\x0b\n\t_video_idB\x0b\n\t_usernameB\x0c\n\n_image_urlB\n\n\x08_log_urlB\x06\n\x04_urlB\x0c\n\n_click_urlB\x0b\n\t_show_urlb\x06proto3'
)




_CREATIVECONTENT = _descriptor.Descriptor(
  name='CreativeContent',
  full_name='com.bapis.bilibili.app.card.v1.CreativeContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='video_id', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.video_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.username', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.image_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.log_url', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.url', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='click_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.click_url', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='show_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent.show_url', index=8,
      number=11, type=9, cpp_type=9, label=1,
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
      name='_title', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._title',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_description', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._description',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_video_id', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._video_id',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_username', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._username',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_image_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._image_url',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_log_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._log_url',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._url',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_click_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._click_url',
      index=7, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_show_url', full_name='com.bapis.bilibili.app.card.v1.CreativeContent._show_url',
      index=8, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=97,
  serialized_end=430,
)

_CREATIVECONTENT.oneofs_by_name['_title'].fields.append(
  _CREATIVECONTENT.fields_by_name['title'])
_CREATIVECONTENT.fields_by_name['title'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_title']
_CREATIVECONTENT.oneofs_by_name['_description'].fields.append(
  _CREATIVECONTENT.fields_by_name['description'])
_CREATIVECONTENT.fields_by_name['description'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_description']
_CREATIVECONTENT.oneofs_by_name['_video_id'].fields.append(
  _CREATIVECONTENT.fields_by_name['video_id'])
_CREATIVECONTENT.fields_by_name['video_id'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_video_id']
_CREATIVECONTENT.oneofs_by_name['_username'].fields.append(
  _CREATIVECONTENT.fields_by_name['username'])
_CREATIVECONTENT.fields_by_name['username'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_username']
_CREATIVECONTENT.oneofs_by_name['_image_url'].fields.append(
  _CREATIVECONTENT.fields_by_name['image_url'])
_CREATIVECONTENT.fields_by_name['image_url'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_image_url']
_CREATIVECONTENT.oneofs_by_name['_log_url'].fields.append(
  _CREATIVECONTENT.fields_by_name['log_url'])
_CREATIVECONTENT.fields_by_name['log_url'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_log_url']
_CREATIVECONTENT.oneofs_by_name['_url'].fields.append(
  _CREATIVECONTENT.fields_by_name['url'])
_CREATIVECONTENT.fields_by_name['url'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_url']
_CREATIVECONTENT.oneofs_by_name['_click_url'].fields.append(
  _CREATIVECONTENT.fields_by_name['click_url'])
_CREATIVECONTENT.fields_by_name['click_url'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_click_url']
_CREATIVECONTENT.oneofs_by_name['_show_url'].fields.append(
  _CREATIVECONTENT.fields_by_name['show_url'])
_CREATIVECONTENT.fields_by_name['show_url'].containing_oneof = _CREATIVECONTENT.oneofs_by_name['_show_url']
DESCRIPTOR.message_types_by_name['CreativeContent'] = _CREATIVECONTENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreativeContent = _reflection.GeneratedProtocolMessageType('CreativeContent', (_message.Message,), {
  'DESCRIPTOR' : _CREATIVECONTENT,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.CreativeContent_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.CreativeContent)
  })
_sym_db.RegisterMessage(CreativeContent)


# @@protoc_insertion_point(module_scope)
