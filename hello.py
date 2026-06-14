import numpy as np

# ── Method 1: from a Python list ──────────────────────────
arr1 = np.array([10, 20, 30, 40, 50])
print("arr1 =", arr1)

# ── Method 2: using np.arange ─────────────────────────────
arr2 = np.arange(1, 10, 2)   # start=1, stop=10, step=2
print("arr2 =", arr2)        # [1 3 5 7 9]

# ── Method 3: using np.linspace ───────────────────────────
arr3 = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print("arr3 =", arr3)        # [0.   0.25 0.5  0.75 1.  ]

# ── Method 4: using np.zeros and np.ones ──────────────────
arr4 = np.zeros(5, dtype=int)
print("arr4 =", arr4)        # [0 0 0 0 0]

# ── Method 5: using np.random ─────────────────────────────
arr5 = np.random.randint(1, 100, size=5)
print("arr5 =", arr5)        # random numbers


# ══ INDEXING (same idea as lists) ══════════════════════════

print(arr1[0])    # first element  → 10
print(arr1[2])    # third element  → 30
print(arr1[-1])   # last element   → 50


# ══ SLICING (same idea as lists) ═══════════════════════════

print(arr1[1:4])   # index 1 to 3   → [20 30 40]
print(arr1[:3])    # first 3        → [10 20 30]
print(arr1[2:])    # from index 2   → [30 40 50]
print(arr1[::2])   # every 2nd      → [10 30 50]
print(arr1[::-1])  # reversed       → [50 40 30 20 10]


