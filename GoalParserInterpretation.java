/*
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 

The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings 
are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
*/

class GoalParserInterpretation {
    public String interpret(String command) {
        char[] chars = command.toCharArray();
        String s = "";
        int index = 0;
        while (index < chars.length) {
            if (chars[index] == 'G') {
                s += "G";
                index++;
            }
            else if (chars[index] == '(' && chars[index + 1] == ')') {
                s += "o";
                index += 2;
            }
            else {
                s += "al";
                index += 4;
            }
        }
        return s;
    }
}