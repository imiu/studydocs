(* return true if first date comes before second, false otherwise *)
fun is_older(date1: (int * int * int), date2: (int * int * int)) =
    if (#1 date1) < (#1 date2)
    then true
    else if (#1 date1) > (#1 date2)
    then false
    else
        if (#2 date1) < (#2 date2)
        then true
        else if (#2 date1) > (#2 date2)
        then false
        else
            if (#3 date1) < (#3 date2)
            then true
            else false

(* count dates with given month *)
fun number_in_month(dates: (int * int * int) list, month: int) =
    if null dates
    then 0
    else
        if (#2 (hd dates)) = month
        then 1 + number_in_month(tl dates, month)
        else number_in_month((tl dates), month)

(* count dates with given list of months *)
fun number_in_months(dates: (int * int * int) list, months: int list) =
    if null months
    then 0
    else
        number_in_month(dates, hd months) + number_in_months(dates, tl months)

(* return list of dates with a given month *)
fun dates_in_month(dates: (int * int * int) list, month: int) =
    if null dates
    then []
    else
        if (#2 (hd dates)) = month
        then (hd dates) :: dates_in_month(tl dates, month)
        else dates_in_month(tl dates, month)

(* return list of dates with a given list of months *)
fun dates_in_months(dates: (int * int * int) list, months: int list) =
    if null months
    then []
    else
        dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

(* return nth element of a string list *)
fun get_nth(strings: string list, n: int) =
    if null strings
    then ""
    else
        if n = 1
        then hd strings
        else
            get_nth(tl strings, n - 1)

(* convert date to representative string *)
fun date_to_string(date: (int * int* int)) =
    let val month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    in
        get_nth(month_names, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
    end

(* return number of elements from the list that sum less than a given number *)
fun number_before_reaching_sum(sum: int, numbers: int list) =
    if (sum - (hd numbers)) <= 0
    then 0
    else 1 + number_before_reaching_sum(sum - (hd numbers), tl numbers)

(* return number of days in a given month *)
fun what_month(day: int) =
    let
        val days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in
        number_before_reaching_sum(day, days_in_months) + 1
    end

(* return array of month numbers for all the dates withing the range *)
fun month_range(day1: int, day2: int) =
    if day1 > day2
    then []
    else what_month(day1) :: month_range(day1 + 1, day2)

(* return the oldest date from a list *)
fun oldest(dates: (int * int * int) list) =
    if null dates
    then NONE
    else let
        fun oldest_nonempty(dates: (int * int * int) list) =
            if null (tl dates)
            then hd dates
            else let val tl_ans = oldest_nonempty(tl dates)
                in
                    if is_older(hd dates, tl_ans)
                    then hd dates
                    else tl_ans
                end
        in
            SOME(oldest_nonempty(dates))
    end

(* return true if x is in a list *)
fun in_a_list(x: int, xs: int list) = 
    if null xs
    then false
    else (hd xs) = x orelse in_a_list(x, tl xs)

(* remove duplicates from a list *)
fun remove_duplicates(xs: int list) =
    if null xs
    then []
    else
        if in_a_list(hd xs, tl xs)
        then remove_duplicates(tl xs)
        else (hd xs) :: remove_duplicates(tl xs)

fun number_in_months_challenge(dates: (int * int * int) list, months: int list) =
    number_in_months(dates, remove_duplicates(months))

fun dates_in_months_challenge(dates: (int * int * int) list, months: int list) =
    dates_in_months(dates, remove_duplicates(months))
