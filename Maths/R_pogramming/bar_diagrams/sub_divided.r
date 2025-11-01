q1 <- c(220, 130, 140)
q2 <- c(150, 160, 155)
q4 <- c(120, 205, 180)
q3 <- c(90, 185, 195)

factories <- c("Factory1", "factory2", "factory3")

quater <- rbind(q1, q2, q3, q4)
bp <- barplot(
  quater,
  beside = FALSE,
  ylim = c(0, 800),
  col = c("#2b2bc5", "#149187", "#f18d0a", "#fff017"),
  border = 0,
  names.arg = factories
)

legend(
  "topleft",
  legend = c("Q1", "Q2", "Q3", "Q4"),
  fill = c("#2b2bc5", "#149187", "#f18d0a", "#fff017"),
  title = "Quaters"
)
