val x = 34
val y = 17
val z = (y + 2) - (x + y )
val abs_of_z = if z < 0 then 0 - z else 0
val a = ~5
val int_div = x div y

(* 2-6 Functions *)
fun pow (x : int, y : int) =
    if y = 0
    then 1
    else x * pow(x, y - 1)

fun cube(x : int) =
    pow(x, 3)

val sixtyfour = cube(4)
val fortytwo = pow(2, 2 + 2) + pow(4, 2) + cube(2) + 2 

(* 2-8 Tuples and lists *)
val t = (1, 2)
val t1 = #1 t (* access first element *)
val t2 = #2 t

fun swap(pr: int*bool) = 
    (#2 pr, #1 pr)

fun sum_two_pairs(pr1: int * int, pr2: int * int) =
    (#1 pr1) + (#2 pr1) + (#1 pr2) + (#2 pr2)

fun div_mod(x: int, y: int)=
    (x div y, x mod y)

fun sort_pair(pr: int * int)=
    if (#1 pr < #2 pr)
    then pr
    else (#2 pr, #1 pr)

(* 2-10 List functions *)
fun sum_list(xs: int list) =
    if null xs
    then 0
    else hd xs + sum_list(tl xs)

fun countdown (x: int) =
    if x = 0
    then []
    else x::countdown(x - 1)

fun append(xs: int list, ys: int list) =
    if null xs
    then ys
    else hd xs :: append(tl xs, ys)

fun sum_pair_list(xs: (int * int) list) =
    if null xs
    then 0
    else #1 (hd xs) + #2 (hd xs) + sum_pair_list(tl xs)

fun firsts(xs: (int * int) list) =
    if null xs
    then []
    else (#1 (hd xs)) :: firsts(tl xs)

(* 2-11 Let expressions *)
fun silly1(z: int) =
    let
        val x = if z > 0 then z else 34
        val y = x + z + 9
    in
        if x > y then x * 2 else y * y
    end

fun silly2() =
    let
        val x = 1
    in
        (let val x = 2 in x + 1 end) + (let val y = x + 2 in y + 1 end)
    end

fun countup_from1(x: int) =
    let
        fun count(from: int) =
            if from=x
            then x :: []
            else from :: count(from + 1)
    in
        count(1)
    end

(* 2^N on growing lists because of 2 recursive calls *)
fun bad_max(xs: int list) =
    if null xs
    then 0
    else if null (tl xs)
    then hd xs
    else if hd xs > bad_max(tl xs)
    then hd xs
    else bad_max(tl xs)

(* using let to store value and not compute it twice *)
fun good_max(xs: int list) =
    if null xs
    then 0
    else if null (tl xs)
    then hd xs
    else
        let val ans_ts = good_max(tl xs)
        in 
            if hd xs > ans_ts
            then hd xs
            else ans_ts
        end

(* 2-14 Options *)
(* fn : int list -> int option *)
fun max1(xs: int list) =
    if null xs
    then NONE
    else
        let val tl_ans = max1(tl xs)
        in if isSome tl_ans andalso valOf tl_ans > hd xs
            then tl_ans
            else SOME (hd xs)
        end

(* Cleaner version *)
fun max2(xs: int list) =
    if null xs
    then NONE
    else let
        fun max_nonempty(xs: int list) =
            if null (tl xs)
            then hd xs
            else let val tl_ans = max_nonempty(tl xs)
                in
                    if hd xs > tl_ans
                    then hd xs
                    else tl_ans
                end
        in
            SOME(max_nonempty xs)
        end
