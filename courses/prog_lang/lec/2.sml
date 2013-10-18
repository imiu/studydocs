(* 3-3 Records *)
val x = {bar=(1 + 2, true), foo=(3 + 4), baz=(false, 9)};
val my_niece = {name = "Amelia", id = 4223};
val mm = {1 = 1, 2 = 2};

(* 3-5 Datatypes *)
datatype suit = Club | Diamond | Heart | Spade
datatype rank = Jack | Queen | King | Ace | Num of int

datatype id = StudentNum of int
            | Name of string * (string option) * string

datatype exp = Constant of int
             | Negate of exp
             | Add of exp * exp
             | Multiply of exp * exp

fun old_eval e = 
    case e of
        Constant i          => i
      | Negate e2           => ~ (old_eval e2)
      | Add(e1, e2)         => (old_eval e1) + (old_eval e2)
      | Multiply(e1, e2)    => (old_eval e1) * (old_eval e2)

fun number_of_adds e =
    case e of
        Constant i          => 0
      | Negate e2           => number_of_adds(e2)
      | Add(e1, e2)         => 1 + number_of_adds(e1) + number_of_adds(e2)
      | Multiply(e1, e2)    => number_of_adds(e1) + number_of_adds(e2)

fun max_constant e =
    let fun max_of_two(e1, e2) =
            let val m1 = max_constant e1
                val m2 = max_constant e2
            in Int.max(m1, m2)
    end
    in
        case e of
            Constant i => i
            | Negate e2 => max_constant(e2)
            | Add(e1, e2) => Int.max(max_constant(e1), max_constant(e2))
            | Multiply(e1, e2) => Int.max(max_constant(e1), max_constant(e2))
    end

val test_exp = Add (Constant 19, Negate (Constant 4))
val nineteen = max_constant test_exp = 19

(* 3-10 Types *)
type card = suit * rank

(* Safer option for options *)
fun inc_or_zero intoption =
    case intoption of
        NONE => 0
      | SOME i => i + 1

(* New style for lists, no hd, tl or null*)
fun sum_list xs =
    case xs of
        [] => 0
      | x::xs' => x + sum_list xs'

fun append (xs, ys) =
    case xs of
        [] => ys
      | x::xs' => x :: append(xs', ys)

(* 3-12 Polymorphic datatypes *)
datatype 'a option = None | SOME of 'a

(* Let's walk trees *)
datatype ('a, 'b) tree = 
    Node of 'a * ('a, 'b) tree  * ('a, 'b) tree 
  | Leaf of 'b

fun sum_tree tr =
    case tr of
        Leaf i => i
      | Node(i, ltree, rtree) => i + sum_tree ltree + sum_tree rtree

(* val st = sum_tree(Node(1, Leaf(2), Node(3, Leaf(1), Leaf(2)))) *)

(* match each-of types *)
fun sum_triple_1 triple =
    case triple of
        (x, y, z) => x + y + z

fun full_name_1 r =
    case r of
        {first = x, middle = y, last = z} => x ^ " " ^ y ^ " " ^ z

(* better match *)
(* cause one-arm case matches are bad *)
fun sum_triple_2 triple = 
    let val (x, y, z) = triple
    in
        x + y + z
    end

fun full_name_2 r =
    let val {first=x, middle=y, last=z} = r
    in
        x ^ " " ^ y ^ " " ^ z
    end

(* best match *)
fun sum_triple_3 (x, y, z) =
    x + y + z

fun full_name_3 {first=x, middle=y, last=z} =
    x ^ " " ^ y ^ " " ^ z

fun rotate_left (x, y, z) = (y, z, x)

val right_rotated = rotate_left(rotate_left(1, 2, 3))
val left_rotated  = rotate_left(1, 2, 3)

(* 3-16 nested patterns *)
exception ListLengthMismatch

fun zip list_triple =
    case list_triple of
        ([], [], []) => []
      | (hd1::tl1, hd2::tl2, hd3::tl3) => (hd1, hd2, hd3)::zip(tl1, tl2, tl3)
      | _ => raise ListLengthMismatch

fun unzip lst =
    case lst of
        [] => ([], [], [])
      | (a, b, c)::tl => let val (l1, l2, l3) = unzip tl
                         in
                            (a::l1, b::l2, c::l3)
                         end

fun nondecreasing xs =
    case xs of
        [] => true
      | _::[] => true
      | head::(neck::rest) => head <= neck andalso nondecreasing(neck::rest)


datatype sgn = P | N | Z

fun multsign(x1, x2) = (* int * int -> sgn *)
    let fun sign x = if x = 0 then Z else if x > 0 then P else N
    in
        case (sign x1, sign x2) of
            (Z, _) => Z
          | (_, Z) => Z
          | (P, P) => P
          | (N, N) => P
(*        | (N, P) => N
          | (P, N) => N
*)
          | _ => N (* we could prefer a shorter version *)
    end

fun len xs =
    case xs of
        [] => 0
      | _::xs' => 1 + len xs'

(* function patterns *)
fun old_eval e = 
    case e of
        Constant i          => i
      | Negate e2           => ~ (old_eval e2)
      | Add(e1, e2)         => (old_eval e1) + (old_eval e2)
      | Multiply(e1, e2)    => (old_eval e1) * (old_eval e2)

fun eval(Constant i) = i
  | eval(Negate e2) = ~(eval e2)
  | eval(Add(e1, e2)) = (eval e1) + eval(e2)
  | eval(Multiply(e1, e2)) = (eval e1) * eval(e2)

fun fun_len([]) = 0
  | fun_len(_::xs') = 1 + fun_len xs'

val flt = fun_len([]) = 0

(* 3-20 exceptions *)
exception MyException
exception MyOtherException of int * string
(* raise MyOtherException(0, 'Dead') *)

fun maxlist(xs, ex) = (* int list * exn -> int *)
    case xs of
        [] => raise ex
      | x::[] => x
      | x::xs' => Int.max(x, maxlist(xs', ex))

val w = maxlist([3, 4, 5], MyException)

(* handle and return 42 instead of raising exception *)
val z = maxlist([], MyException)
        handle MyException => 42

(* 3-21 tail recursion *)
fun fact_simple n =
    if n = 0
    then 1
    else n * fact_simple(n - 1)

val f1 = fact_simple(12) = 479001600

fun fact_tail n =
    let fun aux(n, acc) =
        if n = 0
        then acc
        else aux(n - 1, acc * n)
    in
        aux(n, 1)
    end

val f2 = fact_tail(12) = 479001600

fun sum_tail xs =
    let fun aux(xs, acc) =
            case xs of
                [] => acc
              | x::xs' => aux(xs', x + acc)
    in
        aux(xs, 0)
    end

val st = sum_tail([1, 2, 3]) = 6

fun reverse_tail xs =
    let fun aux(xs, acc) =
            case xs of
                [] => acc
              | x::xs' => aux(xs', x::acc)
    in
        aux(xs, [])
    end

val rt = reverse_tail([1, 2, 3]) = [3, 2, 1]
