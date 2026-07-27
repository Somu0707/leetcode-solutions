class Solution {
public:
    int next_greater(const vector<int>& nums2, int a){
        //find the element
        int i;
        for(i=0;i<nums2.size();i++){
            if(nums2[i]==a) break;
        }
        i++;
        while(i<nums2.size()){
            if(nums2[i]>a) return nums2[i];
            i++;
        }
        return -1;
    }
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        for(int i=0;i<nums1.size();i++){
            int x= next_greater(nums2, nums1[i]);
            ans.push_back(x);
        }
        return ans;
    }
};