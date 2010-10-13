#lang scheme
(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))

(define add1
  (lambda (n)
    (+ n 1)))

(define sub1
  (lambda (n)
    (- n 1)))

;*********************************
;********    Chapter 4    ********
;*********************************

;p59
;(atom? 14)
;(atom? -3)
;(atom? 3.14159)
;(add1 67)
;(sub1 5)
;(sub1 0)
;(zero? 0)
;(zero? 1492)
;(+ 46 12)

;p60
(define pl
  (lambda (n m)
    (cond
      ((zero? m) n)
      (else (add1 (pl n (sub1 m)))))))

;(pl 46 12)

;p61
(define mn
  (lambda (n m)
    (cond
      ((zero? m) n)
      (else (sub1 (mn n (sub1 m)))))))

;(mn 18 25)

;p64
;!!! The First Commandment !!!
;!!! When recurring on a list of atoms,
;!!! lat, ask two questions in it:
;!!! (null? lat) and else.
;!!! When recurring on a number, n,
;!!! ask two questions about it:
;!!! (zeor? n) and else
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

(define addtup
  (lambda (tup)
    (cond
      ((null? tup) 0)
      (else (pl (car tup) (addtup (cdr tup)))))))

;(addtup '(15 6 7 12 3))

;p65
;!!! The Fourth Commandment !!!
;!!! Always change at least one argument while recurring
;!!! It must be changed to be closer to termination:
;!!! when using cdr, test termination with null? and
;!!! when using sub1, test termination with zero?
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

(define ml
  (lambda (n m)
    (cond
      ((zero? m) 0)
      (else (pl n (ml n (sub1 m)))))))

;(ml 3 5)
;(ml 12 3)

;p67
;!!! The Fifth Commandment !!!
;!!! When building a value with +,
;!!! use 0 for termination line.
;!!! +0 adds nothing
;!!! When building with *,
;!!! use 1 for termination line.
;!!! *1 adds nothing.
;!!! When building with cons,
;!!! use () for termination line
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p69
(define tup+
  (lambda (tup1 tup2)
    (cond
      ((null? tup1) tup2)
      ((null? tup2) tup1)
      (else 
       (cons 
        (pl (car tup1) (car tup2)) 
        (tup+ (cdr tup1) (cdr tup2)))))))

;(tup+ '(1 2 3) '(2 3 4 5))

;p71
(define gt
  (lambda (n m)
    (cond
      ((zero? n) #f)
      ((zero? m) #t)
      (else (gt (sub1 n) (sub1 m))))))

;(gt 12 133)
;(gt 120 11)
;(gt 3 3)

;p73
(define lt
  (lambda (n m)
    (cond
      ((zero? m) #f)
      ((zero? n) #t)
      (else (lt (sub1 n) (sub1 m))))))
;(lt 3 4)

;p74
(define eq
  (lambda (n m)
    (cond
      ((gt m n) #f)
      ((lt m n) #f)
      (else #t))))

;(eq 4 4)

(define pw
  (lambda (n m)
    (cond
      ((zero? m) 1)
      (else (ml n (pw n (sub1 m)))))))

;(pw 5 3)

;p75
(define dv
  (lambda (n m)
    (cond
      ((lt n m) 0)
      (else (add1 (dv (mn n m) m))))))
;(dv 15 4)

;p76
(define mlen
  (lambda (lat)
    (cond
      ((null? lat) 0)
      (else (add1 (mlen (cdr lat)))))))

;(mlen'(hotdogs with mustard sauerkraut and pickles))

(define pick
  (lambda (n lat)
    (cond
      ((zero? (sub1 n)) (car lat))
      (else (pick (sub1 n) (cdr lat))))))

;(pick 4 '(lasagna spaghetti ravioli macaroni meatball))

;p77

(define rempick
  (lambda (n lat)
    (cond
      ((zero? (sub1 n)) (cdr lat))
      (else (cons (car lat) (rempick (sub1 n) (cdr lat)))))))

;(rempick 3 '(hotdogs with hot mustard))

;(number? 'tomato)
;(number? 76)

;p78
(define no-nums
  (lambda (lat)
    (cond
      ((null? lat) (quote()))
      ((number? (car lat)) (no-nums(cdr lat)))
      (else (cons (car lat) (no-nums(cdr lat)))))))

;(no-nums '(5 pears 6 prunes 9 dates))

(define all-nums
  (lambda (lat)
    (cond
      ((null? lat) (quote()))
      ((number? (car lat)) (cons (car lat) (all-nums (cdr lat))))
      (else (all-nums (cdr lat))))))

;(all-nums '(5 pears 6 prunes 9 dates))

(define eqan?
  (lambda (a1 a2)
    (cond
      ((and (number? a1) (number? a2)) (eq a1 a2))
      ((or (number? a1) (number? a2)) #f)
      (else (eq? a1 a2)))))

;(eqan? 'a 'a)
;(eqan? 'a 'b)
;(eqan? 1 'a)
;(eqan? 1 1)
;(eqan? 1 2)


(define occur
  (lambda (a lat)
    (cond
      ((null? lat) 0)
      ((eqan? a (car lat)) (add1 (occur a (cdr lat))))
      (else (occur a (cdr lat))))))

;(occur 'a '(a a b a c))

;p79
(define one?
  (lambda (n)
    (eqan? n 1)))

;(one? 1)
;(one? 2)

(define rempickn
  (lambda (n lat)
    (cond
      ((one? n) (cdr lat))
      (else (cons (car lat) (rempickn (sub1 n) (cdr lat)))))))

(rempickn 3 '(lemon meringue salty pie))
