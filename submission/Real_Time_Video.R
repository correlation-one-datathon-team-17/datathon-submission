library(ggplot2)
library(maps)
library(mapdata)
library(animation)
library(ggmap)
library(mapproj)
library(reshape2)
library(anytime)

data <- read.csv("uber_trips_2014_1.csv",stringsAsFactors = FALSE)
data1 <- data[1:1000,]
data1$date <- as.POSIXct(data1$pickup_datetime, tz = '', format = "%m/%d/%Y %H:%M")

plotfunc <- function(x) {
  df <- subset(data1,date <= x)
  ggmap(get_googlemap(center = c(lon = -74,lag = 40.74),zoom= 13 ,maptype='roadmap'),,extent='device')+
    geom_point(data=df,aes(x=pickup_longitude,y=pickup_latitude),colour = 'red',alpha=0.7)
}

time <- sort
ani.options(convert = "C:\\MyDownloads\\Download\\ImageMagick-7.0.5-Q16\\convert.exe")
ani.options(ffmpeg = "C:\\Users\\Cathy\\Downloads\\ffmpeg-20170404-1229007-win64-static\\ffmpeg-20170404-1229007-win64-static\\bin\\ffmpeg.exe")
saveVideo(for( i in time) print(plotfunc(i)))
