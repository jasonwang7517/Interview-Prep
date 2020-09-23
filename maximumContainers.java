import java.util.ArrayList;
import java.util.List;

public class maximumContainers {
    public static void maximumContainers(List<String> scenarios) {
        // Write your code here
        for (int i = 0; i < scenarios.size(); i++) {
            String[] inputs = scenarios.get(i).split("\\s+");
            int budget = Integer.parseInt(inputs[0]);
            int cost = Integer.parseInt(inputs[1]);
            int conversion = Integer.parseInt(inputs[2]);
            int total = 0;
            int purchased = 0;
            total += budget / cost;
            purchased += budget / cost;
            while (purchased >= conversion) {
                total += purchased / conversion;
                purchased = (purchased % conversion) + (purchased / conversion) ;
            }
            System.out.println(total);
        }
    }

    public static void main (String[] args) {
        ArrayList<String> ans = new ArrayList<>();
        ans.add("4 1 2");
        ans.add("10 2 5");
        ans.add("6 2 2");
        maximumContainers(ans);
    }
}
