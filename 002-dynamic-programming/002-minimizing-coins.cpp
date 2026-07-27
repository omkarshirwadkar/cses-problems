#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, x;
    cin >> n >> x;
    vector<int> c(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }
    const int INF = 1000000000;
    vector<int> dp(x + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= x; i++) {
        for (int coin : c) {
            if (i >= coin) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    cout << (dp[x] < INF ? dp[x] : -1) << "\n";
    return 0;
}