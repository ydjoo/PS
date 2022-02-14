#include <stdio.h>
#include <iostream>
#include <queue>
#include <functional>
#include <vector>
#include <algorithm>
using namespace std;

int n,s,t, top_value;
vector<pair<int,int>> cls;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>s>>t;
        cls.push_back(make_pair(s, t));
    }
    sort(cls.begin(), cls.end());

    for(int i=0; i<n; i++){
        if(pq.size() == 0)
            pq.push(cls[i].second);
        else{
            top_value = pq.top();
            if(top_value <= cls[i].first)
                pq.pop();
            pq.push(cls[i].second);
        }
    }
    cout<<pq.size();
    return 0;
}