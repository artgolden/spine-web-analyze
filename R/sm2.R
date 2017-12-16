t = 470
s = 130
qbinom(0.03, 470, 0.34)
pbinom(140, 470, 0.34)
pbinom(141, 470, 0.34)
#ncrit = 140 => отвергнуть Н0
pbinom(140, 470, 0.27, lower.tail = FALSE)
# 7.99%
