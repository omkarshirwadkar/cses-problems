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

    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    const int MOD = 1000000007;

    for (int i = 1; i <= x; ++i) {
        for (int coin : c) {
            if (i >= coin) {
                dp[i] = (dp[i] + dp[i - coin]) % MOD;
            }
        }
    }

    cout << dp[x] << endl;
    return 0;
}