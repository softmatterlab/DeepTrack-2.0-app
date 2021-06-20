# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dtserver/grpc_routing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dtserver/grpc_routing.proto',
  package='dtserver.grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x64tserver/grpc_routing.proto\x12\rdtserver.grpc\"\n\n\x08NoneLike\"<\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"T\n\x07\x46\x65\x61ture\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x03(\x0b\x32\x17.dtserver.grpc.Property2K\n\x07Routing\x12@\n\x0bGetFeatures\x12\x17.dtserver.grpc.NoneLike\x1a\x16.dtserver.grpc.Feature0\x01\x62\x06proto3'
)




_NONELIKE = _descriptor.Descriptor(
  name='NoneLike',
  full_name='dtserver.grpc.NoneLike',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  ],
  serialized_start=46,
  serialized_end=56,
)


_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='dtserver.grpc.Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dtserver.grpc.Property.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dtserver.grpc.Property.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='dtserver.grpc.Property.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  ],
  serialized_start=58,
  serialized_end=118,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='dtserver.grpc.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='module', full_name='dtserver.grpc.Feature.module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='dtserver.grpc.Feature.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='dtserver.grpc.Feature.properties', index=2,
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
  ],
  serialized_start=120,
  serialized_end=204,
)

_FEATURE.fields_by_name['properties'].message_type = _PROPERTY
DESCRIPTOR.message_types_by_name['NoneLike'] = _NONELIKE
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoneLike = _reflection.GeneratedProtocolMessageType('NoneLike', (_message.Message,), {
  'DESCRIPTOR' : _NONELIKE,
  '__module__' : 'dtserver.grpc_routing_pb2'
  # @@protoc_insertion_point(class_scope:dtserver.grpc.NoneLike)
  })
_sym_db.RegisterMessage(NoneLike)

Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTY,
  '__module__' : 'dtserver.grpc_routing_pb2'
  # @@protoc_insertion_point(class_scope:dtserver.grpc.Property)
  })
_sym_db.RegisterMessage(Property)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'dtserver.grpc_routing_pb2'
  # @@protoc_insertion_point(class_scope:dtserver.grpc.Feature)
  })
_sym_db.RegisterMessage(Feature)



_ROUTING = _descriptor.ServiceDescriptor(
  name='Routing',
  full_name='dtserver.grpc.Routing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=206,
  serialized_end=281,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeatures',
    full_name='dtserver.grpc.Routing.GetFeatures',
    index=0,
    containing_service=None,
    input_type=_NONELIKE,
    output_type=_FEATURE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTING)

DESCRIPTOR.services_by_name['Routing'] = _ROUTING

# @@protoc_insertion_point(module_scope)
