f <- read.csv("C:/Users/Артемий/dev/R/5semKr2/delayed_flights.csv") 
association.test<-function(v) { 
  m=matrix(v, nrow=2, ncol=2) 
  res=fisher.test(m) 
  res$p.value 
} 
head(f, n=5)

s<-apply(f[,3:6], 1, association.test) 
ff1<-cbind(f, s) 
pv_norm <- sum(s < 0.05) 
pv_bon <- sum(p.adjust(s, method="bonferroni") < 0.05) 
pv_bh <- sum(p.adjust(s, method="BH") < 0.05) 

exam = read.table("C:/Users/Артемий/dev/R/5semKr2/exam.tab")
plot(exam$passed,exam$score)
logReg <- glm(exam$passed~exam$score, family = "binomial")
logReg
summary(logReg)

cam=read.csv("C:/Users/Артемий/dev/R/5semKr2/camera_price.csv")
head(cam)
attach(cam)
plot(Macro.focus.range, Price)
plot(Dimensions, Price)

lm1<-lm(Price~Macro.focus.range+Dimensions, data=cam)
plot(lm1)
newcam=data.frame(Macro.focus.range=3, Dimensions=210)
newcam
predict(lm1, newcam)

film1 = read.csv("C:/Users/Артемий/dev/R/5semKr2/film_popularity.csv")
fit1=lm(Popularity~Actor,data=film1)
fit2=lm(Popularity~Director,data=film1)
fit3=lm(Popularity~Director+Actor,data=film1)
attach(film1)
dim(fit1)
head(film1, n=5)
plot(Actor,Popularity)
abline(fit1)
anova(fit1, fit2)
anova(fit2, fit3)
anova(fit1, fit3)

pot=read.table("C:/Users/Артемий/dev/R/5semKr2/pottery.txt", header=T)
set.seed(123)
potsc=scale(pot)
km <- kmeans(potsc,5)
km
summary(km)
head(potsc, n=5)
km$size


blood = read.table("C:/Users/Артемий/dev/R/5semKr2/blood.txt",  header = T)
blood
blood1 = as.matrix(blood)
blood2 = cov2cor(blood1)
blood2
pca<-princomp(blood2, cor = T)
summary(pca)