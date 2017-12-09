x<-210 ; repeat { x <- x + 1 ; break } ; x 
x<-1 ; repeat { x <- x + 1 ; if (x > 11) { break } } ; x 
x<-1 ; repeat { x <- x + 1 ; if (x <= 11) { next } else { break } ; x <- 1024 } ; x 
x<-1 ; while(TRUE) { x <- x + 1 ; if (x > 11) { break } } ; x 
x<-1 ; while(x <= 10) { x<-x+1 } ; x 
x<-1 ; for(i in 1:10) { x<-x+1 } ; x 
f<-function(i) { if (i<=1) {1} else {r<-i; for(j in 2:(i-1)) {r=r*j}; r} }; f(10) 
f<-function(i) { x<-integer(i); x[1]<-1; x[2]<-1; if (i>2) { for(j in 3:i) { x[j]<-x[j-1]+x[j-2] } }; x[i] } ; f(32) 
f<-function(r) { x<-0 ; for(i in r) { x<-x+i } ; x } ; f(1:10) ; f(c(1,2,3,4,5)) 
f<-function(r) { x<-0 ; for(i in r) { x<-x+i } ; x } ; f(c(1,2,3,4,5)) ; f(1:10) 
