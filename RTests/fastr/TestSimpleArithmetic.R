1L+1 
1L+1L 
( 1+1)*(3+2) 
1000000000*100000000000 
1000000000L*1000000000L 
1000000000L*1000000000 
1+TRUE 
1L+TRUE 
1+FALSE<=0 
1L+FALSE<=0 
TRUE+TRUE+TRUE*TRUE+FALSE+4 
1L*NA 
1+NA 
2L^10L 
3 %/% 2 
3L %/% 2L 
3L %/% -2L 
3 %/% -2 
3 %/% 0 
3L %/% 0L 
3 %% 2 
3L %% 2L 
3L %% -2L 
3 %% -2 
3 %% 0 
3L %% 0L 
0x10 + 0x10L + 1.28 
(1+2i)*(3+4i) 
x <- 1+2i; "TOKEN" ; y <- 3+4i; "TOKEN" ; x*y 
x <- 1+2i; "TOKEN" ; y <- 3+4i; "TOKEN" ; x/y 
x <- 1+2i; "TOKEN" ; y <- 3+4i; "TOKEN" ; x-y 
x <- 1+2i; "TOKEN" ; y <- 3+4i; "TOKEN" ; x*x*y/(x+y) 
x <- c(-1.5-1i,-1.3-1i) ; "TOKEN" ; y <- c(0+0i, 0+0i) ; "TOKEN" ; y*y+x 
x <- c(-1.5-1i,-1.3-1i) ; "TOKEN" ; y <- c(0+0i, 0+0i) ; "TOKEN" ; y-x 
x <- c(-1-2i,3+10i) ; "TOKEN" ; y <- c(3+1i, -4+5i) ; "TOKEN" ; y-x 
x <- c(-1-2i,3+10i) ; "TOKEN" ; y <- c(3+1i, -4+5i) ; "TOKEN" ; y+x 
x <- c(-1-2i,3+10i) ; "TOKEN" ; y <- c(3+1i, -4+5i) ; "TOKEN" ; y*x 
x <- c(-1-2i,3+10i) ; "TOKEN" ; y <- c(3+1i, -4+5i) ; "TOKEN" ; y/x 
(1+2i)^(3+4i) 
(1+2i)^2 
(1+2i)^(-2) 
(1+2i)^0 
0^(-1+1i) 
(0+0i)/(0+0i) 
(1+0i)/(0+0i) 
(0+1i)/(0+0i) 
(1+1i)/(0+0i) 
(-1+0i)/(0+0i) 
(-1-1i)/(0+0i) 
((0+1i)/0) * ((0+1i)/0) 
((0-1i)/0) * ((0+1i)/0) 
((0-1i)/0) * ((0-1i)/0) 
((0-1i)/0) * ((1-1i)/0) 
((0-1i)/0) * ((-1-1i)/0) 
(1+2i) / ((0-1i)/(0+0i)) 
1/((1+0i)/(0+0i)) 
(1+2i) / ((0-0i)/(0+0i)) 
((1+0i)/(0+0i)) ^ (-3) 
((1+1i)/(0+0i)) ^ (-3) 
((1+1i)/(0+1i)) ^ (-3.54) 
x<-c(1,2,3); "TOKEN" ;x 
x<-c(1,2,3); "TOKEN" ;x*2 
x<-c(1,2,3); "TOKEN" ;x+2 
x<-c(1,2,3); "TOKEN" ;x+FALSE 
x<-c(1,2,3); "TOKEN" ;x+TRUE 
x<-c(1,2,3); "TOKEN" ;x*x+x 
x<-c(1,2); "TOKEN" ;y<-c(3,4,5,6); "TOKEN" ;x+y 
x<-c(1,2); "TOKEN" ;y<-c(3,4,5,6); "TOKEN" ;x*y 
x<-c(1,2); "TOKEN" ;z<-c(); "TOKEN" ;x==z 
x<-1+NA; "TOKEN" ; c(1,2,3,4)+c(x,10) 
c(1L,2L,3L)+TRUE 
c(1L,2L,3L)*c(10L) 
c(1L,2L,3L)*c(10,11,12) 
c(1L,2L,3L,4L)-c(TRUE,FALSE) 
ia<-c(1L,2L); "TOKEN" ;ib<-c(3L,4L); "TOKEN" ;d<-c(5,6); "TOKEN" ;ia+ib+d 
z <- c(-1.5-1i,10) ; "TOKEN" ; (z * z)[1] 
c(1,2,3+1i)^3 
3^c(1,2,3+1i) 
!TRUE 
!FALSE 
!c(TRUE,TRUE,FALSE,NA) 
!c(1,2,3,4,0,0,NA) 
!((0-3):3) 
a <- as.raw(201) ; "TOKEN" ; !a 
a <- as.raw(12) ; "TOKEN" ; !a 
-(0/0) 
-(1/0) 
-(1[2]) 
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) ; "TOKEN" ; m+1L 
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) ; "TOKEN" ; m-1 
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) ; "TOKEN" ; m+m 
z<-matrix(12)+1 ; "TOKEN" ; z 
x <- 1:3 %*% 9:11 ; "TOKEN" ; x[1] 
m<-matrix(1:3, nrow=1) ; "TOKEN" ; 1:2 %*% m 
m<-matrix(1:6, nrow=2) ; "TOKEN" ; 1:2 %*% m 
m<-matrix(1:6, nrow=2) ; "TOKEN" ; m %*% 1:3 
m<-matrix(1:3, ncol=1) ; "TOKEN" ; m %*% 1:2 
a<-matrix(1:6, ncol=2) ; "TOKEN" ; b<-matrix(11:16, nrow=2) ; "TOKEN" ; a %*% b 
a <- array(1:9, dim=c(3,1,3)) ; "TOKEN" ;  a %*% 1:9 
1:3 %o% 1:2 
10 / 1:3 %*% 3:1 
1.1 || 3.15 
0 || 0 
1 || 0 
NA || 1 
NA || 0 
0 || NA 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; NA || f(NA) ; "TOKEN" ; x 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; TRUE || f(FALSE) ; "TOKEN" ; x 
TRUE && FALSE 
FALSE && FALSE 
FALSE && TRUE 
TRUE && TRUE 
TRUE && NA 
FALSE && NA 
NA && TRUE 
NA && FALSE 
NA && NA 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; NA && f(NA) ; "TOKEN" ; x 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; FALSE && f(FALSE) ; "TOKEN" ; x 
1.1 | 3.15 
0 | 0 
1 | 0 
NA | 1 
NA | 0 
0 | NA 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; NA | f(NA) ; "TOKEN" ; x 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; TRUE | f(FALSE) ; "TOKEN" ; x 
TRUE & FALSE 
FALSE & FALSE 
FALSE & TRUE 
TRUE & TRUE 
TRUE & NA 
FALSE & NA 
NA & TRUE 
NA & FALSE 
NA & NA 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; NA & f(NA) ; "TOKEN" ; x 
x <- 1 ; "TOKEN" ; f <- function(r) { x <<- 2; "TOKEN" ; r } ; "TOKEN" ; FALSE & f(FALSE) ; "TOKEN" ; x 
1:4 & c(FALSE,TRUE) 
a <- as.raw(200) ; "TOKEN" ; b <- as.raw(255) ; "TOKEN" ; a | b 
a <- as.raw(200) ; "TOKEN" ; b <- as.raw(1) ; "TOKEN" ; a | b 
a <- as.raw(201) ; "TOKEN" ; b <- as.raw(1) ; "TOKEN" ; a & b 
x <- 2147483647L ; "TOKEN" ; x + 1L 
x <- 2147483647L ; "TOKEN" ; x * x 
x <- -2147483647L ; "TOKEN" ; x - 2L 
x <- -2147483647L ; "TOKEN" ; x - 1L 
3L %/% 0L 
3L %% 0L 
c(3L,3L) %/% 0L 
c(3L,3L) %% 0L 
x <- 3 ; "TOKEN" ; f <- function(z) { if (z) { x <- 1 } ; "TOKEN" ; x <- x + 1L ; "TOKEN" ; x } ; "TOKEN" ; f(FALSE) 
x <- 3 ; "TOKEN" ; f <- function(z) { if (z) { x <- 1 } ; "TOKEN" ; x <- 1L + x ; "TOKEN" ; x } ; "TOKEN" ; f(FALSE) 
x <- 3 ; "TOKEN" ; f <- function(z) { if (z) { x <- 1 } ; "TOKEN" ; x <- x - 1L ; "TOKEN" ; x } ; "TOKEN" ; f(FALSE) 
