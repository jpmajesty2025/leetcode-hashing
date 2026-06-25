# Missing Number, 3 Ways: Hashing vs Math vs XOR

Today I revisited the classic problem:

> Given an array `nums` containing `n` distinct numbers from the range `[0, n]`, return the one missing number.

I implemented this in **three different ways** and compared trade-offs.

## 1) Hash-set lookup (hashing-focused)

Build a set of values, then scan `0..n` and return the first number not in the set.

- **Time:** `O(n)`
- **Space:** `O(n)`

✅ Pros:
- Very intuitive
- Easy to explain and debug
- Great when practicing hash-based membership checks

⚠️ Cons:
- Uses extra memory proportional to input size

---

## 2) Arithmetic sum formula

Expected sum is `n*(n+1)//2`.  
Missing number = expected sum - actual sum.

- **Time:** `O(n)` (because of `sum(nums)`)
- **Space:** `O(1)`

✅ Pros:
- Compact and readable
- No extra data structure
- Great default in many interview/settings

⚠️ Cons:
- Relies on formula insight (less “obvious” than set for some learners)
- In languages with fixed-width ints, overflow needs consideration

---

## 3) XOR cancellation

XOR all indices and values with an accumulator seeded by `n`.  
Matching values cancel (`a ^ a = 0`), leaving only the missing value.

- **Time:** `O(n)`
- **Space:** `O(1)`

✅ Pros:
- Also constant-space
- Elegant bitwise trick
- Avoids arithmetic-overflow concerns in fixed-width languages

⚠️ Cons:
- Least intuitive at first glance
- Slightly harder to explain/maintain for teams unfamiliar with bitwise reasoning

---

## When would I choose each?

- **Learning/practicing hashing concepts:** hash-set approach  
- **Best balance of clarity + space efficiency:** arithmetic sum  
- **Bitwise-heavy contexts / overflow-sensitive environments:** XOR

### My takeaway:
Same problem, same asymptotic time, but different **readability vs space vs conceptual complexity** trade-offs.

That’s why I like implementing multiple solutions: not just to “pass,” but to understand design choices.

#LearningInPublic #LeetCode #Python #Algorithms #DataStructures #Hashing #ProblemSolving #CodingInterview
