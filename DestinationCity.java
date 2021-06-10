/*
    You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, 
    the city without any path outgoing to another city.

    It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
*/

import java.util.*;

public class DestinationCity {
    public String destCity(List<List<String>> paths) {
        String str = "";
        HashMap<String, String> map = new HashMap<>();
        for (int i = 0; i < paths.size(); i++) {
            if(!map.containsKey(paths.get(i).get(0))) {
                map.put(paths.get(i).get(0), paths.get(i).get(1));
            }
        }
        for (String s : map.values()) {
            if (!map.containsKey(s)) {
                return str;
            }
        }
        return str;
    }
}
