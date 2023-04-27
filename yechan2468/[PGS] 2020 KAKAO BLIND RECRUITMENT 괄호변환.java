import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;


class Solution {
    public String solution(String str) {
        if (str.isEmpty()) {
            return "";
        }
        ArrayList<String> w = split(str);
        String u = w.get(0), v = w.get(1);

        if (isCorrectString(u)) {
            return u + solution(v);
        } else {
            u = u.substring(1, u.length() - 1);
            u = replaceParenthesis(u);
            return "(" + solution(v) + ")" + u;
        }
    }

    public ArrayList<String> split(String str) {
        ArrayList<String> result = new ArrayList<>(2);
        int openingParenthesisCount = 0, closingParenthesisCount = 0;

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') {
                openingParenthesisCount += 1;
            } else {
                closingParenthesisCount += 1;
            }
            if (openingParenthesisCount == closingParenthesisCount) {
                result.add(str.substring(0, i+1));
                result.add(str.substring(i+1));
                return result;
            }
        }
        result.add(str);
        result.add("");
        return result;
    }
    
    public boolean isCorrectString(String str) {
        if (str.isEmpty()) {
            return true;
        }
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            Character ch = str.charAt(i);
            if (ch.equals(')')) {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    stack.pop();
                }
            } else {
                stack.push(ch);
            }
            if (stack.isEmpty()) {
                return true;
            }
        }
        return false;
    }

    public String replaceParenthesis(String str) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            Character ch = str.charAt(i);
            result.append(ch.equals('(')? ')' : '(');
        }
        return result.toString();
    }
}
