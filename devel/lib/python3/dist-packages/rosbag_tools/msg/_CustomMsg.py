# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rosbag_tools/CustomMsg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rosbag_tools.msg
import std_msgs.msg

class CustomMsg(genpy.Message):
  _md5sum = "e4d6829bdfe657cb6c21a746c86b21a6"
  _type = "rosbag_tools/CustomMsg"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# CustomMsg.msg


Header header           # ROS standard message header

uint64 timebase         # The time of first point

uint32 point_num        # Total number of pointclouds

uint8 lidar_id          # Lidar device id number

uint8[3] rsvd           # Reserved use

CustomPoint[] points    # Pointcloud data

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: rosbag_tools/CustomPoint
# CustomPoint.msg


uint32 offset_time              # Offset time relative to the base time

float32 x                       # X axis coordinate, unit: m

float32 y                       # Y axis coordinate, unit: m

float32 z                       # Z axis coordinate, unit: m

uint8 reflectivity              # Reflectivity, 0~255

uint8 tag                       # Livox tag

uint8 line                      # Laser number in lidar
"""
  __slots__ = ['header','timebase','point_num','lidar_id','rsvd','points']
  _slot_types = ['std_msgs/Header','uint64','uint32','uint8','uint8[3]','rosbag_tools/CustomPoint[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,timebase,point_num,lidar_id,rsvd,points

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CustomMsg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.timebase is None:
        self.timebase = 0
      if self.point_num is None:
        self.point_num = 0
      if self.lidar_id is None:
        self.lidar_id = 0
      if self.rsvd is None:
        self.rsvd = b'\0'*3
      if self.points is None:
        self.points = []
    else:
      self.header = std_msgs.msg.Header()
      self.timebase = 0
      self.point_num = 0
      self.lidar_id = 0
      self.rsvd = b'\0'*3
      self.points = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_QIB().pack(_x.timebase, _x.point_num, _x.lidar_id))
      _x = self.rsvd
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_I3f3B().pack(_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.points is None:
        self.points = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.timebase, _x.point_num, _x.lidar_id,) = _get_struct_QIB().unpack(str[start:end])
      start = end
      end += 3
      self.rsvd = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = rosbag_tools.msg.CustomPoint()
        _x = val1
        start = end
        end += 19
        (_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line,) = _get_struct_I3f3B().unpack(str[start:end])
        self.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_QIB().pack(_x.timebase, _x.point_num, _x.lidar_id))
      _x = self.rsvd
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_I3f3B().pack(_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.points is None:
        self.points = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.timebase, _x.point_num, _x.lidar_id,) = _get_struct_QIB().unpack(str[start:end])
      start = end
      end += 3
      self.rsvd = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = rosbag_tools.msg.CustomPoint()
        _x = val1
        start = end
        end += 19
        (_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line,) = _get_struct_I3f3B().unpack(str[start:end])
        self.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3B = None
def _get_struct_3B():
    global _struct_3B
    if _struct_3B is None:
        _struct_3B = struct.Struct("<3B")
    return _struct_3B
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3s = None
def _get_struct_3s():
    global _struct_3s
    if _struct_3s is None:
        _struct_3s = struct.Struct("<3s")
    return _struct_3s
_struct_I3f3B = None
def _get_struct_I3f3B():
    global _struct_I3f3B
    if _struct_I3f3B is None:
        _struct_I3f3B = struct.Struct("<I3f3B")
    return _struct_I3f3B
_struct_QIB = None
def _get_struct_QIB():
    global _struct_QIB
    if _struct_QIB is None:
        _struct_QIB = struct.Struct("<QIB")
    return _struct_QIB
