(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2


(* Problem 1a *)
fun all_except_option(str, strs) =
    case strs of
         [] => NONE
       | x::xs' => if same_string(str, x)
                   then SOME(xs')
                   else case all_except_option(str, xs') of
                             NONE => NONE
                           | SOME lst => SOME (x::lst)


(* Problem 1b *)
fun get_substitutions1(subs, name) =
    case subs of
         [] => []
       | x::xs' => case all_except_option(name, x) of
                        NONE => get_substitutions1(xs', name)
                      | SOME lst => lst @ get_substitutions1(xs', name)


(* Problem 1c *)
fun get_substitutions2(subs, name) =
    let fun aux(subs, name, acc) =
            case subs of
                 [] => acc
               | x::xs' => case all_except_option(name, x) of
                                NONE => aux(xs', name, acc)
                              | SOME lst => aux(xs', name, acc @ lst)
    in
        aux(subs, name, [])
    end


(* Problem 1d *)
fun similar_names(lst, name) =
    let
        val {first=tf, middle=tm, last=tl} = name
        val first_subs = get_substitutions2(lst, tf)
        fun aux(tlst, tname, acc) =
            let val {first=atf, middle=atm, last=atl} = tname
            in
                case tlst of
                    [] => acc
                  | x::xs' => aux(xs', tname, acc @ [{first=x, middle=atm, last=atl}])
            end
    in
        aux(first_subs, name, [name])
    end


(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw

exception IllegalMove

(* Problem 2a *)
fun card_color((suit, rank)) =
    case suit of
         Clubs => Black
       | Spades => Black
       | Diamonds => Red
       | Hearts => Red


(* Problem 2b *)
fun card_value((suit, rank)) =
    case rank of
         Ace => 11
       | Num i => i
       | _ => 10


(* Problem 2c *)
fun remove_card(cs, c, ex) =
    case cs of
         [] => raise ex
       | x::xs' => if c = x
                   then xs'
                   else x :: remove_card(xs', c, ex)


(* Problem 2d *)
fun all_same_color(cs) =
    case cs of
         [] => true
       | x::[] => true
       | x::y::[] => card_color(x) = card_color(y)
       | x::y::xs' => card_color(x) = card_color(y) andalso all_same_color(y::xs')


(* Problem 2e *)
fun sum_cards(cs) =
    let fun aux(cs, acc) =
            case cs of
                 [] => acc
               | x::xs' => aux(xs', acc + card_value(x))
    in
        aux(cs, 0)
    end


(* Problem 2f *)
fun score(cs, goal) =
    let
        val s = sum_cards(cs)
        fun pre_score(sum, goal) =
            if sum > goal
            then 3 * (sum - goal)
            else goal - sum
        val ps = pre_score(s, goal)
    in
        if all_same_color(cs)
        then ps div 2
        else ps
    end


(* Problem 2g *)
fun officiate(cs, ms, goal) =
    let 
        fun move(cs, mvs, hand, goal) =
            if sum_cards(hand) > goal
            then hand
            else case mvs of
                     [] => hand
                   | mv::mvs' =>
                           case mv of 
                                Discard dc => 
                                    move(cs, mvs', remove_card(hand, dc, IllegalMove), goal)
                              | Draw => 
                                    case cs of
                                         [] => hand
                                       | c::cs' =>
                                             move(cs', mvs', c::hand, goal)
    in
        score(move(cs, ms, [], goal), goal)
    end
