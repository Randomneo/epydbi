;;; EPyDBI --- Emacs Python DataBase Interface
;;; Commentary:
;;; epc for python db interface

;;; Code:

(package-initialize)
(require 'epc)

(setq epydbi (epc:start-epc "python" '("db_interface.py")))

(deferred:$
  (epc:call-deferred epydbi 'init_connection '("postgres"))
  (deferred:nextc it
    (lambda (x) (message "Return : %S" x))))

(deferred:$
  (epc:call-deferred epydbi 'echo '())
  (deferred:nextc it
    (lambda (x) (message "Return : %S" x))))

(message "Return : %S" (epc:call-sync epydbi 'echo '()))

(message "test")

;;; test.el ends here
