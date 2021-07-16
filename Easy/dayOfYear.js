/*
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41

Example 3:
Input: date = "2003-03-01"
Output: 60

Example 4:
Input: date = "2004-03-01"
Output: 61
*/





/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    var d={},r=0;
    var dates=date.split("-");
    for(var i=0;i<dates.length;i++)
        dates[i]=parseInt(dates[i]);
    
    if(dates[0]%4!=0)															//Defining d as the days in the months of a year, in accordance with if its a leap year or not
        d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};
    else
        if(dates[0]%100!=0)
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};
        else if(dates[0]%100==0 && dates[0]%400==0)
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};
        else
            d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};
    
    for(i=1;i<dates[1];i++)							//Adding the days in the months before the given month
        r+=d[i];
    
    r+=dates[2];									//Adding the days of the final month
    
    return r;
};
