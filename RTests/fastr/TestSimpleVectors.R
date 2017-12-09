x<-1:10; x[3] 
x<-1:10; x[3L] 
x<-c(1,2,3); x[3] 
x<-c(1,2,3); x[3L] 
x<-1:3; x[0-2] 
x<-1:3; x[FALSE] 
x<-1:3; x[TRUE] 
x<-c(TRUE,TRUE,FALSE); x[0-2] 
x<-c(1,2);x[[0-1]] 
x<-c(1,2);x[0-3] 
x<-10; x[0-1] 
x<-10; x[NA] 
x <- c(a=1, b=2, c=3) ; x[2] 
x <- c(a=1, b=2, c=3) ; x[[2]] 
x <- c(a="A", b="B", c="C") ; x[-2] 
x <- c(a=1+2i, b=2+3i, c=3) ; x[-2] 
x <- c(a=1, b=2, c=3) ; x[-2] 
x <- c(a=1L, b=2L, c=3L) ; x[-2] 
x <- c(a=TRUE, b=FALSE, c=NA) ; x[-2] 
x <- c(a=as.raw(10), b=as.raw(11), c=as.raw(12)) ; x[-2] 
x <- c(a=1L, b=2L, c=3L) ; x[0] 
x <- c(a=1L, b=2L, c=3L) ; x[10] 
x <- c(a=TRUE, b=FALSE, c=NA) ; x[0] 
x <- c(TRUE, FALSE, NA) ; x[0] 
x <- list(1L, 2L, 3L) ; x[10] 
x <- list(a=1L, b=2L, c=3L) ; x[0] 
x <- c(a="A", b="B", c="C") ; x[10] 
x <- c(a="A", b="B", c="C") ; x[0] 
x <- c(a=1+1i, b=2+2i, c=3+3i) ; x[10] 
x <- c(a=1+1i, b=2+2i, c=3+3i) ; x[0] 
x <- c(a=as.raw(10), b=as.raw(11), c=as.raw(12)) ; x[10] 
x <- c(a=as.raw(10), b=as.raw(11), c=as.raw(12)) ; x[0] 
x <- c(a=1, b=2, c=3) ; x[10] 
x <- c(a=1, b=2, c=3) ; x[0] 
x <- c(a=1,b=2,c=3,d=4) ; x["b"] 
x <- c(a=1,b=2,c=3,d=4) ; x["d"] 
x <- 1 ; attr(x, "hi") <- 2; x[2] <- 2; attr(x, "hi") 
x<-1:5 ; x[3:4] 
x<-1:5 ; x[4:3] 
x<-c(1,2,3,4,5) ; x[4:3] 
(1:5)[3:4] 
x<-(1:5)[2:4] ; x[2:1] 
x<-1:5;x[c(0-2,0-3)] 
x<-1:5;x[c(0-2,0-3,0,0,0)] 
x<-1:5;x[c(2,5,4,3,3,3,0)] 
x<-1:5;x[c(2L,5L,4L,3L,3L,3L,0L)] 
f<-function(x, i) { x[i] } ; f(1:3,3:1) ; f(1:5,c(0,0,0,0-2)) 
f<-function(x, i) { x[i] } ; f(1:3,0-3) ; f(1:5,c(0,0,0,0-2)) 
f<-function(x, i) { x[i] } ; f(1:3,0L-3L) ; f(1:5,c(0,0,0,0-2)) 
x<-1:5 ; x[c(TRUE,FALSE)] 
x<-1:5 ; x[c(TRUE,TRUE,TRUE,NA)] 
x<-1:5 ; x[c(TRUE,TRUE,TRUE,FALSE,FALSE,FALSE,FALSE,TRUE,NA)] 
f<-function(i) { x<-1:5 ; x[i] } ; f(1) ; f(1L) ; f(TRUE) 
f<-function(i) { x<-1:5 ; x[i] } ; f(1) ; f(TRUE) ; f(1L)  
f<-function(i) { x<-1:5 ; x[i] } ; f(1) ; f(TRUE) ; f(c(3,2))  
f<-function(i) { x<-1:5 ; x[i] } ; f(1)  ; f(3:4) 
f<-function(i) { x<-1:5 ; x[i] } ; f(c(TRUE,FALSE))  ; f(3:4) 
x<-as.complex(c(1,2,3,4)) ; x[2:4] 
x<-as.raw(c(1,2,3,4)) ; x[2:4] 
x<-c(1,2,3,4) ; names(x) <- c("a","b","c","d") ; x[c(10,2,3,0)] 
x<-c(1,2,3,4) ; names(x) <- c("a","b","c","d") ; x[c(10,2,3)] 
x<-c(1,2,3,4) ; names(x) <- c("a","b","c","d") ; x[c(-2,-4,0)] 
x<-c(1,2) ; names(x) <- c("a","b") ; x[c(FALSE,TRUE,NA,FALSE)] 
x<-c(1,2) ; names(x) <- c("a","b") ; x[c(FALSE,TRUE)] 
x <- c(a=1,b=2,c=3,d=4) ; x[character()] 
x <- c(a=1,b=2,c=3,d=4) ; x[c("b","b","d","a","a")] 
x <- c(a=as.raw(10),b=as.raw(11),c=as.raw(12),d=as.raw(13)) ; f <- function(s) { x[s] } ; f(TRUE) ; f(1L) ; f(as.character(NA)) 
x <- c(a=1,b=2,c=3,d=4) ; f <- function(s) { x[s] } ; f(TRUE) ; f(1L) ; f("b") 
x <- c(a=as.raw(10),b=as.raw(11),c=as.raw(12),d=as.raw(13)) ; f <- function(s) { x[c(s,s)] } ; f(TRUE) ; f(1L) ; f(as.character(NA)) 
x <- c(a=1,b=2,c=3,d=4) ; f <- function(s) { x[c(s,s)] } ; f(TRUE) ; f(1L) ; f("b") 
x<-1:3; x[1]<-100L; x 
x<-c(1,2,3); x[2L]<-100L; x 
x<-c(1,2,3); x[2L]<-100; x 
x<-c(1,2,3); x[2]<-FALSE; x 
x<-1:5; x[2]<-1000; x[3] <- TRUE; x[8]<-3L; x 
x<-5:1; x[0-2]<-1000; x 
x<-c(); x[[TRUE]] <- 2; x 
x<-1:2; x[[0-2]]<-100; x 
f<-function(x,i,v) { x<-1:5; x[i]<-v; x} ; f(c(1L,2L),1,3L) ; f(c(1L,2L),2,3) 
f<-function(x,i,v) { x<-1:5; x[i]<-v; x} ; f(c(1L,2L),1,3L) ; f(c(1L,2L),8,3L) 
f<-function(x,i,v) { x<-1:5; x[i]<-v; x} ; f(c(1L,2L),1,FALSE) ; f(c(1L,2L),2,3) 
f<-function(x,i,v) { x<-1:5; x[i]<-v; x} ; f(c(1L,2L),1,FALSE) ; f(c(1L,2L),8,TRUE) 
a <- c(1L,2L,3L); a <- 1:5; a[3] <- TRUE; a 
x <- 1:3 ; x[2] <- "hi"; x 
x <- c(1,2,3) ; x[2] <- "hi"; x 
x <- c(TRUE,FALSE,FALSE) ; x[2] <- "hi"; x 
x <- c(2,3,4) ; x[1] <- 3+4i ; x  
a <- c(1,2,3) ; b <- a; a[1] <- 4L; a 
a <- c(1,2,3) ; b <- a; a[2] <- 4L; a 
a <- c(1,2,3) ; b <- a; a[3] <- 4L; a 
a <- c(2.1,2.2,2.3); b <- a; a[[1]] <- TRUE; a 
a <- c(2.1,2.2,2.3); b <- a; a[[2]] <- TRUE; a 
a <- c(2.1,2.2,2.3); b <- a; a[[3]] <- TRUE; a 
a <- c(TRUE,TRUE,TRUE); b <- a; a[[1]] <- FALSE; a 
a <- c(TRUE,TRUE,TRUE); b <- a; a[[2]] <- FALSE; a 
a <- c(TRUE,TRUE,TRUE); b <- a; a[[3]] <- FALSE; a 
x<-c(1,2,3,4,5); x[3:4]<-c(300L,400L); x 
x<-c(1,2,3,4,5); x[4:3]<-c(300L,400L); x 
x<-1:5; x[4:3]<-c(300L,400L); x 
x<-5:1; x[3:4]<-c(300L,400L); x 
x<-5:1; x[3:4]<-c(300,400); x 
x<-1:5; x[c(0-2,0-3,0-3,0-100,0)]<-256; x 
x<-1:5; x[c(4,2,3)]<-c(256L,257L,258L); x 
x<-c(1,2,3,4,5); x[c(TRUE,FALSE)] <- 1000; x 
x<-c(1,2,3,4,5,6); x[c(TRUE,TRUE,FALSE)] <- c(1000L,2000L) ; x 
x<-c(1,2,3,4,5); x[c(TRUE,FALSE,TRUE,TRUE,FALSE)] <- c(1000,2000,3000); x 
x<-c(1,2,3,4,5); x[c(TRUE,FALSE,TRUE,TRUE,0)] <- c(1000,2000,3000); x 
x<-1:3; x[c(TRUE, FALSE, TRUE)] <- c(TRUE,FALSE); x 
x<-c(TRUE,TRUE,FALSE); x[c(TRUE, FALSE, TRUE)] <- c(FALSE,TRUE); x 
x<-c(TRUE,TRUE,FALSE); x[c(TRUE, FALSE, TRUE)] <- c(1000,2000); x 
x<-11:9 ; x[c(TRUE, FALSE, TRUE)] <- c(1000,2000); x 
l <- double() ; l[c(TRUE,TRUE)] <-2 ; l
l <- double() ; l[c(FALSE,TRUE)] <-2 ; l
a<- c('a','b','c','d'); a[3:4] <- c(4,5); a
a<- c('a','b','c','d'); a[3:4] <- c(4L,5L); a
a<- c('a','b','c','d'); a[3:4] <- c(TRUE,FALSE); a
f<-function(i,v) { x<-1:5 ; x[i]<-v ; x } ; f(1,1) ; f(1L,TRUE) ; f(2,TRUE) 
f<-function(i,v) { x<-1:5 ; x[[i]]<-v ; x } ; f(1,1) ; f(1L,TRUE) ; f(2,TRUE) 
f<-function(i,v) { x<-1:5 ; x[i]<-v ; x } ; f(3:2,1) ; f(1L,TRUE) ; f(2:4,4:2) 
f<-function(i,v) { x<-1:5 ; x[i]<-v ; x } ; f(c(3,2),1) ; f(1L,TRUE) ; f(2:4,c(4,3,2)) 
f<-function(b,i,v) { b[i]<-v ; b } ; f(1:4,4:1,TRUE) ; f(c(3,2,1),8,10) 
f<-function(b,i,v) { b[i]<-v ; b } ; f(1:4,4:1,TRUE) ; f(c(3,2,1),8,10) ; f(c(TRUE,FALSE),TRUE,FALSE) 
x<-c(TRUE,TRUE,FALSE,TRUE) ; x[3:2] <- TRUE; x 
x<-1:3 ; y<-(x[2]<-100) ; y 
x<-1:5 ; x[x[4]<-2] <- (x[4]<-100) ; x 
x<-1:5 ; x[3] <- (x[4]<-100) ; x 
x<-5:1 ; x[x[2]<-2] 
x<-5:1 ; x[x[2]<-2] <- (x[3]<-50) ; x 
v<-1:3 ; v[TRUE] <- 100 ; v 
v<-1:3 ; v[-1] <- c(100,101) ; v 
v<-1:3 ; v[TRUE] <- c(100,101,102) ; v 
x <- c(a=1,b=2,c=3) ; x[2]<-10; x 
x <- c(a=1,b=2,c=3) ; x[2:3]<-10; x 
x <- c(a=1,b=2,c=3) ; x[c(2,3)]<-10; x 
x <- c(a=1,b=2,c=3) ; x[c(TRUE,TRUE,FALSE)]<-10; x 
x <- c(a=1,b=2) ; x[2:3]<-10; x 
x <- c(a=1,b=2) ; x[c(2,3)]<-10; x 
x <- c(a=1,b=2) ; x[3]<-10; x 
x <- matrix(1:2) ; x[c(FALSE,FALSE,TRUE)]<-10; x 
x <- 1:2 ; x[c(FALSE,FALSE,TRUE)]<-10; x 
x <- c(a=1,b=2) ; x[c(FALSE,FALSE,TRUE)]<-10; x 
x<-c(a=1,b=2,c=3) ; x[["b"]]<-200; x 
x<-c(a=1,b=2,c=3) ; x[["d"]]<-200; x 
x<-c() ; x[c("a","b","c","d")]<-c(1,2); x 
x<-c(a=1,b=2,c=3) ; x["d"]<-4 ; x 
x<-c(a=1,b=2,c=3) ; x[c("d","e")]<-c(4,5) ; x 
x<-c(a=1,b=2,c=3) ; x[c("d","a","d","a")]<-c(4,5) ; x 
a = c(1, 2); a[['a']] = 67; a; 
a = c(a=1,2,3); a[['x']] = 67; a; 
x <- c(TRUE,TRUE,TRUE,TRUE); x[2:3] <- c(FALSE,FALSE); x 
x <- c(TRUE,TRUE,TRUE,TRUE); x[3:2] <- c(FALSE,TRUE); x 
x <- c('a','b','c','d'); x[2:3] <- 'x'; x
x <- c('a','b','c','d'); x[2:3] <- c('x','y'); x
x <- c('a','b','c','d'); x[3:2] <- c('x','y'); x
x <- c('a','b','c','d'); x[c(TRUE,FALSE,TRUE)] <- c('x','y','z'); x 
x <- c(TRUE,TRUE,TRUE,TRUE); x[c(TRUE,TRUE,FALSE)] <- c(10L,20L,30L); x 
x <- c(1L,1L,1L,1L); x[c(TRUE,TRUE,FALSE)] <- c('a','b','c'); x
x <- c(TRUE,TRUE,TRUE,TRUE); x[c(TRUE,TRUE,FALSE)] <- list(10L,20L,30L); x 
x <- c(); x[c('a','b')] <- c(1L,2L); x 
x <- c(); x[c('a','b')] <- c(TRUE,FALSE); x 
x <- c(); x[c('a','b')] <- c('a','b'); x 
x <- list(); x[c('a','b')] <- c('a','b'); x 
x <- list(); x[c('a','b')] <- list('a','b'); x 
x = c(1,2,3,4); x[x %% 2 == 0] <- c(1,2,3,4); 
x <- 1:3 ; x[c(-2, 1)] <- 10 
list(1:4) 
list(1,list(2,list(3,4))) 
list(1,b=list(2,3)) 
list(1,b=list(c=2,3)) 
list(list(c=2)) 
l<-list(1,2L,TRUE) ; l[[2]] 
l<-list(1,2L,TRUE) ; l[c(FALSE,FALSE,TRUE)] 
l<-list(1,2L,TRUE) ; l[FALSE] 
l<-list(1,2L,TRUE) ; l[-2] 
l<-list(1,2L,TRUE) ; l[NA] 
l<-list(1,2,3) ; l[c(1,2)] 
l<-list(1,2,3) ; l[c(2)] 
x<-list(1,2L,TRUE,FALSE,5) ; x[2:4] 
x<-list(1,2L,TRUE,FALSE,5) ; x[4:2] 
x<-list(1,2L,TRUE,FALSE,5) ; x[c(-2,-3)] 
x<-list(1,2L,TRUE,FALSE,5) ; x[c(-2,-3,-4,0,0,0)] 
x<-list(1,2L,TRUE,FALSE,5) ; x[c(2,5,4,3,3,3,0)] 
x<-list(1,2L,TRUE,FALSE,5) ; x[c(2L,5L,4L,3L,3L,3L,0L)] 
m<-list(1,2) ; m[NULL] 
f<-function(x, i) { x[i] } ; f(list(1,2,3),3:1) ; f(list(1L,2L,3L,4L,5L),c(0,0,0,0-2)) 
x<-list(1,2,3,4,5) ; x[c(TRUE,TRUE,TRUE,FALSE,FALSE,FALSE,FALSE,TRUE,NA)] 
f<-function(i) { x<-list(1,2,3,4,5) ; x[i] } ; f(1) ; f(1L) ; f(TRUE) 
f<-function(i) { x<-list(1,2,3,4,5) ; x[i] } ; f(1) ; f(TRUE) ; f(1L)  
f<-function(i) { x<-list(1L,2L,3L,4L,5L) ; x[i] } ; f(1) ; f(TRUE) ; f(c(3,2))  
f<-function(i) { x<-list(1,2,3,4,5) ; x[i] } ; f(1)  ; f(3:4) 
f<-function(i) { x<-list(1,2,3,4,5) ; x[i] } ; f(c(TRUE,FALSE))  ; f(3:4) 
l<-(list(list(1,2),list(3,4))); l[[c(1,2)]] 
l<-(list(list(1,2),list(3,4))); l[[c(1,-2)]] 
l<-(list(list(1,2),list(3,4))); l[[c(1,-1)]] 
l<-(list(list(1,2),list(3,4))); l[[c(1,TRUE)]] 
l<-(list(list(1,2),c(3,4))); l[[c(2,1)]] 
l <- list(a=1,b=2,c=list(d=3,e=list(f=4))) ; l[[c(3,2)]] 
l <- list(a=1,b=2,c=list(d=3,e=list(f=4))) ; l[[c(3,1)]] 
l <- list(c=list(d=3,e=c(f=4)), b=2, a=3) ; l[[c("c","e")]] 
l <- list(c=list(d=3,e=c(f=4)), b=2, a=3) ; l[[c("c","e", "f")]] 
l <- list(c=list(d=3,e=c(f=4)), b=2, a=3) ; l[[c("c")]] 
l<-list(1,2L,TRUE) ; l[[2]]<-100 ; l 
l<-list(1,2L,TRUE) ; l[[5]]<-100 ; l 
l<-list(1,2L,TRUE) ; l[[3]]<-list(100) ; l 
v<-1:3 ; v[2] <- list(100) ; v 
v<-1:3 ; v[[2]] <- list(100) ; v 
l <- list() ; l[[1]] <-2 ; l
l<-list() ; x <- 1:3 ; l[[1]] <- x  ; l 
l <- list(1,2,3) ; l[2] <- list(100) ; l[2] 
l <- list(1,2,3) ; l[[2]] <- list(100) ; l[2] 
m<-list(1,2) ; m[TRUE] <- NULL ; m 
m<-list(1,2) ; m[[TRUE]] <- NULL ; m 
m<-list(1,2) ; m[[1]] <- NULL ; m 
m<-list(1,2) ; m[[-1]] <- NULL ; m 
m<-list(1,2) ; m[[-2]] <- NULL ; m 
l <- matrix(list(1,2)) ; l[3] <- NULL ; l 
l <- matrix(list(1,2)) ; l[[3]] <- NULL ; l 
l <- matrix(list(1,2)) ; l[[4]] <- NULL ; l 
l <- matrix(list(1,2)) ; l[4] <- NULL ; l 
l <- list(a=1,b=2,c=3) ; l[1] <- NULL ; l 
l <- list(a=1,b=2,c=3) ; l[3] <- NULL ; l 
l <- list(a=1,b=2,c=3) ; l[5] <- NULL ; l
l <- list(a=1,b=2,c=3) ; l[4] <- NULL ; l
l <- list(a=1,b=2,c=3) ; l[[5]] <- NULL ; l
l <- list(a=1,b=2,c=3) ; l[[4]] <- NULL ; l
l <- list(1,2); l[0] <- NULL; l
l <- list(1,2); l[[0]] 
l <- list(1,2,3) ; l[c(2,3)] <- c(20,30) ; l 
l <- list(1,2,3) ; l[c(2:3)] <- c(20,30) ; l 
l <- list(1,2,3) ; l[-1] <- c(20,30) ; l 
l <- list(1,2,3) ; l[-1L] <- c(20,30) ; l 
l <- list(1,2,3) ; l[c(FALSE,TRUE,TRUE)] <- c(20,30) ; l 
l <- list() ; l[c(TRUE,TRUE)] <-2 ; l 
x <- 1:3 ; l <- list(1) ; l[[TRUE]] <- x ; l[[1]] 
x<-list(1,2,3,4,5); x[3:4]<-c(300L,400L); x 
x<-list(1,2,3,4,5); x[4:3]<-c(300L,400L); x 
x<-list(1,2L,TRUE,TRUE,FALSE); x[c(-2,-3,-3,-100,0)]<-256; x 
x<-list(1,2L,list(3,list(4)),list(5)) ; x[c(4,2,3)]<-list(256L,257L,258L); x 
x<-list(FALSE,NULL,3L,4L,5.5); x[c(TRUE,FALSE)] <- 1000; x 
x<-list(11,10,9) ; x[c(TRUE, FALSE, TRUE)] <- c(1000,2000); x 
l <- list(1,2,3) ; x <- list(100) ; y <- x; l[1:1] <- x ; l[[1]] 
l <- list(1,2,3) ; x <- list(100) ; y <- x; l[[1:1]] <- x ; l[[1]] 
v<-list(1,2,3) ; v[c(2,3,NA,7,0)] <- NULL ; v 
v<-list(1,2,3) ; v[c(2,3,4)] <- NULL ; v 
v<-list(1,2,3) ; v[c(-1,-2,-6)] <- NULL ; v 
v<-list(1,2,3) ; v[c(TRUE,FALSE,TRUE)] <- NULL ; v 
v<-list(1,2,3) ; v[c()] <- NULL ; v 
v<-list(1,2,3) ; v[integer()] <- NULL ; v 
v<-list(1,2,3) ; v[double()] <- NULL ; v 
v<-list(1,2,3) ; v[logical()] <- NULL ; v 
v<-list(1,2,3) ; v[c(TRUE,FALSE)] <- NULL ; v 
v<-list(1,2,3) ; v[c(TRUE,FALSE,FALSE,FALSE,FALSE,TRUE)] <- NULL ; v 
l<-list(a=1,b=2,c=3,d=4); l[c(-1,-3)] <- NULL ; l
l<-list(a=1,b=2,c=3,d=4); l[c(-1,-10)] <- NULL ; l
l<-list(a=1,b=2,c=3,d=4); l[c(2,3)] <- NULL ; l
l<-list(a=1,b=2,c=3,d=4); l[c(2,3,5)] <- NULL ; l
l<-list(a=1,b=2,c=3,d=4); l[c(2,3,6)] <- NULL ; l
l<-list(a=1,b=2,c=3,d=4); l[c(TRUE,TRUE,FALSE,TRUE)] <- NULL ; l
l<-list(a=1,b=2,c=3,d=4); l[c(TRUE,FALSE)] <- NULL ; l
l<-list(a=1,b=2,c=3,d=4); l[c(TRUE,FALSE,FALSE,TRUE,FALSE,NA,TRUE,TRUE)] <- NULL ; l
l <- list(a=1,b=2,c=3) ; l[["b"]] <- NULL ; l 
l <- list(1,list(2,c(3))) ; l[[c(2,2)]] <- NULL ; l 
l <- list(1,list(2,c(3))) ; l[[c(2,2)]] <- 4 ; l 
l <- list(1,list(2,list(3))) ; l[[1]] <- NULL ; l 
l <- list(1,list(2,list(3))) ; l[[1]] <- 5 ; l 
l<-list(a=1,b=2,list(c=3,d=4,list(e=5:6,f=100))) ; l[[c(3,3,1)]] <- NULL ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; l[[c("c","f","zz")]] <- 100 ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; l[[c("c","f","z")]] <- 100 ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; l[[c("c","f")]] <- NULL ; l 
l<-list(a=1,b=2,c=3) ; l[c("a","a","a","c")] <- NULL ; l 
l<-list(a=1L,b=2L,c=list(d=1L,e=2L,f=c(x=1L,y=2L,z=3L))) ; l[[c("c","f","zz")]] <- 100L ; l 
l<-list(a=TRUE,b=FALSE,c=list(d=TRUE,e=FALSE,f=c(x=TRUE,y=FALSE,z=TRUE))) ; l[[c("c","f","zz")]] <- TRUE ; l 
l<-list(a="a",b="b",c=list(d="cd",e="ce",f=c(x="cfx",y="cfy",z="cfz"))) ; l[[c("c","f","zz")]] <- "cfzz" ; l 
l<-list(a=1,b=2,c=list(d=1,e=2,f=c(x=1,y=2,z=3))) ; l[[c("c","f","zz")]] <- list(100) ; l 
l<-list(a=1L,b=2L,c=list(d=1L,e=2L,f=c(x=1L,y=2L,z=3L))) ; l[[c("c","f")]] <- 100L ; l 
l<-list(a=1L,b=2L,c=list(d=1L,e=2L,f=c(x=1L,y=2L,z=3L))) ; l[[c("c","f")]] <- list(haha="gaga") ; l 
x<-c(1,2,3) ; y<-x ; x[2]<-100 ; y 
l<-list() ; x <- 1:3 ; l[[1]] <- x; x[2] <- 100L; l[[1]] 
l <- list(1, list(2)) ;  m <- l ; l[[c(2,1)]] <- 3 ; m[[2]][[1]] 
l <- list(1, list(2,3,4)) ;  m <- l ; l[[c(2,1)]] <- 3 ; m[[2]][[1]] 
x <- c(1L,2L,3L) ; l <- list(1) ; l[[1]] <- x ; x[2] <- 100L ; l[[1]] 
l <- list(100) ; f <- function() { l[[1]] <- 2 } ; f() ; l 
l <- list(100,200,300,400,500) ; f <- function() { l[[3]] <- 2 } ; f() ; l 
x <-2L ; y <- x; x[1] <- 211L ; y 
f <- function() { l[1:2] <- x ; x[1] <- 211L  ; l[1] } ; l <- 1:3 ; x <- 10L ; f() 
a <- 'hello'; a[[5]] <- 'done'; a[[3]] <- 'muhuhu'; a; 
a <- 'hello'; a[[5]] <- 'done'; b <- a; b[[3]] <- 'muhuhu'; b; 
a <- TRUE; a[[2]] <- FALSE; a; 
x <- 1:3 ; f <- function() { x[2] <<- 100 } ; f() ; x 
x <- 1:3 ; f <- function() { x[2] <- 10 ; x[2] <<- 100 ; x[2] <- 1000 } ; f() ; x 
m <- matrix(1:6, nrow=2) ; m[1,2] 
m <- matrix(1:6, nrow=2) ; m[1,] 
m <- matrix(1:6, nrow=2) ; m[1,,drop=FALSE] 
m <- matrix(1:6, nrow=2) ; m[,1] 
m <- matrix(1:6, nrow=2) ; m[,] 
m <- matrix(1:6, nrow=2) ; m[1:2,2:3] 
m <- matrix(1:6, nrow=2) ; m[1:2,-1] 
m <- matrix(1:6, nrow=2) ; m[,-1] 
m <- matrix(1:6, nrow=2) ; m[,c(-1,0,0,-1)] 
m <- matrix(1:6, nrow=2) ; m[,c(1,NA,1,NA)] 
m <- matrix(1:6, nrow=2) ; m[,1[2],drop=FALSE] 
m <- matrix(1:6, nrow=2) ; m[,c(NA,1,0)] 
m <- matrix(1:16, nrow=8) ; m[c(TRUE,FALSE,FALSE),c(FALSE,NA), drop=FALSE]
m <- matrix(1:16, nrow=8) ; m[c(TRUE,FALSE),c(FALSE,TRUE), drop=TRUE]
m <- matrix(1:16, nrow=8) ; m[c(TRUE,FALSE,FALSE),c(FALSE,TRUE), drop=TRUE]
m <- matrix(1:6, nrow=3) ; f <- function(i,j) { m[i,j] } ; f(1,c(1,2)) ; f(1,c(-1,0,-1,-10)) 
m <- matrix(1:6, nrow=3) ; f <- function(i,j) { m[i,j] } ; f(1,c(1,2)) ; f(c(TRUE),c(FALSE,TRUE)) 
m <- matrix(1:6, nrow=2) ; x<-2 ; m[[1,x]] 
m <- matrix(1:6, nrow=2) ; m[[1,2]] 
m <- matrix(1:6, nrow=2) ; f <- function(i,j) { m[i,j] } ;  f(1,1); f(1,1:3) 
m <- matrix(1:4, nrow=2) ; m[[2,1,drop=FALSE]] 
1:3 %in% 1:10 
1 %in% 1:10 
c("1L","hello") %in% 1:10 
a <- list(); a$a = 6; a; 
a <- list(); a[['b']] = 6; a; 
a <- list(a = 1, b = 2); a$a; 
a <- list(a = 1, b = 2); a$b; 
a <- list(a = 1, b = 2); a$c; 
a <- list(a = 1, b = 2); a$a <- 67; a; 
a <- list(a = 1, b = 2); a$b <- 67; a; 
a <- list(a = 1, b = 2); a$c <- 67; a; 
v <- list(xb=1, b=2, aa=3, aa=4) ; v$aa 
v <- list(xb=1, b=2, aa=3, aa=4) ; v$x 
v <- list(xb=1, b=2, aa=3, aa=4) ; v$a 
f <- function(v) { v$x } ; f(list(xa=1, xb=2, hello=3)) ; f(list(y=2,x=3)) 
f <- function(v) { v$x } ; f(list(xa=1, xb=2, hello=3)) ; l <- list(y=2,x=3) ; f(l) ; l[[2]] <- 4 ; f(l) 
a <- c(a=1,b=2); a$a; 
a <- c(1,2); a$a = 3; a; 
