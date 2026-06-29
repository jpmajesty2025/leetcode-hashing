🧠 **HashMap pattern shift: from counting to “first occurrence memory”**

Consider this problem:

> Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0s and 1s.

Clearly, there is some counting going on, so it seems reasonable that a HashMap might be useful. But the usage here is subtly different from the usual “frequency counter” pattern.

In many problems, we use a HashMap to count occurrences.  
Here, we track a balance, representing the relative number of 1s and 0s we've seen so far. 


### Core idea
- Treat `1` as `+1` (arbitrary choice)
- Treat `0` as `-1`
- Walk the array and keep a running `balance`
- We use balance to store the only **the first index where each balance appears**.

If the same `balance` appears first at index `i` and later at `j`, then the subarray `(i+1 ... j)` has net balance `0` → equal number of 0s and 1s.

### Why we only store first occurrence
For each distinct balance, we store its index **once** (the first time we see it).  
We do **not** overwrite it later.

Why? Because the earliest index gives the longest possible span when that balance reappears:
`length = current_index - first_seen_index[balance]`

So on repeat balances, we update `max_len`, not the map.

This works for any balance value (positive, zero, or negative). The particular balance the produces the longest subarray with equal 1s and 0s is the overall answer. Here is a Python implementation:

```
first_seen = {0: -1}
balance = 0
max_len = 0

for i, num in enumerate(nums):
    balance += 1 if num == 1 else -1
    if balance in first_seen:
        max_len = max(max_len, i - first_seen[balance])
    else:
        first_seen[balance] = i
```

✅ Big takeaway:  
Not every HashMap problem is “count everything.”  
Sometimes the win comes from storing **the earliest structural state** and leveraging repeats.

#LearningInPublic #Python #Algorithms #DataStructures #HashMap #LeetCode #CodingInterview #PrefixSum
