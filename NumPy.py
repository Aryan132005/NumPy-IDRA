import numpy as np
print("===== 1. Creating Arrays =====")

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)
# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)
# 3D Array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr3)

# 2. Dimensions and Data Types
print("\n===== 2. Dimensions and Data Types =====")

print("1D Dimensions:", arr1.ndim)
print("2D Dimensions:", arr2.ndim)
print("3D Dimensions:", arr3.ndim)

print("Data Type:", arr1.dtype)
print("Shape of 2D Array:", arr2.shape)

# 3. Indexing
print("\n===== 3. Indexing =====")

print("First Element:", arr1[0])
print("Third Element:", arr1[2])
print("2D Element:", arr2[1, 2])

# 4. Slicing
print("\n===== 4. Slicing =====")

print("First 3 Elements:", arr1[:3])
print("Last 2 Elements:", arr1[-2:])
print("2D Slicing:\n", arr2[:, 1:])

# 5. Reshaping
print("\n===== 5. Reshaping =====")

arr = np.arange(1, 13)
print("Original Array:", arr)

reshaped = arr.reshape(3, 4)
print("Reshaped Array:\n", reshaped)

# 6. Array Creation Functions
print("\n===== 6. Array Creation Functions =====")

print("Zeros:")
print(np.zeros((2, 3)))

print("Ones:")
print(np.ones((2, 3)))

print("Arange:")
print(np.arange(1, 11, 2))

print("Linspace:")
print(np.linspace(0, 10, 5))


# 7. Mathematical Operations
print("\n===== 7. Mathematical Operations =====")
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Power:", a ** 2)

# 8. Vectorized Operations
print("\n===== 8. Vectorized Operations =====")
numbers = np.array([1, 2, 3, 4, 5])

print("Original:", numbers)
print("Multiply by 2:", numbers * 2)
print("Add 10:", numbers + 10)

# 9. Boolean Masking
print("\n===== 9. Boolean Masking =====")
marks = np.array([45, 67, 89, 32, 76, 55])

print("Marks:", marks)
print("Marks greater than 60:", marks[marks > 60])
print("Marks less than 50:", marks[marks < 50])

# 10. Broadcasting
print("\n===== 10. Broadcasting =====")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
number = 10

print("Original Matrix:")
print(matrix)

print("After Broadcasting:")
print(matrix + number)

# 11. Aggregate Functions
print("\n===== 11. Aggregate Functions =====")
data = np.array([10, 20, 30, 40, 50])

print("Data:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Median:", np.median(data))