/*
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked 
up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 
*/

public class CarPooling {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] timeline = new int[1001];
        for (int i = 0; i < trips.length; i++) {
            timeline[trips[i][1]] += trips[i][0];
            timeline[trips[i][2]] -= trips[i][0];
        }
        int currCap = 0;
        for (int i : timeline) {
            currCap += i;
            if (currCap > capacity) {
                return false;
            }
        }
        return true;
    }
}