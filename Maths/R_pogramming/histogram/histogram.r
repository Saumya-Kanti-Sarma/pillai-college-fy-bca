lb <- seq(0, 60, 10)
ub <- seq(10, 70, 75)
x <- (lb + ub) / 2
f <- c(5, 15, 20, 23, 17, 11, 9)
y <- rep(x, f)
y
x0 <- c(0, x, 40)
f0 <- c(0, f, 0)
bks <- seq(0, 70, 10)
hist(y, bks)
lines(x0, f0)
