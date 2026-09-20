# NumPy Practice Roadmap

##  NumPy Basics
* What is NumPy, and how is a NumPy array different from a Python list?
* Create 1D, 2D, and 3D arrays using `np.array()`.
* Find the `ndim`, `shape`, `size`, `dtype`, and `itemsize` of an array.
* Create arrays using `np.zeros()`, `np.ones()`, and `np.empty()`.
* Use `np.arange()` to create an array containing even numbers from 1 to 50.
* Use `np.linspace()` to generate 11 equally spaced values between 0 and 1.
* Create NumPy arrays using different data types such as `int32`, `float64`, and `bool`.
* Convert a Python list into a NumPy array and a NumPy array back into a Python list.

---

## Indexing & Slicing
* Access the first, last, and middle elements of a 1D array.
* Access a specific row and column from a 2D array.
* Extract the first two rows and last two columns from a 2D array.
* Reverse a NumPy array using slicing.
* Access a specific element from a 3D array.
* Use Boolean indexing to extract all values greater than 50.
* Extract all even and odd numbers from an array.
* Replace elements in an array that satisfy a given condition.

---

##  Array Operations
* Perform addition, subtraction, multiplication, and division between two arrays.
* Calculate the square and cube of every element in an array.
* Calculate sum, mean, median, min, max, and std of an array.
* Calculate row-wise and column-wise sums using the `axis` parameter.
* Sort an array using `np.sort()`.
* Find the indices of the maximum and minimum values using `np.argmax()` and `np.argmin()`.
* Find unique values in an array and count their frequencies.
* Find the common elements between two NumPy arrays.

---

## Reshaping & Array Manipulation
* Reshape a 1D array into 2D and 3D arrays.
* Explain and demonstrate the difference between `reshape()` and `resize()`.
* Flatten an array using both `flatten()` and `ravel()`.
* Combine two arrays vertically and horizontally.
* Use `np.concatenate()`, `np.vstack()`, and `np.hstack()`.
* Split an array into multiple smaller arrays using `np.split()`.

---

##  Broadcasting & Advanced NumPy
* What is broadcasting in NumPy? Demonstrate it with arrays of different shapes.
* Add a vector to every row of a matrix using broadcasting.
* Perform matrix multiplication using `np.dot()` and the `@` operator.
* Find the transpose of a matrix.
* Create an identity matrix, diagonal matrix, and random matrix.
* Generate random integers using `np.random` and make the results reproducible using a random seed.
* Create an array containing `NaN` values and identify them using `np.isnan()`.
* Replace `NaN` values with zero or the mean of the available values.
* Normalize a NumPy array using Min-Max normalization.
* **Mini Challenge:** Create a 2D array containing student marks and calculate each student's total, average, highest subject mark, pass/fail status, and class average.

---

## AIML-Oriented Practice
* Generate 100 random values and calculate their mean, median, variance, and standard deviation.
* Generate a $5 \times 5$ matrix and extract its diagonal, upper triangular, and lower triangular parts.
* Create a 3D array representing an RGB image and extract the individual R, G, and B channels.
* Create a feature matrix of shape $(100, 5)$ and calculate the mean and standard deviation of each feature.
* **Final Challenge:** Create a dataset with 1000 samples and 5 features $\rightarrow$ introduce missing values $\rightarrow$ detect and fill the missing values $\rightarrow$ normalize the features $\rightarrow$ split the dataset into training and testing sets using only NumPy.