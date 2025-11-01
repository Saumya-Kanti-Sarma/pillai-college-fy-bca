# 2. R programs on Graphs and Diagram

We’ll cover base graphics for Bar diagrams, Pie charts, Histogram. I’ll show simple, multiple (grouped), and subdivided (stacked) bar diagrams.

---

## 2.a Bar diagrams — simple, multiple (grouped), subdivided (stacked)

**Key functions**

* `barplot()`, `tapply()`, `table()`, `matrix()` (for grouped bars), `legend()`

**Examples**

### Simple bar plot

```r
counts = c(10, 15, 7, 12)
names(counts) = c("A","B","C","D")
barplot(counts, main="Simple Bar Plot", xlab="Category", ylab="Count")
```

### Grouped (multiple) bar plot

```r
# Two groups (male/female) across 3 categories
male   = c(20, 30, 15)
female = c(25, 28, 20)
mat = rbind(male, female)   # rows = groups, cols = categories
colnames(mat) = c("Cat1","Cat2","Cat3")
barplot(mat, beside=TRUE, legend.text=c("Male","Female"), main="Grouped Bar Plot")
```

### Stacked (subdivided) bar plot

```r
barplot(mat, beside=FALSE, legend.text=c("Male","Female"), main="Stacked Bar Plot")
```

**Practice**

1. From a data frame with `gender` and `department`, create a grouped barplot of counts across departments.
2. Convert the grouped plot to stacked and add a legend.

---

## 2.b Pie chart

**Key functions**

* `pie()`, `labels`, `percentages`, `col=rainbow()`

**Example**

```r
vals = c(30, 20, 25, 25)
lbls = c("A","B","C","D")
pct = round(vals/sum(vals)*100)
lbls2 = paste(lbls, pct, "%")
pie(vals, labels = lbls2, main="Pie Chart Example")
```

**Practice**

1. Build a pie chart showing distribution of marks categories (A/B/C/D) from a sample vector.
2. Try `pie3D()` from package `plotrix` (install first) — optional.

---

## 2.c Histogram

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

---

# 3. Matrix operations

**Goal:** Create matrices and perform arithmetic, transpose, inverse, rank.

**Key functions**

* `matrix()`, `%*%` (matrix multiplication), `t()` (transpose), `solve()` (inverse), `det()` (determinant), `rankMatrix()` from `Matrix` package or use `qr()` to get rank via `qr()`.

**Examples**

```r
A = matrix(c(2,1,3,4,5,6), nrow=2, byrow=TRUE)  # 2x3
B = matrix(1:4, nrow=2)                         # 2x2

# For square matrices
M = matrix(c(2,1,1,3), nrow=2)
M_inv = solve(M)      # inverse
tM = t(M)             # transpose
det(M)
# Rank (using qr)
qr_M = qr(M)
rank = qr_M$rank
rank
# Multiply (if dims match)
C = M %*% M
```

**Practice**

1. Create 3x3 matrix, compute inverse and check `M %*% solve(M)` equals identity.
2. Find rank of matrix `matrix(c(1,2,2,4), nrow=2)` (should be 1).

---

# 4. Eigenvalues and Eigenvectors

**Goal:** Compute eigenvalues & eigenvectors of square matrices.

**Key functions**

* `eigen()` returns values and vectors.

**Example**

```r
M = matrix(c(4,2,1,3), nrow=2)
e = eigen(M)
e$values    # eigenvalues
e$vectors   # columns are eigenvectors
# Check: M %*% v = lambda * v
lambda1 = e$values[1]
v1 = e$vectors[,1]
all.equal(M %*% v1, lambda1 * v1)
```

**Practice**

1. Find eigenvalues of covariance matrix of a 3-variable dataset (use `cov()` then `eigen()`).
2. For matrix `[[2,1],[1,2]]`, compute eigenvalues and eigenvectors and interpret.

---

# 5. Measures of Central Tendency — Ungrouped data

**Goal:** Compute mean, median, mode, quartiles for raw (ungrouped) data.

**Key functions**

* `mean()`, `median()`, `quantile()`
* Mode isn't built-in; compute by frequency (`table()` & `which.max()`)

**Example**

```r
x = c(2,3,4,4,5,6,6,6,7)
mean(x)
median(x)
quantile(x, probs=c(0.25, 0.5, 0.75))

# Mode function
mode_func = function(v){
  tbl = table(v)
  as.numeric(names(tbl)[which.max(tbl)])
}
mode_func(x)
```

**Practice**

1. Compute mean, median, mode for a sample of 15 integers (mix repeated values).
2. Compute quartiles and IQR and detect outliers using 1.5*IQR rule.

---

# 6. Measures of Central Tendency — Grouped data

**Goal:** For frequency distribution (class intervals), compute mean, median, mode approximately using class midpoints.

**Approach & key steps**

* Given intervals and frequencies, use class midpoints `m_i`, compute mean ≈ Σ(f_i * m_i)/Σf_i.
* Median class: use cumulative frequencies and linear interpolation.
* Mode class: use formula for grouped mode.

**Example**

```r
# Suppose classes and frequencies
classes = matrix(c(0,10, 10,20, 20,30, 30,40), ncol=2, byrow=TRUE)
freq = c(5, 12, 8, 5)

midpoints = rowMeans(classes)
mean_grouped = sum(freq * midpoints) / sum(freq)

# Median (interpolation)
cumf = cumsum(freq)
N = sum(freq)
median_class_index = which(cumf >= N/2)[1]
L = classes[median_class_index,1]         # lower class boundary
h = classes[median_class_index,2] - L
cf_prev = ifelse(median_class_index == 1, 0, cumf[median_class_index - 1])
fm = freq[median_class_index]
median_grouped = L + ((N/2 - cf_prev) / fm) * h

mean_grouped; median_grouped
```

**Practice**

1. Given class intervals 0–10,10–20,... and frequencies, compute grouped mean & median (use the formula).
2. Compute grouped mode using `Mode ≈ L + ((fm - f1)/(2*fm - f1 - f2))*h`.

---

# 7. Measure of Dispersion — Grouped data (Absolute & Relative)

**Goal:** Compute variance, standard deviation, coefficient of variation (CV) for grouped data.

**Formula**

* Variance ≈ (Σ f*(m_i - mean)^2) / (Σ f)  (for population) or divide by (Σ f - 1) for sample.
* CV = (sd/mean) * 100%

**Example**

```r
# reusing midpoints and freq from previous
mean_g = mean_grouped
variance_g = sum(freq * (midpoints - mean_g)^2) / sum(freq)   # population
sd_g = sqrt(variance_g)
cv_g = (sd_g / mean_g) * 100
mean_g; sd_g; cv_g
```

**Practice**

1. Compute variance and CV for a grouped distribution you create.
2. Compare grouped variance estimate vs raw data variance by expanding grouped data into raw observations.

---

# 8. Measure of Dispersion — Ungrouped data

**Goal:** Compute range, mean deviation, variance, standard deviation, CV.

**Key functions**

* `abs()`, `sum()`, `mean()`, `var()`, `sd()`

**Examples**

```r
x = c(5,7,8,10,12)
range_val = max(x) - min(x)
mean_dev = mean(abs(x - mean(x)))
variance = var(x)       # sample variance (divides by n-1)
sd_x = sd(x)
cv = sd_x / mean(x) * 100
range_val; mean_dev; variance; sd_x; cv
```

**Practice**

1. For a sample vector compute mean absolute deviation and compare to sd.
2. Show how variance changes dividing by `n` vs `n-1` (population vs sample).

---

# 9. Correlation & Scatter diagram

**Goal:** Compute Pearson and Spearman correlations and plot scatterplots.

**Key functions**

* `cor(x, y, method="pearson")`, `cor(..., method="spearman")`, `plot(x,y)`, `cor.test()` for hypothesis testing

**Examples**

```r
x = c(10,20,30,40,50)
y = c(15,25,35,45,55)

# Pearson
cor(x,y, method="pearson")
cor.test(x,y, method="pearson")

# Spearman
cor(x,y, method="spearman")
cor.test(x,y, method="spearman")

# Scatter plot
plot(x, y, main="Scatter Plot", xlab="X", ylab="Y", pch=19)
abline(lm(y~x), col="red")   # regression line
```

**Practice**

1. Given paired data, compute Pearson correlation and test significance (use `cor.test`).
2. Rank the data and compute Spearman correlation manually (rank then Pearson on ranks) and compare with `cor(method="spearman")`.
3. Draw scatter plot and overlay regression line and report R².

---

# 10. Regression

**Goal:** Fit simple linear regression Y on X and X on Y, interpret coefficients and make predictions.

**Key functions**

* `lm(y ~ x, data=...)`, `summary(lmobj)`, `predict()`, `confint()`

**Examples**

```r
# Y on X
x = c(1,2,3,4,5)
y = c(2,4.1,6,7.9,10)
model_Y_on_X = lm(y ~ x)
summary(model_Y_on_X)

# coefficients
coef(model_Y_on_X)

# Predictions
newx = data.frame(x = c(6,7))
predict(model_Y_on_X, newx, interval="confidence")

# X on Y (reverse regression)
model_X_on_Y = lm(x ~ y)
summary(model_X_on_Y)
```

**Interpretation notes**

* For `y ~ x`, `Intercept + slope*x` gives expected y.
* `R-squared` shows proportion of variance explained.
* Standard errors and p-values indicate significance.

**Practice**

1. Fit regression for dataset of heights vs weights; interpret slope, intercept, R².
2. Estimate `y` for a given `x` with 95% confidence interval using `predict()`.
3. Fit `x ~ y` and compare slopes and R²; discuss why slopes differ.

---

# Sample practical assignments (combined, useful to submit)

**Assignment A — Data Import & Summary + Plots**

* Import `students.csv` (columns: id, gender, marks).
* Show `str()`, `summary()`.
* Create grouped bar plot of counts by gender and histogram of marks.
* Save plots to PNG files.

**Assignment B — Matrix & Eigen**

* Create matrix `A = matrix(c(4,2,2,3),2,2)`:

  * compute inverse, determinant, rank.
  * compute eigenvalues/eigenvectors and verify `A %*% v = λ*v`.

**Assignment C — Grouped Statistics**

* Given class interval table:

  * Compute grouped mean, median, mode, variance, sd, CV.
  * Expand grouped data to raw and compare sample mean & sd.

**Assignment D — Correlation & Regression**

* Given paired sample (x,y):

  * Draw scatter plot.
  * Compute Pearson & Spearman correlations.
  * Fit regression y~x, plot line, predict y for new x.

---

# How to run these in VS Code

* Put code blocks into `basics.r` and run using:

  * Open R terminal in VS Code and `source("basics.r")`, or
  * Use `Rscript basics.r` from Command Prompt:
    `Rscript basics.r` → outputs to console.
  * For plotting to files: use `png("plot.png")` ... `dev.off()` to save.

---

# Quick reference functions (cheat-sheet)

* Data I/O: `read.csv()`, `write.csv()`
* Dataframe: `head()`, `str()`, `summary()`, `subset()`
* Vectors: `c()`, `seq()`, `rep()`, `rnorm()`
* Stats: `mean()`, `median()`, `var()`, `sd()`, `quantile()`
* Correlation/regression: `cor()`, `cor.test()`, `lm()`, `summary()`, `predict()`
* Matrices: `matrix()`, `%*%`, `t()`, `solve()`, `eigen()`
* Plots: `plot()`, `hist()`, `barplot()`, `pie()`, `abline()`
* Save plot: `png()`, `pdf()`, `dev.off()`

