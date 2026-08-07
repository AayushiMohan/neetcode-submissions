class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {

        stack<pair<int, int>> st;
        int maxArea = 0;
        int n = heights.size();

        for (int i = 0; i < n; i++) {

            int start = i;

            while (!st.empty() && st.top().second > heights[i]) {

                int index = st.top().first;
                int height = st.top().second;
                st.pop();

                maxArea = max(maxArea, height * (i - index));

                start = index;
            }

            st.push({start, heights[i]});
        }

        while (!st.empty()) {

            int index = st.top().first;
            int height = st.top().second;
            st.pop();

            maxArea = max(maxArea, height * (n - index));
        }

        return maxArea;
    }
};