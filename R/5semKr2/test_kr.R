laptop=read.csv(file="C:/Users/Артемий/dev/R/5semKr2/laptop_price.csv", header=T)

head(laptop, n=5)
fit2=lm(Price_RUR ~ Memory_Gb+HDD_Gb+HDD_type, data=laptop)
fit1=lm(Price_RUR ~ Memory_Gb, data=laptop)
anova(fit1, fit2)


plot(mtcars$mpg, mtcars$wt)
head(mtcars, n = 5)
lm1<-lm(mtcars$wt~mtcars$mpg)
abline(lm1, col='red')
lm1$coefficients
lm1$coefficients[1]
plot(mtcars$mpg, lm1$residuals, pch=19, col='red')
plot(density(lm1$residuals), col='red', main="")
