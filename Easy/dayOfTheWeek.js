/*
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:
Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"
*/





//We add the total days from 1971 until the current date. We find its remainder with 7. We know the first day of 1971 was a Friday. We use that info to find the 
//current day.
/**
 * @param {number} day
 * @param {number} month
 * @param {number} year
 * @return {string}
 */
var dayOfTheWeek = function(day, month, year) {
    var i,d={},r=0;
    
    for(var i=1971;i<year;i++){					//Calculating the no. of days just nefore the current year, starting from 1st January,1971.
        if(i%4!=0)															
            r+=365;
        else
            if(i%100!=0)
                r+=366;
            else if(i%100==0 && i%400==0)
                r+=366;
            else
                r+=365;
    
    }
    
    if(year%4!=0)															
        d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};			//Adding the days in the current year
    else
        if(year%100!=0)
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};
        else if(year%100==0 && year%400==0)
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};
        else
            d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31};
    
    for(i=1;i<month;i++)							
        r+=d[i];
    
    r+=day;									//r stores the total no. of days from 1971. We find its remainder when divided by 7.
    
    var ans={0:'Thursday',1:'Friday',2:'Saturday',3:'Sunday',4:'Monday',5:'Tuesday',6:'Wednesday'}	//1st January, 1971 was a Friday.
    
    var j=r%7;
    return ans[j];
};
