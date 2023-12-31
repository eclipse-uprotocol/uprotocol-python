# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uattributes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import uprotocol.proto.uri_pb2 as uri__pb2
import uprotocol.proto.uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11uattributes.proto\x12\x0cuprotocol.v1\x1a\turi.proto\x1a\nuuid.proto\"\xf8\x02\n\x0bUAttributes\x12\x1e\n\x02id\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUID\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.uprotocol.v1.UMessageType\x12%\n\x04sink\x18\x03 \x01(\x0b\x32\x12.uprotocol.v1.UUriH\x00\x88\x01\x01\x12)\n\x08priority\x18\x04 \x01(\x0e\x32\x17.uprotocol.v1.UPriority\x12\x10\n\x03ttl\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x1d\n\x10permission_level\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x17\n\ncommstatus\x18\x07 \x01(\x05H\x03\x88\x01\x01\x12&\n\x05reqid\x18\x08 \x01(\x0b\x32\x12.uprotocol.v1.UUIDH\x04\x88\x01\x01\x12\x12\n\x05token\x18\t \x01(\tH\x05\x88\x01\x01\x42\x07\n\x05_sinkB\x06\n\x04_ttlB\x13\n\x11_permission_levelB\r\n\x0b_commstatusB\x08\n\x06_reqidB\x08\n\x06_token*\x7f\n\x0cUMessageType\x12\x1d\n\x19UMESSAGE_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15UMESSAGE_TYPE_PUBLISH\x10\x01\x12\x19\n\x15UMESSAGE_TYPE_REQUEST\x10\x02\x12\x1a\n\x16UMESSAGE_TYPE_RESPONSE\x10\x03*\xab\x01\n\tUPriority\x12\x19\n\x15UPRIORITY_UNSPECIFIED\x10\x00\x12\x11\n\rUPRIORITY_CS0\x10\x01\x12\x11\n\rUPRIORITY_CS1\x10\x02\x12\x11\n\rUPRIORITY_CS2\x10\x03\x12\x11\n\rUPRIORITY_CS3\x10\x04\x12\x11\n\rUPRIORITY_CS4\x10\x05\x12\x11\n\rUPRIORITY_CS5\x10\x06\x12\x11\n\rUPRIORITY_CS6\x10\x07\x42.\n\x18org.eclipse.uprotocol.v1B\x10UAttributesProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uattributes_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030org.eclipse.uprotocol.v1B\020UAttributesProtoP\001'
  _globals['_UMESSAGETYPE']._serialized_start=437
  _globals['_UMESSAGETYPE']._serialized_end=564
  _globals['_UPRIORITY']._serialized_start=567
  _globals['_UPRIORITY']._serialized_end=738
  _globals['_UATTRIBUTES']._serialized_start=59
  _globals['_UATTRIBUTES']._serialized_end=435
# @@protoc_insertion_point(module_scope)
