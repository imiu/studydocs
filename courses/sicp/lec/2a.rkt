(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))

(define (1+ a)
  (+ 1 a))
(define (square a)
  (* a a))

(define (sum-int a b)
  (define (identity x) x)
  (sum identity a 1+ b))

(define (sum-sq a b)
  (sum square a 1+ b))

(define (pi-sum a b)
  (sum (lambda (i) (/ 1 (* i (+ i 2))))
       a
       (lambda (i) (+ i 4))
       b))

(pi-sum 1 2)

; Newton's method
(define (sqrt x)
  (newton (lambda (y) (- x (square y)))
          1))

(define (newton f guess)
  (define df (deriv f))
  (fixed-point
   (lambda (x) (-x (/ f(x) (df x))))
   guess))

(define deriv
  (lambda (f)
    (lambda (x)
      (/ (- (f (+ x dx))
            (f x))
         dx))))

(define dx .000001)