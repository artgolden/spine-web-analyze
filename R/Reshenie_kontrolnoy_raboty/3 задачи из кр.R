<<<<<<< HEAD
#---------------------------------------------------------------------
#Варианты 2 и 3, 3 задача (Критерии знаковый и знако-ранговый)

#Ставим галочку в Packages!! Или вместо этого запускаем строку:
library(exactRankTests)

data = read.table(choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

smoke_do = data[[1]]
smoke_posle = data[[2]]
co2_do = data[[3]]
co2_posle = data[[4]]

#--- 1 вариант решения - сравнить попарно --------------------------------------- 
wilcox.exact(smoke_posle, smoke_do, paired = TRUE, alternative = "less", exact = TRUE)
wilcox.exact(co2_posle, co2_do, paired = TRUE, alternative = "less", exact = TRUE)
wilcox.exact(co2_do, smoke_do, paired = TRUE, alternative = "two.sided", exact = TRUE)
wilcox.exact(co2_posle, smoke_posle, paired = TRUE, alternative = "greater", exact = TRUE)

#Критерий знаков:
b_do = sum(co2_do > smoke_do) #Количество Y_i > X_i
b_posle = sum(co2_posle > smoke_posle)
n = length(smoke_do) 
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b_do, n, p=0.5, alternative = "two.sided")
binom.test(b_posle, n, p=0.5, alternative = "greater")

#-----2 вариант решения (!) - сравнить разницы------------------------
smoke_dif = smoke_posle - smoke_do
co2_dif = co2_posle - co2_do

wilcox.exact(co2_dif, smoke_dif, paired = TRUE, alternative = "greater", exact = TRUE)

#Критерий знаков:
b_dif = sum(co2_dif > smoke_dif) #Количество Y_i > X_i
n = length(smoke_dif) 
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b_dif, n, p=0.5, alternative = "greater")

#---------------------------------------------------------------------
#Варианты 1 и 4, 3 задача (Критерии знаковый и знако-ранговый)

#Ставим галочку в Packages!! Или вместо этого запускаем строку:
library(exactRankTests)

di_data = read.table(choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

di_do = di_data[[1]]
di_posle = di_data[[2]]

wilcox.test(di_posle, di_do, paired = TRUE, alternative = "greater", exact = FALSE)
wilcox.exact(di_posle, di_do, paired = TRUE, alternative = "greater", exact = TRUE)

#Критерий знаков:
b = sum(di_posle > di_do) #Количество Y_i > X_i
n = length(di_do) 
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b, n, p=0.5, alternative = "greater")



=======
#---------------------------------------------------------------------
#Варианты 2 и 3, 3 задача (Критерии знаковый и знако-ранговый)

#Ставим галочку в Packages!! Или вместо этого запускаем строку:
library(exactRankTests)

data = read.table(choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

smoke_do = data[[1]]
smoke_posle = data[[2]]
co2_do = data[[3]]
co2_posle = data[[4]]

#--- 1 вариант решения - сравнить попарно --------------------------------------- 
wilcox.exact(smoke_posle, smoke_do, paired = TRUE, alternative = "less", exact = TRUE)
wilcox.exact(co2_posle, co2_do, paired = TRUE, alternative = "less", exact = TRUE)
wilcox.exact(co2_do, smoke_do, paired = TRUE, alternative = "two.sided", exact = TRUE)
wilcox.exact(co2_posle, smoke_posle, paired = TRUE, alternative = "greater", exact = TRUE)

#Критерий знаков:
b_do = sum(co2_do > smoke_do) #Количество Y_i > X_i
b_posle = sum(co2_posle > smoke_posle)
n = length(smoke_do) 
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b_do, n, p=0.5, alternative = "two.sided")
binom.test(b_posle, n, p=0.5, alternative = "greater")

#-----2 вариант решения (!) - сравнить разницы------------------------
smoke_dif = smoke_posle - smoke_do
co2_dif = co2_posle - co2_do

wilcox.exact(co2_dif, smoke_dif, paired = TRUE, alternative = "greater", exact = TRUE)

#Критерий знаков:
b_dif = sum(co2_dif > smoke_dif) #Количество Y_i > X_i
n = length(smoke_dif) 
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b_dif, n, p=0.5, alternative = "greater")

#---------------------------------------------------------------------
#Варианты 1 и 4, 3 задача (Критерии знаковый и знако-ранговый)

#Ставим галочку в Packages!! Или вместо этого запускаем строку:
library(exactRankTests)

di_data = read.table(choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

di_do = di_data[[1]]
di_posle = di_data[[2]]

wilcox.test(di_posle, di_do, paired = TRUE, alternative = "greater", exact = FALSE)
wilcox.exact(di_posle, di_do, paired = TRUE, alternative = "greater", exact = TRUE)

#Критерий знаков:
b = sum(di_posle > di_do) #Количество Y_i > X_i
n = length(di_do) 
# Критерий знаков = бином.критерий с H_0: p=0.5
binom.test(b, n, p=0.5, alternative = "greater")



>>>>>>> 426d272dfb6c61356a4ecc5effec1bfae4179cfb
