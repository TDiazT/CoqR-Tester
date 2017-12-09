a<-1 
a<-FALSE ; b<-a 
x = if (FALSE) 1 
x <<- 1 
x <<- 1 ; x 
f <- function() { x <<- 2 } ; f() ; x 
x <- 10 ; f <- function() { x <<- 2 } ; f() ; x 
x <- 10 ; f <- function() { x <<- 2 ; x } ; c(f(), f()) 
x <- 10 ; f <- function() { x <- x ; x <<- 2 ; x } ; c(f(), f()) 
x <- 10 ; g <- function() { f <- function() { x <- x ; x <<- 2 ; x } ; c(f(), f()) } ; g() 
x <- 10 ; g <- function() { x ; f <- function() { x <- x ; x <<- 2 ; x } ; c(f(), f()) } ; g() 
x <- 10 ; g <- function() { x <- 100 ; f <- function() { x <- x ; x <<- 2 ; x } ; c(f(), f()) } ; g() 
