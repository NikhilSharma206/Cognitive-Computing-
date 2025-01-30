#q1
import numpy as np
arr = np.array([12,13,20,50,100])

print("Original array :", arr)

print("Addition of 2 -")
print(arr+2)

print("Multiply with 3 -")
print(arr * 3)

print("Divide by 2 -")
print(arr/2)
#q2
import numpy as np

arr = np.array([1, 2, 3, 6, 4, 5])
rev = arr[::-1]

print(f"Reversed array is {rev}")

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

# Count occurrences of each integer
counts = np.bincount(x)

# Get the most frequent value
most_frequent_value = np.argmax(counts)

# Get the indices where this value occurs
indices = np.where(x == most_frequent_value)[0]

print("Most frequent value in x:", most_frequent_value)
print("Indices of most frequent value:", indices)

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

# Count occurrences of each integer
counts = np.bincount(y)

# Get the most frequent value
most_frequent_value = np.argmax(counts)

# Get the indices where this value occurs
indices = np.where(y == most_frequent_value)[0]

print("Most frequent value in y:", most_frequent_value)
print("Indices of most frequent value:", indices)
#q3
import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Access 1st row, 2nd column :-")

element_a = arr[0, 1]
print("Element is", element_a)

element_b = arr[2,0]
print("Element is", element_b)
#q4
import numpy as np
yourname = np.linspace(10,100,25)

print(yourname)

print("Shape: ",yourname.shape)
print("Size: ",yourname.size)
print("Data type: ",yourname.dtype)

reshaped = yourname.reshape(5,5)
print("Reshaped data: ",reshaped)
print("Transpose data: ",reshaped.T)
#q5
import numpy as np

# Create a 2D array (3 rows, 4 columns) - Replace <your_name> with your actual name
ucs420_YourName = np.array([[10, 20, 30, 40],
                            [50, 60, 70, 80],
                            [90, 15, 20, 35]])

# Compute statistical values
mean_value = np.mean(ucs420_YourName)
median_value = np.median(ucs420_YourName)
max_value = np.max(ucs420_YourName)
min_value = np.min(ucs420_YourName)
unique_elements = np.unique(ucs420_YourName)

# Reshape the array to 4 rows and 3 columns
reshaped_ucs420_YourName = ucs420_YourName.reshape(4, 3)

# Resize the array to 2 rows and 3 columns (this modifies the array)
resized_ucs420_YourName = np.resize(ucs420_YourName, (2, 3))

# Print results
print("Original Array:\n", ucs420_YourName)
print("Mean:", mean_value)
print("Median:", median_value)
print("Max:", max_value)
print("Min:", min_value)
print("Unique Elements:", unique_elements)

print("\nReshaped Array (4x3):\n", reshaped_ucs420_YourName)
print("\nResized Array (2x3):\n", resized_ucs420_YourName)