/*
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes 
immediately after second.
Return an array of all the words third for each occurrence of "first second third".

Example 1:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:
Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
*/





/**
 * @param {string} text
 * @param {string} first
 * @param {string} second
 * @return {string[]}
 */
var findOcurrences = function(text, first, second) {
    var words=text.split(" ");								//Splits the string into an array of its words
    var i=0,l=[];

    while(i<words.length-2){
        if(words[i]==first && words[i+1]==second)
            l.push(words[i+2]);
        i+=1;
    }
    
    return l;
};
