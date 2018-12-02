
(cl:in-package :asdf)

(defsystem "artag_location-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AT_Message" :depends-on ("_package_AT_Message"))
    (:file "_package_AT_Message" :depends-on ("_package"))
  ))