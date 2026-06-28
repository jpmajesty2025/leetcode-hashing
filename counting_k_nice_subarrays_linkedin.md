🚀 **Counting “k-nice” subarrays with Prefix + HashMap**

Today I worked through a 'nice' array problem:

> Given an array of integers `nums` and an integer `k`. A continuous subarray is called `k-nice` if it contains exactly k odd integers. Goal: count the number of k-nice subarrays in `nums`.

A super clean way to solve it in **O(n)** is:

- Track a running count of odds seen so far: `curr_odd_count`
- Use a hashmap (`prefix_odd_counts`) to store:  
  **how many prefixes have exactly X odds**
- Keep a running total of k-nice subarrays at each step by adding on:
  `prefix_odd_counts[curr_odd_count - k]`

Key insight:

- Current prefix has `curr_odd_count` odds -> removing an earlier prefix with `curr_odd_count - k` odds leaves a k-nice subarray.

---

### Core idea:

```
def number_of_subarrays(nums, k):
    prefix_odd_counts = defaultdict(int)
    prefix_odd_counts[0] = 1
    total_subarrays = 0
    curr_odd_count = 0

    for num in nums:
        curr_odd_count += num % 2
        total_subarrays += prefix_odd_counts[curr_odd_count - k]
        prefix_odd_counts[curr_odd_count] += 1

    return total_subarrays
```

---

### Snapshots: what `prefix_odd_counts` means

Example: `nums = [2,2,2,1,2,2,1,2,2,2], k = 2`

Implement the algorithm and log to the console. For indexes 0-5, `total_subarrays == 0`. At index 6 the second odd arrives and the console shows:

`curr_odd_count: 2, total_subarrays: 4, prefix_odd_counts: {0: 4, -2: 0, -1: 0, 1: 3, 2: 1}`

How did `total_subarrays` jump from 0 to 4? Let's dig in to the hashmap a bit!

- `0: 4` → means we have seen 4 prefixes with 0 odds:  
  `[]`, `[2]`, `[2,2]`, `[2,2,2]`

- `2: 1` → we have seen one 2-nice prefix, `[2,2,2,1,2,2,1]`.

- This means we can split `[2,2,2,1,2,2,1]` into a 0-nice prefix a 2-nice subarray, four ways in fact! The 2-nice subarrays:
  - `[2,2,2,1,2,2,1]`
  - `[2,2,1,2,2,1]`
  - `[2,1,2,2,1]`
  - `[1,2,2,1]`

- So `total_subarrays` jumps by **4**

At indices 7, 8, and 9, `curr_odd_count` stays 2:
- Each step again adds `prefix_odd_counts[0] = 4` to `total_subarrays`

✅ Final answer: **16** 2-nice subarrays.

---

### Fun Python detail: `defaultdict(int)` behavior

During tracing you might see hashmap entries like `-2: 0` or `-1: 0`.

Why? Reading a missing key in `defaultdict(int)` creates it with value `0`. This happens at the step

- `... prefix_odd_counts[curr_odd_count - k]`

When `curr_odd_count < k` , we get these **expected and harmless** negative keys.


#Python #Algorithms #DataStructures #HashMap #Prefix #LeetCode #CodingInterview #SoftwareEngineering #LearningInPublic
