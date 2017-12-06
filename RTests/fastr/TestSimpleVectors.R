x<-1:10; "TOKEN" ; x[3] 
x<-1:10; "TOKEN" ; x[3L] 
x<-c(1,2,3); "TOKEN" ; x[3] 
x<-c(1,2,3); "TOKEN" ; x[3L] 
x<-1:3; "TOKEN" ; x[0-2] 
x<-1:3; "TOKEN" ; x[FALSE] 
x<-1:3; "TOKEN" ; x[TRUE] 
x<-c(TRUE,TRUE,FALSE); "TOKEN" ; x[0-2] 
x<-c(1,2); "TOKEN" ;x[[0-1]] 
x<-c(1,2); "TOKEN" ;x[0-3] 
x<-10; "TOKEN" ; x[0-1] 
x<-10; "TOKEN" ; x[NA] 
x <- c(a=1, b=2, c=3) ; "TOKEN" ; x[2] 
x <- c(a=1, b=2, c=3) ; "TOKEN" ; x[[2]] 
x <- c(a="A", b="B", c="C") ; "TOKEN" ; x[-2] 
x <- c(a=1+2i, b=2+3i, c=3) ; "TOKEN" ; x[-2] 
x <- c(a=1, b=2, c=3) ; "TOKEN" ; x[-2] 
x <- c(a=1L, b=2L, c=3L) ; "TOKEN" ; x[-2] 
x <- c(a=TRUE, b=FALSE, c=NA) ; "TOKEN" ; x[-2] 
x <- c(a=as.raw(10), b=as.raw(11), c=as.raw(12)) ; "TOKEN" ; x[-2] 
x <- c(a=1L, b=2L, c=3L) ; "TOKEN" ; x[0] 
x <- c(a=1L, b=2L, c=3L) ; "TOKEN" ; x[10] 
x <- c(a=TRUE, b=FALSE, c=NA) ; "TOKEN" ; x[0] 
x <- c(TRUE, FALSE, NA) ; "TOKEN" ; x[0] 
x <- list(1L, 2L, 3L) ; "TOKEN" ; x[10] 
x <- list(a=1L, b=2L, c=3L) ; "TOKEN" ; x[0] 
x <- c(a="A", b="B", c="C") ; "TOKEN" ; x[10] 
x <- c(a="A", b="B", c="C") ; "TOKEN" ; x[0] 
x <- c(a=1+1i, b=2+2i, c=3+3i) ; "TOKEN" ; x[10] 
x <- c(a=1+1i, b=2+2i, c=3+3i) ; "TOKEN" ; x[0] 
x <- c(a=as.raw(10), b=as.raw(11), c=as.raw(12)) ; "TOKEN" ; x[10] 
x <- c(a=as.raw(10), b=as.raw(11), c=as.raw(12)) ; "TOKEN" ; x[0] 
x <- c(a=1, b=2, c=3) ; "TOKEN" ; x[10] 
x <- c(a=1, b=2, c=3) ; "TOKEN" ; x[0] 
x <- c(a=1,b=2,c=3,d=4) ; "TOKEN" ; x["b"] 
x <- c(a=1,b=2,c=3,d=4) ; "TOKEN" ; x["d"] 
x <- 1 ; "TOKEN" ; attr(x, "hi") <- 2; "TOKEN" ; x[2] <- 2; "TOKEN" ; attr(x, "hi") 
x<-1:5 ; "TOKEN" ; x[3:4] 
x<-1:5 ; "TOKEN" ; x[4:3] 
x<-c(1,2,3,4,5) ; "TOKEN" ; x[4:3] 
(1:5)[3:4] 
x<-(1:5)[2:4] ; "TOKEN" ; x[2:1] 
x<-1:5; "TOKEN" ;x[c(0-2,0-3)] 
x<-1:5; "TOKEN" ;x[c(0-2,0-3,0,0,0)] 
x<-1:5; "TOKEN" ;x[c(2,5,4,3,3,3,0)] 
x<-1:5; "TOKEN" ;x[c(2L,5L,4L,3L,3L,3L,0L)] 
f<-function(x, i) { x[i] } ; "TOKEN" ; f(1:3,3:1) ; "TOKEN" ; f(1:5,c(0,0,0,0-2)) 
f<-function(x, i) { x[i] } ; "TOKEN" ; f(1:3,0-3) ; "TOKEN" ; f(1:5,c(0,0,0,0-2)) 
f<-function(x, i) { x[i] } ; "TOKEN" ; f(1:3,0L-3L) ; "TOKEN" ; f(1:5,c(0,0,0,0-2)) 
x<-1:5 ; "TOKEN" ; x[c(TRUE,FALSE)] 
x<-1:5 ; "TOKEN" ; x[c(TRUE,TRUE,TRUE,NA)] 
x<-1:5 ; "TOKEN" ; x[c(TRUE,TRUE,TRUE,FALSE,FALSE,FALSE,FALSE,TRUE,NA)] 
f<-function(i) { x<-1:5 ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1) ; "TOKEN" ; f(1L) ; "TOKEN" ; f(TRUE) 
f<-function(i) { x<-1:5 ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1) ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(1L)  
f<-function(i) { x<-1:5 ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1) ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(c(3,2))  
f<-function(i) { x<-1:5 ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1)  ; "TOKEN" ; f(3:4) 
f<-function(i) { x<-1:5 ; "TOKEN" ; x[i] } ; "TOKEN" ; f(c(TRUE,FALSE))  ; "TOKEN" ; f(3:4) 
x<-as.complex(c(1,2,3,4)) ; "TOKEN" ; x[2:4] 
x<-as.raw(c(1,2,3,4)) ; "TOKEN" ; x[2:4] 
x<-c(1,2,3,4) ; "TOKEN" ; names(x) <- c("a","b","c","d") ; "TOKEN" ; x[c(10,2,3,0)] 
x<-c(1,2,3,4) ; "TOKEN" ; names(x) <- c("a","b","c","d") ; "TOKEN" ; x[c(10,2,3)] 
x<-c(1,2,3,4) ; "TOKEN" ; names(x) <- c("a","b","c","d") ; "TOKEN" ; x[c(-2,-4,0)] 
x<-c(1,2) ; "TOKEN" ; names(x) <- c("a","b") ; "TOKEN" ; x[c(FALSE,TRUE,NA,FALSE)] 
x<-c(1,2) ; "TOKEN" ; names(x) <- c("a","b") ; "TOKEN" ; x[c(FALSE,TRUE)] 
x <- c(a=1,b=2,c=3,d=4) ; "TOKEN" ; x[character()] 
x <- c(a=1,b=2,c=3,d=4) ; "TOKEN" ; x[c("b","b","d","a","a")] 
x <- c(a=as.raw(10),b=as.raw(11),c=as.raw(12),d=as.raw(13)) ; "TOKEN" ; f <- function(s) { x[s] } ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(1L) ; "TOKEN" ; f(as.character(NA)) 
x <- c(a=1,b=2,c=3,d=4) ; "TOKEN" ; f <- function(s) { x[s] } ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(1L) ; "TOKEN" ; f("b") 
x <- c(a=as.raw(10),b=as.raw(11),c=as.raw(12),d=as.raw(13)) ; "TOKEN" ; f <- function(s) { x[c(s,s)] } ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(1L) ; "TOKEN" ; f(as.character(NA)) 
x <- c(a=1,b=2,c=3,d=4) ; "TOKEN" ; f <- function(s) { x[c(s,s)] } ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(1L) ; "TOKEN" ; f("b") 
x<-1:3; "TOKEN" ; x[1]<-100L; "TOKEN" ; x 
x<-c(1,2,3); "TOKEN" ; x[2L]<-100L; "TOKEN" ; x 
x<-c(1,2,3); "TOKEN" ; x[2L]<-100; "TOKEN" ; x 
x<-c(1,2,3); "TOKEN" ; x[2]<-FALSE; "TOKEN" ; x 
x<-1:5; "TOKEN" ; x[2]<-1000; "TOKEN" ; x[3] <- TRUE; "TOKEN" ; x[8]<-3L; "TOKEN" ; x 
x<-5:1; "TOKEN" ; x[0-2]<-1000; "TOKEN" ; x 
x<-c(); "TOKEN" ; x[[TRUE]] <- 2; "TOKEN" ; x 
x<-1:2; "TOKEN" ; x[[0-2]]<-100; "TOKEN" ; x 
f<-function(x,i,v) { x<-1:5; "TOKEN" ; x[i]<-v; "TOKEN" ; x} ; "TOKEN" ; f(c(1L,2L),1,3L) ; "TOKEN" ; f(c(1L,2L),2,3) 
f<-function(x,i,v) { x<-1:5; "TOKEN" ; x[i]<-v; "TOKEN" ; x} ; "TOKEN" ; f(c(1L,2L),1,3L) ; "TOKEN" ; f(c(1L,2L),8,3L) 
f<-function(x,i,v) { x<-1:5; "TOKEN" ; x[i]<-v; "TOKEN" ; x} ; "TOKEN" ; f(c(1L,2L),1,FALSE) ; "TOKEN" ; f(c(1L,2L),2,3) 
f<-function(x,i,v) { x<-1:5; "TOKEN" ; x[i]<-v; "TOKEN" ; x} ; "TOKEN" ; f(c(1L,2L),1,FALSE) ; "TOKEN" ; f(c(1L,2L),8,TRUE) 
a <- c(1L,2L,3L); "TOKEN" ; a <- 1:5; "TOKEN" ; a[3] <- TRUE; "TOKEN" ; a 
x <- 1:3 ; "TOKEN" ; x[2] <- "hi"; "TOKEN" ; x 
x <- c(1,2,3) ; "TOKEN" ; x[2] <- "hi"; "TOKEN" ; x 
x <- c(TRUE,FALSE,FALSE) ; "TOKEN" ; x[2] <- "hi"; "TOKEN" ; x 
x <- c(2,3,4) ; "TOKEN" ; x[1] <- 3+4i ; "TOKEN" ; x  
a <- c(1,2,3) ; "TOKEN" ; b <- a; "TOKEN" ; a[1] <- 4L; "TOKEN" ; a 
a <- c(1,2,3) ; "TOKEN" ; b <- a; "TOKEN" ; a[2] <- 4L; "TOKEN" ; a 
a <- c(1,2,3) ; "TOKEN" ; b <- a; "TOKEN" ; a[3] <- 4L; "TOKEN" ; a 
a <- c(2.1,2.2,2.3); "TOKEN" ; b <- a; "TOKEN" ; a[[1]] <- TRUE; "TOKEN" ; a 
a <- c(2.1,2.2,2.3); "TOKEN" ; b <- a; "TOKEN" ; a[[2]] <- TRUE; "TOKEN" ; a 
a <- c(2.1,2.2,2.3); "TOKEN" ; b <- a; "TOKEN" ; a[[3]] <- TRUE; "TOKEN" ; a 
a <- c(TRUE,TRUE,TRUE); "TOKEN" ; b <- a; "TOKEN" ; a[[1]] <- FALSE; "TOKEN" ; a 
a <- c(TRUE,TRUE,TRUE); "TOKEN" ; b <- a; "TOKEN" ; a[[2]] <- FALSE; "TOKEN" ; a 
a <- c(TRUE,TRUE,TRUE); "TOKEN" ; b <- a; "TOKEN" ; a[[3]] <- FALSE; "TOKEN" ; a 
x<-c(1,2,3,4,5); "TOKEN" ; x[3:4]<-c(300L,400L); "TOKEN" ; x 
x<-c(1,2,3,4,5); "TOKEN" ; x[4:3]<-c(300L,400L); "TOKEN" ; x 
x<-1:5; "TOKEN" ; x[4:3]<-c(300L,400L); "TOKEN" ; x 
x<-5:1; "TOKEN" ; x[3:4]<-c(300L,400L); "TOKEN" ; x 
x<-5:1; "TOKEN" ; x[3:4]<-c(300,400); "TOKEN" ; x 
x<-1:5; "TOKEN" ; x[c(0-2,0-3,0-3,0-100,0)]<-256; "TOKEN" ; x 
x<-1:5; "TOKEN" ; x[c(4,2,3)]<-c(256L,257L,258L); "TOKEN" ; x 
x<-c(1,2,3,4,5); "TOKEN" ; x[c(TRUE,FALSE)] <- 1000; "TOKEN" ; x 
x<-c(1,2,3,4,5,6); "TOKEN" ; x[c(TRUE,TRUE,FALSE)] <- c(1000L,2000L) ; "TOKEN" ; x 
x<-c(1,2,3,4,5); "TOKEN" ; x[c(TRUE,FALSE,TRUE,TRUE,FALSE)] <- c(1000,2000,3000); "TOKEN" ; x 
x<-c(1,2,3,4,5); "TOKEN" ; x[c(TRUE,FALSE,TRUE,TRUE,0)] <- c(1000,2000,3000); "TOKEN" ; x 
x<-1:3; "TOKEN" ; x[c(TRUE, FALSE, TRUE)] <- c(TRUE,FALSE); "TOKEN" ; x 
x<-c(TRUE,TRUE,FALSE); "TOKEN" ; x[c(TRUE, FALSE, TRUE)] <- c(FALSE,TRUE); "TOKEN" ; x 
x<-c(TRUE,TRUE,FALSE); "TOKEN" ; x[c(TRUE, FALSE, TRUE)] <- c(1000,2000); "TOKEN" ; x 
x<-11:9 ; "TOKEN" ; x[c(TRUE, FALSE, TRUE)] <- c(1000,2000); "TOKEN" ; x 
l <- double() ; "TOKEN" ; l[c(TRUE,TRUE)] <-2 ; "TOKEN" ; l
l <- double() ; "TOKEN" ; l[c(FALSE,TRUE)] <-2 ; "TOKEN" ; l
a<- c('a','b','c','d'); "TOKEN" ; a[3:4] <- c(4,5); "TOKEN" ; a
a<- c('a','b','c','d'); "TOKEN" ; a[3:4] <- c(4L,5L); "TOKEN" ; a
a<- c('a','b','c','d'); "TOKEN" ; a[3:4] <- c(TRUE,FALSE); "TOKEN" ; a
f<-function(i,v) { x<-1:5 ; "TOKEN" ; x[i]<-v ; "TOKEN" ; x } ; "TOKEN" ; f(1,1) ; "TOKEN" ; f(1L,TRUE) ; "TOKEN" ; f(2,TRUE) 
f<-function(i,v) { x<-1:5 ; "TOKEN" ; x[[i]]<-v ; "TOKEN" ; x } ; "TOKEN" ; f(1,1) ; "TOKEN" ; f(1L,TRUE) ; "TOKEN" ; f(2,TRUE) 
f<-function(i,v) { x<-1:5 ; "TOKEN" ; x[i]<-v ; "TOKEN" ; x } ; "TOKEN" ; f(3:2,1) ; "TOKEN" ; f(1L,TRUE) ; "TOKEN" ; f(2:4,4:2) 
f<-function(i,v) { x<-1:5 ; "TOKEN" ; x[i]<-v ; "TOKEN" ; x } ; "TOKEN" ; f(c(3,2),1) ; "TOKEN" ; f(1L,TRUE) ; "TOKEN" ; f(2:4,c(4,3,2)) 
f<-function(b,i,v) { b[i]<-v ; "TOKEN" ; b } ; "TOKEN" ; f(1:4,4:1,TRUE) ; "TOKEN" ; f(c(3,2,1),8,10) 
f<-function(b,i,v) { b[i]<-v ; "TOKEN" ; b } ; "TOKEN" ; f(1:4,4:1,TRUE) ; "TOKEN" ; f(c(3,2,1),8,10) ; "TOKEN" ; f(c(TRUE,FALSE),TRUE,FALSE) 
x<-c(TRUE,TRUE,FALSE,TRUE) ; "TOKEN" ; x[3:2] <- TRUE; "TOKEN" ; x 
x<-1:3 ; "TOKEN" ; y<-(x[2]<-100) ; "TOKEN" ; y 
x<-1:5 ; "TOKEN" ; x[x[4]<-2] <- (x[4]<-100) ; "TOKEN" ; x 
x<-1:5 ; "TOKEN" ; x[3] <- (x[4]<-100) ; "TOKEN" ; x 
x<-5:1 ; "TOKEN" ; x[x[2]<-2] 
x<-5:1 ; "TOKEN" ; x[x[2]<-2] <- (x[3]<-50) ; "TOKEN" ; x 
v<-1:3 ; "TOKEN" ; v[TRUE] <- 100 ; "TOKEN" ; v 
v<-1:3 ; "TOKEN" ; v[-1] <- c(100,101) ; "TOKEN" ; v 
v<-1:3 ; "TOKEN" ; v[TRUE] <- c(100,101,102) ; "TOKEN" ; v 
x <- c(a=1,b=2,c=3) ; "TOKEN" ; x[2]<-10; "TOKEN" ; x 
x <- c(a=1,b=2,c=3) ; "TOKEN" ; x[2:3]<-10; "TOKEN" ; x 
x <- c(a=1,b=2,c=3) ; "TOKEN" ; x[c(2,3)]<-10; "TOKEN" ; x 
x <- c(a=1,b=2,c=3) ; "TOKEN" ; x[c(TRUE,TRUE,FALSE)]<-10; "TOKEN" ; x 
x <- c(a=1,b=2) ; "TOKEN" ; x[2:3]<-10; "TOKEN" ; x 
x <- c(a=1,b=2) ; "TOKEN" ; x[c(2,3)]<-10; "TOKEN" ; x 
x <- c(a=1,b=2) ; "TOKEN" ; x[3]<-10; "TOKEN" ; x 
x <- matrix(1:2) ; "TOKEN" ; x[c(FALSE,FALSE,TRUE)]<-10; "TOKEN" ; x 
x <- 1:2 ; "TOKEN" ; x[c(FALSE,FALSE,TRUE)]<-10; "TOKEN" ; x 
x <- c(a=1,b=2) ; "TOKEN" ; x[c(FALSE,FALSE,TRUE)]<-10; "TOKEN" ; x 
x<-c(a=1,b=2,c=3) ; "TOKEN" ; x[["b"]]<-200; "TOKEN" ; x 
x<-c(a=1,b=2,c=3) ; "TOKEN" ; x[["d"]]<-200; "TOKEN" ; x 
x<-c() ; "TOKEN" ; x[c("a","b","c","d")]<-c(1,2); "TOKEN" ; x 
x<-c(a=1,b=2,c=3) ; "TOKEN" ; x["d"]<-4 ; "TOKEN" ; x 
x<-c(a=1,b=2,c=3) ; "TOKEN" ; x[c("d","e")]<-c(4,5) ; "TOKEN" ; x 
x<-c(a=1,b=2,c=3) ; "TOKEN" ; x[c("d","a","d","a")]<-c(4,5) ; "TOKEN" ; x 
a = c(1, 2); "TOKEN" ; a[['a']] = 67; "TOKEN" ; a; "TOKEN" ; 
a = c(a=1,2,3); "TOKEN" ; a[['x']] = 67; "TOKEN" ; a; "TOKEN" ; 
x <- c(TRUE,TRUE,TRUE,TRUE); "TOKEN" ; x[2:3] <- c(FALSE,FALSE); "TOKEN" ; x 
x <- c(TRUE,TRUE,TRUE,TRUE); "TOKEN" ; x[3:2] <- c(FALSE,TRUE); "TOKEN" ; x 
x <- c('a','b','c','d'); "TOKEN" ; x[2:3] <- 'x'; "TOKEN" ; x
x <- c('a','b','c','d'); "TOKEN" ; x[2:3] <- c('x','y'); "TOKEN" ; x
x <- c('a','b','c','d'); "TOKEN" ; x[3:2] <- c('x','y'); "TOKEN" ; x
x <- c('a','b','c','d'); "TOKEN" ; x[c(TRUE,FALSE,TRUE)] <- c('x','y','z'); "TOKEN" ; x 
x <- c(TRUE,TRUE,TRUE,TRUE); "TOKEN" ; x[c(TRUE,TRUE,FALSE)] <- c(10L,20L,30L); "TOKEN" ; x 
x <- c(1L,1L,1L,1L); "TOKEN" ; x[c(TRUE,TRUE,FALSE)] <- c('a','b','c'); "TOKEN" ; x
x <- c(TRUE,TRUE,TRUE,TRUE); "TOKEN" ; x[c(TRUE,TRUE,FALSE)] <- list(10L,20L,30L); "TOKEN" ; x 
x <- c(); "TOKEN" ; x[c('a','b')] <- c(1L,2L); "TOKEN" ; x 
x <- c(); "TOKEN" ; x[c('a','b')] <- c(TRUE,FALSE); "TOKEN" ; x 
x <- c(); "TOKEN" ; x[c('a','b')] <- c('a','b'); "TOKEN" ; x 
x <- list(); "TOKEN" ; x[c('a','b')] <- c('a','b'); "TOKEN" ; x 
x <- list(); "TOKEN" ; x[c('a','b')] <- list('a','b'); "TOKEN" ; x 
x = c(1,2,3,4); "TOKEN" ; x[x %% 2 == 0] <- c(1,2,3,4); "TOKEN" ; 
x <- 1:3 ; "TOKEN" ; x[c(-2, 1)] <- 10 
list(1:4) 
list(1,list(2,list(3,4))) 
list(1,b=list(2,3)) 
list(1,b=list(c=2,3)) 
list(list(c=2)) 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[[2]] 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[c(FALSE,FALSE,TRUE)] 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[FALSE] 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[-2] 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[NA] 
l<-list(1,2,3) ; "TOKEN" ; l[c(1,2)] 
l<-list(1,2,3) ; "TOKEN" ; l[c(2)] 
x<-list(1,2L,TRUE,FALSE,5) ; "TOKEN" ; x[2:4] 
x<-list(1,2L,TRUE,FALSE,5) ; "TOKEN" ; x[4:2] 
x<-list(1,2L,TRUE,FALSE,5) ; "TOKEN" ; x[c(-2,-3)] 
x<-list(1,2L,TRUE,FALSE,5) ; "TOKEN" ; x[c(-2,-3,-4,0,0,0)] 
x<-list(1,2L,TRUE,FALSE,5) ; "TOKEN" ; x[c(2,5,4,3,3,3,0)] 
x<-list(1,2L,TRUE,FALSE,5) ; "TOKEN" ; x[c(2L,5L,4L,3L,3L,3L,0L)] 
m<-list(1,2) ; "TOKEN" ; m[NULL] 
f<-function(x, i) { x[i] } ; "TOKEN" ; f(list(1,2,3),3:1) ; "TOKEN" ; f(list(1L,2L,3L,4L,5L),c(0,0,0,0-2)) 
x<-list(1,2,3,4,5) ; "TOKEN" ; x[c(TRUE,TRUE,TRUE,FALSE,FALSE,FALSE,FALSE,TRUE,NA)] 
f<-function(i) { x<-list(1,2,3,4,5) ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1) ; "TOKEN" ; f(1L) ; "TOKEN" ; f(TRUE) 
f<-function(i) { x<-list(1,2,3,4,5) ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1) ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(1L)  
f<-function(i) { x<-list(1L,2L,3L,4L,5L) ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1) ; "TOKEN" ; f(TRUE) ; "TOKEN" ; f(c(3,2))  
f<-function(i) { x<-list(1,2,3,4,5) ; "TOKEN" ; x[i] } ; "TOKEN" ; f(1)  ; "TOKEN" ; f(3:4) 
f<-function(i) { x<-list(1,2,3,4,5) ; "TOKEN" ; x[i] } ; "TOKEN" ; f(c(TRUE,FALSE))  ; "TOKEN" ; f(3:4) 
l<-(list(list(1,2),list(3,4))); "TOKEN" ; l[[c(1,2)]] 
l<-(list(list(1,2),list(3,4))); "TOKEN" ; l[[c(1,-2)]] 
l<-(list(list(1,2),list(3,4))); "TOKEN" ; l[[c(1,-1)]] 
l<-(list(list(1,2),list(3,4))); "TOKEN" ; l[[c(1,TRUE)]] 
l<-(list(list(1,2),c(3,4))); "TOKEN" ; l[[c(2,1)]] 
l <- list(a=1,b=2,c=list(d=3,e=list(f=4))) ; "TOKEN" ; l[[c(3,2)]] 
l <- list(a=1,b=2,c=list(d=3,e=list(f=4))) ; "TOKEN" ; l[[c(3,1)]] 
l <- list(c=list(d=3,e=c(f=4)), b=2, a=3) ; "TOKEN" ; l[[c("c","e")]] 
l <- list(c=list(d=3,e=c(f=4)), b=2, a=3) ; "TOKEN" ; l[[c("c","e", "f")]] 
l <- list(c=list(d=3,e=c(f=4)), b=2, a=3) ; "TOKEN" ; l[[c("c")]] 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[[2]]<-100 ; "TOKEN" ; l 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[[5]]<-100 ; "TOKEN" ; l 
l<-list(1,2L,TRUE) ; "TOKEN" ; l[[3]]<-list(100) ; "TOKEN" ; l 
v<-1:3 ; "TOKEN" ; v[2] <- list(100) ; "TOKEN" ; v 
v<-1:3 ; "TOKEN" ; v[[2]] <- list(100) ; "TOKEN" ; v 
l <- list() ; "TOKEN" ; l[[1]] <-2 ; "TOKEN" ; l
l<-list() ; "TOKEN" ; x <- 1:3 ; "TOKEN" ; l[[1]] <- x  ; "TOKEN" ; l 
l <- list(1,2,3) ; "TOKEN" ; l[2] <- list(100) ; "TOKEN" ; l[2] 
l <- list(1,2,3) ; "TOKEN" ; l[[2]] <- list(100) ; "TOKEN" ; l[2] 
m<-list(1,2) ; "TOKEN" ; m[TRUE] <- NULL ; "TOKEN" ; m 
m<-list(1,2) ; "TOKEN" ; m[[TRUE]] <- NULL ; "TOKEN" ; m 
m<-list(1,2) ; "TOKEN" ; m[[1]] <- NULL ; "TOKEN" ; m 
m<-list(1,2) ; "TOKEN" ; m[[-1]] <- NULL ; "TOKEN" ; m 
m<-list(1,2) ; "TOKEN" ; m[[-2]] <- NULL ; "TOKEN" ; m 
l <- matrix(list(1,2)) ; "TOKEN" ; l[3] <- NULL ; "TOKEN" ; l 
l <- matrix(list(1,2)) ; "TOKEN" ; l[[3]] <- NULL ; "TOKEN" ; l 
l <- matrix(list(1,2)) ; "TOKEN" ; l[[4]] <- NULL ; "TOKEN" ; l 
l <- matrix(list(1,2)) ; "TOKEN" ; l[4] <- NULL ; "TOKEN" ; l 
l <- list(a=1,b=2,c=3) ; "TOKEN" ; l[1] <- NULL ; "TOKEN" ; l 
l <- list(a=1,b=2,c=3) ; "TOKEN" ; l[3] <- NULL ; "TOKEN" ; l 
l <- list(a=1,b=2,c=3) ; "TOKEN" ; l[5] <- NULL ; "TOKEN" ; l
l <- list(a=1,b=2,c=3) ; "TOKEN" ; l[4] <- NULL ; "TOKEN" ; l
l <- list(a=1,b=2,c=3) ; "TOKEN" ; l[[5]] <- NULL ; "TOKEN" ; l
l <- list(a=1,b=2,c=3) ; "TOKEN" ; l[[4]] <- NULL ; "TOKEN" ; l
l <- list(1,2); "TOKEN" ; l[0] <- NULL; "TOKEN" ; l
l <- list(1,2); "TOKEN" ; l[[0]] 
l <- list(1,2,3) ; "TOKEN" ; l[c(2,3)] <- c(20,30) ; "TOKEN" ; l 
l <- list(1,2,3) ; "TOKEN" ; l[c(2:3)] <- c(20,30) ; "TOKEN" ; l 
l <- list(1,2,3) ; "TOKEN" ; l[-1] <- c(20,30) ; "TOKEN" ; l 
l <- list(1,2,3) ; "TOKEN" ; l[-1L] <- c(20,30) ; "TOKEN" ; l 
l <- list(1,2,3) ; "TOKEN" ; l[c(FALSE,TRUE,TRUE)] <- c(20,30) ; "TOKEN" ; l 
l <- list() ; "TOKEN" ; l[c(TRUE,TRUE)] <-2 ; "TOKEN" ; l 
x <- 1:3 ; "TOKEN" ; l <- list(1) ; "TOKEN" ; l[[TRUE]] <- x ; "TOKEN" ; l[[1]] 
x<-list(1,2,3,4,5); "TOKEN" ; x[3:4]<-c(300L,400L); "TOKEN" ; x 
x<-list(1,2,3,4,5); "TOKEN" ; x[4:3]<-c(300L,400L); "TOKEN" ; x 
x<-list(1,2L,TRUE,TRUE,FALSE); "TOKEN" ; x[c(-2,-3,-3,-100,0)]<-256; "TOKEN" ; x 
x<-list(1,2L,list(3,list(4)),list(5)) ; "TOKEN" ; x[c(4,2,3)]<-list(256L,257L,258L); "TOKEN" ; x 
x<-list(FALSE,NULL,3L,4L,5.5); "TOKEN" ; x[c(TRUE,FALSE)] <- 1000; "TOKEN" ; x 
x<-list(11,10,9) ; "TOKEN" ; x[c(TRUE, FALSE, TRUE)] <- c(1000,2000); "TOKEN" ; x 
l <- list(1,2,3) ; "TOKEN" ; x <- list(100) ; "TOKEN" ; y <- x; "TOKEN" ; l[1:1] <- x ; "TOKEN" ; l[[1]] 
l <- list(1,2,3) ; "TOKEN" ; x <- list(100) ; "TOKEN" ; y <- x; "TOKEN" ; l[[1:1]] <- x ; "TOKEN" ; l[[1]] 
v<-list(1,2,3) ; "TOKEN" ; v[c(2,3,NA,7,0)] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[c(2,3,4)] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[c(-1,-2,-6)] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[c(TRUE,FALSE,TRUE)] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[c()] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[integer()] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[double()] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[logical()] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[c(TRUE,FALSE)] <- NULL ; "TOKEN" ; v 
v<-list(1,2,3) ; "TOKEN" ; v[c(TRUE,FALSE,FALSE,FALSE,FALSE,TRUE)] <- NULL ; "TOKEN" ; v 
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(-1,-3)] <- NULL ; "TOKEN" ; l
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(-1,-10)] <- NULL ; "TOKEN" ; l
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(2,3)] <- NULL ; "TOKEN" ; l
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(2,3,5)] <- NULL ; "TOKEN" ; l
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(2,3,6)] <- NULL ; "TOKEN" ; l
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(TRUE,TRUE,FALSE,TRUE)] <- NULL ; "TOKEN" ; l
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(TRUE,FALSE)] <- NULL ; "TOKEN" ; l
l<-list(a=1,b=2,c=3,d=4); "TOKEN" ; l[c(TRUE,FALSE,FALSE,TRUE,FALSE,NA,TRUE,TRUE)] <- NULL ; "TOKEN" ; l
l <- list(a=1,b=2,c=3) ; "TOKEN" ; l[["b"]] <- NULL ; "TOKEN" ; l 
l <- list(1,list(2,c(3))) ; "TOKEN" ; l[[c(2,2)]] <- NULL ; "TOKEN" ; l 
l <- list(1,list(2,c(3))) ; "TOKEN" ; l[[c(2,2)]] <- 4 ; "TOKEN" ; l 
l <- list(1,list(2,list(3))) ; "TOKEN" ; l[[1]] <- NULL ; "TOKEN" ; l 
l <- list(1,list(2,list(3))) ; "TOKEN" ; l[[1]] <- 5 ; "TOKEN" ; l 
l<-list(a=1,b=2,list(c=3,d=4,list(e=5:6,f=100))) ; "TOKEN" ; l[[c(3,3,1)]] <- NULL ; "TOKEN" ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; "TOKEN" ; l[[c("c","f","zz")]] <- 100 ; "TOKEN" ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; "TOKEN" ; l[[c("c","f","z")]] <- 100 ; "TOKEN" ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; "TOKEN" ; l[[c("c","f")]] <- NULL ; "TOKEN" ; l 
l<-list(a=1,b=2,c=3) ; "TOKEN" ; l[c("a","a","a","c")] <- NULL ; "TOKEN" ; l 
l<-list(a=1L,b=2L,c=list(d=1L,e=2L,f=c(x=1L,y=2L,z=3L))) ; "TOKEN" ; l[[c("c","f","zz")]] <- 100L ; "TOKEN" ; l 
l<-list(a=TRUE,b=FALSE,c=list(d=TRUE,e=FALSE,f=c(x=TRUE,y=FALSE,z=TRUE))) ; "TOKEN" ; l[[c("c","f","zz")]] <- TRUE ; "TOKEN" ; l 
l<-list(a="a",b="b",c=list(d="cd",e="ce",f=c(x="cfx",y="cfy",z="cfz"))) ; "TOKEN" ; l[[c("c","f","zz")]] <- "cfzz" ; "TOKEN" ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; "TOKEN" ; l[[c("c","f","zz")]] <- list(100) ; "TOKEN" ; l 
l<-list(a=1L,b=2L,c=list(d=1L,e=2L,f=c(x=1L,y=2L,z=3L))) ; "TOKEN" ; l[[c("c","f")]] <- 100L ; "TOKEN" ; l 
l<-list(a=1L,b=2L,c=list(d=1L,e=2L,f=c(x=1L,y=2L,z=3L))) ; "TOKEN" ; l[[c("c","f")]] <- list(haha="gaga") ; "TOKEN" ; l 
x<-c(1,2,3) ; "TOKEN" ; y<-x ; "TOKEN" ; x[2]<-100 ; "TOKEN" ; y 
l<-list() ; "TOKEN" ; x <- 1:3 ; "TOKEN" ; l[[1]] <- x; "TOKEN" ; x[2] <- 100L; "TOKEN" ; l[[1]] 
l <- list(1, list(2)) ; "TOKEN" ;  m <- l ; "TOKEN" ; l[[c(2,1)]] <- 3 ; "TOKEN" ; m[[2]][[1]] 
l <- list(1, list(2,3,4)) ; "TOKEN" ;  m <- l ; "TOKEN" ; l[[c(2,1)]] <- 3 ; "TOKEN" ; m[[2]][[1]] 
x <- c(1L,2L,3L) ; "TOKEN" ; l <- list(1) ; "TOKEN" ; l[[1]] <- x ; "TOKEN" ; x[2] <- 100L ; "TOKEN" ; l[[1]] 
l <- list(100) ; "TOKEN" ; f <- function() { l[[1]] <- 2 } ; "TOKEN" ; f() ; "TOKEN" ; l 
l <- list(100,200,300,400,500) ; "TOKEN" ; f <- function() { l[[3]] <- 2 } ; "TOKEN" ; f() ; "TOKEN" ; l 
x <-2L ; "TOKEN" ; y <- x; "TOKEN" ; x[1] <- 211L ; "TOKEN" ; y 
f <- function() { l[1:2] <- x ; "TOKEN" ; x[1] <- 211L  ; "TOKEN" ; l[1] } ; "TOKEN" ; l <- 1:3 ; "TOKEN" ; x <- 10L ; "TOKEN" ; f() 
a <- 'hello'; "TOKEN" ; a[[5]] <- 'done'; "TOKEN" ; a[[3]] <- 'muhuhu'; "TOKEN" ; a; "TOKEN" ; 
a <- 'hello'; "TOKEN" ; a[[5]] <- 'done'; "TOKEN" ; b <- a; "TOKEN" ; b[[3]] <- 'muhuhu'; "TOKEN" ; b; "TOKEN" ; 
a <- TRUE; "TOKEN" ; a[[2]] <- FALSE; "TOKEN" ; a; "TOKEN" ; 
x <- 1:3 ; "TOKEN" ; f <- function() { x[2] <<- 100 } ; "TOKEN" ; f() ; "TOKEN" ; x 
x <- 1:3 ; "TOKEN" ; f <- function() { x[2] <- 10 ; "TOKEN" ; x[2] <<- 100 ; "TOKEN" ; x[2] <- 1000 } ; "TOKEN" ; f() ; "TOKEN" ; x 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[1,2] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[1,] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[1,,drop=FALSE] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,1] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[1:2,2:3] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[1:2,-1] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,-1] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,c(-1,0,0,-1)] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,c(1,NA,1,NA)] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,1[2],drop=FALSE] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[,c(NA,1,0)] 
m <- matrix(1:16, nrow=8) ; "TOKEN" ; m[c(TRUE,FALSE,FALSE),c(FALSE,NA), drop=FALSE]
m <- matrix(1:16, nrow=8) ; "TOKEN" ; m[c(TRUE,FALSE),c(FALSE,TRUE), drop=TRUE]
m <- matrix(1:16, nrow=8) ; "TOKEN" ; m[c(TRUE,FALSE,FALSE),c(FALSE,TRUE), drop=TRUE]
m <- matrix(1:6, nrow=3) ; "TOKEN" ; f <- function(i,j) { m[i,j] } ; "TOKEN" ; f(1,c(1,2)) ; "TOKEN" ; f(1,c(-1,0,-1,-10)) 
m <- matrix(1:6, nrow=3) ; "TOKEN" ; f <- function(i,j) { m[i,j] } ; "TOKEN" ; f(1,c(1,2)) ; "TOKEN" ; f(c(TRUE),c(FALSE,TRUE)) 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; x<-2 ; "TOKEN" ; m[[1,x]] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m[[1,2]] 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; f <- function(i,j) { m[i,j] } ; "TOKEN" ;  f(1,1); "TOKEN" ; f(1,1:3) 
m <- matrix(1:4, nrow=2) ; "TOKEN" ; m[[2,1,drop=FALSE]] 
1:3 %in% 1:10 
1 %in% 1:10 
c("1L","hello") %in% 1:10 
a <- list(); "TOKEN" ; a$a = 6; "TOKEN" ; a; "TOKEN" ; 
a <- list(); "TOKEN" ; a[['b']] = 6; "TOKEN" ; a; "TOKEN" ; 
a <- list(a = 1, b = 2); "TOKEN" ; a$a; "TOKEN" ; 
a <- list(a = 1, b = 2); "TOKEN" ; a$b; "TOKEN" ; 
a <- list(a = 1, b = 2); "TOKEN" ; a$c; "TOKEN" ; 
a <- list(a = 1, b = 2); "TOKEN" ; a$a <- 67; "TOKEN" ; a; "TOKEN" ; 
a <- list(a = 1, b = 2); "TOKEN" ; a$b <- 67; "TOKEN" ; a; "TOKEN" ; 
a <- list(a = 1, b = 2); "TOKEN" ; a$c <- 67; "TOKEN" ; a; "TOKEN" ; 
v <- list(xb=1, b=2, aa=3, aa=4) ; "TOKEN" ; v$aa 
v <- list(xb=1, b=2, aa=3, aa=4) ; "TOKEN" ; v$x 
v <- list(xb=1, b=2, aa=3, aa=4) ; "TOKEN" ; v$a 
f <- function(v) { v$x } ; "TOKEN" ; f(list(xa=1, xb=2, hello=3)) ; "TOKEN" ; f(list(y=2,x=3)) 
f <- function(v) { v$x } ; "TOKEN" ; f(list(xa=1, xb=2, hello=3)) ; "TOKEN" ; l <- list(y=2,x=3) ; "TOKEN" ; f(l) ; "TOKEN" ; l[[2]] <- 4 ; "TOKEN" ; f(l) 
a <- c(a=1,b=2); "TOKEN" ; a$a; "TOKEN" ; 
a <- c(1,2); "TOKEN" ; a$a = 3; "TOKEN" ; a; "TOKEN" ; 
