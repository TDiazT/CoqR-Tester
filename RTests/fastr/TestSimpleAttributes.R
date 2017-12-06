x <- as.raw(10) ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  x 
x <- TRUE ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  x 
x <- 1L ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  x 
x <- 1 ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  x 
x <- 1+1i ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  x 
x <- "s" ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  x 
x <- c(1L, 2L) ; "TOKEN" ; attr(x, "hi") <- 2; "TOKEN" ; x 
x <- c(1, 2) ; "TOKEN" ; attr(x, "hi") <- 2; "TOKEN" ; x 
x <- c(1L, 2L) ; "TOKEN" ; attr(x, "hi") <- 2; "TOKEN" ; attr(x, "hello") <- 1:2 ; "TOKEN" ;  x 
x <- c(hello=9) ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  y <- x ; "TOKEN" ; y 
x <- c(hello=1) ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  attr(x,"names") <- "HELLO" ; "TOKEN" ; x 
x <- 1:2; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  x+1:4 
x <- c(1+1i,2+2i); "TOKEN" ;  attr(x, "hi") <- 3 ; "TOKEN" ; y <- 2:3 ; "TOKEN" ; attr(y,"zz") <- 2; "TOKEN" ; x+y 
x <- 1+1i; "TOKEN" ;  attr(x, "hi") <- 1+2 ; "TOKEN" ; y <- 2:3 ; "TOKEN" ; attr(y,"zz") <- 2; "TOKEN" ; x+y 
x <- c(1+1i, 2+2i) ; "TOKEN" ;  attr(x, "hi") <- 3 ; "TOKEN" ; attr(x, "hihi") <- 10 ; "TOKEN" ; y <- c(2+2i, 3+3i) ; "TOKEN" ; attr(y,"zz") <- 2; "TOKEN" ; attr(y,"hi") <-3; "TOKEN" ; attr(y,"bye") <- 4 ; "TOKEN" ; x+y 
x <- 1+1i; "TOKEN" ;  attr(x, "hi") <- 1+2 ; "TOKEN" ; y <- 2:3 ; "TOKEN" ;  x+y 
x <- 1:2; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  x+1 
x <- 1:2; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ; y <- 2:3 ; "TOKEN" ; attr(y,"hello") <- 3; "TOKEN" ; x+y 
x <- 1; "TOKEN" ;  attr(x, "hi") <- 1+2 ; "TOKEN" ; y <- 2:3 ; "TOKEN" ; attr(y, "zz") <- 2; "TOKEN" ; x+y 
x <- 1:2 ; "TOKEN" ;  attr(x, "hi") <- 3 ; "TOKEN" ; attr(x, "hihi") <- 10 ; "TOKEN" ; y <- 2:3 ; "TOKEN" ; attr(y,"zz") <- 2; "TOKEN" ; attr(y,"hi") <-3; "TOKEN" ; attr(y,"bye") <- 4 ; "TOKEN" ; x+y 
x <- c(a=1,b=2) ; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  -x  
x <- 1:2; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  x & x 
x <- as.raw(1:2); "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  x & x 
x <- 1:2 ; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  !x  
x <- c(a=FALSE,b=TRUE) ; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  !x  
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1 ; "TOKEN" ; as.character(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1 ; "TOKEN" ; as.double(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1 ; "TOKEN" ; as.integer(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; x[c(1,1)] 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; x["a"] <- 2 ; "TOKEN" ; x 
x <- c(a=TRUE, b=FALSE) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; x[2] <- 2 ; "TOKEN" ; x 
x <- TRUE ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; x[2] <- 2 ; "TOKEN" ; x 
x <- TRUE ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; x[1] <- 2 ; "TOKEN" ; x 
m <- matrix(rep(1,4), nrow=2) ; "TOKEN" ; attr(m, "a") <- 1 ; "TOKEN" ;  m[2,2] <- 1+1i ; "TOKEN" ; m 
a <- array(c(1,1), dim=c(1,2)) ; "TOKEN" ; attr(a, "a") <- 1 ; "TOKEN" ;  a[1,1] <- 1+1i ; "TOKEN" ; a 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1 ; "TOKEN" ; abs(x) 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; attr(m,"a") <- 1 ; "TOKEN" ;  aperm(m) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1 ; "TOKEN" ; sapply(1:2, function(z) {x}) 
x <- c(a=1) ; "TOKEN" ; attr(x, "myatt") <- 1 ; "TOKEN" ; lapply(1:2, function(z) {x}) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; array(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; matrix(x) 
x <- "a" ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; toupper(x) 
x <- 1 ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; x:x 
x <- 1 ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; c(x, x, x) 
x <- 1 ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; cumsum(c(x, x, x)) 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; attr(m,"a") <- 1 ; "TOKEN" ;  diag(m) <- c(1,1) ; "TOKEN" ; m 
m <- matrix(c(1,1,1,1), nrow=2) ; "TOKEN" ; attr(m,"a") <- 1 ; "TOKEN" ;  eigen(m) 
x <- 1 ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; exp(x) 
x <- 1 ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; min(x) 
x <- c(a=1) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; log10(x) 
x <- c(a=1) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; nchar(x) 
x <- 1 ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; x%o%x 
x <- 1 ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; rep(x,2) 
x <- c(a=TRUE) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; rep(x,2) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; rev(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; seq(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; order(x) 
x <- c(hello=1, hi=9) ; "TOKEN" ; attr(x, "hi") <- 2 ; "TOKEN" ;  sqrt(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; sum(x) 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; attr(m,"a") <- 1 ; "TOKEN" ;  t(m) 
m <- 1:3 ; "TOKEN" ; attr(m,"a") <- 1 ; "TOKEN" ;  t(m) 
m <- matrix(rep(1,4), nrow=2) ; "TOKEN" ; attr(m,"a") <- 1 ; "TOKEN" ;  upper.tri(m) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; unlist(x) 
x <- c(a=1, b=2) ; "TOKEN" ; attr(x, "myatt") <- 1; "TOKEN" ; unlist(list(x,x)) 
x <- 1:2; "TOKEN" ;  attr(x, "hi") <- 2 ; "TOKEN" ;  x == x 
