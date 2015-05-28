# -*- coding: utf-8 -*-
"""Parser for Windows Restore Point (rp.log) files."""

import logging
import os

import construct

from plaso.events import time_events
from plaso.lib import errors
from plaso.lib import eventdata
from plaso.parsers import interface
from plaso.parsers import manager


class RestorePointInfoEvent(time_events.FiletimeEvent):
  """Class that defines a Windows Restore Point information event."""

  DATA_TYPE = u'windows:restore_point:info'

  def __init__(
      self, timestamp, restore_point_event_type, restore_point_type,
      sequence_number, description):
    """Initializes the event object.

    Args:
      timestamp: The FILETIME timestamp value.
      restore_point_event_type: The restore point event type.
      restore_point_type: The restore point type.
      sequence_number: The restore point sequence number.
      description: The restore point description.
    """
    super(RestorePointInfoEvent, self).__init__(
        timestamp, eventdata.EventTimestamp.CREATION_TIME)

    self.offset = 0
    self.description = description
    self.restore_point_event_type = restore_point_event_type
    self.restore_point_type = restore_point_type
    self.sequence_number = sequence_number


class RestorePointLogParser(interface.BaseParser):
  """A parser for Windows Restore Point (rp.log) files."""

  NAME = u'rplog'
  DESCRIPTION = u'Parser for Windows Restore Point (rp.log) files.'

  _FILE_HEADER_STRUCT = construct.Struct(
      u'file_header',
      construct.ULInt32(u'event_type'),
      construct.ULInt32(u'restore_point_type'),
      construct.ULInt64(u'sequence_number'),
      construct.RepeatUntil(
          lambda obj, ctx: obj == b'\x00\x00',
          construct.Field(u'description', 2)))

  _FILE_FOOTER_STRUCT = construct.Struct(
      u'file_footer',
      construct.ULInt64(u'creation_time'))

  def _ParseFileHeader(self, file_object):
    """Parses the file header.

    Args:
      file_object: A file-like object to read data from.

    Returns:
      The file header construct object.
    """
    try:
      file_header = self._FILE_HEADER_STRUCT.parse_stream(file_object)
    except (IOError, construct.FieldError) as exception:
      raise errors.UnableToParseFile(
          u'Unable to parse file header with error: {0:s}'.format(exception))

    if not file_header:
      raise errors.UnableToParseFile(u'Unable to read file header')

    return file_header

  def _ParseFileFooter(self, file_object):
    """Parses the file footer.

    Args:
      file_object: A file-like object to read data from.

    Returns:
      The file footer construct object.
    """
    try:
      file_footer = self._FILE_FOOTER_STRUCT.parse_stream(file_object)
    except (IOError, construct.FieldError) as exception:
      raise errors.UnableToParseFile(
          u'Unable to parse file footer with error: {0:s}'.format(exception))

    if not file_footer:
      raise errors.UnableToParseFile(u'Unable to read file footer')

    return file_footer

  def Parse(self, parser_mediator, **kwargs):
    """Parses a single file.

    Args:
      parser_mediator: A parser mediator object (instance of ParserMediator).
    """
    # TODO: for now cheat with detecting this file type.
    file_entry = parser_mediator.GetFileEntry()
    if file_entry.name.lower() != u'rp.log':
      raise errors.UnableToParseFile(u'File not named: rp.log')

    file_object = parser_mediator.GetFileObject(offset=None)
    try:
      self.ParseFileObject(parser_mediator, file_object, **kwargs)
    finally:
      file_object.close()

  def ParseFileObject(self, parser_mediator, file_object, **unused_kwargs):
    """Parses a Windows Prefetch file-like object.

    Args:
      parser_mediator: A parser mediator object (instance of ParserMediator).
      file_object: A file-like object.

    Raises:
      UnableToParseFile: when the file cannot be parsed.
    """
    file_object.seek(0, os.SEEK_SET)
    file_header = self._ParseFileHeader(file_object)

    try:
      # The struct includes the end-of-string character that we need
      # to strip off.
      description = b''.join(file_header.description).decode(u'utf16')[:-1]
    except UnicodeDecodeError as exception:
      description = u''
      logging.warning((
          u'[{0:s}] Unable to decode description UTF-16 stream with '
          u'error: {1:s}').format(self.NAME, exception))

    file_object.seek(-8, os.SEEK_END)
    file_footer = self._ParseFileFooter(file_object)

    timestamp = file_footer.get(u'creation_time', 0)
    if not timestamp:
      parser_mediator.ProduceParseError(u'Timestamp not set.')
    else:
      event_object = RestorePointInfoEvent(
          timestamp, file_header.event_type, file_header.restore_point_type,
          file_header.sequence_number, description)
      parser_mediator.ProduceEvent(event_object)


manager.ParsersManager.RegisterParser(RestorePointLogParser)
