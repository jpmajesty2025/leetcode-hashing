# From Brute Force O(n²) to O(n): Choosing the right hash structure (or when to skip it)

I revisited the classic **Two Sum** problem:

> Given an array of integers and a target, return the **indices** of the two numbers that sum to the target.

I bolded **indices** on purpose. That one word determines the best data structure.

## 1) Brute-force baseline

Use a nested loop to check every pair `(i, j)`:

- **Time:** O(n²)
- **Space:** O(1)

It works, but it scales poorly because many pair checks are repeated work.

## 2) Hashing for the win

For each number `num`, compute:

`complement = target - num`

Then ask: **“Have I seen this complement before?”**

A hash map (Python `dict`) answers that in O(1) average lookup time.  
Store `value -> index` as you scan once through the array.

Result:

- **Time:** O(n)
- **Space:** O(n)

You can also exit early as soon as a valid pair is found.

## 3) Why **indices** matters

The prompt asks for **distinct indices**, not just values.  
So we must track where each value appeared:

- Store `value -> index`
- If `complement` is already stored, return `[current_index, stored_index]`

That index bookkeeping is exactly why a hash map is the right fit here.

## 4) If the prompt changes, the structure should change too

- **If asked for a boolean** (“does any pair exist?”):  
  A **set** is enough. Track seen values and check complement membership.

- **If asked for the values themselves** (not positions):  
  A **set** is usually enough in one pass, or you can use **sort + two pointers** depending on constraints.

### Important nuance

A set and hash map both use hashing under the hood.

- **Set:** keys only
- **Hash map / dict:** key-value pairs

So the principle is not “hashing vs no hashing.”  
It’s choosing the **minimal hash-based structure** that matches the required output.

---

## Takeaways

- **Return type drives data structure choice.**
- **Constraints decide which resource you spend:**
  - If O(n) extra space is allowed → hashing (`dict`/`set`) gives O(n) time.
  - If extra space is tight but mutation is allowed → in-place sort + two pointers gives O(n log n) time and O(1) extra space.

Curious how others approach this:  
Do you start from the data structure first, or from constraints first?