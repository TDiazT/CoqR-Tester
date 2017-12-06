a<-1 
a<-FALSE ; "TOKEN" ; b<-a 
x = if (FALSE) 1 
x <<- 1 
x <<- 1 ; "TOKEN" ; x 
f <- function() { x <<- 2 } ; "TOKEN" ; f() ; "TOKEN" ; x 
x <- 10 ; "TOKEN" ; f <- function() { x <<- 2 } ; "TOKEN" ; f() ; "TOKEN" ; x 
x <- 10 ; "TOKEN" ; f <- function() { x <<- 2 ; "TOKEN" ; x } ; "TOKEN" ; c(f(), f()) 
x <- 10 ; "TOKEN" ; f <- function() { x <- x ; "TOKEN" ; x <<- 2 ; "TOKEN" ; x } ; "TOKEN" ; c(f(), f()) 
x <- 10 ; "TOKEN" ; g <- function() { f <- function() { x <- x ; "TOKEN" ; x <<- 2 ; "TOKEN" ; x } ; "TOKEN" ; c(f(), f()) } ; "TOKEN" ; g() 
x <- 10 ; "TOKEN" ; g <- function() { x ; "TOKEN" ; f <- function() { x <- x ; "TOKEN" ; x <<- 2 ; "TOKEN" ; x } ; "TOKEN" ; c(f(), f()) } ; "TOKEN" ; g() 
x <- 10 ; "TOKEN" ; g <- function() { x <- 100 ; "TOKEN" ; f <- function() { x <- x ; "TOKEN" ; x <<- 2 ; "TOKEN" ; x } ; "TOKEN" ; c(f(), f()) } ; "TOKEN" ; g() 
