class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int left = 1;
        int right = *max_element(piles.begin(), piles.end());

        while(left <= right) {

            int k = left + (right - left) / 2;

            long long hours = 0;

            for(int bananas : piles) {
                hours += (bananas + k - 1) / k;
            }

            if(hours <= h) {
                right = k - 1;
            }
            else {
                left = k + 1;
            }
        }

        return left;
    }
};