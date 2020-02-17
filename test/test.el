(require 'epc)

(defvar my-epc (epc:start-epc "python" '("my-server.py")))

(deferred:$
  (epc:call-deferred my-epc 'echo '(10))
  (deferred:nextc it
    (lambda (x) (message "Return : %S" x))))

(message "Return : %S" (epc:call-sync my-epc 'echo '(10 40)))
