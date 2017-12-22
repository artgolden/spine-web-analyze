# Multiple plot function
#
# ggplot objects can be passed in ..., or to plotlist (as a list of ggplot objects)
# - cols:   Number of columns in layout
# - layout: A matrix specifying the layout. If present, 'cols' is ignored.
#
# If the layout is something like matrix(c(1,2,3,3), nrow=2, byrow=TRUE),
# then plot 1 will go in the upper left, 2 will go in the upper right, and
# 3 will go all the way across the bottom.
#
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  require(grid)

  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)

  numPlots = length(plots)

  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                    ncol = cols, nrow = ceiling(numPlots/cols))
  }

 if (numPlots==1) {
    print(plots[[1]])

  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))

    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))

      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}






#==========1=========
setwd('~/dev/R/5semKr1')
coord<-read.table('graphic_data2.tab')
head(coord)
plot(coord$func1~coord$x, type='l')
lines(coord$func2~coord$x)

#==========2=========
library(ggplot2, help, pos = 2, lib.loc = NULL)
library(dplyr, help, pos = 2, lib.loc = NULL)

bones<-read.csv('bones.txt', sep='\t')
head(bones, n=15)
attach(bones)
bones$age
old <- filter(bones, age > 16) 
young <- filter(bones, bones$age<16)
head(young, n=10)
boxplot(spnbmd~gender, data=young)
ggplot(young, aes(x=gender, y=spnbmd)) + geom_boxplot()
ggplot(bones$old, aes(x=bones$gender, y=bones$spnbmd)) + geom_boxplot()
multiplot(p,q)
p

#==========3=========

load('vector.RData')
vector
table(vector)


#==========6=========
petowner <- read.csv('pet_owner_data.csv', skip=1)
head(petowner)
sex <- read.csv('sex_data.csv')
head(sex)
fullpet<-left_join(petowner, sex, by='respondent')
head(fullpet, n=15)
vec<-c()
for(i in c('yes','no')){
  for(j in c('F', 'M')){
    filtered = filter(fullpet, pet.owner==i & sex==j)
    n = dim(filtered)[1]
    vec <- c(vec, n)
  }
}
vec
m <- matrix(vec, ncol=2, nrow=2)
m
pv<-fisher.test(m)$p.value
pv > 10**(-6)
pv < 10**(-5)

#==========7=========
movies<-read.table('movies.tab')
head(movies)
drama <- filter(movies, genre=='drama')
action <- filter(movies, genre=='action/adventure')
drama <- drama$box.office
action <- action$box.office
shapiro.test(drama)
shapiro.test(action)
wilcox.test(drama, action, alternative='l', paired=F)

popular <- filter(movies, score >= 55)
unpopular <- filter(movies, score < 55)
head(popular)
popular <- popular$running.time
unpopular <- unpopular$running.time
shapiro.test(popular)
shapiro.test(unpopular)
wilcox.test(popular, unpopular, alternative='g', paired=F)
t.test(popular, unpopular)


#==========8=========
genexp <- read.csv('gene_expression.csv')
head(genexp)
pvcol <- c()
for(i in c(1:dim(genexp)[1])){
  line = genexp[i,]
  normal = line[3:10]
  diseased = line[11:18]
  pvcol<- c(pvcol,t.test(normal, diseased, alternative='t', paired=F)$p.value)
}

head(pvcol)
genexp<-cbind(genexp, pvcol)
head(genexp)
final<-filter(genexp, pvcol<9.47e-07)
final
final2<-filter(genexp, pvcol>9.47e-07)
summary(final)