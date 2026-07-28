#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, x;
    cin >> n >> x;
    vector<int> c(n);
    for (int i = 0; i < n; ++i) {
        cin >> c[i];
    }
    vector<vector<int>> dp(n + 1, vector<int>(x + 1));
    int MOD = 1000000007;

    // base case
    for(int i = 0; i < n; i++){
        dp[i][0] = 1;
    }

    for(int i = n - 1; i >= 0; i--){
        for(int j = 1; j <= x; j++){
            int skipping = dp[i + 1][j];
            int picking = 0;
            if(c[i] <= j){
                picking = dp[i][j - c[i]];
            }
            dp[i][j] = (skipping + picking) % MOD;
        }
    }

    cout<<dp[0][x]<<endl;
    return 0;
}