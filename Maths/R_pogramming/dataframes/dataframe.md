# Data frames

**Goal:** Create, inspect, subset, and manipulate data frames.

**Key functions**

* `data.frame()`, `read.csv()`, `str()`, `summary()`, `$`, `names()`, `nrow()`, `ncol()`, `merge()`, `cbind()`, `rbind()`
| **Function**    | **Category / Purpose** | **Description**                                                    | **Example**                                       | **Output / Explanation**                                    |
| --------------- | ---------------------- | ------------------------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------------- |
| `data.frame()`  | Creation               | Create a data frame from vectors                                   | `df <- data.frame(name=c("A","B"), age=c(23,25))` | Creates a table with columns `name` and `age`               |
| `read.csv()`    | Import                 | Load CSV data into R                                               | `df <- read.csv("data.csv")`                      | Reads CSV file into a data frame                            |
| `str()`         | Inspection             | Shows structure of data frame (types, rows, columns)               | `str(df)`                                         | `'data.frame': 2 obs. of 2 variables'`                      |
| `summary()`     | Inspection / Stats     | Gives summary stats of numeric columns (min, max, mean, quartiles) | `summary(df)`                                     | Shows min, max, mean, median, quartiles for numeric columns |
| `$`             | Access                 | Access a specific column by name                                   | `df$age`                                          | Returns column `age` as a vector                            |
| `names()`       | Column names           | Returns names of all columns                                       | `names(df)`                                       | `name "age"`                                                |
| `nrow()`        | Dimension              | Number of rows                                                     | `nrow(df)`                                        | `2`                                                         |
| `ncol()`        | Dimension              | Number of columns                                                  | `ncol(df)`                                        | `2`                                                         |
| `merge()`       | Combine                | Merge two data frames by common column(s)                          | `merge(df1, df2, by="id")`                        | Joins two data frames based on `id`                         |
| `cbind()`       | Combine                | Combine vectors or data frames column-wise                         | `cbind(df1, df2)`                                 | Adds columns side by side                                   |
| `rbind()`       | Combine                | Combine data frames row-wise                                       | `rbind(df1, df2)`                                 | Adds rows at the bottom                                     |
| `[row, col]`    | Subset                 | Access specific rows/columns                                       | `df[2,1]`                                         | Element at 2nd row, 1st column                              |
| `[row, ]`       | Subset rows            | Access entire row                                                  | `df[5, ]`                                         | Returns 5th row as a data frame                             |
| `[ , col]`      | Subset column          | Access entire column                                               | `df[,2]`                                          | Returns 2nd column as a vector                              |
| `[row_name, ]`  | Subset by row name     | Access row by its name                                             | `df["Akash", ]`                                   | Returns row for "Akash"                                     |

**Examples**

```r
df1 <- df <- data.frame(
  Python = c(98, 95, 99, 45, 65, 71, 90),
  Maths = c(98, 100, 56, 71, 23, 45, 87),
  Names = c("Saumya", "Tvisha", "Roshan", "Abi", "Akash", "Susanti", "Bhumika")
)
df2 <- df <- data.frame(
  IBT = c(98, 95, 99, 45, 65, 71, 90),
  ECS = c(98, 100, 56, 71, 23, 45, 87),
  Names = c("Saumya", "Tvisha", "Roshan", "Abi", "Akash", "Susanti", "Bhumika")
)
df3 <- df <- data.frame(
  Python = c(84, 70, 89, 25, 62, 09, 86),
  Maths = c(67, 05, 87, 20, 26, 75, 43),
  Names = c("Rahul", "harsha", "Varsha", "Trusha", "Rohit", "Arshdeep", "Uzma")
)

merge(df1, df2, by = "Names")
names(df1) # "Python" "Maths"  "Names"
cbind(df1, df2)
#   Python Maths   Names IBT ECS   Names
# 1     98    98  Saumya  98  98  Saumya
# 2     95   100  Tvisha  95 100  Tvisha
# 3     99    56  Roshan  99  56  Roshan
# 4     45    71     Abi  45  71     Abi
# 5     65    23   Akash  65  23   Akash
# 6     71    45 Susanti  71  45 Susanti
# 7     90    87 Bhumika  90  87 Bhumika

# rbind(df1, df2)
# Error in match.names(clabs, names(xi)) :
#   names do not match previous names

rbind(df1, df3)
#    Python Maths    Names
# 1      98    98   Saumya
# 2      95   100   Tvisha
# 3      99    56   Roshan
# 4      45    71      Abi
# 5      65    23    Akash
# 6      71    45  Susanti
# 7      90    87  Bhumika
# 8      84    67    Rahul
# 9      70     5   harsha
# 10     89    87   Varsha
# 11     25    20   Trusha
# 12     62    26    Rohit
# 13      9    75 Arshdeep
# 14     86    43     Uzma
df1
#   Python Maths   Names
# 1     98    98  Saumya
# 2     95   100  Tvisha
# 3     99    56  Roshan
# 4     45    71     Abi
# 5     65    23   Akash
# 6     71    45 Susanti
# 7     90    87 Bhumika

df1[2, 1] # 95
df1[, "Maths"] # 98 100  56  71  23  45  87
df1[6, ]
# Python Maths   Names
# 6     71    45 Susanti
```

**Practice**

1. Create a data frame of students (name, marks, pass(TRUE/FALSE)). Filter passed students.
2. Add a new column `grade` based on `score`: A if >=90, B if 80–89, else C.
