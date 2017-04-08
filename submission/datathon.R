library(ggplot2)
library(maps)
library(ggmap)
library(mapproj)
library(reshape2)
library(anytime)

data <- read.csv("uber_trips_2014_1.csv",stringsAsFactors = FALSE)
class(data$pickup_datetime)
data$date <- anytime(data$pickup_datetime, tz = '' ,asUTC =  FALSE)

data$date <- as.POSIXct(data$pickup_datatime)
                        , tz = '', format = "%m/%d/%Y %H:%M")


time <- data$pickup_datetime

plotfunc <- function(x) {
  df <- subset(data,date <= x)
  df <- 
  p <- ggmap(get_googlemap(center = 'new york city', zoom= 7 ,maptype='roadmap'),,extent='device')+
    geom_point(data=df,aes(x=pickup_longitude,y=pickup_latitude),colour = 'red',alpha=0.7)
}
# 获取地震的日期
time <- sort(unique(data$date))
# 生成并保存动画
saveMovie(for( i in time) print(plotfunc(i)))

