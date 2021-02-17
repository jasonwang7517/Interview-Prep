class interpret {
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