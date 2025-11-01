# students <- c("Roshan", "Abi", "Akash", "Sujay", "Bhumika")
# maths <- c(80, 70, 90, 56, 74)
# science <- c(85, 75, 95, 68, 77)

# scores <- rbind(maths, science)
# scores

# barplot(scores,
#   beside = TRUE, # grouped bars
#   names.arg = students,
#   ylim = c(0, 100),
#   col = c("red", "green"),
#   main = "Student Scores",
#   width = 0.8,
#   ylab = "Marks"
# )


q1 <- c(120, 130, 140)
q2 <- c(150, 160, 155)
q4 <- c(170, 175, 180)
q3 <- c(190, 185, 195)

factories <- c("Factory1", "factory2", "factory3")

quater <- rbind(q1, q2, q3, q4)
bp <- barplot(
  quater,
  beside = TRUE,
  ylim = c(0, 200),
  col = c("#2b2bc5", "#149187", "#f18d0a", "#fff017"),
  border = 0,
  names.arg = factories
)

text(
  x = bp,
  y = quater + 2,
  label = quater
)
legend(
  "topleft",
  legend = c("Q1", "Q2", "Q3", "Q4"),
  fill = c("#2b2bc5", "#149187", "#f18d0a", "#fff017"),
  title = "Quaters"
)


x = c(210,450,250,100,50,90)
y= c(' A','B','C','D','E','F')

pie(
  x,
  y,
  col=c("red","black","white","blue","purple","green"),
   main="Distance travelled "
)

