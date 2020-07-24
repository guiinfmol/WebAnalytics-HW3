
library("class")
library("dplyr")

sportal = read.csv2('Web_Anlaytics_Nov_2018_final.csv', sep="\t", dec=".",
                   na.strings = "", as.is = TRUE,
                   stringsAsFactors = FALSE)


#remove needless columns
sportal <- within(sportal, rm("Browser.Version",
                              "Device.Type",
                              "Device",
                              "OS.Version",
                              "User.Agent",
                              "Conversion.Time",
                              "Traffic.Source",
                              "Hit.Time",
                              "URL",
                              "Referring.URL",
                              "City",
                              "Region",
                              "Goal.1.Converted", 
                              "Goal.1.Converted.Time"))

#reduce rows for dev purposes
#sportal <- sportal[1:100,]

#take a random sample
set.seed(123)
sportal <- sample_n(sportal, 15000)

#keep only complete cases
sportal <- sportal[complete.cases(sportal), ]


#keep only width of resolution column and bin it
for (i in 1:nrow(sportal)) {
  #take width and convert to numeric to do comparisons later
  width <- strsplit(sportal[i,"Screen.Resolution"], "x")[[1]][1]
  width <- as.numeric(width)
  
  #bin it using Bootstrap's grid values
  if (width < 576){
    new_width <- "Extra Small"
  } else if (width < 768) {
    new_width <- "Small"
  } else if (width < 992) {
    new_width <- "Medium"
  } else if (width < 1200) {
    new_width <- "Large"
  } else {
    new_width <- "Extra Large"
  }
  
  sportal[i,"Screen.Resolution"] <- new_width

}

sort(table(sportal$Screen.Resolution), decreasing = T)


#Bin windows versions 
for (i in 1:nrow(sportal)) {
  #chech if dealing with windows
  if(grepl("Windows", sportal[i,"OS"], fixed=TRUE))
  {
    if(grepl("10", sportal[i,"OS"], fixed=TRUE) || 
       grepl("8.1", sportal[i,"OS"], fixed=TRUE) || 
       grepl("8", sportal[i,"OS"], fixed=TRUE) || 
       grepl("7", sportal[i,"OS"], fixed=TRUE) || 
       grepl("RT", sportal[i,"OS"], fixed=TRUE) || 
       grepl("Vista", sportal[i,"OS"], fixed=TRUE)
      )
      {
        sportal[i,"OS"] <- "Windows New"
    }
    if(grepl("XP", sportal[i,"OS"], fixed=TRUE) || 
       grepl("2000", sportal[i,"OS"], fixed=TRUE)
    )
    {
      sportal[i,"OS"] <- "Windows Old"
    }
    
    
  }
  
  #handle entires that just have windwos with no version attached to it
  if(identical(sportal[i,"OS"], "Windows")){
    sportal[i,"OS"] <- "Windows Old"
  }
}


sort(table(sportal$OS), decreasing = T)



#Hande odd OS 
for (i in 1:nrow(sportal)) {
 
  #handle Linux
  if(identical(sportal[i,"OS"], "Ubuntu") ||
     identical(sportal[i,"OS"], "Fedora")
     ){
    sportal[i,"OS"] <- "Linux"
  }
  
  #handle odd OS
  if(identical(sportal[i,"OS"], "Maemo") ||
     identical(sportal[i,"OS"], "FreeBSD") ||
     identical(sportal[i,"OS"], "MeeGo") ||
     identical(sportal[i,"OS"], "VRE") ||
     identical(sportal[i,"OS"], "Windows Mobile") ||
     identical(sportal[i,"OS"], "Firefox OS")
  ){
    sportal[i,"OS"] <- "Other"
  }
  
}


sort(table(sportal$OS), decreasing = T)




country_tresh <- 50
#Hande odd countires
countries <- table(sportal$Country)
for (i in 1:nrow(sportal)) {
  country_name <- sportal[i,"Country"]
  
  if(countries[country_name] < country_tresh){
    sportal[i,"Country"] <- "Other"
  }
  
  
}

sort(table(sportal$Country), decreasing = T)



lan_tresh <- 50
#Hande odd langiages
languages <- table(sportal$User.Language)
for (i in 1:nrow(sportal)) {
  language_name <- sportal[i,"User.Language"]
  
  if(languages[language_name] < lan_tresh){
    sportal[i,"User.Language"] <- "Other"
  }
  
  
}

for (i in 1:nrow(sportal)) {
  returning <- sportal[i,"Returning.Visitor"]
  
  if(returning == 'TRUE'){
    sportal[i,"Returning.Visitor"] <- 1
  }else{
    sportal[i,"Returning.Visitor"] <- 0
  }
}

sort(table(sportal$User.Language), decreasing = T)

sportal$Returning.Visitor <- as.numeric(sportal$Returning.Visitor)


a = c()

for(i in colnames(sportal)){
  i <- gsub("\\.", " ", i)
  a = c(a, i)
}

colnames(sportal) <- a

write.table(sportal, file = paste(getwd(), "/modified.csv", sep=""), sep="\t", dec=".", row.names = FALSE, quote = FALSE)










