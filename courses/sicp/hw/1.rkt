(define (square x) (* x x))
(define (sum-of-squares x y) (+ (square x) (square y)))

(define (abs x)
  (cond ((< x 0) (- x))
        (else x)))


;1.2
; (/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5)))))
;   (* 3 (- 6 2) (- 2 7)))


;1.3
;(min-three 3 3 3)
(define (max-square x y z)
  (define (min-three x y z)
    (cond ((and (< x y) (< x z)) x)
          ((and (< y x) (< y z)) y)
          ((and (< z x) (< z y)) z)
          (else x)))
  (cond ((= (min-three x y z) x)
         (sum-of-squares y z))
        ((= (min-three x y z) y)
         (sum-of-squares x z))
        ((= (min-three x y z) z)
         (sum-of-squares x y))))
; (max-square 3 4 2)


;1.5
(define (p) (p))
(define (test x y)
  (if (= x 0)
      0
      y))
; (test 0 (p))


;1.6
(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

; (sqrt 9)


;1.7
(define (better-good-enough? guess x)
  (< (abs ( - guess (improve guess x))) 0.000001))
(define (better-sqrt-iter guess x)
  (if (better-good-enough? guess x)
      guess
      (better-sqrt-iter (improve guess x) x)))
(define (better-sqrt x)
  (better-sqrt-iter 1.0 x))
; (better-sqrt 0.0005)


;1.8
(define (cube-good-enough? guess x)
  (< (abs ( - guess (improve-cube guess x))) 0.000001))
(define (improve-cube guess x)
  (/ (+ (/ x (* guess guess)) (* 2 guess)) 3))
(define (cube-sqrt-iter guess x)
  (if (cube-good-enough? guess x)
      guess
      (cube-sqrt-iter (improve-cube guess x) x)))
(define (cube-sqrt x)
  (cube-sqrt-iter 1.0 x))
; (cube-sqrt 27)


;1.9
(define (factorial-rec n)
  (if (= 1 n)
      1
      (* n (factorial-rec (- n 1)))))
; (factorial-rec 6)

(define (factorial-it n)
  (define (iter product counter n)
    (if (> counter n)
        product
        (iter (* counter product)
              (+ counter 1)
              n)))
  (iter 1 1 n))
; (factorial-it 40000)


;1.10
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1)
                 (A x (- y 1))))))


; 1.11
(define (ƒ n)
  (cond ((< n 3) n)
        (else (+ (ƒ (- n 1)) (ƒ (- n 2)) (ƒ (- n 3))))))
; (ƒ 3)


; 1.12
(define (pascal row col)
  (cond ((= col 1) 1)
        ((= row 1) 1)
        ((= row col) 1)
        (else (+ (pascal (- row 1) col)
                 (pascal (- row 1) (- col 1))))))

; (pascal 4 4)


(define (expt b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))

(define (expt-i b n)
  (expt-iter b n 1))
(define (expt-iter b counter product)
  (if (= counter 0)
      product
      (expt-iter b
                 (- counter 1)
                 (* b product))))
; (expt-i 3 4)

(define (even? n)
  (= (remainder n 2) 0))

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

; (fast-expt 33 44343)


; (1.16)
(define (fast-expt-i b n)
  (fast-expt-iter b n 1))

(define (fast-expt-iter b counter product)
  (cond ((= counter 0) product)
        ((even? counter) (fast-expt-iter (square b) (/ counter 2) product))
        (else (fast-expt-iter b (- counter 1) (* b product)))))
; (fast-expt-i 3 3)

; 1.17
(define (double a)
  (+ a a))
(define (halve a)
  (/ a 2))
(define (fast-mult a b)
  (cond ((= b 0) 0)
        ((= b 1) a)
        ((even? b) (double (fast-mult a (halve b))))
        (else (+ a (fast-mult a (- b 1))))))
; (fast-mult 3 4)


; 1.18
(define (fast-mult-i a b)
  (fast-mult-iter a b 0))
(define (fast-mult-iter a b product)
  (cond ((= b 0) product)
        ((even? b) (fast-mult-iter (double a) (halve b) product))
        (else (fast-mult-iter a (- b 1) (+ a product)))))
; (fast-mult-i 4 5)

; 1.19
(define (fib n)
  (fib-iter 1 0 0 1 n))
(define (fib-iter a b p q count)
  (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                   (+ (square p) (square q))
                   (+ (* 2 p q) (square q))
                   (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
              (+ (* b p) (* a q))
              p
              q
              (- count 1)))))
; (fib 20)


; 1.20
(define (gcb a b)
  (if (= b 0)
      a
      (gcb b (remainder a b))))
; (gcb 16 28)

(define (smallest-divisor n)
  (find-divisor n 2))
(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))
(define (divides? a b)
  (= (remainder b a) 0))
(define (prime? n)
  (= n (smallest-divisor n)))

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp) (remainder (square (expmod base (/ exp 2) m)) m))
        (else (remainder (* base (expmod base (- exp 1) m)) m))))
(define (fermat-test n)
  (define (try-it a)
    (= (expmod a n n) a))
  (try-it (+ 1 (random (- n 1)))))
(define (fast-prime? n times)
  (cond ((= times 0) true)
        ((fermat-test n) (fast-prime? n (- times 1)))
        (else false)))

; 1.21
; (smallest-divisor 199)
; (smallest-divisor 1999)
; (smallest-divisor 19999)

; 1.22
