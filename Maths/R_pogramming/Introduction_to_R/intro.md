# 1. Introduction to R — Basic commands

**Goal:** Learn R basics: arithmetic, vectors, logicals, indexing, and simple help & workspace management.

**Key concepts & commands**

* Arithmetic: `+ - * / ^`, `sqrt()`, `log()`
* Vectors: `c()`, `seq()`, `rep()`
* Indexing: `x[1]`, `x[c(1,3)]`, `x[x>value]`
* Basic functions: `length()`, `sum()`, `mean()`, `sd()`, `min()`, `max()`
* Workspace: `ls()`, `rm()`, `save()`, `load()`

---

###  **R Basic Commands Overview**

| **Category**   | **Function / Operator** | **Description**              | **Example** | **Output / Explanation** |
| -------------- | ----------------------- | ---------------------------- | ----------- | ------------------------ |
| **Arithmetic** | `+`                     | Addition                     | `5 + 3`     | `8`                      |
|                | `-`                     | Subtraction                  | `10 - 4`    | `6`                      |
|                | `*`                     | Multiplication               | `6 * 3`     | `18`                     |
|                | `/`                     | Division                     | `12 / 4`    | `3`                      |
|                | `^`                     | Exponentiation (power)       | `2 ^ 3`     | `8`                      |
|                | `sqrt()`                | Square root                  | `sqrt(16)`  | `4`                      |
|                | `log()`                 | Natural logarithm (base *e*) | `log(10)`   | `2.3026`                 |


| **Category** | **Function / Operator** | **Description**              | **Example**           | **Output / Explanation** |
| ------------ | ----------------------- | ---------------------------- | --------------------- | ------------------------ |
| **Vectors**  | `c()`                   | Combine values into a vector | `x <- c(1, 2, 3, 4)`  | Creates vector `1 2 3 4` |
|              | `seq()`                 | Generate a sequence          | `seq(1, 10, by=2)`    | `1 3 5 7 9`              |
|              | `rep()`                 | Repeat elements              | `rep(5, times=3)`     | `5 5 5`                  |
|              |                         |                              | `rep(c(1,2), each=3)` | `1 1 1 2 2 2`            |

---

| **Category** | **Function / Operator** | **Description**          | **Example**              | **Output / Explanation** |
| ------------ | ----------------------- | ------------------------ | ------------------------ | ------------------------ |
| **Indexing** | `x[1]`                  | Access first element     | `x <- c(10,20,30); x[1]` | `10`                     |
|              | `x[c(1,3)]`             | Access multiple elements | `x[c(1,3)]`              | `10 30`                  |
|              | `x[x > value]`          | Conditional selection    | `x[x > 15]`              | `20 30`                  |

---

| **Category**        | **Function / Operator**    | **Description / Use**                          | **Example**       | **Output / Explanation**                             |
| ------------------- | -------------------------- | ---------------------------------------------- | ----------------- | ---------------------------------------------------- |
| **Basic Functions** | `length(x)`                | Count number of elements in vector `x`         | `length(x)`       | `11` (for x = 10:20)                                 |
|                     | `sum(x)`                   | Sum of all elements                            | `sum(x)`          | `165`                                                |
|                     | `prod(x)`                  | Product of all elements                        | `prod(1:5)`       | `120` (1*2*3*4*5)                                    |
|                     | `mean(x)`                  | Arithmetic mean (average)                      | `mean(x)`         | `15`                                                 |
|                     | `median(x)`                | Middle value when sorted                       | `median(x)`       | `15`                                                 |
|                     | `mode()`                   | Most frequent value (custom function required) | See code          | `NA if all unique`                                   |
|                     | `sd(x)`                    | Standard deviation                             | `sd(x)`           | `3.3166`                                             |
|                     | `var(x)`                   | Variance (spread of data)                      | `var(x)`          | `11`                                                 |
|                     | `min(x)`                   | Minimum value                                  | `min(x)`          | `10`                                                 |
|                     | `max(x)`                   | Maximum value                                  | `max(x)`          | `20`                                                 |
|                     | `summary(x)`               | Gives min, 1st Qu., median, mean, 3rd Qu., max | `summary(x)`      | Min:10, 1Q:12.5, Median:15, Mean:15, 3Q:17.5, Max:20 |
|                     | `sort(x)`                  | Sort vector in ascending order                 | `sort(x)`         | `10 11 12 ... 20`                                    |
|                     | `sort(x, decreasing=TRUE)` | Sort vector in descending order                | `sort(x, TRUE)`   | `20 19 18 ... 10`                                    |
|                     | `cumsum(x)`                | Cumulative sum of elements                     | `cumsum(1:5)`     | `1 3 6 10 15`                                        |
|                     | `round(x, digits=n)`       | Round values to `n` decimal places             | `round(3.1456,2)` | `3.15`                                               |
|                     | `seq(from, to, by)`        | Generate sequence                              | `seq(0,20,5)`     | `0 5 10 15 20`                                       |
|                     | `rep(x, times)`            | Repeat elements                                | `rep(2,3)`        | `2 2 2`                                              |
|                     | `x[i]`                     | Access element at index `i`                    | `x[1]`            | `10`                                                 |
|                     | `x[c(1,5)]`                | Access multiple elements                       | `x[c(1,5)]`       | `10 14`                                              |


Explanation of the new functions:
`prod()` — multiplies all vector elements together. Useful for factorial or product computations.
`cumsum()` — gives cumulative sums at each position. Example: cumsum(1:5) → 1 3 6 10 15.
`round(x, digits=n)` — rounds numeric values to n decimal places.
`seq(from, to, by)` — creates arithmetic sequences. Example: seq(0, 20, 5) → 0 5 10 15 20.
`rep(x, times)` — repeats a value multiple times. Can also repeat each element in a vector individually.
`x[i] / x[c(...)]` — indexing to access specific elements. x[x > value] can filter elements conditionally.
`summary()` — gives min, max, median, mean, and quartiles in one function.

**`mode()`** Function:
```r
mode <- function(x) {
  u <- unique(x)
  u[which.max(tabulate(match(x, u)))]
}
```
---

| **Category**             | **Function / Operator** | **Description**              | **Example**                  | **Output / Explanation** |
| ------------------------ | ----------------------- | ---------------------------- | ---------------------------- | ------------------------ |
| **Workspace Management** | `ls()`                  | List all variables in memory | `ls()`                       | Lists variable names     |
|                          | `rm()`                  | Remove objects from memory   | `rm(x)`                      | Deletes object `x`       |
|                          | `save()`                | Save variables to a file     | `save(x, file="data.RData")` | Saves object to disk     |
|                          | `load()`                | Load saved data file         | `load("data.RData")`         | Loads saved variables    |

---

**Examples**

```r
# Basic arithmetic and variables
a = 5
b = 2
a + b
a^2
sqrt(25)
log(10)     # natural log

# Vectors and indexing
v = c(2,4,6,8,10)
v[1]        # 1st element
v[2:4]      # slice
v[v > 5]    # conditional filter

# Useful summary functions
length(v)
sum(v)
mean(v)
sd(v)
```

**Practice**

1. Create `vec = seq(1,50,by=1)` and compute mean, median, sd.
2. Create vector of 20 random normal numbers `rnorm(20, mean=10, sd=2)` and find how many values > 12.
3. Save `v` to disk and reload it (`save(v, file="v.RData")` / `load("v.RData")`).
