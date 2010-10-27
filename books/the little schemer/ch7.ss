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
;********    Chapter 7    ********
;*********************************

(define set?
  (lambda (lat)
    (cond
      ((null? lat) #t)
      ((member? (car lat) (cdr lat)) #f)
      (else (set? (cdr lat))))))

;(set? '(apple peaches apple plum))
;(set? '())
;(set? '(apples peaches pears plums))
;(set? '(apple 3 pear 4 9 apple 3 4))
;(set? '(apple 3 pear 4 9 5))

;(define makeset
;  (lambda (lat)
;    (cond
;      ((null? lat) (quote()))
;      ((member? (car lat) (cdr lat)) (makeset (cdr lat)))
;      (else (cons (car lat) (makeset (cdr lat)))))))

(define makeset
  (lambda (lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cons (car lat) (makeset (multirember (car lat) (cdr lat))))))))

;(makeset '(apple peach pear peach plum apple lemon peach))
;(makeset '(apple 7 peach 2 pear 7))


(define subset?
  (lambda (set1 set2)
    (cond
      ((null? set1) #t)
      ((and (member? (car set1) set2)
            (subset? (cdr set1) set2)))
      (else #f))))

;(subset? '(5 chicken wings) '(5 hamburgers 2 pieces fried chicken and light duckling wings))
;(subset? '(4 puunds of forseradish) '(four pounds chicken and 5 ounces horsedish))

(define eqset?
  (lambda (set1 set2)
      ((and (subset? set1 set2) (subset? set2 set1)))))

(define intersect?
  (lambda (set1 set2)
    (cond
      ((null? set1) #f)
      (else (or (member? (car set1) set2) (intersect? (cdr set1) set2))))))

;(intersect? '(stewed tomatoes and macaroni) '(macaroni and chese))

(define intersect
  (lambda (set1 set2)
    (cond
      ((null? set1) (quote()))
      ((member? (car set1) set2) (cons (car set1) (intersect (cdr set1) set2)))
      (else (intersect (cdr set1) set2)))))

;(intersect '(stewed tomatoes and macaroni) '(macaroni and chese))

(define union
  (lambda (set1 set2)
    (cond
      ((null? set1) set2)
      ((member? (car set1) set2) (union (cdr set1) set2))
      (else (cons (car set1) (union (cdr set1) set2))))))

;(union '(stewed tomatoes and macaroni casserole) '(macaroni and chese))

(define intersectall
  (lambda (l-set)
    (cond
      ((null? (cdr l-set)) (car l-set))
      (else (intersect (car l-set) (intersectall (cdr l-set)))))))

;(intersectall '((a b c) (c a d e) (e f g h a b)))

(define a-pair?
  (lambda (x)
    (cond
      ((atom? x) #f)
      ((null? x) #f)
      ((null? (cdr x)) #f)
      ((null? (cdr (cdr x))) #t)
      (else #f))))

;(a-pair? '(3 7))
;(a-pair? '(full (house)))
;(a-pair? '((2) (pair)))

(define first
  (lambda (p)
    (car p)))

(define second
  (lambda (p)
    (car (cdr p))))

(define build
  (lambda (s1 s2)
    (cons s1 (cons s2 (quote())))))

(define firsts
  (lambda (fun)
    (cond
      ((null? fun) (quote()))
      (else (cons (first (first fun)) (firsts (cdr fun)))))))

(define fun?
  (lambda (rel)
    (set? (firsts rel))))

(define revrel
  (lambda (rel)
    (cond
      ((null? rel) (quote()))
      (else (cons (build (second (car rel)) (first (car rel))) (revrel (cdr rel)))))))

;(revrel '((8 a) (pumpkin pie) (got sick)))

(define seconds
  (lambda (fun)
    (cond
      ((null? fun) (quote()))
      (else (cons (second (first fun)) (seconds (cdr fun)))))))

(define fullfun?
  (lambda (fun)
    (set? (seconds fun))))

;(fullfun? '((2 3) (3 4) (5 6)))
;(fullfun? '((2 3) (3 4) (5 4)))
