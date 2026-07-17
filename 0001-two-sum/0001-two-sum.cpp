class Solution {
public:
    vector<int> twoSum(vector<int>& a, int target) {
        unordered_map<int, int> mp;
        int sum=0;
        // vector<int> ans;
        for(int i=0;i<a.size();i++){
            if(mp.find(target-a[i])!=mp.end()){
                return {i,mp[target-a[i]]};
            }
            mp[a[i]] = i;
        }
        return {};
    }
};