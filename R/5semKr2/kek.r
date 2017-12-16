#vlad mnev #ira
#zadanie1 #dasha
f <- read.csv("C:/Users/Артемий/dev/R/5semKr2/delayed_flights.csv") 
association.test<-function(v) { 
  m=matrix(v, nrow=2, ncol=2) 
  res=fisher.test(m) 
  res$p.value 
} 

s<-apply(f[,3:6], 1, association.test) 
ff1<-cbind(f, s) 
ff1
pv_norm <- sum(s < 0.05) 
pv_bon <- sum(p.adjust(s, method="bonferroni") < 0.05) 
pv_bh <- sum(p.adjust(s, method="BH") < 0.05) 
pv_bon
#без поправок - 110 
#с поправкой Бонферонни - 44 
#с поправкой BH - 82
#zadanie5
set.seed(123)
pot=read.table("pottery.txt", header=T)
potsc=scale(pot)
km <- kmeans(potsc,5)
km
#12, 14, 9, 5, 5
#zadanie3
cam=read.csv("C:/Users/Артемий/dev/R/5semKr2/camera_price.csv")
attach(cam)
plot(Effective.pixels+Dimensions,Price)
lm1<-lm(Price~Effective.pixels+Dimensions, data=cam)
summary(lm1)
newcam=data.frame(Effective.pixels=5, Dimensions=140)
predict(lm1,newcam)
#767
#zadanie4 (tchem men'she p-value, tem xuzhe??)
film1 = read.csv("film_popularity.csv")
fit1=lm(Popularity~Actor,data=film1)
fit2=lm(Popularity~Director,data=film1)
fit3=lm(Popularity~Director+Actor,data=film1)
plot(fit1)
anova(fit1, fit2)
anova(fit2, fit3)
anova(fit1, fit3)
#0.0127<0.05 --> повлияло добавление актера. режиссера можно убрать
#модель, использующая в качестве предиктора режиссера, значительно хуже, чем модель, использующая и актера, и режиссера
#можно без существенных потерь для модели исключить из нее предиктор режиссера
#0.0127
#zadanie2
exam = read.table("C:/Users/Артемий/dev/R/5semKr2/exam.tab")
plot(exam$passed,exam$score)
logReg <- glm(exam$passed~exam$score, family = "binomial")
logReg
summary(logReg)
#0.00446
#zadanie6
wine = read.table("C:/Users/Артемий/dev/R/5semKr2/wine.txt")
head(wine)
winsc = scale(wine)
pca<-prcomp(winsc, scale = T)
summary(pca)
#2.169 #2 компоненты (а почему 2 - это сумма компонент подходящих, здесь 1ая и 2ая)
#drugoi = livenskyi lesha
#zadanie1
f1<-read.csv("C:/Users/Артемий/dev/R/5semKr2/SNP_counts.csv")

association.test<-function(v) { 
         m=matrix(v, nrow=2, ncol=2) 
         res=fisher.test(m) 
         res$p.value 
     } 
s<-apply(f1[,4:7], 1, association.test) 
ff1<-cbind(f1, s) 
pv_norm <- sum(s < 0.01)
pv_bon <- sum(p.adjust(s, method="bonferroni") < 0.01) 
pv_bh <- sum(p.adjust(s, method="BH") < 0.01) 
pv_norm
pv_bon
pv_bh
#без поправок - 1111, бонферонни - 755, BH - 1009
#zadanie2
lm1<-lm(cars$dist~cars$speed)
summary(lm1)
#0.0123
#zadanie3
cam=read.csv("camera_price.csv")
lm1<-lm(Price~Max.resolution+Dimensions, data=cam)
newcam=data.frame(Max.resolution=1024,Dimensions=113)
predict(lm1,newcam)
#253.6834
#zadanie4
film1 = read.csv("C:/Users/Артемий/dev/R/5semKr2/film_popularity.csv")
fit1=lm(Popularity~Actor,data=film1)
fit2=lm(Popularity~Actress,data=film1)
fit3=lm(Popularity~Actress+Actor,data=film1)
anova(fit1, fit2)
anova(fit2,fit3)
anova(fit1,fit3)
#модель, использующая в качестве предиктора актрису, значимо хуже, чем модель, использующая и актера, и актрису
#можно без существенных потерь для модели исключить из нее предиктор главной актрисы
#0.02517
#zadanie5 #neuveren
pot=read.table("pottery.txt", header=T)
potsc=scale(pot)
hc1<-hclust(dist(potsc), method="complete")
plot(hc1)
hc2<-cutree(hc1, k=3)
hc2
#21 14 10
#zadanie6
blood = read.table("blood.txt",  header = T)
blood
blood1 = as.matrix(blood)
blood2 = cov2cor(blood1)
blood2
pca<-princomp(blood2, cor = T)
summary(pca)
#0.98 #2 компоненты (1,3)
#german 
#zadanie2 == rainy
smok=read.table("smoking.dat", header=T)
head(smok)
glm1<-glm(dead~age+smoke+pop, data=smok, family="poisson")
confint(glm1, level=0.95)

#zadanie1 == rainy (u germana otvet neveren???)
gene=read.csv("gene_activity.csv")
head(gene)
tail(gene)
pValues <- rep(NA,10563)
for(i in 1:10563){
norm<-gene[i,3:10]
mut<-gene[i,11:18]  
pValues[i] <- t.test(norm,mut, alternative="less")$p.value}
head(pValues)
sum(pValues<0.1) #1059
sum(p.adjust(pValues, method="bonferroni") < 0.1)#2
sum(p.adjust(pValues, method="BH") < 0.1)#3
#zadanie3 == rainy
cam=read.csv("C:/Users/Артемий/dev/R/5semKr2/camera_price.csv")
head(cam)
lm1<-lm(Price~Macro.focus.range+Dimensions, data=cam)
newcam=data.frame(Macro.focus.range=3, Dimensions=210)
newcam
predict(lm1, newcam)
#1341.284
#zadanie4 #rainy ne delala
fit1=lm(Popularity~Actor,data=film1)
fit2=lm(Popularity~Awards,data=film1)
fit3=lm(Popularity~Awards+Actor,data=film1)
anova(fit1, fit2)
anova(fit2,fit3)
anova(fit1,fit3)
#модель, использующая в качестве предиктора наличие наград, значимо хуже, чем модель, использующая и актера, и наличие наград
#можно без существенных потерь для модели исключить из нее предиктор наличие наград
#0.008196 

#у германа - модель, использующая в качестве предиктора наличие наград, значительно хуже, чем модель, использующая и актера, и наличие наград
#можно без существенных потерь для модели исключить из нее предиктор главного актера
#алена - ...главного актера, 2ое то же
#zadanie5 == rainy
pot=read.table("pottery.txt", header=T)
potsc=scale(pot)
hc1<-hclust(dist(potsc), method="single")
hc2<-cutree(hc1, k=4)
hc2
#20 1 14 10
#zadanie6 == rainy (зачем шкалирование? правда, здесь результат одинаков)
hep=read.table("C:/Users/Артемий/dev/R/5semKr2/heptathlon.txt",header=T)
head(hep)
hep
hepsc=scale(hep)
head(hepsc)
dim(hepsc)
hepsc

pca<-prcomp(hepsc)
summary(pca)
pca<-prcomp(hepsc, scale = T)
summary(pca)
#?  (по чему смотреть - 4 или 5, с 4 чуть меньше, с 5 чуть больше)?? 2,30
#4


