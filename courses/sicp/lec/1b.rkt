(define (sos x y)
  (+ (sq x) (sq y)))
(define (sq x)
  (* x x))

(define (-1+ x)
  (- x 1))
(define (1+ x)
  (+ x 1))

(define (plus x y)
  (if (= x 0)
      y
      (+ (-1+ x) (1+ y))))


; Simpliest Fibonacci
(define (fib n)
  (if (< n 2)
      n
      (+ (fib (- n 1))
         (fib (- n 2)))))
