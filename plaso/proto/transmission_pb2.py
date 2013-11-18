# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='plaso/proto/transmission.proto',
  package='transmission',
  serialized_pb='\n\x1eplaso/proto/transmission.proto\x12\x0ctransmission\"\xc6\t\n\x08PathSpec\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32\x1f.transmission.PathSpec.FileType:\x05UNSET\x12\x11\n\tfile_path\x18\x02 \x01(\t\x12\x16\n\x0e\x63ontainer_path\x18\x03 \x01(\t\x12\x14\n\x0cimage_offset\x18\x04 \x01(\x04\x12\x13\n\x0bimage_inode\x18\x05 \x01(\x04\x12/\n\x0fnested_pathspec\x18\x06 \x01(\x0b\x32\x16.transmission.PathSpec\x12\x13\n\x0b\x66ile_offset\x18\x07 \x01(\x04\x12\x11\n\tfile_size\x18\x08 \x01(\x04\x12\x46\n\x10transmit_options\x18\t \x01(\x0e\x32\x1e.transmission.PathSpec.Options:\x0c\x43\x41SE_LITERAL\x12Q\n\tntfs_type\x18\n \x01(\x0e\x32$.transmission.PathSpec.TskFsAttrType:\x18TSK_FS_ATTR_TYPE_DEFAULT\x12\x0f\n\x07ntfs_id\x18\x0b \x01(\x04\x12\x18\n\x10vss_store_number\x18\x0c \x01(\x04\x12\x14\n\x0cpath_prepend\x18\r \x01(\t\"]\n\x08\x46ileType\x12\x12\n\x05UNSET\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x06\n\x02OS\x10\x00\x12\x07\n\x03TSK\x10\x01\x12\x07\n\x03ZIP\x10\x02\x12\x08\n\x04GZIP\x10\x03\x12\x07\n\x03\x42Z2\x10\x04\x12\x07\n\x03TAR\x10\x05\x12\x07\n\x03VSS\x10\x06\"1\n\x07Options\x12\x14\n\x10\x43\x41SE_INSENSITIVE\x10\x00\x12\x10\n\x0c\x43\x41SE_LITERAL\x10\x01\"\xe6\x04\n\rTskFsAttrType\x12\x1c\n\x18TSK_FS_ATTR_TYPE_DEFAULT\x10\x01\x12\x1c\n\x18TSK_FS_ATTR_TYPE_NTFS_SI\x10\x10\x12\"\n\x1eTSK_FS_ATTR_TYPE_NTFS_ATTRLIST\x10 \x12\x1f\n\x1bTSK_FS_ATTR_TYPE_NTFS_FNAME\x10\x30\x12\x1e\n\x1aTSK_FS_ATTR_TYPE_NTFS_VVER\x10@\x12\x1d\n\x19TSK_FS_ATTR_TYPE_NTFS_SEC\x10P\x12\x1f\n\x1bTSK_FS_ATTR_TYPE_NTFS_VNAME\x10`\x12\x1f\n\x1bTSK_FS_ATTR_TYPE_NTFS_VINFO\x10p\x12\x1f\n\x1aTSK_FS_ATTR_TYPE_NTFS_DATA\x10\x80\x01\x12\"\n\x1dTSK_FS_ATTR_TYPE_NTFS_IDXROOT\x10\x90\x01\x12#\n\x1eTSK_FS_ATTR_TYPE_NTFS_IDXALLOC\x10\xa0\x01\x12!\n\x1cTSK_FS_ATTR_TYPE_NTFS_BITMAP\x10\xb0\x01\x12!\n\x1cTSK_FS_ATTR_TYPE_NTFS_SYMLNK\x10\xc0\x01\x12!\n\x1cTSK_FS_ATTR_TYPE_NTFS_EAINFO\x10\xd0\x01\x12\x1d\n\x18TSK_FS_ATTR_TYPE_NTFS_EA\x10\xe0\x01\x12\x1f\n\x1aTSK_FS_ATTR_TYPE_NTFS_PROP\x10\xf0\x01\x12\x1e\n\x19TSK_FS_ATTR_TYPE_NTFS_LOG\x10\x80\x02\x12 \n\x1bTSK_FS_ATTR_TYPE_UNIX_INDIR\x10\x81 \"H\n\nPathBundle\x12\x0f\n\x07pattern\x18\x01 \x02(\t\x12)\n\tpathspecs\x18\x02 \x03(\x0b\x32\x16.transmission.PathSpec\"#\n\nPathFilter\x12\x15\n\rfilter_string\x18\x01 \x03(\t')



_PATHSPEC_FILETYPE = descriptor.EnumDescriptor(
  name='FileType',
  full_name='transmission.PathSpec.FileType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=-1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='OS', index=1, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK', index=2, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ZIP', index=3, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GZIP', index=4, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BZ2', index=5, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TAR', index=6, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='VSS', index=7, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=510,
  serialized_end=603,
)

_PATHSPEC_OPTIONS = descriptor.EnumDescriptor(
  name='Options',
  full_name='transmission.PathSpec.Options',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CASE_INSENSITIVE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CASE_LITERAL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=605,
  serialized_end=654,
)

_PATHSPEC_TSKFSATTRTYPE = descriptor.EnumDescriptor(
  name='TskFsAttrType',
  full_name='transmission.PathSpec.TskFsAttrType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_DEFAULT', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_SI', index=1, number=16,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_ATTRLIST', index=2, number=32,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_FNAME', index=3, number=48,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_VVER', index=4, number=64,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_SEC', index=5, number=80,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_VNAME', index=6, number=96,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_VINFO', index=7, number=112,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_DATA', index=8, number=128,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_IDXROOT', index=9, number=144,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_IDXALLOC', index=10, number=160,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_BITMAP', index=11, number=176,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_SYMLNK', index=12, number=192,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_EAINFO', index=13, number=208,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_EA', index=14, number=224,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_PROP', index=15, number=240,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_NTFS_LOG', index=16, number=256,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TSK_FS_ATTR_TYPE_UNIX_INDIR', index=17, number=4097,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=657,
  serialized_end=1271,
)


_PATHSPEC = descriptor.Descriptor(
  name='PathSpec',
  full_name='transmission.PathSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='transmission.PathSpec.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file_path', full_name='transmission.PathSpec.file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='container_path', full_name='transmission.PathSpec.container_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='image_offset', full_name='transmission.PathSpec.image_offset', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='image_inode', full_name='transmission.PathSpec.image_inode', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nested_pathspec', full_name='transmission.PathSpec.nested_pathspec', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file_offset', full_name='transmission.PathSpec.file_offset', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file_size', full_name='transmission.PathSpec.file_size', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transmit_options', full_name='transmission.PathSpec.transmit_options', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ntfs_type', full_name='transmission.PathSpec.ntfs_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ntfs_id', full_name='transmission.PathSpec.ntfs_id', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vss_store_number', full_name='transmission.PathSpec.vss_store_number', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='path_prepend', full_name='transmission.PathSpec.path_prepend', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PATHSPEC_FILETYPE,
    _PATHSPEC_OPTIONS,
    _PATHSPEC_TSKFSATTRTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=1271,
)


_PATHBUNDLE = descriptor.Descriptor(
  name='PathBundle',
  full_name='transmission.PathBundle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pattern', full_name='transmission.PathBundle.pattern', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pathspecs', full_name='transmission.PathBundle.pathspecs', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1273,
  serialized_end=1345,
)


_PATHFILTER = descriptor.Descriptor(
  name='PathFilter',
  full_name='transmission.PathFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='filter_string', full_name='transmission.PathFilter.filter_string', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1347,
  serialized_end=1382,
)

_PATHSPEC.fields_by_name['type'].enum_type = _PATHSPEC_FILETYPE
_PATHSPEC.fields_by_name['nested_pathspec'].message_type = _PATHSPEC
_PATHSPEC.fields_by_name['transmit_options'].enum_type = _PATHSPEC_OPTIONS
_PATHSPEC.fields_by_name['ntfs_type'].enum_type = _PATHSPEC_TSKFSATTRTYPE
_PATHSPEC_FILETYPE.containing_type = _PATHSPEC;
_PATHSPEC_OPTIONS.containing_type = _PATHSPEC;
_PATHSPEC_TSKFSATTRTYPE.containing_type = _PATHSPEC;
_PATHBUNDLE.fields_by_name['pathspecs'].message_type = _PATHSPEC
DESCRIPTOR.message_types_by_name['PathSpec'] = _PATHSPEC
DESCRIPTOR.message_types_by_name['PathBundle'] = _PATHBUNDLE
DESCRIPTOR.message_types_by_name['PathFilter'] = _PATHFILTER

class PathSpec(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PATHSPEC
  
  # @@protoc_insertion_point(class_scope:transmission.PathSpec)

class PathBundle(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PATHBUNDLE
  
  # @@protoc_insertion_point(class_scope:transmission.PathBundle)

class PathFilter(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PATHFILTER
  
  # @@protoc_insertion_point(class_scope:transmission.PathFilter)

# @@protoc_insertion_point(module_scope)
