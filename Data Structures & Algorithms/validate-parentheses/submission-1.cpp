class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,int>symbol={{'(',-1},{'{',-2},{'[',-3},{')',1},{'}',2},{']',3}};
        stack<char>st;
        for(char brackets:s){
            if(symbol[brackets]<0){
                st.push(brackets);
            }
            else{
                if(st.empty()) return false;
                char top = st.top();
                st.pop();
                if(symbol[top]+symbol[brackets]!=0) return false;
            }
        }
        return st.empty();
    }
};
