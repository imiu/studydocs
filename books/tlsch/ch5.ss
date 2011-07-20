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
;********    Chapter 5    ********
;*********************************

;p81
(define rember*
  (lambda (a l)
    (cond
      ((null? l) (quote()))
      ((atom? (car l))
       (cond
         ((eq? a (car l)) (rember* a (cdr l)))
         (else (cons (car l) (rember* a (cdr l))))))
      (else (cons (rember* a (car l)) (rember* a (cdr l)))))))

; (rember* 'cup '((coffee) cup ((tea) cup) (and (hick)) cup))

;p82
(define insertR*
  (lambda (new old l)
    (cond
      ((null? l) (quote()))
      ((atom? (car l))
       (cond
         ((eq? old (car l)) (cons old (cons new (insertR* new old (cdr l)))))
         (else (cons (car l) (insertR* new old (cdr l))))))
      (else (cons (insertR* new old (car l)) (insertR* new old (cdr l)))))))

;(insertR* 'roast 'chuck '((how much (wood)) could ((a (wood) chuck)) (((chuck))) (if (a) ((wood chuck))) could chuck wood))

;p83
;!!! The First Commandment !!!
;!!! When recurring on a list of atoms,
;!!! lat, ask two questions in it:
;!!! (null? lat) and else.
;!!! When recurring on a number, n,
;!!! ask two questions about it:
;!!! (zeor? n) and else
;!!! When recurring on a list of S-expressions, l,
;!!! ask three questions about it:
;!!! (null? l), (atom? (car l)) and else
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p84
;!!! The Fourth Commandment !!!
;!!! Always change at least one argument while recurring.
;!!! When recurring on a list of atoms, lat, use (cdr lat).
;!!! When recurring on a list of S-expressions, l,
;!!! use (car l) and (cdr l) if neither (null? l)
;!!! nor (atom? (car l)) are true.
;!!! It must be changed to be closer to termination:
;!!! when using cdr, test termination with null? and
;!!! when using sub1, test termination with zero?
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p85
(define occur*
  (lambda (a l)
    (cond
      ((null? l) 0)
      ((atom? (car l))
       (cond
         ((eq? a (car l)) (add1 (occur* a (cdr l))))
         (else (occur* a (cdr l)))))
      (else (+ (occur* a (car l)) (occur* a (cdr l)))))))

;(occur* 'banana '((banana) (split ((((banana ice))) (cream (banana)) sherbet)) (banana) (bread) (banana brandy)))

(define subst*
  (lambda (new old l)
    (cond
      ((null? l) (quote()))
      ((atom? (car l))
       (cond
         ((eq? old (car l)) (cons new (subst* new old (cdr l))))
         (else (cons (car l) (subst* new old (cdr l))))))
      (else (cons (subst* new old (car l)) (subst* new old (cdr l)))))))

;(subst* 'orange 'banana '((banana) (split ((((banana ice))) (cream (banana)) sherbet)) (banana) (bread) (banana brandy)))

;p86
(define insertL*
  (lambda (new old l)
    (cond
      ((null? l) (quote()))
      ((atom? (car l))
       (cond
         ((eq? old (car l)) (cons new (cons old (insertL* new old (cdr l)))))
         (else (cons (car l) (insertL* new old (cdr l))))))
      (else (cons (insertL* new old (car l)) (insertL* new old (cdr l)))))))

;(insertL* 'pecker 'chuck '((how much (wood)) could ((a (wood) chuck)) (((chuck))) (if (a) ((wood chuck))) could chuck wood))

;p87
(define member*
  (lambda (a l)
    (cond
      ((null? l) #f)
      ((atom? (car l))
       (or (eq? a (car l)) (member* a (cdr l))))
      (else (or (member* a (car l)) (member* a (cdr l)))))))

;(member* 'chips '((potato) (chips ((with) fish) (chips))))

;p88
(define leftmost
  (lambda (l)
    (cond
      ((null? l) #f)
      ((atom? (car l)) (car l))
      (else (leftmost (car l))))))

;(leftmost '((potato) (chips ((with) fish) (chips))))
;(leftmost '(((() four)) 17 (seventeen)))

;p91
(define eqlist?
  (lambda (l1 l2)
    (cond
      ((and (null? l1) (null? l2)) #t)
      ((or (null? l1) (null? l2)) #f)
      ((and (atom? (car l1)) (atom? (car l2)))
         (and (eqan? (car l1) (car l2)) (eqlist? (cdr l1) (cdr l2))))
      ((or (atom? (car l1)) (atom? (car l2))) #f)
      (else (and (eqlist? (car l1) (car l2)) (eqlist? (cdr l1) (cdr l2)))))))

;(eqlist? '() '())
;(eqlist? '() '(a))
;(eqlist? '(strawberry ice cream) '(strawberry ice cream))
;(eqlist? '(beef ((sausage)) (and (soda))) '(beef ((salami)) (and (soda))))

;p92
(define equal?
  (lambda (s1 s2)
    (cond
      ((and (atom? s1) (atom? s2))
       (eqan? s1 s2))
      ((or (atom? s1) (atom? s2)) #f)
      (else (eqlist? s1 s2)))))

;p94
;!!! The Sixth Commandment !!!
;!!! Simplify only after the function is correct.
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p95
(define rember
  (lambda (s l)
    (cond
      ((null? l) (quote()))
      ((equal? (car l) s) (cdr l))
      (else (cons (car l) (rember s (cdr l)))))))





















