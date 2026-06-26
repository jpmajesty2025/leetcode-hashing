# One problem, 3 hashing approaches (+ robust upgrade)

Consider the following problem:

> Given `nums`, an array of arrays of **distinct** integers, return a **sorted** list of values that appear in **every** array.

This hashing problem from a DS&A course highlights a subtle point:

- **sets** are hash-based
- **dicts** are hash-based
- the right choice depends on readability, extensibility, and input constraints

## Version 1: Iterative set intersection (readable)

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
⚠️ Less beginner-friendly

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

✅ Great for frequency-style variants  
⚠️ Important caveat: this assumes each row has distinct elements

### If rows may contain duplicates, v1/v2 still work; v3 can overcount and be wrong.

---

## Robust dict upgrade (v3 -> v4)

```python
for arr in nums:
    for x in set(arr):
        counts[x] += 1
```

This deduplicates each row first, making dict counting robust even with duplicates.

---

## Which one would I choose?

- **Most readable:** v1  
- **Most concise:** v2  
- **Most extensible for counting-style variants:** v4 (dict + per-row dedup)

Example where v4 is the right choice:
- “Return all values that appear in **at least 3 arrays**” (or, more generally, at least `m` arrays).
  - With v4, this is a tiny change from `c == n` to `c >= m` after per-row dedup.

### Takeaway

The key isn’t “set vs dict” alone.  
Match the structure to guarantees and likely variants.

#LearningInPublic #LeetCode #Python #Hashing #DataStructures #Algorithms #ProblemSolving #CodingInterview #SoftwareEngineering
