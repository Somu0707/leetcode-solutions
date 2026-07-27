class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        for(string op:operations){
            if(op=="C") st.pop();
            else if(op == "D") st.push(2*st.top());
            else if(op == "+") {
                int last = st.top();
                st.pop();
                int sec_last = st.top();
                st.push(last);
                st.push(last+sec_last);
            }
            else st.push(stoi(op));
        }
        int sum =0;
        while (!st.empty()) {
        sum += st.top();
        st.pop();
    }
    return sum;
    }
};