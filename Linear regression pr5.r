x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131) 
y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

relation <- lm(y ~ x)

# Save plot as PNG
png(file = "linearregression.png") 
plot(x, y, col = "blue", main = "Height & Weight Regression",
     cex = 1.3, pch = 16, xlab = "Height in cm", ylab = "Weight in Kg")
abline(relation, col = "red")  
dev.off()

# Display plot in RStudio
plot(x, y, col = "blue", main = "Height & Weight Regression",
     cex = 1.3, pch = 16, xlab = "Height in cm", ylab = "Weight in Kg")
abline(relation, col = "red")
