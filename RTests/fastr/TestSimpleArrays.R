a = array(); length(a) == 1;
a = array(); is.na(a[1]);
a = array(); is.null(dimnames(a));
a <- array(); dim(a) == 1;
a = array(1:10, dim = c(2,6)); length(a) == 12;
array(dim=c(-2,2));
array(dim=c(-2,-2));
length(array(dim=c(1,0,2,3))) == 0;
a = dim(array(dim=c(2.1,2.9,3.1,4.7))); a[1] == 2 && a[2] == 2 && a[3] == 3 && a[4] == 4;
length(matrix()) == 1;
a = array(1:27,c(3,3,3)); a[1,1,1] == 1 && a[3,3,3] == 27 && a[1,2,3] == 22 && a[3,2,1] == 6;
a = array(1:27, c(3,3,3)); b = a[,,]; d = dim(b); d[1] == 3 && d[2] == 3 && d[3] == 3;
a = array(1,c(3,3,3)); a = dim(a[,1,]); length(a) == 2 && a[1] == 3 && a[2] == 3;
a = array(1,c(3,3,3)); is.null(dim(a[1,1,1]));
a = array(1,c(3,3,3)); is.null(dim(a[1,1,]));
a = array(1,c(3,3,3)); a = dim(a[1,1,1, drop = FALSE]); length(a) == 3 && a[1] == 1 && a[2] == 1 && a[3] == 1;
m <- array(1:4, dim=c(4,1,1)) ; x <- m[[2,1,1,drop=FALSE]] ; is.null(dim(x))
a = array(1:27, c(3,3,3)); a[1] == 1 && a[27] == 27 && a[22] == 22 && a[6] == 6;
a = array(1,c(3,3,3)); a[2,2];
m <- array(c(1,2,3), dim=c(3,1,1)) ; x <- m[1:2,1,1] ; x[1] == 1 && x[2] == 2
m <- array(c(1,2,3), dim=c(3,1,1)) ; x <- dim(m[1:2,1,1]) ; is.null(x)
m <- array(c(1,2,3), dim=c(3,1,1)) ; x <- dim(m[1:2,1,1,drop=FALSE]) ; x[1] == 2 && x[2] == 1 && x[3] == 1
m <- array(c(1,2,3), dim=c(3,1,1)) ; x <- m[1:2,1,integer()] ; d <- dim(x) ; length(x) == 0
m <- array(c(1,2,3), dim=c(3,1,1)) ; x <- m[1:2,1,integer()] ; d <- dim(x) ; d[1] == 2 && d[2] == 0
array(1,c(3,3,3))[1,1,1] == 1;
array(1,c(3,3,3))[[1,1,1]] == 1;
array(1,c(3,3,3))[[,,]];
array(1,c(3,3,3))[[c(1,2),1,1]];
m <- array(1:24, dim=c(2,3,4)) ; m[,,2]
m <- array(1:24, dim=c(2,3,4)) ; m[,,2,drop=FALSE]
m <- array(1:24, dim=c(2,3,4)) ; f <- function(i) { m[,,i] } ; f(1) ; f(2) ; dim(f(1:2))
m <- array(1:24, dim=c(2,3,4)) ; f <- function(i) { m[,,i] } ; f(1[2]) ; f(3)
matrix(1,3,3)[1,1] == 1;
matrix(1,3,3)[[1,1]] == 1;
matrix(1,3,3)[[,]];
matrix(1,3,3)[[c(1,2),1]];
a = matrix(1,2,2); a[1,2] = 3; a[1,2] == 3;
a = array(1,c(3,3,3)); a[1,2,3] = 3; a[1,2,3] == 3;
a = array(1,c(3,3,3)); (a[1,2,3] = 3) == 3;
a = array(1,c(3,3,3)); b = a; b[1,2,3] = 3; a[1,2,3] == 1 && b[1,2,3] == 3;
x <- array(c(1,2,3), dim=c(3,1,1)) ; x[1:2,1,1] <- sqrt(x[2:1]) ; x[1] == sqrt(2) && x[2] == 1 && x[3] == 3
a = array(TRUE,c(3,3,3)); a[1,2,3] = 8L; a[1,2,3] == 8L;
a = array(TRUE,c(3,3,3)); a[1,2,3] = 8.1; a[1,2,3] == 8.1;
a = array(1L,c(3,3,3)); a[1,2,3] = 8.1; a[1,2,3] == 8.1;
a = array(TRUE,c(3,3,3)); a[1,2,3] = 2+3i; a[1,2,3] == 2+3i;
a = array(1L,c(3,3,3)); a[1,2,3] = 2+3i; a[1,2,3] == 2+3i;
a = array(1.3,c(3,3,3)); a[1,2,3] = 2+3i; a[1,2,3] == 2+3i;
a = array(TRUE,c(3,3,3)); a[1,2,3] = "2+3i"; a[1,2,3] == "2+3i" && a[1,1,1] == "TRUE";
a = array(1L,c(3,3,3)); a[1,2,3] = "2+3i"; a[1,2,3] == "2+3i" && a[1,1,1] == "1L";
a = array(1.5,c(3,3,3)); a[1,2,3] = "2+3i"; a[1,2,3] == "2+3i" && a[1,1,1] == "1.5";
a = array(7L,c(3,3,3)); b = TRUE; a[1,2,3] = b; a[1,2,3] == 1L && a[1,1,1] == 7L;
a = array(1.7,c(3,3,3)); b = TRUE; a[1,2,3] = b; a[1,2,3] == 1 && a[1,1,1] == 1.7;
a = array(3+2i,c(3,3,3)); b = TRUE; a[1,2,3] = b; a[1,2,3] == 1 && a[1,1,1] == 3+2i;
a = array("3+2i",c(3,3,3)); b = TRUE; a[1,2,3] = b; a[1,2,3] == "TRUE" && a[1,1,1] == "3+2i";
a = array(1.7,c(3,3,3)); b = 3L; a[1,2,3] = b; a[1,2,3] == 3 && a[1,1,1] == 1.7;
a = array(3+2i,c(3,3,3)); b = 4L; a[1,2,3] = b; a[1,2,3] == 4 && a[1,1,1] == 3+2i;
m <- array(c(1+1i,2+2i,3+3i), dim=c(3,1,1)) ; m[1:2,1,1] <- c(100L,101L) ; m ; m[1,1,1] == 100 && m[2,1,1] == 101
a = array("3+2i",c(3,3,3)); b = 7L; a[1,2,3] = b; a[1,2,3] == "7L" && a[1,1,1] == "3+2i";
a = array(3+2i,c(3,3,3)); b = 4.2; a[1,2,3] = b; a[1,2,3] == 4.2 && a[1,1,1] == 3+2i;
a = array("3+2i",c(3,3,3)); b = 2+3i; a[1,2,3] = b; a[1,2,3] == "2.0+3.0i" && a[1,1,1] == "3+2i";
a = matrix(1,3,3); a[1,] = c(3,4,5); a[1,1] == 3 && a[1,2] == 4 && a[1,3] == 5;
a = matrix(1,3,3); a[,1] = c(3,4,5); a[1,1] == 3 && a[2,1] == 4 && a[3,1] == 5;
a = array(1,c(3,3,3)); a[1,1,] = c(3,4,5); a[1,1,1] == 3 && a[1,1,2] == 4 && a[1,1,3] == 5;
a = array(1,c(3,3,3)); a[1,,1] = c(3,4,5); a[1,1,1] == 3 && a[1,2,1] == 4 && a[1,3,1] == 5;
a = array(1,c(3,3,3)); a[,1,1] = c(3,4,5); a[1,1,1] == 3 && a[2,1,1] == 4 && a[3,1,1] == 5;
a = array(1,c(3,3,3)); a[1,,] = matrix(1:9,3,3); a[1,1,1] == 1 && a[1,3,1] == 3 && a[1,3,3] == 9;
m <- array(1:3, dim=c(3,1,1)) ; f <- function(x,v) { x[1:2,1,1] <- v ; x } ; f(m,10L) ; f(m,10) ; f(m,c(11L,12L)); m[1,1,1] == 1L && m[2,1,1] == 2L && m[3,1,1] == 3L
a = matrix(1,3,3); is.null(dim(a[1,]));
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) ; m
m <- matrix(1:6, ncol=3, byrow=TRUE) ; m
m <- matrix(1:6, nrow=2, byrow=TRUE) ; m
m <- matrix() ; m
matrix( (1:6) * (1+3i), nrow=2 )
matrix( as.raw(101:106), nrow=2 )
m <- matrix(c(1,2,3,4,5,6), nrow=3) ; m[0]
m <- matrix(list(1,2,3,4,5,6), nrow=3) ; m[0]
m <- matrix(1:6, nrow=2) ; m[upper.tri(m)]
m <- matrix(list(1,2,3,4,5,6), nrow=3) ; m[[2]] <- list(100) ; m
m <- matrix(list(1,2,3,4,5,6), nrow=3) ; m[2] <- list(100) ; m
m <- matrix(1:6, nrow=3) ; m[2] <- list(100) ; m
m <- matrix(list(1,2,3,4,5,6), nrow=3) ; m[c(2,3,4,6)] <- NULL ; m
m <- matrix(1,2,2); m[1,1] = 6; m
m <- matrix(1,2,2); m[,1] = 7; m
m <- matrix(1,2,2); m[1,] = 7; m
m <- matrix(1,2,2); m[,1] = c(10,11); m
m <- matrix(1,2,2); m[,1] = c(1,2,3,4); m
m <- matrix(1:6, nrow=2) ; m[,2] <- 10:11 ; m
m <- matrix(1:6, nrow=2) ; m[,2:3] <- 10:11 ; m
m <- array(1:24, dim=c(2,3,4)) ; m[,,4] <- 10:15 ; m[,,4]
m <- matrix(1:6, nrow=2) ; m[,integer()] <- integer() ; m 
m <- matrix(1:6, nrow=2) ; m[,2] <- integer()
m <- array(1:3, dim=c(3,1,1)) ; f <- function(x,v) { x[[2,1,1]] <- v ; x } ; f(m,10L) ; f(m,10) ; x <- f(m,11L) ; x[1] == 1 && x[2] == 11 && x[3] == 3
a <- 1:9 ; a[,,1] <- 10L
a <- 1:9 ; a[,1] <- 10L
a <- 1:9 ; a[1,1] <- 10L
a <- 1:9 ; a[1,1,1] <- 10L
m <- matrix(1:6, nrow=2) ; m[[1:2,1]] <- 1
m <- matrix(1:6, nrow=2) ; m[[integer(),1]] <- 1
m <- matrix(1:6, nrow=2) ; m[[1,1]] <- integer()
m <- matrix(1:6, nrow=2) ; m[[1:2,1]] <- integer()
m <- matrix(1:6, nrow=2) ; m[1,2] <- integer()
m <- matrix(1:6, nrow=2) ; m[1,2] <- 1:3
