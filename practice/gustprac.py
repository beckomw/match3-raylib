# ============================================
# PYTHON & DATA STRUCTURES PRACTICE
# ============================================

# ============================================
# SECTION 1: CORE PYTHON CONCEPTS
# ============================================

print("=" * 50)
print("SECTION 1: CORE PYTHON CONCEPTS")
print("=" * 50)

# EXERCISE 1.1: Lists - Create, access, modify
print("\n--- EXERCISE 1.1: Lists ---")
print("Task: Create a list of 5 numbers, access the 3rd element, and add a new element")
print("\nSolution:")
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"3rd element (index 2): {numbers[2]}")
numbers.append(60)
print(f"After append: {numbers}")

# EXERCISE 1.2: Dictionaries
print("\n--- EXERCISE 1.2: Dictionaries ---")
print("Task: Create a dict of students with grades, access one value, add a new student")
print("\nSolution:")
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"Dictionary: {students}")
print(f"Alice's grade: {students['Alice']}")
students["Diana"] = 95
print(f"After adding Diana: {students}")

# EXERCISE 1.3: For Loop with Lists
print("\n--- EXERCISE 1.3: For Loop with Lists ---")
print("Task: Print each fruit in a list with its index")
fruits = ["apple", "banana", "cherry", "date"]
print(f"Fruits: {fruits}")
print("Output:")
for i, fruit in enumerate(fruits):
    print(f"  Index {i}: {fruit}")

# EXERCISE 1.4: String Manipulation
print("\n--- EXERCISE 1.4: String Manipulation ---")
print("Task: Take a string, reverse it, convert to uppercase")
text = "python"
print(f"Original: {text}")
print(f"Reversed: {text[::-1]}")
print(f"Uppercase: {text.upper()}")
print(f"All together: {text[::-1].upper()}")

# EXERCISE 1.5: Function with Return Value
print("\n--- EXERCISE 1.5: Functions ---")
print("Task: Write a function that adds two numbers and returns the result")
print("\nCode:")
print("""
def add_numbers(a, b):
    return a + b

result = add_numbers(15, 25)
print(f"15 + 25 = {result}")
""")
def add_numbers(a, b):
    return a + b
result = add_numbers(15, 25)
print(f"Result: 15 + 25 = {result}")


# ============================================
# SECTION 2: DATA STRUCTURES
# ============================================

print("\n" + "=" * 50)
print("SECTION 2: DATA STRUCTURES")
print("=" * 50)

# EXERCISE 2.1: Array/List Indexing and Slicing
print("\n--- EXERCISE 2.1: List Indexing & Slicing ---")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Array: {arr}")
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")
print(f"Elements from index 2 to 5: {arr[2:6]}")
print(f"Every 2nd element: {arr[::2]}")

# EXERCISE 2.2: Linked List Node
print("\n--- EXERCISE 2.2: Linked List Node ---")
print("Code for creating a simple linked list node:")
print("""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Traverse
current = head
while current:
    print(current.data)
    current = current.next
""")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Linked List traversal output:")
current = head
while current:
    print(f"  {current.data}")
    current = current.next

# EXERCISE 2.3: Stack (LIFO)
print("\n--- EXERCISE 2.3: Stack (Last In, First Out) ---")
print("Using a list as a stack:")
stack = []
stack.append(1)  # Push
stack.append(2)  # Push
stack.append(3)  # Push
print(f"Stack after pushes: {stack}")
print(f"Pop: {stack.pop()}")
print(f"Stack after pop: {stack}")
print(f"Top of stack: {stack[-1]}")

# EXERCISE 2.4: Queue (FIFO)
print("\n--- EXERCISE 2.4: Queue (First In, First Out) ---")
from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)  # Enqueue
queue.append(3)  # Enqueue
print(f"Queue after enqueues: {list(queue)}")
print(f"Dequeue: {queue.popleft()}")
print(f"Queue after dequeue: {list(queue)}")


# ============================================
# SECTION 3: MATRIX TRAVERSALS
# ============================================

print("\n" + "=" * 50)
print("SECTION 3: MATRIX TRAVERSALS")
print("=" * 50)

# Create a sample matrix for all exercises
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

def print_matrix(m):
    for row in m:
        print(f"  {row}")

print("\nMatrix:")
print_matrix(matrix)

# EXERCISE 3.1: Row-by-Row Traversal
print("\n--- EXERCISE 3.1: Row-by-Row Traversal ---")
print("Code:")
print("""
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
""")
print("Output: ", end="")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
print()

# EXERCISE 3.2: Column-by-Column Traversal
print("\n--- EXERCISE 3.2: Column-by-Column Traversal ---")
print("Code:")
print("""
for j in range(len(matrix[0])):  # Go through columns first
    for i in range(len(matrix)):  # Then rows
        print(matrix[i][j], end=' ')
""")
print("Output: ", end="")
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=' ')
print()

# EXERCISE 3.3: Diagonal Traversal (top-left to bottom-right)
print("\n--- EXERCISE 3.3: Diagonal Traversal (TL to BR) ---")
print("Code:")
print("""
# Main diagonal (where i == j)
for i in range(min(len(matrix), len(matrix[0]))):
    print(matrix[i][i], end=' ')
""")
print("Output: ", end="")
for i in range(min(len(matrix), len(matrix[0]))):
    print(matrix[i][i], end=' ')
print()

# EXERCISE 3.4: Anti-Diagonal Traversal (top-right to bottom-left)
print("\n--- EXERCISE 3.4: Anti-Diagonal Traversal (TR to BL) ---")
print("Code:")
print("""
# Anti-diagonal (where i + j = n-1, for a square matrix)
for i in range(len(matrix)):
    j = len(matrix[0]) - 1 - i
    if j >= 0 and j < len(matrix[0]):
        print(matrix[i][j], end=' ')
""")
print("Output: ", end="")
for i in range(len(matrix)):
    j = len(matrix[0]) - 1 - i
    if j >= 0 and j < len(matrix[0]):
        print(matrix[i][j], end=' ')
print()

# EXERCISE 3.5: Spiral Traversal
print("\n--- EXERCISE 3.5: Spiral Traversal (Clockwise) ---")
print("Code:")
print("""
top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
result = []

while top <= bottom and left <= right:
    # Traverse right
    for j in range(left, right + 1):
        result.append(matrix[top][j])
    top += 1
    
    # Traverse down
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1
    
    # Traverse left (if row still exists)
    if top <= bottom:
        for j in range(right, left - 1, -1):
            result.append(matrix[bottom][j])
        bottom -= 1
    
    # Traverse up (if column still exists)
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(result)
""")
print("Output: ", end="")
top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
result = []

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        result.append(matrix[top][j])
    top += 1
    
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1
    
    if top <= bottom:
        for j in range(right, left - 1, -1):
            result.append(matrix[bottom][j])
        bottom -= 1
    
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(result)


# ============================================
# PRACTICE PROBLEMS - TRY THESE YOURSELF!
# ============================================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS - TRY THESE!")
print("=" * 50)

print("""
PROBLEM 1 (Core Python):
Write a function that takes a list of numbers and returns their sum.
Example: sum_list([1, 2, 3, 4, 5]) should return 15

PROBLEM 2 (Core Python):
Create a dictionary of 3 favorite foods with their calories, then print each one.
Example: {"pizza": 300, "burger": 250, "salad": 100}

PROBLEM 3 (Data Structures - Stack):
Using a list as a stack, push numbers 1-5, then pop them all and print them.
What order do they come out?

PROBLEM 4 (Data Structures - List Slicing):
Given: arr = [10, 20, 30, 40, 50, 60]
- Get elements from index 1 to 4
- Get every other element
- Get the last 3 elements

PROBLEM 5 (Matrix Traversal):
Given: matrix = [[1, 2], [3, 4]]
Print all elements in row-by-row order, then column-by-column order

PROBLEM 6 (Matrix Traversal):
Given a 3x3 matrix, print the main diagonal.
Example: [[1,2,3], [4,5,6], [7,8,9]] → diagonal is 1, 5, 9
""")

print("\n" + "=" * 50)
print("KEY REMINDERS FOR YOUR TEST")
print("=" * 50)
print("""
✓ Index 0 is the FIRST element (not 1)
✓ List slicing: arr[start:end] goes UP TO but NOT including end
✓ For loops: for i in range(len(list)) to access by index
✓ Nested loops are key for matrices: for i (rows), for j (columns)
✓ matrix[i][j] means row i, column j
✓ Watch out for off-by-one errors!
✓ When in doubt, draw it out or print intermediate values

Good luck on your test! 🎯
""")