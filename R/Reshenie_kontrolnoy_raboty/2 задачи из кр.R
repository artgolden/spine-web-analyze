#---------------------------------------------------------------------
#Варианты 1 и 2, 2 задача (Критерий ранговых сумм)

#Ставим галочку в Packages!! Или вместо этого запускаем строку:
library(exactRankTests)

#Можно создать отдельные переменные для всех трех вариантов файлов
data1 = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")
data2 = read.table(choose.files(default = ""), header = TRUE, sep = " ", dec = ".")
data3 = read.table(choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

h_1 = data1[[1]] #ставим двойные скобки, чтобы получить именно столбец значений
w_1 = data1[[2]]



wilcox.exact(w_1, h_1, paired = FALSE, alternative = "greater", exact = TRUE)
wilcox.test(w_1, h_1, paired = TRUE, alternative = "less", exact = FALSE)

b = sum(w_1 > h_1)
n = length(w_1)

binom.test(b, n, p=0.5, alternative = "less")

t.test (w_1, h_1, alternative = "less", mu = 0, paired = TRUE)

#---------------------------------------------------------------------
#Варианты 3 и 4, 2 задача (Критерий ранговых сумм)

#Ставим галочку в Packages!! Или вместо этого запускаем строку:
library(exactRankTests)

usual = read.table(choose.files(default = ""), header = FALSE, sep = " ", dec = ",")
new = read.table(choose.files(default = ""), header = FALSE, sep = " ", dec = ",")

usual_data = usual[[1]] #ставим двойные скобки, чтобы получить именно столбец значений
new_data = new[[1]]


wilcox.exact(new_data, usual_data, paired = FALSE, alternative = "greater", exact = TRUE)
wilcox.test(new_data, usual_data, paired = FALSE, alternative = "greater", exact = FALSE)

