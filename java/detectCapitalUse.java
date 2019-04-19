/***

Coding Problem: https://leetcode.com/problems/detect-capital/

Statistics: 

  Runtime: 2 ms, faster than 81.36% of Java online submissions for Detect Capital.
  Memory Usage: 36.9 MB, less than 90.12% of Java online submissions for Detect Capital.

***/

class Solution {
    public boolean detectCapitalUse(String word) {
        if (word.equals(word.toLowerCase())) { 
            return true;
        }
        else if (word.equals(word.toUpperCase())) {
            return true;
        }
        else if (word.charAt(0) == Character.toUpperCase(word.charAt(0)) &&
                word.substring(1).equals(word.substring(1).toLowerCase())) {
            return true;
        }   
        else {
            return false;
        }
        
    }
}
