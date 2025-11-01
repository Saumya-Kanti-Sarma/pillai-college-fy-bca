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
