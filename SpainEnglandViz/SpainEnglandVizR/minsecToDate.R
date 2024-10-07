library("lubridate")
library("bupaverse")

toDateFormat <- function(min, sec) {
  if (min < 60) {
    date <- paste("2000-01-01", paste("0", min, sec, sep=":"), sep = " ")
  } else {
    date <- paste("2000-01-01", paste("1", min-60, sec, sep=":"), sep = " ")
  }
  return(as.POSIXct(date, tz="", format="%Y-%m-%d %H:%M:%S"))
}

