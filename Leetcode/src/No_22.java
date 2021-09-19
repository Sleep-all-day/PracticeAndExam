/*
数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
有效括号组合需满足：左括号必须以正确的顺序闭合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]
*/


import java.util.ArrayList;
import java.util.List;

public class No_22 {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        int left = n;
        int right = n;
        backtrack(res, new StringBuilder(), left, right);
        return res;
    }

    public void backtrack(List<String> res, StringBuilder cur, int left, int right){
        if(left == 0 && right == 0){
            res.add(cur.toString());
        }
        if(left != 0){
            backtrack(res, cur.append("("), left-1, right);
            cur.deleteCharAt(cur.length() - 1);
        }
        if(right > left){
            backtrack(res, cur.append(")"), left, right - 1);
            cur.deleteCharAt(cur.length() - 1);
        }
    }
}
