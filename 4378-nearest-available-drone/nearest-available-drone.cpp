class Solution {
public:
    int nearestDrone(vector<vector<int>>& drones, vector<int>& target) {
        
    int idx = -1;
    int mini = INT_MAX;

    int a = target[0];
    int b = target[1];
    for(int i  = 0;i<drones.size();i++){

        int x = drones[i][0];
        int y = drones[i][1];
        int z = drones[i][2];

        int min_d = abs(x-a) + abs(y- b);

        if (min_d <= z and min_d < mini){

            mini = min_d;
            idx = i;
        }

    }   
    return idx;

    }
};