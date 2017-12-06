1==1
2==1
1L<=1
1<=0L
x<-2; "TOKEN" ; f<-function(z=x) { if (z<=x) {z} else {x} } ; "TOKEN" ; f(1.4)
1==NULL
1L==1
TRUE==1
TRUE==FALSE
FALSE<=TRUE
FALSE<TRUE
TRUE>FALSE
TRUE>=FALSE
TRUE!=FALSE
1+1i == 1-1i 
1+1i == 1+1i 
x<-c(1,2,3,4); "TOKEN" ;y<-c(10,2); "TOKEN" ;x<=y
x<-c(1,2,3,4); "TOKEN" ;y<-2.5; "TOKEN" ;x<=y
x<-c(1,2,3,4); "TOKEN" ;y<-c(2.5+NA,2.5); "TOKEN" ;x<=y
x<-c(1L,2L,3L,4L); "TOKEN" ;y<-c(2.5+NA,2.5); "TOKEN" ;x<=y
x<-c(1L,2L,3L,4L); "TOKEN" ;y<-c(TRUE,FALSE); "TOKEN" ;x<=y
x<-c(1L,2L,3L,4L); "TOKEN" ;y<-1.5; "TOKEN" ;x<=y
c(1:3,4,5)==1:5
0/0 == c(1,2,3,4)
matrix(1) > matrix(2) 
matrix(1) > NA 
m <- matrix(1:6, nrow=2) ; "TOKEN" ; m > c(1,2,3) 
"a" <= "b" 
"a" > "b" 
"2.0" == 2 
a <- as.raw(1) ; "TOKEN" ; b <- as.raw(2) ; "TOKEN" ; a < b 
a <- as.raw(1) ; "TOKEN" ; b <- as.raw(2) ; "TOKEN" ; a > b 
a <- as.raw(1) ; "TOKEN" ; b <- as.raw(2) ; "TOKEN" ; a == b 
a <- as.raw(1) ; "TOKEN" ; b <- as.raw(200) ; "TOKEN" ; a < b 
a <- as.raw(200) ; "TOKEN" ; b <- as.raw(255) ; "TOKEN" ; a < b 
