# One problem, 3 hashing implementations (+ 1 robustness upgrade)

Consider the following problem:

> Given `nums`, an array of arrays of **distinct** integers, return a **sorted** list of values that appear in **every** array.

This problem appeared in the hashing module of a DS&A course, and it turned out to be a great example of something subtle:

- **sets** are hash-based
- **dicts** are hash-based
- the right choice depends on readability, extensibility, and input constraints

## Version 1: Iterative set intersection (explicit/readable)

```python
common = set(nums[0])
for row in nums[1:]:
    common &= set(row)
return sorted(common)
```

- **Time:** ~`O(K + L log L)`
- **Space:** `O(U)`

Where:
- `K` = total number of elements across all arrays (including duplicates if present)
- `U` = number of unique values across all arrays (global union size)
- `L` = size of the final intersection (output length)

✅ Clear and easy to debug  
⚠️ Slightly more verbose

---

## Version 2: One-liner set intersection (compact)

```python
return sorted(set.intersection(*(set(row) for row in nums))) if nums else []
```

- Same asymptotic complexity as v1

✅ Concise and idiomatic  
⚠️ Less beginner-friendly / less step-by-step

---

## Version 3: Dict frequency counting (flexible pattern)

```python
for arr in nums:
    for x in arr:
        counts[x] += 1
return sorted(x for x, c in counts.items() if c == len(nums))
```

- **Time:** ~`O(K + U + L log L)`
- **Space:** `O(U)`

(Using the same definitions of `K`, `U`, and `L` above.)

✅ Great when you need frequency-style variants  
⚠️ Important caveat: this assumes each row has distinct elements

### Important: If row-level distinctness is relaxed/dropped, versions 1 and 2 still work, but with version 3, duplicates can overcount and produce incorrect results.

---

## Robust dict upgrade (v3 -> v4)

```python
for arr in nums:
    for x in set(arr):
        counts[x] += 1
```

This deduplicates each row before counting, making the dict approach as robust as set-intersection even when arrays contain duplicates.

---

## Which one would I choose?

- **Most readable:** v1  
- **Most concise:** v2  
- **Most extensible for counting-style variants:** v4 (dict + per-row dedup)

Example where v4 is the right choice:
- “Return all values that appear in **at least 3 arrays**” (or, more generally, at least `m` arrays).
  - With v4, this is a tiny change from `c == n` to `c >= m` after per-row dedup.

### Takeaway

The key decision isn’t “set vs dict” in isolation.  
It’s matching the data structure to the exact problem guarantees and future variants.

#LearningInPublic #LeetCode #Python #Hashing #DataStructures #Algorithms #ProblemSolving #CodingInterview #SoftwareEngineering
