#include <iostream>
#include <queue>
#include <functional>
#include <vector>
#include <algorithm>
using namespace std;

int n, k;
vector<pair<int,int>> gem;
vector<int> bag;
priority_queue<int, vector<int>, less<int> > pq;

int main(){
    cin>>n>>k;
    int m, v;
    for(int i=0; i<n; i++){
        cin>>m>>v;
        gem.push_back(make_pair(m, v));
    }
    int c;
    for(int i=0; i<k; i++){
        cin>>c;
        bag.push_back(c);
    }
    sort(gem.begin(), gem.end());
    sort(bag.begin(), bag.end());

    int now_gem = 0;
    long long int result = 0;
    for(int i=0; i<k; i++){

        while(now_gem < n && gem[now_gem].first <= bag[i])
            pq.push(gem[now_gem++].second);
        if(pq.size() != 0) {
            result += pq.top();
            pq.pop();
        }
    }
    cout<<result;
}