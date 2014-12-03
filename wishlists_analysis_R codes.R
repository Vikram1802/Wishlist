###---Please use R studio or R for running the code---###
#Datasets used wishlist_bb_amazon_revised,wishlist_bb_only_revised.json,bb_amazon_oo_error.json, bb_only_oo_errors.json

getwd() #Getting the current working directory
setwd("F:/Beachbody_amazon/Ara/wishlists") #set you working directory and put all your datasets in that directory to use them
install.packages("jsonlite") #install package jsonlite
library(jsonlite)
library(dplyr)

# You can skip the next two lines of code
#checking for error if using openoffice (number of characters exceeding the cell size limit)

amazon_bb<-which(lapply(readLines('F:/Beachbody_amazon/Ara/wishlists/wishlist_bb_amazon_revised.json'), function(x) tryCatch({jsonlite::fromJSON(x); 1}, error=function(e) 0)) == 0) #finding the rows causing error while reading json file
bb_only<-which(lapply(readLines('F:/Beachbody_amazon/Ara/wishlists/wishlist_bb_only_revised.json'), function(x) tryCatch({jsonlite::fromJSON(x); 1}, error=function(e) 0)) == 0)

#Exporting the json files in R
amazon_bb_final1<-rbind_all(lapply(readLines('F:/Beachbody_amazon/Ara/wishlists/bb_amazon_oo_error.json'), jsonlite::fromJSON)) # Reading the bb_amazon wishlist json file in R after cleaning
bb_only_final1<-rbind_all(lapply(readLines('F:/Beachbody_amazon/Ara/wishlists/bb_only_oo_errors.json'), jsonlite::fromJSON)) # Reading the bb_only wishlist json file in R 
names(amazon_bb_final1) #to check the column names in the data
names(bb_only_final1) #to check the column names in the data

amazon_bb_final<-amazon_bb_final1[,2] # new dataset with only the names column
bb_only_final<-bb_only_final1[,2] # new dataset with only the names column
count_bb_amazon <- as.data.frame(table(amazon_bb_final$name))
sorted_count<- count_bb_amazon[order(-count_bb_amazon$Freq),] # sorted count of each product (frequency based for beachbody+amazon)
count_bb_only <- as.data.frame(table(bb_only_final$name))
sorted_count<- count_bb_only[order(-count_bb_amazon$Freq),] # sorted count of each product (frequency based for beachbody+amazon)

#-----Not required------# 

#Product_names_Intersection <- merge(amazon_bb_final,bb_only_final,by="name")
#fix(Product_names_Intersection)
#count_bb_amazon <- as.data.frame(table(amazon_bb_final$name))
#sorted_count<- count_bb_amazon[order(-count_bb_amazon$Freq),]
#fourhundred1<-rbind_all(lapply(readLines('F:/Beachbody_amazon/Ara/wishlists/400.json'), jsonlite::fromJSON))
#oneeightyseven1<-rbind_all(lapply(readLines('F:/Beachbody_amazon/Ara/wishlists/187.json'), jsonlite::fromJSON))
#fourhundred<-fourhundred1[,2]
#oneeightyseven<-oneeightyseven1[,2]
#Product_names_Intersection_four <- merge(bb_only_final,fourhundred,by="name")
#Product_names_Intersection_one <- merge(bb_only_final, oneeightyseven,by="name")
#names(fourhundred)
#total <- merge(matching_bb_amazon,Matching_bb_only,by="Email_ID")
