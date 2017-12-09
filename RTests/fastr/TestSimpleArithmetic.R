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
x <- 1+2i; y <- 3+4i; x*y 
x <- 1+2i; y <- 3+4i; x/y 
x <- 1+2i; y <- 3+4i; x-y 
x <- 1+2i; y <- 3+4i; x*x*y/(x+y) 
x <- c(-1.5-1i,-1.3-1i) ; y <- c(0+0i, 0+0i) ; y*y+x 
x <- c(-1.5-1i,-1.3-1i) ; y <- c(0+0i, 0+0i) ; y-x 
x <- c(-1-2i,3+10i) ; y <- c(3+1i, -4+5i) ; y-x 
x <- c(-1-2i,3+10i) ; y <- c(3+1i, -4+5i) ; y+x 
x <- c(-1-2i,3+10i) ; y <- c(3+1i, -4+5i) ; y*x 
x <- c(-1-2i,3+10i) ; y <- c(3+1i, -4+5i) ; y/x 
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
x<-c(1,2,3);x 
x<-c(1,2,3);x*2 
x<-c(1,2,3);x+2 
x<-c(1,2,3);x+FALSE 
x<-c(1,2,3);x+TRUE 
x<-c(1,2,3);x*x+x 
x<-c(1,2);y<-c(3,4,5,6);x+y 
x<-c(1,2);y<-c(3,4,5,6);x*y 
x<-c(1,2);z<-c();x==z 
x<-1+NA; c(1,2,3,4)+c(x,10) 
c(1L,2L,3L)+TRUE 
c(1L,2L,3L)*c(10L) 
c(1L,2L,3L)*c(10,11,12) 
c(1L,2L,3L,4L)-c(TRUE,FALSE) 
ia<-c(1L,2L);ib<-c(3L,4L);d<-c(5,6);ia+ib+d 
z <- c(-1.5-1i,10) ; (z * z)[1] 
c(1,2,3+1i)^3 
3^c(1,2,3+1i) 
!TRUE 
!FALSE 
!c(TRUE,TRUE,FALSE,NA) 
!c(1,2,3,4,0,0,NA) 
!((0-3):3) 
a <- as.raw(201) ; !a 
a <- as.raw(12) ; !a 
-(0/0) 
-(1/0) 
-(1[2]) 
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) ; m+1L 
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) ; m-1 
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) ; m+m 
z<-matrix(12)+1 ; z 
x <- 1:3 %*% 9:11 ; x[1] 
m<-matrix(1:3, nrow=1) ; 1:2 %*% m 
m<-matrix(1:6, nrow=2) ; 1:2 %*% m 
m<-matrix(1:6, nrow=2) ; m %*% 1:3 
m<-matrix(1:3, ncol=1) ; m %*% 1:2 
a<-matrix(1:6, ncol=2) ; b<-matrix(11:16, nrow=2) ; a %*% b 
a <- array(1:9, dim=c(3,1,3)) ;  a %*% 1:9 
1:3 %o% 1:2 
10 / 1:3 %*% 3:1 
1.1 || 3.15 
0 || 0 
1 || 0 
NA || 1 
NA || 0 
0 || NA 
x <- 1 ; f <- function(r) { x <<- 2; r } ; NA || f(NA) ; x 
x <- 1 ; f <- function(r) { x <<- 2; r } ; TRUE || f(FALSE) ; x 
TRUE && FALSE 
FALSE && FALSE 
FALSE && TRUE 
TRUE && TRUE 
TRUE && NA 
FALSE && NA 
NA && TRUE 
NA && FALSE 
NA && NA 
x <- 1 ; f <- function(r) { x <<- 2; r } ; NA && f(NA) ; x 
x <- 1 ; f <- function(r) { x <<- 2; r } ; FALSE && f(FALSE) ; x 
1.1 | 3.15 
0 | 0 
1 | 0 
NA | 1 
NA | 0 
0 | NA 
x <- 1 ; f <- function(r) { x <<- 2; r } ; NA | f(NA) ; x 
x <- 1 ; f <- function(r) { x <<- 2; r } ; TRUE | f(FALSE) ; x 
TRUE & FALSE 
FALSE & FALSE 
FALSE & TRUE 
TRUE & TRUE 
TRUE & NA 
FALSE & NA 
NA & TRUE 
NA & FALSE 
NA & NA 
x <- 1 ; f <- function(r) { x <<- 2; r } ; NA & f(NA) ; x 
x <- 1 ; f <- function(r) { x <<- 2; r } ; FALSE & f(FALSE) ; x 
1:4 & c(FALSE,TRUE) 
a <- as.raw(200) ; b <- as.raw(255) ; a | b 
a <- as.raw(200) ; b <- as.raw(1) ; a | b 
a <- as.raw(201) ; b <- as.raw(1) ; a & b 
x <- 2147483647L ; x + 1L 
x <- 2147483647L ; x * x 
x <- -2147483647L ; x - 2L 
x <- -2147483647L ; x - 1L 
3L %/% 0L 
3L %% 0L 
c(3L,3L) %/% 0L 
c(3L,3L) %% 0L 
x <- 3 ; f <- function(z) { if (z) { x <- 1 } ; x <- x + 1L ; x } ; f(FALSE) 
x <- 3 ; f <- function(z) { if (z) { x <- 1 } ; x <- 1L + x ; x } ; f(FALSE) 
x <- 3 ; f <- function(z) { if (z) { x <- 1 } ; x <- x - 1L ; x } ; f(FALSE) 
