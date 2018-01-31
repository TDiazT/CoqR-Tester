x <- as.raw(10) ; attr(x, "hi") <- 2 ;  x 
x <- TRUE ; attr(x, "hi") <- 2 ;  x 
x <- 1L ; attr(x, "hi") <- 2 ;  x 
x <- 1 ; attr(x, "hi") <- 2 ;  x 
x <- 1+1i ; attr(x, "hi") <- 2 ;  x 
x <- "s" ; attr(x, "hi") <- 2 ;  x 
x <- c(1L, 2L) ; attr(x, "hi") <- 2; x 
x <- c(1, 2) ; attr(x, "hi") <- 2; x 
x <- c(1L, 2L) ; attr(x, "hi") <- 2; attr(x, "hello") <- 1:2 ;  x 
x <- c(hello=9) ; attr(x, "hi") <- 2 ;  y <- x ; y 
x <- c(hello=1) ; attr(x, "hi") <- 2 ;  attr(x,"names") <- "HELLO" ; x 
x <- 1:2;  attr(x, "hi") <- 2 ;  x+1:4 
x <- c(1+1i,2+2i);  attr(x, "hi") <- 3 ; y <- 2:3 ; attr(y,"zz") <- 2; x+y 
x <- 1+1i;  attr(x, "hi") <- 1+2 ; y <- 2:3 ; attr(y,"zz") <- 2; x+y 
x <- c(1+1i, 2+2i) ;  attr(x, "hi") <- 3 ; attr(x, "hihi") <- 10 ; y <- c(2+2i, 3+3i) ; attr(y,"zz") <- 2; attr(y,"hi") <-3; attr(y,"bye") <- 4 ; x+y 
x <- 1+1i;  attr(x, "hi") <- 1+2 ; y <- 2:3 ;  x+y 
x <- 1:2;  attr(x, "hi") <- 2 ;  x+1 
x <- 1:2;  attr(x, "hi") <- 2 ; y <- 2:3 ; attr(y,"hello") <- 3; x+y 
x <- 1;  attr(x, "hi") <- 1+2 ; y <- 2:3 ; attr(y, "zz") <- 2; x+y 
x <- 1:2 ;  attr(x, "hi") <- 3 ; attr(x, "hihi") <- 10 ; y <- 2:3 ; attr(y,"zz") <- 2; attr(y,"hi") <-3; attr(y,"bye") <- 4 ; x+y 
x <- c(a=1,b=2) ;  attr(x, "hi") <- 2 ;  -x  
x <- 1:2;  attr(x, "hi") <- 2 ;  x & x 
x <- as.raw(1:2);  attr(x, "hi") <- 2 ;  x & x 
x <- 1:2 ;  attr(x, "hi") <- 2 ;  !x  
x <- c(a=FALSE,b=TRUE) ;  attr(x, "hi") <- 2 ;  !x  
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1 ; as.character(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1 ; as.double(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1 ; as.integer(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; x[c(1,1)] 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; x["a"] <- 2 ; x 
x <- c(a=TRUE, b=FALSE) ; attr(x, "myatt") <- 1; x[2] <- 2 ; x 
x <- TRUE ; attr(x, "myatt") <- 1; x[2] <- 2 ; x 
x <- TRUE ; attr(x, "myatt") <- 1; x[1] <- 2 ; x 
m <- matrix(rep(1,4), nrow=2) ; attr(m, "a") <- 1 ;  m[2,2] <- 1+1i ; m 
a <- array(c(1,1), dim=c(1,2)) ; attr(a, "a") <- 1 ;  a[1,1] <- 1+1i ; a 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1 ; abs(x) 
m <- matrix(1:6, nrow=2) ; attr(m,"a") <- 1 ;  aperm(m) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1 ; sapply(1:2, function(z) {x}) 
x <- c(a=1) ; attr(x, "myatt") <- 1 ; lapply(1:2, function(z) {x}) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; array(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; matrix(x) 
x <- "a" ; attr(x, "myatt") <- 1; toupper(x) 
x <- 1 ; attr(x, "myatt") <- 1; x:x 
x <- 1 ; attr(x, "myatt") <- 1; c(x, x, x) 
x <- 1 ; attr(x, "myatt") <- 1; cumsum(c(x, x, x)) 
m <- matrix(1:6, nrow=2) ; attr(m,"a") <- 1 ;  diag(m) <- c(1,1) ; m 
m <- matrix(c(1,1,1,1), nrow=2) ; attr(m,"a") <- 1 ;  eigen(m) 
x <- 1 ; attr(x, "myatt") <- 1; exp(x) 
x <- 1 ; attr(x, "myatt") <- 1; min(x) 
x <- c(a=1) ; attr(x, "myatt") <- 1; log10(x) 
x <- c(a=1) ; attr(x, "myatt") <- 1; nchar(x) 
x <- 1 ; attr(x, "myatt") <- 1; x%o%x 
x <- 1 ; attr(x, "myatt") <- 1; rep(x,2) 
x <- c(a=TRUE) ; attr(x, "myatt") <- 1; rep(x,2) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; rev(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; seq(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; order(x) 
x <- c(hello=1, hi=9) ; attr(x, "hi") <- 2 ;  sqrt(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; sum(x) 
m <- matrix(1:6, nrow=2) ; attr(m,"a") <- 1 ;  t(m) 
m <- 1:3 ; attr(m,"a") <- 1 ;  t(m) 
m <- matrix(rep(1,4), nrow=2) ; attr(m,"a") <- 1 ;  upper.tri(m) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; unlist(x) 
x <- c(a=1, b=2) ; attr(x, "myatt") <- 1; unlist(list(x,x)) 
x <- 1:2;  attr(x, "hi") <- 2 ;  x == x 
