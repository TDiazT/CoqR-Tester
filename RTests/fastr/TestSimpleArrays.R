a = array(); "TOKEN" ; length(a) == 1; "TOKEN" ; 
a = array(); "TOKEN" ; is.na(a[1]); "TOKEN" ; 
a = array(); "TOKEN" ; is.null(dimnames(a)); "TOKEN" ; 
a <- array(); "TOKEN" ; dim(a) == 1; "TOKEN" ; 
a = array(1:10, dim = c(2,6)); "TOKEN" ; length(a) == 12; "TOKEN" ; 
array(dim=c(-2,2)); "TOKEN" ; 
array(dim=c(-2,-2)); "TOKEN" ; 
length(array(dim=c(1,0,2,3))) == 0; "TOKEN" ; 
a = dim(array(dim=c(2.1,2.9,3.1,4.7))); "TOKEN" ; a[1] == 2 && a[2] == 2 && a[3] == 3 && a[4] == 4; "TOKEN" ; 
length(matrix()) == 1; "TOKEN" ; 
a = array(1:27,c(3,3,3)); "TOKEN" ; a[1,1,1] == 1 && a[3,3,3] == 27 && a[1,2,3] == 22 && a[3,2,1] == 6; "TOKEN" ; 
a = array(1:27, c(3,3,3)); "TOKEN" ; b = a[,,]; "TOKEN" ; d = dim(b); "TOKEN" ; d[1] == 3 && d[2] == 3 && d[3] == 3; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a = dim(a[,1,]); "TOKEN" ; length(a) == 2 && a[1] == 3 && a[2] == 3; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; is.null(dim(a[1,1,1])); "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; is.null(dim(a[1,1,])); "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a = dim(a[1,1,1, drop = FALSE]); "TOKEN" ; length(a) == 3 && a[1] == 1 && a[2] == 1 && a[3] == 1; "TOKEN" ; 
m <- array(1:4, dim=c(4,1,1)) ; "TOKEN" ; x <- m[[2,1,1,drop=FALSE]] ; "TOKEN" ; is.null(dim(x)) 
a = array(1:27, c(3,3,3)); "TOKEN" ; a[1] == 1 && a[27] == 27 && a[22] == 22 && a[6] == 6; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a[2,2]; "TOKEN" ; 
m <- array(c(1,2,3), dim=c(3,1,1)) ; "TOKEN" ; x <- m[1:2,1,1] ; "TOKEN" ; x[1] == 1 && x[2] == 2 
m <- array(c(1,2,3), dim=c(3,1,1)) ; "TOKEN" ; x <- dim(m[1:2,1,1]) ; "TOKEN" ; is.null(x) 
m <- array(c(1,2,3), dim=c(3,1,1)) ; "TOKEN" ; x <- dim(m[1:2,1,1,drop=FALSE]) ; "TOKEN" ; x[1] == 2 && x[2] == 1 && x[3] == 1 
m <- array(c(1,2,3), dim=c(3,1,1)) ; "TOKEN" ; x <- m[1:2,1,integer()] ; "TOKEN" ; d <- dim(x) ; "TOKEN" ; length(x) == 0 
m <- array(c(1,2,3), dim=c(3,1,1)) ; "TOKEN" ; x <- m[1:2,1,integer()] ; "TOKEN" ; d <- dim(x) ; "TOKEN" ; d[1] == 2 && d[2] == 0 
array(1,c(3,3,3))[1,1,1] == 1; "TOKEN" ; 
array(1,c(3,3,3))[[1,1,1]] == 1; "TOKEN" ; 
array(1,c(3,3,3))[[,,]]; "TOKEN" ; 
array(1,c(3,3,3))[[c(1,2),1,1]]; "TOKEN" ; 
m <- array(1:24, dim=c(2,3,4)) ; "TOKEN" ; m[,,2] 
m <- array(1:24, dim=c(2,3,4)) ; "TOKEN" ; m[,,2,drop=FALSE] 
m <- array(1:24, dim=c(2,3,4)) ; "TOKEN" ; f <- function(i) { m[,,i] } ; "TOKEN" ; f(1) ; "TOKEN" ; f(2) ; "TOKEN" ; dim(f(1:2)) 
m <- array(1:24, dim=c(2,3,4)) ; "TOKEN" ; f <- function(i) { m[,,i] } ; "TOKEN" ; f(1[2]) ; "TOKEN" ; f(3) 
matrix(1,3,3)[1,1] == 1; "TOKEN" ; 
matrix(1,3,3)[[1,1]] == 1; "TOKEN" ; 
matrix(1,3,3)[[,]]; "TOKEN" ; 
matrix(1,3,3)[[c(1,2),1]]; "TOKEN" ; 
a = matrix(1,2,2); "TOKEN" ; a[1,2] = 3; "TOKEN" ; a[1,2] == 3; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a[1,2,3] = 3; "TOKEN" ; a[1,2,3] == 3; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; (a[1,2,3] = 3) == 3; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; b = a; "TOKEN" ; b[1,2,3] = 3; "TOKEN" ; a[1,2,3] == 1 && b[1,2,3] == 3; "TOKEN" ; 
x <- array(c(1,2,3), dim=c(3,1,1)) ; "TOKEN" ; x[1:2,1,1] <- sqrt(x[2:1]) ; "TOKEN" ; x[1] == sqrt(2) && x[2] == 1 && x[3] == 3 
a = array(TRUE,c(3,3,3)); "TOKEN" ; a[1,2,3] = 8L; "TOKEN" ; a[1,2,3] == 8L; "TOKEN" ; 
a = array(TRUE,c(3,3,3)); "TOKEN" ; a[1,2,3] = 8.1; "TOKEN" ; a[1,2,3] == 8.1; "TOKEN" ; 
a = array(1L,c(3,3,3)); "TOKEN" ; a[1,2,3] = 8.1; "TOKEN" ; a[1,2,3] == 8.1; "TOKEN" ; 
a = array(TRUE,c(3,3,3)); "TOKEN" ; a[1,2,3] = 2+3i; "TOKEN" ; a[1,2,3] == 2+3i; "TOKEN" ; 
a = array(1L,c(3,3,3)); "TOKEN" ; a[1,2,3] = 2+3i; "TOKEN" ; a[1,2,3] == 2+3i; "TOKEN" ; 
a = array(1.3,c(3,3,3)); "TOKEN" ; a[1,2,3] = 2+3i; "TOKEN" ; a[1,2,3] == 2+3i; "TOKEN" ; 
a = array(TRUE,c(3,3,3)); "TOKEN" ; a[1,2,3] = "2+3i"; "TOKEN" ; a[1,2,3] == "2+3i" && a[1,1,1] == "TRUE"; "TOKEN" ; 
a = array(1L,c(3,3,3)); "TOKEN" ; a[1,2,3] = "2+3i"; "TOKEN" ; a[1,2,3] == "2+3i" && a[1,1,1] == "1L"; "TOKEN" ; 
a = array(1.5,c(3,3,3)); "TOKEN" ; a[1,2,3] = "2+3i"; "TOKEN" ; a[1,2,3] == "2+3i" && a[1,1,1] == "1.5"; "TOKEN" ; 
a = array(7L,c(3,3,3)); "TOKEN" ; b = TRUE; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == 1L && a[1,1,1] == 7L; "TOKEN" ; 
a = array(1.7,c(3,3,3)); "TOKEN" ; b = TRUE; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == 1 && a[1,1,1] == 1.7; "TOKEN" ; 
a = array(3+2i,c(3,3,3)); "TOKEN" ; b = TRUE; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == 1 && a[1,1,1] == 3+2i; "TOKEN" ; 
a = array("3+2i",c(3,3,3)); "TOKEN" ; b = TRUE; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == "TRUE" && a[1,1,1] == "3+2i"; "TOKEN" ; 
a = array(1.7,c(3,3,3)); "TOKEN" ; b = 3L; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == 3 && a[1,1,1] == 1.7; "TOKEN" ; 
a = array(3+2i,c(3,3,3)); "TOKEN" ; b = 4L; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == 4 && a[1,1,1] == 3+2i; "TOKEN" ; 
m <- array(c(1+1i,2+2i,3+3i), dim=c(3,1,1)) ; "TOKEN" ; m[1:2,1,1] <- c(100L,101L) ; "TOKEN" ; m ; "TOKEN" ; m[1,1,1] == 100 && m[2,1,1] == 101 
a = array("3+2i",c(3,3,3)); "TOKEN" ; b = 7L; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == "7L" && a[1,1,1] == "3+2i"; "TOKEN" ; 
a = array(3+2i,c(3,3,3)); "TOKEN" ; b = 4.2; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == 4.2 && a[1,1,1] == 3+2i; "TOKEN" ; 
a = array("3+2i",c(3,3,3)); "TOKEN" ; b = 2+3i; "TOKEN" ; a[1,2,3] = b; "TOKEN" ; a[1,2,3] == "2.0+3.0i" && a[1,1,1] == "3+2i"; "TOKEN" ; 
a = matrix(1,3,3); "TOKEN" ; a[1,] = c(3,4,5); "TOKEN" ; a[1,1] == 3 && a[1,2] == 4 && a[1,3] == 5; "TOKEN" ; 
a = matrix(1,3,3); "TOKEN" ; a[,1] = c(3,4,5); "TOKEN" ; a[1,1] == 3 && a[2,1] == 4 && a[3,1] == 5; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a[1,1,] = c(3,4,5); "TOKEN" ; a[1,1,1] == 3 && a[1,1,2] == 4 && a[1,1,3] == 5; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a[1,,1] = c(3,4,5); "TOKEN" ; a[1,1,1] == 3 && a[1,2,1] == 4 && a[1,3,1] == 5; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a[,1,1] = c(3,4,5); "TOKEN" ; a[1,1,1] == 3 && a[2,1,1] == 4 && a[3,1,1] == 5; "TOKEN" ; 
a = array(1,c(3,3,3)); "TOKEN" ; a[1,,] = matrix(1:9,3,3); "TOKEN" ; a[1,1,1] == 1 && a[1,3,1] == 3 && a[1,3,3] == 9; "TOKEN" ; 
m <- array(1:3, dim=c(3,1,1)) ; "TOKEN" ; f <- function(x,v) { x[1:2,1,1] <- v ; "TOKEN" ; x } ; "TOKEN" ; f(m,10L) ; "TOKEN" ; f(m,10) ; "TOKEN" ; f(m,c(11L,12L)); "TOKEN" ; m[1,1,1] == 1L && m[2,1,1] == 2L && m[3,1,1] == 3L 
a = matrix(1,3,3); "TOKEN" ; is.null(dim(a[1,])); "TOKEN" ; 
m <- matrix(1:6, nrow=2, ncol=3, byrow=TRUE) nm 
m <- matrix(1:6, ncol=3, byrow=TRUE) nm 
m <- matrix(1:6, nrow=2, byrow=TRUE) nm 
m <- matrix() nm 
matrix( (1:6) * (1+3i), nrow=2 ) 
matrix( as.raw(101:106), nrow=2 ) 
m <- matrix(c(1,2,3,4,5,6), nrow=3) nm[0] 
m <- matrix(list(1,2,3,4,5,6), nrow=3) nm[0] 
m <- matrix(1:6, nrow=2) nm[upper.tri(m)] 
m <- matrix(list(1,2,3,4,5,6), nrow=3) nm[[2]] <- list(100) nm 
m <- matrix(list(1,2,3,4,5,6), nrow=3) nm[2] <- list(100) nm 
m <- matrix(1:6, nrow=3) nm[2] <- list(100) nm 
m <- matrix(list(1,2,3,4,5,6), nrow=3) nm[c(2,3,4,6)] <- NULL nm 
m <- matrix(1,2,2)nm[1,1] = 6nm 
m <- matrix(1,2,2)nm[,1] = 7nm 
m <- matrix(1,2,2)nm[1,] = 7nm 
m <- matrix(1,2,2)nm[,1] = c(10,11)nm 
m <- matrix(1,2,2)nm[,1] = c(1,2,3,4)nm 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,2] <- 10:11 ; "TOKEN" ; m 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,2:3] <- 10:11 ; "TOKEN" ; m 
m <- array(1:24, dim=c(2,3,4)) ; "TOKEN" ; m[,,4] <- 10:15 ; "TOKEN" ; m[,,4] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,integer()] <- integer() ; "TOKEN" ; m 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,2] <- integer() 
m <- array(1:3, dim=c(3,1,1)) ; "TOKEN" ; f <- function(x,v) { x[[2,1,1]] <- v ; "TOKEN" ; x } ; "TOKEN" ; f(m,10L) ; "TOKEN" ; f(m,10) ; "TOKEN" ; x <- f(m,11L) ; "TOKEN" ; x[1] == 1 && x[2] == 11 && x[3] == 3 
a <- 1:9 ; "TOKEN" ; a[,,1] <- 10L 
a <- 1:9 ; "TOKEN" ; a[,1] <- 10L 
a <- 1:9 ; "TOKEN" ; a[1,1] <- 10L 
a <- 1:9 ; "TOKEN" ; a[1,1,1] <- 10L 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[[1:2,1]] <- 1 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[[integer(),1]] <- 1 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[[1,1]] <- integer() 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[[1:2,1]] <- integer() 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[1,2] <- integer() 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[1,2] <- 1:3 
