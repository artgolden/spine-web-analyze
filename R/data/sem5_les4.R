signups = read.csv("dev/R/data/signups.csv", header = TRUE)

install.packages("dplyr")

signups

data.frame(signups)



a = signups[signups$device == "1"]

nrow(signups)
head(signups)

