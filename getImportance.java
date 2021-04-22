import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class getImportance {
    public int getImportance(List<Employee> employees, int id) {
        Queue<Integer> subordinateList = new LinkedList<>();
        HashMap<Integer, Employee> toAdd = new HashMap<>();
        int ans = 0;
        for (Employee e : employees) {
            if (e.id == id) {
                ans += e.importance;
                for (int i : e.subordinates) {
                    subordinateList.add(i);
                }
            }
            toAdd.put(e.id, e);
        }
        while (!subordinateList.isEmpty()) {
            int currEmployee = subordinateList.poll();
            Employee curr = toAdd.get(currEmployee);
            ans += curr.importance;
            for (int i : curr.subordinates) {
                subordinateList.add(i);
            }
        }
        return ans;
    }
}

class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
