class Solution {
public:
    int elevatorRequests(int n, vector<int>& requests) {
        

        int cnt = requests[0];
        int top = requests[0];
        for (int i = 1;i < requests.size();i++){

            cnt+=abs((top - requests[i]));
            top = requests[i];
        }
        return cnt;
    }

    
};