x <- c(21, 34, 48, 57, 68, 75, 77, 68, 57, 48, 34, 21)
y <- c("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC")

# plotting bar
bp <- barplot(
  x, # mathematical value
  names.arg = y, # x axis values
  main = "Sales Report of 2025", # the heading
  ylim = c(0, 85), # y starts from 0 and ends at 100
  width = 1, # bar width
  space = 0, # gap between bars
  col = c("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#aec7e8", "#ffbb78")
)

# adding text into it
text(
  x = bp, # bar positision
  y = x + 2, # slight above bar,
  label = x
)
