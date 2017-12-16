ave(airquality)
a = airquality[airquality$Month == 5,]
b = a$Ozone
mean(b, na.rm=TRUE)

sss <- airquality[order(airquality$Month, airquality$Temp),]
sss
