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

;*********************************
;********    Chapter 6    ********
;*********************************

;p99
;(define numbered?
;  (lambda (aexp)
;    (cond
;      ((atom? aexp) (number? aexp))
;      ((eq? (car (cdr aexp)) (quote pl))
;       (and (numbered? (car aexp))
;            (numbered? (car (cdr (cdr aexp))))))
;      ((eq? (car (cdr aexp)) (quote ml))
;       (and (numbered? (car aexp))
;            (numbered? (car (cdr (cdr aexp))))))
;      ((eq? (car (cdr aexp)) (quote pw))
;       (and (numbered? (car aexp))
;            (numbered? (car (cdr (cdr aexp)))))))))

(define numbered?
  (lambda (aexp)
    (cond
      ((atom? aexp) (number? aexp))
      (else
       (and (numbered? (car aexp))
            (numbered? (car (cdr (cdr aexp)))))))))

(numbered? '(3 pl 4 ml 5))

;p103
;!!! The Seventh Commandment !!!
;!!! Recur on the subparts that are of the same nature:
;!!! - On the sublist of a list
;!!! - On the subexpressions of an arithmetic expression.
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p107
;!!! The Eights Commandment !!!
;!!! Use help functions to abstract from representations.
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
