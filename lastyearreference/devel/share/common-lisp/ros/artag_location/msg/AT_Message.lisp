; Auto-generated. Do not edit!


(cl:in-package artag_location-msg)


;//! \htmlinclude AT_Message.msg.html

(cl:defclass <AT_Message> (roslisp-msg-protocol:ros-message)
  ((tran_x
    :reader tran_x
    :initarg :tran_x
    :type cl:float
    :initform 0.0)
   (tran_y
    :reader tran_y
    :initarg :tran_y
    :type cl:float
    :initform 0.0)
   (reached
    :reader reached
    :initarg :reached
    :type cl:string
    :initform ""))
)

(cl:defclass AT_Message (<AT_Message>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AT_Message>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AT_Message)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name artag_location-msg:<AT_Message> is deprecated: use artag_location-msg:AT_Message instead.")))

(cl:ensure-generic-function 'tran_x-val :lambda-list '(m))
(cl:defmethod tran_x-val ((m <AT_Message>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader artag_location-msg:tran_x-val is deprecated.  Use artag_location-msg:tran_x instead.")
  (tran_x m))

(cl:ensure-generic-function 'tran_y-val :lambda-list '(m))
(cl:defmethod tran_y-val ((m <AT_Message>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader artag_location-msg:tran_y-val is deprecated.  Use artag_location-msg:tran_y instead.")
  (tran_y m))

(cl:ensure-generic-function 'reached-val :lambda-list '(m))
(cl:defmethod reached-val ((m <AT_Message>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader artag_location-msg:reached-val is deprecated.  Use artag_location-msg:reached instead.")
  (reached m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AT_Message>) ostream)
  "Serializes a message object of type '<AT_Message>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'tran_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'tran_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'reached))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'reached))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AT_Message>) istream)
  "Deserializes a message object of type '<AT_Message>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'tran_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'tran_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'reached) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'reached) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AT_Message>)))
  "Returns string type for a message object of type '<AT_Message>"
  "artag_location/AT_Message")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AT_Message)))
  "Returns string type for a message object of type 'AT_Message"
  "artag_location/AT_Message")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AT_Message>)))
  "Returns md5sum for a message object of type '<AT_Message>"
  "feb690295f73f6492a4c2be8cafaaeec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AT_Message)))
  "Returns md5sum for a message object of type 'AT_Message"
  "feb690295f73f6492a4c2be8cafaaeec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AT_Message>)))
  "Returns full string definition for message of type '<AT_Message>"
  (cl:format cl:nil "float64 tran_x~%float64 tran_y~%string reached~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AT_Message)))
  "Returns full string definition for message of type 'AT_Message"
  (cl:format cl:nil "float64 tran_x~%float64 tran_y~%string reached~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AT_Message>))
  (cl:+ 0
     8
     8
     4 (cl:length (cl:slot-value msg 'reached))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AT_Message>))
  "Converts a ROS message object to a list"
  (cl:list 'AT_Message
    (cl:cons ':tran_x (tran_x msg))
    (cl:cons ':tran_y (tran_y msg))
    (cl:cons ':reached (reached msg))
))
