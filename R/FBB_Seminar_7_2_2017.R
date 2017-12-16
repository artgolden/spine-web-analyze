
#-----Задача № 1.1 (из семинара 3, зависимые выборки) -----------------------------------
weight_data = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

do = weight_data[[1]]
posle = weight_data[[2]]

#Если в Packages нет пакета exactRankTests, устанавливаем его:
install.packages("exactRankTests")

#Далее в любом случае ставим галочку в Packages или вместо этого запускаем строку
library(exactRankTests)

#Было ранее (непараметрические критерии, не требующие условия нормальности выборок):
#Знако-ранговый критерий (зависимые выборки!, paired = TRUE):
wilcox.exact(posle, do, paired = TRUE, alternative = "less", exact = TRUE)
#Если проблемы с загрузкой пакета exactRankTests, вместо wilcox.exact c exact = TRUE
#используем wilcox.test и exact = FALSE:
wilcox.test(posle, do, paired = TRUE, alternative = "less", exact = FALSE)

#Критерий знаков:
b = sum(posle > do) #Количество Y_i > X_i
n = length(do) 
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b, n, p=0.5, alternative = "less")

#Новый критерий (параметрический, требует условия нормальности выборок):
#Проверяем равенство средних с помощью t-теста для зависимых (paired = TRUE!!) выборок
t.test (posle, do, alternative = "less", mu = 0, paired = TRUE)


#-----Задача № 1.2 (из семинара 3, зависимые выборки) -----------------------------------

????????????????????????

#-----Задача № 2-------------------------------------------------------------------------
towns_data = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

skov = towns_data[[1]]
kastrul = towns_data[[2]]

#Новый критерий (параметрический, требует условия нормальности выборок):

#Выборки независимы, 
#поэтому сначала для t-теста должны проверить равенство дисперсий!!
var.test (skov, kastrul, ratio=1, alternative = "two.sided")
#Получаем, что p-value близко к 0 => дисперсии не равны!

#Применяем t-тест для независимых выборок (paired = FALSE) и неравных дисперсий (var.equal = FALSE)
t.test (skov, kastrul, alternative = "greater", mu = 0, paired = FALSE, var.equal = FALSE)

#Было ранее (непараметрический критерий, не требующий условия нормальности выборок):

#Если в Packages нет пакета exactRankTests, устанавливаем его:
install.packages("exactRankTests")

#Далее в любом случае ставим галочку в Packages или вместо этого запускаем строку
library(exactRankTests)

#Критерий ранговых сумм (независимые выборки, paired = FALSE):
#wilcox.exact(skov, kastrul, paired = FALSE, alternative = "greater", exact = TRUE)
#Если считает очень долго или не скачивается пакет exactRankTests, запускаем строку
wilcox.test(skov, kastrul, paired = FALSE, alternative = "greater", exact = FALSE)


#-----Задача № 3--------------------------------------------------------------------------

??????????????????????


