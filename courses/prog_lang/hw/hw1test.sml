(* Homework1 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)
use "hw1.sml";

val test_is_older = is_older((2,3,3),(2,3,4)) = true
val test_is_older_equal = is_older((2,3,4),(2,3,4)) = false
val test_is_older_nope = is_older((4,3,2),(4,3,1)) = false
val test_is_older_nope = is_older((2011, 3, 3), (2011, 2, 2)) = false

val test_number_in_month = number_in_month([(2012,2,28),(2013,12,1)],2) = 1
val test_number_in_month_none = number_in_month([(2012,2,28),(2013,12,1)],3) = 0
val test_number_in_month_empty = number_in_month([],2) = 0

val test_number_in_months = number_in_months([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = 3
val test_number_in_months_none = number_in_months([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[1,5,7]) = 0
val test_number_in_months_empty = number_in_months([],[2,3,4]) = 0

val test_dates_in_month = dates_in_month([(2012,2,28),(2013,12,1)],2) = [(2012,2,28)]
val test_dates_in_month_none = dates_in_month([(2012,2,28),(2013,12,1)],1) = []
val test_dates_in_month_empty = dates_in_month([],2) = []

val test_dates_in_months = dates_in_months([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = [(2012,2,28),(2011,3,31),(2011,4,28)]
val test_dates_in_none = dates_in_months([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[1, 5, 7]) = []
val test_dates_in_empty = dates_in_months([],[2,3,4]) = []

val test_get_nth = get_nth(["hi", "there", "how", "are", "you"], 2) = "there"
val test_get_nth_overflow = get_nth(["hi", "there", "how", "are", "you"], 6) = ""

val test_date_to_string_avg = date_to_string((2013, 6, 1)) = "June 1, 2013"
val test_date_to_string_min = date_to_string((2013, 1, 1)) = "January 1, 2013"
val test_date_to_string_max = date_to_string((2013, 12, 31)) = "December 31, 2013"

val test_number_before_reaching_sum = number_before_reaching_sum(10, [1,2,3,4,5]) = 3
val test_number_before_reaching_sum_first = number_before_reaching_sum(3, [2,2,3,4,5]) = 1
val test_number_before_reaching_sum_none = number_before_reaching_sum(3, [4,2,3,4,5]) = 0

val test_what_month_avg = what_month(70) = 3
val test_what_month_min = what_month(1) = 1
val test_what_month_max = what_month(364) = 12

val test_month_range = month_range(31, 34) = [1,2,2,2]
val test_month_range_one = month_range(34, 34) = [2]
val test_month_range_noop = month_range(35, 34) = []

val test_oldest = oldest([(2012,2,28),(2011,3,31),(2011,4,28)]) = SOME(2011,3,31)
val test_oldest_2 = oldest([(2011,1,1), (2011,1,2)]) = SOME(2011,1,1)
val test_oldest_3 = oldest([(2011,3,3), (2011,2,2), (2012,2,2)]) = SOME(2011,2,2)
val test_oldest_none = oldest([]) = NONE

val test_number_in_months_challenge = number_in_months_challenge([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,2,3,4,2]) = 3
val test_dates_in_months_challenge = dates_in_months_challenge([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4,2,3,3,4]) = [(2012,2,28),(2011,3,31),(2011,4,28)]
