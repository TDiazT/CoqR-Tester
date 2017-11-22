"SPECIAL_SUPER_TOKEN"
zero <- function (f) function (x) x
"SPECIAL_SUPER_TOKEN"
succ <- function (n) function (f) function (x) n (f) (f (x))
"SPECIAL_SUPER_TOKEN"
add <- function (n, m) function (f) function (x) n (f) (m (f) (x))
"SPECIAL_SUPER_TOKEN"
mult <- function (n, m) function (f) n (m (f))
"SPECIAL_SUPER_TOKEN"
exp <- function (n, m) m (n)
"SPECIAL_SUPER_TOKEN"
pair <- function (a, b) function (c) c (a) (b)
"SPECIAL_SUPER_TOKEN"
left <- function (a) function (b) a # Also named “K”.
"SPECIAL_SUPER_TOKEN"
right <- function (a) function (b) b # Also named “SKK”.
"SPECIAL_SUPER_TOKEN"
pred <- function (n) n (function (p) pair (p (right), succ (p (right)))) (pair (zero, zero)) (left)
"SPECIAL_SUPER_TOKEN"
sub <- function (n, m) m (pred) (n)
"SPECIAL_SUPER_TOKEN"
isZero <- function (n) n (function (p) right) (left)
"SPECIAL_SUPER_TOKEN"
le <- function (n, m) isZero (sub (m, n))
"SPECIAL_SUPER_TOKEN"
ge <- function (n, m) le (m, n)
"SPECIAL_SUPER_TOKEN"
and <- function (a, b) a (b) (right)
"SPECIAL_SUPER_TOKEN"
eq <- function (n, m) and (le (n, m), ge (n, m))
"SPECIAL_SUPER_TOKEN"
one <- succ (zero)
"SPECIAL_SUPER_TOKEN"
two <- add (one, one)
"SPECIAL_SUPER_TOKEN"
three <- succ (two)
"SPECIAL_SUPER_TOKEN"
four <- add (two, two)
"SPECIAL_SUPER_TOKEN"
five <- add (two, three)
"SPECIAL_SUPER_TOKEN"
six <- mult (three, two)
"SPECIAL_SUPER_TOKEN"
eq (sub (exp (six, two), five), add (exp (five, two), mult (two, three))) (TRUE) (FALSE)
"SPECIAL_SUPER_TOKEN"
