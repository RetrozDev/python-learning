# e : loops

# --- For loop ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range
for i in range(1, 6):
    print(i)  # prints 1 to 5

# --- While loop ---
count = 0
while count < 5:
    print(count)
    count += 1  # increment to avoid infinite loop

# --- Nested loop example ---
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")