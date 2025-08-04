from collections import Counter
import bisect
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        unique_powers = sorted(count.keys())
        if not unique_powers:
            return 0
        n = len(unique_powers)
        dp = [0] * n
        dp[0] = unique_powers[0] * count[unique_powers[0]]
        for i in range(1,n):
            current_power = unique_powers[i]
            current_damage = current_power * count[current_power]
            dp[i] = dp[i-1]
            target = current_power - 2
            j = bisect.bisect_left(unique_powers,target) - 1
            if j >= 0:
                dp[i] = max(dp[i],dp[j] + current_damage)
            else:
                dp[i] = max(dp[i],current_damage)
        return dp[n-1]

