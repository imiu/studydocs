#lang scheme
(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))

;*********************************
;********    Chapter 1    ********
;*********************************
;p3
;(atom? "atom")
;(atom? "turkey")
;(atom? 1492)
;(atom? "u")
;(atom? "*abc$")
;(list? '(atom))
;(list? '(atom turkey or))

;p4
;(list? '((atom turkey) or))
;(atom? "xyz")
;(list? '(x y z))
;(list? '((x y) z))
;(list? '(how are you doing so far))
;(list? '(((how) are) ((you) (doing so)) far))

;p5
;(list? '())
;(atom? '())
;(list? '(() () () ()))
;(car '(a b c))
;(car '((a b c) x y z))
;(car "hotdog")
;(car '())

;p6
;(car '(((hotdogs)) (and) (pickle) relish))
;(car (car '(((hotdogs)) (and))))
;(cdr '(a b c))
;(cdr '((a b c) x y z))
;(cdr '(hamburger))
;(cdr '((x) t r))
;(define a "hotdogs")
;(cdr a)

;p7
;(define l '())
;(cdr l)
;(car (cdr '((b) (x y) ((c)))))
;(cdr (cdr '((b) (x y) ((c)))))
;(cdr (car '(a (b (c)) d)))
;(define a 'peanut)
;(define l '(butter and jelly))
;(cons a l)

;p8
;(cons '(banana and) '(peanut butter and jelly))
;(cons '((help) this) '(is very ((hard) to learn)))
;(cons '(a b (c)) '())
;(cons 'a '())
;(cons '((a b c)) 'b)

;p9
;(cons 'a (car '((b) c d)))
;(cons 'a (cdr '((b) c d)))
;(null? '())
;(null? '(a b c))

;p10
;(null? 'spaghetti)
;(atom? 'Hurry)

;p11
;(atom? (car '(Harry had a heap of apples)))
;(atom? (cdr '(Harry had a heap of apples)))
;(atom? (cdr '(Harry)))
;(atom? (car (cdr '(swing low sweet cherry oat))))
;(atom? (car (cdr '(swing (low sweet) cherry oat))))
;(eq? 'Harry 'Harry)
;(eq? 'margarine 'butter)

;p12
;(eq? '() '(strawberry))
;(eq? 6 7)
;(eq? (car '(Mary had a little lamb chop)) 'Mary)
;(eq? (cdr '(sourced milk)) 'milk)

;p13
;(define l '(beans beans we need jelly beans))
;(eq? (car l) (car (cdr l)))


;*********************************
;********    Chapter 2    ********
;*********************************
(define lat?
  (lambda (l)
    (cond
      ((null? l) #t )
      ((atom? (car l)) (lat? (cdr l)))
      (else #f ))))

(define member?
  (lambda (a lat)
    (cond
      ((null? lat) #f)
      (else (or (eq? (car lat) a)
                (member? a (cdr lat)))))))
;p15
;(lat? '(Jack Sprat could eat no chicken fat))
;(lat? '((Jack) Sprat could eat no chicken fat))
;(lat? '(Jack (Sprat could) eat no chicken fat))
;(lat? '())

;p21
;(or (null? '()) (atom? '(d e f g)))
;(or (null? '(a b c)) (null? '()))
;(or (null? '(a b c)) (null? '(atom)))

;p22
;(member? 'meat '(mashed potatoes and meat gravy))

;!!! The First Commandment !!!
;!!! Always ask null? as the first question 
;!!! in expressing any function
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p28
;(member? 'liver '(bagels and lox))


;*********************************
;********    Chapter 3    ********
;*********************************
(define rember
  (lambda (a lat)
    (cond
      ((null? lat) (quote()))
      ((eq? (car lat) a) (cdr lat))
      (else (cons (car lat) (rember a (cdr lat)))))))

;p33
;(rember 'mint '(mint lamb chops and mint jelly))

;p34
;(rember 'bacon '(bacon lettuce and tomato))

;p35
;(rember 'and '(bacon lettuce and tomato))

;!!! The Second Commandment !!!
;!!! Use cons to build lists
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p37
;(rember 'and '(bacon lettuce and tomato))

;p42
;(rember 'sause '(soy sauce and tomato sauce))

;p44
(define first
  (lambda (l)
    (cond
      ((null? l) (quote()))
      (else (cons (car (car l)) (first (cdr l)))))))

;(define l '((a b) (c d) (e f)))
;(define l '())
;(define l '((five plums) (four) (eleven green oranges)))
;(define l '(((five plums) four) (eleven green oranges) ((no) more)))
;(first l)

;!!! The Third Commandment !!!
;!!! When building a list, describe the first typical element,
;!!! and then cons it onto the natural recursion
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

;p48
(define insertR
  (lambda (new old lat)
    (cond
      ((null? lat) (quote()))
      (else 
       (cond 
         ((eq? (car lat) old) (cons old (cons new (cdr lat))))
         (else (cons (car lat) (insertR new old (cdr lat)))))))))

;p50
;(insertR 'topping 'fudge '(ice cream with fudge for desert))

;p51
(define insertL
  (lambda (new old lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((eq? (car lat) old) (cons new lat))
         (else (cons (car lat) (insertL new old (cdr lat)))))))))

;(insertL 'topping 'fudge '(ice cream with fudge for desert))

(define subst
  (lambda (new old lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((eq? (car lat) old) (cons new (cdr lat)))
         (else (cons (car lat) (subst new old (cdr lat)))))))))

;(subst 'topping 'fudge '(ice cream with fudge for desert))

;p52
(define subst2
  (lambda (new o1 o2 lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((or (eq? (car lat) o1) (eq? (car lat) o2)) (cons new (cdr lat)))
         (else (cons (car lat) (subst2 new o1 o2 (cdr lat)))))))))
;(subst2 'vanilla 'chocolate 'banana '(banana ice cream with chocolate topping))

;p53
(define multirember
  (lambda (a lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((eq? (car lat) a) (multirember a (cdr lat)))
         (else (cons (car lat) (multirember a (cdr lat)))))))))

;(multirember 'cup '(coffee cup tea cup and hick cup))

;p56
(define multiinsertR 
  (lambda (new old lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((eq? (car lat) old) (cons old (cons new (multiinsertR new old (cdr lat)))))
         (else (cons (car lat) (multiinsertR new old (cdr lat)))))))))

;(multiinsertR 'no 'and '(coffee and sugar and milk and stuff))

(define multiinsertL
  (lambda (new old lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((eq? (car lat) old) (cons new (cons old (multiinsertL new old (cdr lat)))))
         (else (cons (car lat) (multiinsertL new old (cdr lat)))))))))

;(multiinsertL 'and 'no '(coffee no sugar no milk no stuff))

;!!! The Fourth Commandment !!!
;!!! Always change at least one argument while recurring
;!!! It must be changed to be closer to termination.
;!!! The changing argument must be tested in the terminaion condition:
;!!! when using cdr, test termination with null?.
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

(define multisubst
  (lambda (new old lat)
    (cond
      ((null? lat) (quote()))
      (else
       (cond
         ((eq? (car lat) old) (cons new (multisubst new old (cdr lat))))
         (else (cons (car lat) (multisubst new old (cdr lat)))))))))

;(multisubst 'and 'no '(coffee no sugar no milk no stuff))

































