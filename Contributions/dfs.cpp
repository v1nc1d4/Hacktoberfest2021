#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj; // graph represented as an adjacency list
int n; // number of vertices

vector<bool> visited;

void dfs(int v) {
    visited[v] = true;
    for (int u : adj[v]) {
        if (!visited[u])
            dfs(u);
    }
}

int main() {
    int m;
    cin>>n>>m;
    for(int i=0; i<m; i++) {
        int a,b;
        cin>>a>>b;
        adj[a] = b;
        adj[b] = a;
    }
    dfs(1);

    for(int i=1; i<=n; i++) {
        if(visited[i]==false) {
            cout<<i<<'\n';
        }
    }
    return 0;
}