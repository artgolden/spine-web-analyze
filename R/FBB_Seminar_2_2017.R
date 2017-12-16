#Задача 1
#Загружаем данные из файла:
data = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")
#header = TRUE: в исходном файле в первой строке были указаны названия столбцов
#dec = ".": в исходном файле в качестве десятичного разделителя выбрана точка

#Теперь формируем отдельные столбцы:
weight_do = data[[1]]
weight_posle = data[[2]]
#ставим двойные скобки, чтобы получить именно столбец значений

#Важно!! Весь код ниже подходит только для случая левой альтернативы!

#----------------Критерий знаков-------------------------------------------
b = sum(weight_posle > weight_do) #Количество Y_i > X_i
n = length(weight_do)
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b, n, p=0.5, alternative = "less")
#или вручную p-value с помощью функции распределения (что одно и то же)
pbinom(b, n, 0.5, lower.tail = TRUE)


#Асимпт.критерий знаков = асимпт.бином.критерий:
#Квантиль станд.нормального распределения (задает крит.множество):
qnorm(0.05, mean = 0, sd = 1, lower.tail = TRUE)
#Находим новую статистику B*:
B_star = (b - n*0.5) / sqrt(n*0.5*(1-0.5))
B_star
#Cравниваем B_star и квантиль и делаем вывод.

#p-value для асимпт.бином.критерия:
pnorm(B_star, mean = 0, sd = 1, lower.tail = TRUE)


#Для точного критерия знаков = бином.критерия можно построить крит.множ-во.
#Находим для этого квантиль бином.распределения:
qb = qbinom(0.05, n, prob = 0.5, lower.tail = TRUE)
qb
#Из-за разрывности функции распределения бином.распр-я квантиль находится
#неточно, при левосторон.альтернативе надо взять на 1 меньше, проверим это:
pbinom(qb-1, n, 0.5, lower.tail = TRUE)
pbinom(qb, n, 0.5, lower.tail = TRUE)
#при qb-1 получаем <0.05, при qb получаем >0.05 (что плохо)

#Далее для точного критерия знаков можно построить функцию мощности
#как функцию от вероятности p = P(Y_i - X_i > 0) = P(theta + e_i > 0)
power = function(p) {pbinom(qb-1, n, p, lower.tail = TRUE)}
plot(power, 0, 0.5, xlab = "p", ylab = "The power function")
power(0.5)

#-------------------Знако-ранговый критерий---------------------------------------------

#Для "проблемных" выборок и точного критерия вместо wilcox.test
#можно использовать wilcox.exact, который содержится в пакете "exactRankTests".
#Устанавливаем пакет:
install.packages("exactRankTests")

#Ставим галочку в Packages или вместо этого запускаем строку
library(exactRankTests)

wilcox.test(weight_posle, weight_do, paired = TRUE, alternative = "less", exact = TRUE)
wilcox.exact(weight_posle, weight_do, paired = TRUE, alternative = "less", exact = TRUE)

#Для получения медианы Ходжеса - Лемана (оценки theta) ставим в конце conf.int = TRUE:
wilcox.test(weight_posle, weight_do, paired = TRUE, alternative = "less", exact = TRUE, conf.int = TRUE)
wilcox.exact(weight_posle, weight_do, paired = TRUE, alternative = "less", exact = TRUE, conf.int = TRUE)

#---------------------------------------------------------------------------------------