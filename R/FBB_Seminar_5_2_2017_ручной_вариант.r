
#Задача №2
#Загружаем данные из файла:
adults = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")
babies = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

#Считаем объемы выборок 
#NB! в зависимости от способа хранения данных подсчет объемов может различаться!
ad = adults[[1]]
ba = babies[[1]]
k=2 #количество выборок

#Все данные добавляем в один массив
total = c(adults[[1]], babies[[1]])

wilcox.test(ad, ba, paired = FALSE, alternative = "less", exact = FALSE)

var.test (ad, ba, ratio=1, alternative = "two.sided")

t.test (ad, ba, alternative = "two.sided", mu = 0, paired = FALSE, var.equal = FALSE)

#Создаем отдельный массив с наименованиями категорий (факторов)
g = factor(rep(1:2, c(n1, n2)), labels = c("adult", "baby"))

#Применим критерий Краскела-Уоллиса с использованием столбца факторов
kruskal.test(total, g)

#Задача №2
#Загружаем данные из файла:
cows = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")
#babies = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

#Считаем объемы выборок 
#NB! в зависимости от способа хранения данных подсчет объемов может различаться!
gr1 = length(nurses[[1]])
gr2 = length(nurses[[2]])
gr3 = length(nurses[[3]])
k=3 #количество выборок

nurses
#Все данные добавляем в один массив
total = c(nurses[[1]], nurses[[2]], nurses[[3]])
total

#Создаем отдельный массив с наименованиями категорий (факторов)
g = factor(rep(1:3, c(gr1, gr2, gr3)), labels = c("light", "medium", "tought"))

#Применим критерий Краскела-Уоллиса с использованием столбца факторов
kruskal.test(nurses)

posthoc.kruskal.dunn.test(cows, p.adjust.method = "none")

#Посчитаем средние ранги по группам:
Rteacher = sum(rank(total_school, ties.method = "average")*(g == "teacher"))/n1
Radmin = sum(rank(total_school, ties.method = "average")*(g == "admin"))/n2
Rpersonal = sum(rank(total_school, ties.method = "average")*(g == "personal"))/n3

NNplus1 = (n1 + n2 + n3)*(n1 + n2 + n3 + 1)
alphaNew = 0.05/k/(k-1)
#считаем квантиль N(0, 1), используемый при множественных сравнениях
z = qnorm(alphaNew, mean = 0, sd = 1, lower.tail = FALSE)

#Считаем поправку для критерия Данна
#as.factor(total_school): теперь воспринимаем значения в total_school как значения(уровни) фактора
#table(as.factor(total_school)): группируем значения в total_school по различным значениям фактора,
#то есть в нашей задаче считаем, сколько у нас есть людей каждого возраста
#as.data.frame(...): для удобства переводим в формат data.frame
for_B = as.data.frame(table(as.factor(total_school)), row.names = NULL)
#Для понимания переименовали столбцы (возраст и частота возраста):
colnames(for_B) = c("age", "freq")
#Теперь высчитываем поправку по формуле:
#r = количество групп = количество строк в таблице for_B
B_adj = sum(((for_B[["freq"]])^3-(for_B[["freq"]]))/12/ (n1 + n2 + n3 - 1))
#sum: суммируем по всем строкам в таблице

#Выражение, с которым мы сравниваем модуль разности средних рангов (при необходимости подставить нужные n_i)
Right_part = z*sqrt(NNplus1/12 - B_adj)*sqrt(1/n1+1/n2)
Right_part
Rteacher - Rpersonal
Radmin - Rpersonal

#Считаем p-value для каждой пары вручную:
2*pnorm(abs(Rteacher - Radmin)/sqrt(NNplus1/12-B_adj)/(sqrt(1/n1+1/n2)), mean = 0, sd = 1, lower.tail = FALSE)
2*pnorm(abs(Rteacher - Rpersonal)/sqrt(NNplus1/12-B_adj)/(sqrt(1/n1+1/n3)), mean = 0, sd = 1, lower.tail = FALSE)
2*pnorm(abs(Radmin - Rpersonal)/sqrt(NNplus1/12-B_adj)/(sqrt(1/n2+1/n3)), mean = 0, sd = 1, lower.tail = FALSE)





