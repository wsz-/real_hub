(defun hello () "hello")
(defun hi (s) (list s "sb"))
(defun find-d (x)
  (defun test? (x y)
    (= (rem x y) 0))
  (defun find-divisor (x cc)
    (cond ((= cc x) x)
	  ((test? x cc) cc)
	  ('t (find-divisor x (+ cc 1)))))
  (find-divisor x 2))