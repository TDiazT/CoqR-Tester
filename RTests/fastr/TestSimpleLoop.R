x<-210 ; "TOKEN" ; repeat { x <- x + 1 ; "TOKEN" ; break } ; "TOKEN" ; x 
x<-1 ; "TOKEN" ; repeat { x <- x + 1 ; "TOKEN" ; if (x > 11) { break } } ; "TOKEN" ; x 
x<-1 ; "TOKEN" ; repeat { x <- x + 1 ; "TOKEN" ; if (x <= 11) { next } else { break } ; "TOKEN" ; x <- 1024 } ; "TOKEN" ; x 
x<-1 ; "TOKEN" ; while(TRUE) { x <- x + 1 ; "TOKEN" ; if (x > 11) { break } } ; "TOKEN" ; x 
x<-1 ; "TOKEN" ; while(x <= 10) { x<-x+1 } ; "TOKEN" ; x 
x<-1 ; "TOKEN" ; for(i in 1:10) { x<-x+1 } ; "TOKEN" ; x 
f<-function(i) { if (i<=1) {1} else {r<-i; "TOKEN" ; for(j in 2:(i-1)) {r=r*j}; "TOKEN" ; r} }; "TOKEN" ; f(10) 
f<-function(i) { x<-integer(i); "TOKEN" ; x[1]<-1; "TOKEN" ; x[2]<-1; "TOKEN" ; if (i>2) { for(j in 3:i) { x[j]<-x[j-1]+x[j-2] } }; "TOKEN" ; x[i] } ; "TOKEN" ; f(32) 
f<-function(r) { x<-0 ; "TOKEN" ; for(i in r) { x<-x+i } ; "TOKEN" ; x } ; "TOKEN" ; f(1:10) ; "TOKEN" ; f(c(1,2,3,4,5)) 
f<-function(r) { x<-0 ; "TOKEN" ; for(i in r) { x<-x+i } ; "TOKEN" ; x } ; "TOKEN" ; f(c(1,2,3,4,5)) ; "TOKEN" ; f(1:10) 
