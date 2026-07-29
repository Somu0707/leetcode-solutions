class Solution {
public:
    string minWindow(string s, string t) {
        if (s.size() < t.size())
            return "";

        unordered_map<char, int> mp;

        for (char c : t)
            mp[c]++;

        int left = 0;
        int right = 0;

        int required = t.size();

        int start = 0;
        int minLen = INT_MAX;

        while (right < s.size()) {

            if (mp[s[right]] > 0)
                required--;

            mp[s[right]]--;

            right++;

            while (required == 0) {

                if (right - left < minLen) {
                    minLen = right - left;
                    start = left;
                }

                mp[s[left]]++;

                if (mp[s[left]] > 0)
                    required++;

                left++;
            }
        }

        return minLen == INT_MAX ? "" : s.substr(start, minLen);
    }
};