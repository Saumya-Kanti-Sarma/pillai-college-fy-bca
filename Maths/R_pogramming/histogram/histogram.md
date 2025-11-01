2.c Histogram

**Key functions**

* `hist()`, `breaks`, `freq=TRUE/FALSE`, `density()`

**Example**

```r
data = rnorm(500, mean=50, sd=10)
hist(data, breaks=20, main="Histogram of Data", xlab="Value")
```

**Practice**

1. Create histogram of exam scores (0–100), choose appropriate `breaks`, overlay `density()` curve.
2. Plot histogram with probability density (use `prob=TRUE`) and superimpose `lines(density(data))`.
