#Для "проблемных" выборок и точного критерия вместо wilcox.test 
#можно использовать wilcox.exact, который содержится в пакете "exactRankTests".
#Устанавливаем пакет:

install.packages("exactRankTests")

#Ставим галочку в Packages или вместо этого запускаем строку:
library(exactRankTests)

#Загружаем данные из файлов:
female_data = read.table(choose.files(default = ""), header=TRUE, sep=";", dec = ",")
male_data = read.table(choose.files(default = ""), header=TRUE, sep=";", dec = ",")
#NB! Проверить, как хранятся данные в файле (разделитель, есть ли название столбцов...)

#Формируем столбцы чисел:
female=female_data[[1]]
male = male_data[[1]]

#1ая задача. Критерий ранговых сумм (ставим paired = FALSE!!):
#пункт а):
wilcox.exact(female, male, paired = FALSE, alternative = "less", exact = TRUE)
wilcox.test(female, male, paired = FALSE, alternative = "less", exact = TRUE)

#пункт б):
wilcox.exact(female, male, paired = FALSE, alternative = "two.sided", exact = TRUE)
wilcox.test(female, male, paired = FALSE, alternative = "two.sided", exact = FALSE)


#2ая задача. Оценка Ходжеса-Лемана (добавили conf.int = TRUE):
wilcox.exact(female, male, paired = FALSE, alternative = "less", exact = TRUE, conf.int = TRUE)
wilcox.test(female, male, paired = FALSE, alternative = "less", exact = FALSE, conf.int = TRUE)

#3я задача. Ошибка в данных:
#Создадим female_2 с ошибкой в последнем значении (увелич.в 10 раз):
female_2 = female
f_length = length(female)
female_2[f_length] = female_2[f_length]*10

#Проверим, что оценка Ходжеса-Лемана относительно устойчива
#к выбросам и ошибкам в данных:
wilcox.exact(female_2, male, paired = FALSE, alternative = "less", exact = TRUE, conf.int = TRUE)
wilcox.test(female_2, male, paired = FALSE, alternative = "less", exact = FALSE, conf.int = TRUE)


