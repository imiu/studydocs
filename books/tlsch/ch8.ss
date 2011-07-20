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

(define eqan?
  (lambda (a1 a2)
    (cond
      ((and (number? a1) (number? a2)) (eq? a1 a2))
      ((or (number? a1) (number? a2)) #f)
      (else (eq? a1 a2)))))

(define eqlist?
  (lambda (l1 l2)
    (cond
      ((and (null? l1) (null? l2)) #t)
      ((or (null? l1) (null? l2)) #f)
      ((and (atom? (car l1)) (atom? (car l2)))
       (and (eqan? (car l1) (car l2)) (eqlist? (cdr l1) (cdr l2))))
      ((or (atom? (car l1)) (atom? (car l2))) #f)
      (else (and (eqlist? (car l1) (car l2)) (eqlist? (cdr l1) (cdr l2)))))))

(define equal?
  (lambda (s1 s2)
    (cond
      ((and (atom? s1) (atom? s2))
       (eqan? s1 s2))
      ((or (atom? s1) (atom? s2)) #f)
      (else (eqlist? s1 s2)))))

(define member?
  (lambda (a lat)
    (cond
      ((null? lat) #f)
      (else (or (equal? (car lat) a)
                (member? a (cdr lat)))))))

(define multirember
  (lambda (a lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((equal? (car lat) a) (multirember a (cdr lat)))
         (else (cons (car lat) (multirember a (cdr lat)))))))))

;*********************************
;********    Chapter 8    ********
;*********************************

;(define rember-f
;  (lambda (test? a l)
;    (cond
;      ((null? l) (quote()))
;      ((test? (car l) a) (cdr l))
;      (else (cons (car l) (rember-f test? a (cdr l)))))))

;(rember-f equal? '(pop corn) '(lemonade (pop corn) and (cake)))

(define eq?-c
  (lambda (a)
    (lambda (x)
      (eq? x a))))

(define rember-f
  (lambda (test?)
    (lambda (a l)
      (cond
        ((null? l) (quote()))
        ((test? (car l) a) (cdr l))
        (else (cons (car l) ((rember-f test?) a (cdr l))))))))

(define rember-eq? (rember-f eq?))
;(rember-eq? 'tuna '(tuna salad is good))

;(define insertL-f
;  (lambda (test?)
;    (lambda (new old l)
;      (cond
;        ((null? l) (quote()))
;        ((test? (car l) old) (cons (new (cons old (cdr l)))))
;        (else (cons (car l) ((insertL-f test?) new old (cdr l))))))))
;
;(define insertR-f
;  (lambda (test?)
;    (lambda (new old l)
;      (cond
;        ((null? l) (quote()))
;        ((test? (car l) old) (cons (old (cons new (cdr l)))))
;        (else (cons (car l) ((insertR-f test?) new old (cdr l))))))))

;(define seqL
;  (lambda (new old l)
;    (cons new (cons old l))))
;
;(define seqR
;  (lambda (new old l)
;    (cons old (cons new l))))

(define insert-g
  (lambda (seq)
    (lambda (new old l)
      (cond
        ((null? l) (quote()))
        ((eq? (car l) old) (seq new old (cdr l)))
        (else (cons (car l) ((insert-g seq) new old (cdr l))))))))

(define insert-L
  (insert-g
      (lambda (new old l)
        (cons new (cons old l)))))

(define insert-R
  (insert-g
      (lambda (new old l)
        (cons old (cons new l)))))

;p134
;!!! The Ninth Commandment !!!
;!!! Abstract common patterns with a function.
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

(define multirember-f
  (lambda (test?)
    (lambda (a lat)
      (cond
        ((null? lat) (quote()))
        ((test? a (car lat)) ((multirember-f test?) a (cdr lat)))
        (else (cons (car lat) ((multirember-f test?) a (cdr lat))))))))

(define multiremberT
  (lambda (test? lat)
    (cond
      ((null? lat) (quote()))
      ((test? (car lat)) (multiremberT test? (cdr lat)))
      (else (cons (car lat) (multiremberT test? (cdr lat)))))))

(define multirember&co
  (lambda (a lat col)
    (cond
      ((null? lat) (col (quote()) (quote())))
      ((eq? (car lat) a) (multirember&co a (cdr lat) (lambda (newlat seen)
                                                       (col newlat (cons (car lat) seen)))))
      (else
       (multirember&co a (cdr lat) (lambda (newlat seen)
                                     (col (cons (car lat) newlat) seen)))))))

(define a-friend
  (lambda (x y)
    (null? y)))

;(multirember&co 'tuna '(strawberries tuna and swordfish) a-friend)
;(multirember&co 'tuna '() a-friend)
;(multirember&co 'tuna '(and tuna) a-friend)

;p140
;!!! The Tenth Commandment !!!
;!!! Build functions to collect more than one value at a time.
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

(define multiinsertLR
  (lambda (new oldL oldR lat)
    (cond
      ((null? lat) (quote()))
      ((eq? (car lat) oldL)
       (cons new (cons oldL (multiinsertLR new oldL oldR (cdr lat)))))
      ((eq? (car lat) oldR)
       (cons oldR (cons new (multiinsertLR new oldL oldR (cdr lat)))))
      (else
       (cons (car lat) (multiinsertLR new oldL oldR (cdr lat)))))))

(define evens-only*
  (lambda (l)
    (cond
      ((null? l) (quote()))
      ((atom? (car l))
       (cond ((even? (car l)) (cons (car l) (evens-only* (cdr l))))
             (else (evens-only* (cdr l)))))
      (else (cons (evens-only* (car l)) (evens-only* (cdr l)))))))

(evens-only* '((9 1 2 8) 3 10 ((9 9) 7 6) 2))

































