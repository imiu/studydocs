(* Homework2 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)
use "hw2.sml";

val test1a_none = all_except_option("string", ["sting", "ming"]) = NONE
val test1a_one = all_except_option("string", ["string"]) = SOME []
val test1a_first = all_except_option("string",
["string", "some", "value"]) = SOME ["some", "value"]
val test1a_last = all_except_option("string",
["some", "value", "string"]) = SOME ["some", "value"]
val test1a_mid = all_except_option("string",
["some", "string", "value", "string"]) = SOME ["some", "value", "string"]

val test1b = get_substitutions1([["foo"],["there"]], "foo") = []
val test1b_fred = get_substitutions1([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], "Fred") = ["Fredrick","Freddie","F"]
val test1b_jeff = get_substitutions1([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]], "Jeff") = ["Jeffrey","Geoff","Jeffrey"]


val test1c = get_substitutions2([["foo"],["there"]], "foo") = []
val test1c_fred = get_substitutions2([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], "Fred") = ["Fredrick","Freddie","F"]
val test1c_jeff = get_substitutions2([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]], "Jeff") = ["Jeffrey","Geoff","Jeffrey"]

val test1d = similar_names([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], {first="Fred", middle="W", last="Smith"})
           = [{first="Fred", last="Smith", middle="W"}, {first="Fredrick", last="Smith", middle="W"}, {first="Freddie", last="Smith", middle="W"}, {first="F", last="Smith", middle="W"}]

val test2a_black = card_color((Clubs, Num 2)) = Black
val test2a_red = card_color((Diamonds, King)) = Red

val test2b_num = card_value((Clubs, Num 2)) = 2
val test2b_ace = card_value((Clubs, Ace)) = 11
val test2b_king = card_value((Clubs, King)) = 10

val test2c_one = remove_card([(Hearts, Ace)], (Hearts, Ace), IllegalMove) = []
val test2c_first = remove_card([(Hearts, Ace), (Spades, Num 4)], (Hearts, Ace), IllegalMove) = [(Spades, Num 4)]
val test2c_last = remove_card([(Spades, Num 4), (Hearts, Ace)], (Hearts, Ace), IllegalMove) = [(Spades, Num 4)]
val test2c_mid = remove_card([(Spades, Num 4), (Hearts, Ace), (Diamonds, King)], (Hearts, Ace), IllegalMove) = [(Spades, Num 4), (Diamonds, King)]

val test2e_none = all_same_color([]) = true
val test2e_same = all_same_color([(Hearts, Ace), (Hearts, Ace)]) = true
val test2e_diff = all_same_color([(Hearts, Ace), (Spades, King)]) = false
val test2e_more = all_same_color([(Hearts, Ace), (Diamonds, King), (Diamonds, Num 10), (Hearts, King)]) = true

val test2e_num = sum_cards([(Clubs, Num 2),(Clubs, Num 5)]) = 7
val test2e_ace = sum_cards([(Diamonds, Ace),(Spades, King)]) = 21

val test2f_same = score([(Spades, Num 2),(Clubs, Num 4)],10) = 2
val test2f_diff = score([(Hearts, Num 2),(Clubs, Num 4)],10) = 4
val test2f_over = score([(Hearts, King), (Clubs, Ace)], 20) = 3
val test2f_none = score([], 10) = 5 

val test11 = officiate([(Hearts, Num 2),(Clubs, Num 4)],[Draw], 15) = 6

val test12 = officiate([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)],
                       [Draw,Draw,Draw,Draw,Draw],
                       42)
             = 3

val test13 = ((officiate([(Clubs,Jack),(Spades,Num(8))],
                         [Draw,Discard(Hearts,Jack)],
                         42);
               false) 
              handle IllegalMove => true)

