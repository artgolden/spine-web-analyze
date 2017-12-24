install.packages("ggplot2")
library(ggplot2)

t <- seq(0, 120, 10)
# t <- seq(0, 2, 10)
t
# absorb = matrix(
sample1 = c(.822, .801, .794, .785, .778,
 .772, .766, .761, .755, .751, .747, .742, .738)
sample2 = c(.838, .810, NaN, .788, .780, .772, .766, .756, 
.750, .744, .739, .734, .729)
sample3 = c(.814, .784, .773, .761, .751, .742, .734, .726, .719, .712, .706,
 .700, .694)
sample4 = c(.809, .788, .774, .762, .752, .742, .731, .720, .711, .703,
 .696, .690, .683)
sample5 = c(.802, .762, .747, .738, .726, .711, .696, .668, .653, .631,
 .616, .602, .593)
sample6 = c(.803, .766, .745, .726, .713, NaN, .676, .662, .649, .636, .621,
 .611, .598)
sample7 = c(.770, .730, .704, .680, .657, .638, .612, .592, .571, .553, .536,
 .521, .504)
sample8 = c(.800, .738,  .709, .681, .653, .627, .603, .582, .561, .540, .520,
 .502, .485)
sample9 = c(.827, .782, .751, .719, .692, .668, .642, .619, .595, .576, .554,
 .534, .515)
sample10 = c(.840, .780, .742, .703, .665, .630, .595, .569, .538, .510, .482,
 .458, .435)
biochem.data = data.frame(t, sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8, sample9, sample10 )


fit = lm(sample1~t)
pdf("BiochemMasha2.pdf",width=8.3, height=5.8)

fits = c(0,coef(lm(sample1~t))[[2]], coef(lm(sample2~t))[[2]], coef(lm(sample3~t))[[2]], coef(lm(sample4~t))[[2]], coef(lm(sample5~t))[[2]], coef(lm(sample6~t))[[2]], coef(lm(sample7~t))[[2]], coef(lm(sample8~t))[[2]], coef(lm(sample9~t))[[2]], coef(lm(sample10~t))[[2]])
fits = fits * -1
pvk_conc = c(0,32, 48, 64, 80, 120, 160, 320, 480, 800, 1600)
speed = data.frame(fits, pvk_conc)
ggplot(speed, aes(x = pvk_conc, y = fits)) + 
  geom_point() + geom_line()
# qplot(pvk_conc, fits, geom="line")
dev.off()

pdf("BiochemMasha3.pdf", width=8.3, height=5.8)
fits = c(coef(lm(sample1~t))[[2]], coef(lm(sample2~t))[[2]], coef(lm(sample3~t))[[2]], coef(lm(sample4~t))[[2]], coef(lm(sample5~t))[[2]], coef(lm(sample6~t))[[2]], coef(lm(sample7~t))[[2]], coef(lm(sample8~t))[[2]], coef(lm(sample9~t))[[2]], coef(lm(sample10~t))[[2]])
fits = 1/(fits * -1)
pvk_conc = c(32, 48, 64, 80, 120, 160, 320, 480, 800, 1600)
pvk_conc = 1/pvk_conc
speed = data.frame(fits, pvk_conc)
ff = lm(fits~pvk_conc)
coo = coef(ff)
coo[[2]]

ggplot(speed, aes(x = pvk_conc, y = fits)) +
    geom_point() +
    geom_smooth(method = "lm", col = "red", se = FALSE, fullrange = T) +
    xlim(-0.001, 0.032)
# qplot(pvk_conc, fits, geom="line")
dev.off()

# tans = c()
# for (i in fits){
#     tans <- coef(i)
# }
# setwd('~/dev/R/')
pdf("BiochemMasha.pdf", width=8.3, height=5.8)

ggplot(biochem.data, aes(t, y = value, color = variable)) +
    geom_point(aes(y = sample1, col = "sample1")) +
    geom_point(aes(y = sample2, col = "sample2")) +
    geom_point(aes(y = sample3, col = "sample3")) +
    geom_point(aes(y = sample4, col = "sample4")) +
    geom_point(aes(y = sample5, col = "sample5")) +
    geom_point(aes(y = sample6, col = "sample6")) +
    geom_point(aes(y = sample7, col = "sample7")) +
    geom_point(aes(y = sample8, col = "sample8")) +
    geom_point(aes(y = sample9, col = "sample9")) +
    geom_point(aes(y = sample10, col = "sample10")) +
    geom_smooth(aes(y = sample1, col = "sample1"), method = "lm", se = FALSE) +  
    geom_smooth(aes(y = sample2, col = "sample2"), method = "lm", se = FALSE) +
    geom_smooth(aes(y = sample3, col = "sample3"), method = "lm", se = FALSE)+
    geom_smooth(aes(y = sample4, col = "sample4"), method = "lm", se = FALSE)+
    geom_smooth(aes(y = sample5, col = "sample5"), method = "lm", se = FALSE)+
    geom_smooth(aes(y = sample6, col = "sample6"), method = "lm", se = FALSE)+
    geom_smooth(aes(y = sample7, col = "sample7"), method = "lm", se = FALSE)+
    geom_smooth(aes(y = sample8, col = "sample8"), method = "lm", se = FALSE)+
    geom_smooth(aes(y = sample9, col = "sample9"), method = "lm", se = FALSE)+
    geom_smooth(aes(y = sample10, col = "sample10"), method = "lm", se = FALSE)+
    ylim(0,0.9)
    # scale_x_continuous(expand = c(0, 0)) + scale_y_continuous(expand = c(0,0))

dev.off()

