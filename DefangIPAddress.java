/*
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
*/
public class DefangIPAddress {
    public String defangIPaddr(String address) {
        String s = "";
        int length = address.length();
        for (int i = 0; i < length; i++) {
            if (address.charAt(i) != '.') {
                s += address.charAt(i);
            }
            else if (address.charAt(i) == '.') {
                s += "[.]";
            }
        }
        return s;
    }
}
