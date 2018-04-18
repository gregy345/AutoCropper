
##### below is explination for automated naming convention ####
Create 3 rows, each representing the settings.
The first row is the settings for pi.
Second row settings for ma.
Third row settings for he.

Each colum represents the take/round number.
The autocropper program inserts the correct mic/position number.

02, 01, 03, 04
03, 04, 05, 07
09, 12, 06, 08


An extra colum may need to be attached to end.  Hopefully I will have fixed this problem 
by the time you are reading this "ReadMe" file.


##### below is explination for algorithum that selects point to crop ####
1000 is a number b/c the first few seconds or so data points are 
zero and so any number is going to be infinitly higher then the moving average
7.4 is the ratio that works with 1000, nn is the length in seconds of the 
window for which the moving average is taken
