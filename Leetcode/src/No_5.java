public class No_5 {

    //方法1：暴力
    public String violence(String s) {
        char[] charArray = s.toCharArray();
        int begin = 0;
        int maxLen = 1;
        int len = s.length();

        for (int i = 0; i < len - 1; i++) {
            for (int j = i + 1; j < len; j++) {
                if (j - i + 1 > maxLen && vaildPalindromic(charArray, i, j)) {
                    begin = i;
                    maxLen = j - i + 1;
                }
            }
        }
        return s.substring(begin, begin + maxLen);
    }

    public boolean vaildPalindromic(char[] charArray, int left, int right) {
        while (left < right) {
            if (charArray[left] != charArray[right]) {
                return false;
            } else {
                left += 1;
                right -= 1;
            }
        }
        return true;
    }

    //方法2：中心扩散法
    public String centerSpread(String s){
        char[] charArray = s.toCharArray();
        int len = s.length();
        int maxLen = 1;
        int begin = 0;

        for(int i = 0; i < len - 1; i++){
            int oddLen = expandCenter(charArray, i, i, len);
            int evenLen = expandCenter(charArray, i, i+1, len);
            int tempMax = Math.max(oddLen, evenLen);
            if(tempMax > maxLen){
                maxLen = tempMax;
                begin = i - (maxLen - 1)/2;
            }
        }
        return s.substring(begin, begin + maxLen);
    }

    public int expandCenter(char[] charArray, int left, int right, int len){
        while(left >= 0 && right < len){
            if(charArray[left] != charArray[right]){
                return right - left - 1;
            }
            else {
                left--;
                right++;
            }
        }
        return right - left - 1;
    }

    //方法3：动态规划
    public String dp(String s){
       int len = s.length();
       if(len < 2){
           return s;
       }

       int maxLen = 1;
       int begin = 0;

       char[] charArray = s.toCharArray();

       boolean[][] dp = new boolean[len][len];
       for(int i = 0; i < len; i++){
           dp[i][i] = true;
       }

       for(int j = 1; j < len; j++){
           for(int i = 0; i < j; i++){
               if(charArray[i] != charArray[j]){
                   dp[i][j] = false;
               }
               else {
                   if(j - i + 1 < 3){
                       dp[i][j] = true;
                   }
                   else {
                       dp[i][j] = dp[i+1][j-1];
                   }
               }

               if(dp[i][j] && j - i +1 > maxLen){
                   maxLen = j - i + 1;
                   begin = i;
               }

           }
       }
       return s.substring(begin, begin + maxLen);

    }

}
