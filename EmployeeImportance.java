/*
You have a data structure of employee information, which includes the employee's unique id, their importance value, and their direct subordinates' id.

You are given an array of employees employees where:
    - employees[i].id is the ID of the ith employee.
    - employees[i].importance is the importance value of the ith employee.
    - employees[i].subordinates is a list of the IDs of the subordinates of the ith employee.

Given an integer id that represents the ID of an employee, return the total importance value of this employee and all their subordinates.
*/

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class EmployeeImportance {
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
