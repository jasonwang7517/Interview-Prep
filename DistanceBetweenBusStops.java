/**
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.
 */

class DistanceBetweenBusStops {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int ans1 = 0;
        if (start < destination) {
            for (int i = start; i < destination; i++) {
                ans1 += distance[i];
            }
        }
        else {
            for (int i = start; i < distance.length; i++) {
                ans1 += distance[i];
            }
            for (int i = 0; i < destination; i++) {
                ans1 += distance[i];
            }
        }
        int ans2 = 0;
        if (start > destination) {
            for (int i = start - 1; i >= destination; i--) {
                ans2 += distance[i];
            }
        }
        else {
            for (int i = start - 1; i >= 0; i--) {
                ans2 += distance[i];
            }
            for (int i = distance.length - 1; i >= destination; i--) {
                ans2 += distance[i];
            }
        }
        return Math.min(ans1, ans2);
    }
}