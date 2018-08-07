# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='chat',
  syntax='proto3',
  serialized_pb=_b('\n\nchat.proto\x12\x04\x63hat\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x15\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"/\n\rLoginResponse\x12\x1e\n\x07session\x18\x01 \x01(\x0b\x32\r.chat.Session\"/\n\rLogoutRequest\x12\x1e\n\x07session\x18\x01 \x01(\x0b\x32\r.chat.Session\"\x10\n\x0eLogoutResponse\"\x16\n\x06Member\x12\x0c\n\x04name\x18\x01 \x01(\t\",\n\x0bMembersList\x12\x1d\n\x07members\x18\x01 \x03(\x0b\x32\x0c.chat.Member\"/\n\rMemberRequest\x12\x1e\n\x07session\x18\x01 \x01(\x0b\x32\r.chat.Session\"B\n\x12SendMessageRequest\x12\x1e\n\x07session\x18\x01 \x01(\x0b\x32\r.chat.Session\x12\x0c\n\x04text\x18\x02 \x01(\t\"/\n\rStreamRequest\x12\x1e\n\x07session\x18\x01 \x01(\x0b\x32\r.chat.Session\"w\n\x05Stock\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x63hange\x18\x03 \x01(\x02\x12\x16\n\x0epercent_change\x18\x04 \x01(\x02\x12\r\n\x05price\x18\x05 \x01(\x02\x12\x0c\n\x04high\x18\x06 \x01(\x02\x12\x0b\n\x03low\x18\x07 \x01(\x02\"{\n\x0eStreamResponse\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x1a\n\x05stock\x18\x04 \x03(\x0b\x32\x0b.chat.Stock2\x9f\x02\n\x04\x43hat\x12\x32\n\x05Login\x12\x12.chat.LoginRequest\x1a\x13.chat.LoginResponse\"\x00\x12\x35\n\x06Logout\x12\x13.chat.LogoutRequest\x1a\x14.chat.LogoutResponse\"\x00\x12\x30\n\x07Members\x12\x13.chat.MemberRequest\x1a\x0c.chat.Member\"\x00\x30\x01\x12\x41\n\x0bSendMessage\x12\x18.chat.SendMessageRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x37\n\x06Stream\x12\x13.chat.StreamRequest\x1a\x14.chat.StreamResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='chat.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chat.Session.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=103,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='chat.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='password', full_name='chat.LoginRequest.password', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='chat.LoginRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=155,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='chat.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='chat.LoginResponse.session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=204,
)


_LOGOUTREQUEST = _descriptor.Descriptor(
  name='LogoutRequest',
  full_name='chat.LogoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='chat.LogoutRequest.session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=253,
)


_LOGOUTRESPONSE = _descriptor.Descriptor(
  name='LogoutResponse',
  full_name='chat.LogoutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=271,
)


_MEMBER = _descriptor.Descriptor(
  name='Member',
  full_name='chat.Member',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chat.Member.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=295,
)


_MEMBERSLIST = _descriptor.Descriptor(
  name='MembersList',
  full_name='chat.MembersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='members', full_name='chat.MembersList.members', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=341,
)


_MEMBERREQUEST = _descriptor.Descriptor(
  name='MemberRequest',
  full_name='chat.MemberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='chat.MemberRequest.session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=390,
)


_SENDMESSAGEREQUEST = _descriptor.Descriptor(
  name='SendMessageRequest',
  full_name='chat.SendMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='chat.SendMessageRequest.session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='chat.SendMessageRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=458,
)


_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='chat.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='chat.StreamRequest.session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=507,
)


_STOCK = _descriptor.Descriptor(
  name='Stock',
  full_name='chat.Stock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='chat.Stock.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chat.Stock.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change', full_name='chat.Stock.change', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent_change', full_name='chat.Stock.percent_change', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='chat.Stock.price', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='chat.Stock.high', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='chat.Stock.low', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=628,
)


_STREAMRESPONSE = _descriptor.Descriptor(
  name='StreamResponse',
  full_name='chat.StreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='chat.StreamResponse.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='chat.StreamResponse.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='chat.StreamResponse.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stock', full_name='chat.StreamResponse.stock', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=753,
)

_LOGINRESPONSE.fields_by_name['session'].message_type = _SESSION
_LOGOUTREQUEST.fields_by_name['session'].message_type = _SESSION
_MEMBERSLIST.fields_by_name['members'].message_type = _MEMBER
_MEMBERREQUEST.fields_by_name['session'].message_type = _SESSION
_SENDMESSAGEREQUEST.fields_by_name['session'].message_type = _SESSION
_STREAMREQUEST.fields_by_name['session'].message_type = _SESSION
_STREAMRESPONSE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMRESPONSE.fields_by_name['stock'].message_type = _STOCK
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['LogoutRequest'] = _LOGOUTREQUEST
DESCRIPTOR.message_types_by_name['LogoutResponse'] = _LOGOUTRESPONSE
DESCRIPTOR.message_types_by_name['Member'] = _MEMBER
DESCRIPTOR.message_types_by_name['MembersList'] = _MEMBERSLIST
DESCRIPTOR.message_types_by_name['MemberRequest'] = _MEMBERREQUEST
DESCRIPTOR.message_types_by_name['SendMessageRequest'] = _SENDMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['Stock'] = _STOCK
DESCRIPTOR.message_types_by_name['StreamResponse'] = _STREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), dict(
  DESCRIPTOR = _SESSION,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Session)
  ))
_sym_db.RegisterMessage(Session)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQUEST,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.LoginRequest)
  ))
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRESPONSE,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.LoginResponse)
  ))
_sym_db.RegisterMessage(LoginResponse)

LogoutRequest = _reflection.GeneratedProtocolMessageType('LogoutRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUTREQUEST,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.LogoutRequest)
  ))
_sym_db.RegisterMessage(LogoutRequest)

LogoutResponse = _reflection.GeneratedProtocolMessageType('LogoutResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUTRESPONSE,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.LogoutResponse)
  ))
_sym_db.RegisterMessage(LogoutResponse)

Member = _reflection.GeneratedProtocolMessageType('Member', (_message.Message,), dict(
  DESCRIPTOR = _MEMBER,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Member)
  ))
_sym_db.RegisterMessage(Member)

MembersList = _reflection.GeneratedProtocolMessageType('MembersList', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERSLIST,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MembersList)
  ))
_sym_db.RegisterMessage(MembersList)

MemberRequest = _reflection.GeneratedProtocolMessageType('MemberRequest', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERREQUEST,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MemberRequest)
  ))
_sym_db.RegisterMessage(MemberRequest)

SendMessageRequest = _reflection.GeneratedProtocolMessageType('SendMessageRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDMESSAGEREQUEST,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.SendMessageRequest)
  ))
_sym_db.RegisterMessage(SendMessageRequest)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMREQUEST,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.StreamRequest)
  ))
_sym_db.RegisterMessage(StreamRequest)

Stock = _reflection.GeneratedProtocolMessageType('Stock', (_message.Message,), dict(
  DESCRIPTOR = _STOCK,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Stock)
  ))
_sym_db.RegisterMessage(Stock)

StreamResponse = _reflection.GeneratedProtocolMessageType('StreamResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMRESPONSE,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.StreamResponse)
  ))
_sym_db.RegisterMessage(StreamResponse)



_CHAT = _descriptor.ServiceDescriptor(
  name='Chat',
  full_name='chat.Chat',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=756,
  serialized_end=1043,
  methods=[
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='chat.Chat.Login',
    index=0,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Logout',
    full_name='chat.Chat.Logout',
    index=1,
    containing_service=None,
    input_type=_LOGOUTREQUEST,
    output_type=_LOGOUTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Members',
    full_name='chat.Chat.Members',
    index=2,
    containing_service=None,
    input_type=_MEMBERREQUEST,
    output_type=_MEMBER,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='chat.Chat.SendMessage',
    index=3,
    containing_service=None,
    input_type=_SENDMESSAGEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stream',
    full_name='chat.Chat.Stream',
    index=4,
    containing_service=None,
    input_type=_STREAMREQUEST,
    output_type=_STREAMRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHAT)

DESCRIPTOR.services_by_name['Chat'] = _CHAT

# @@protoc_insertion_point(module_scope)
