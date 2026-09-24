# Python Functions – Beginner Assessment

## Topics Covered

* Functions without parameters
* Functions with parameters
* Functions with no return value
* Calling functions
* Basic calculations
* Basic conditions and loops

## Instructions

1. Write a separate function for each question.
2. Use `print()` to display the output.
3. Do not use `return`.
4. Call the function after defining it.
5. Use meaningful function names.
6. Keep the code simple and beginner-friendly.

---

# Part A – Functions Without Parameters

## Question 1 – Greeting Function

Create a function `greet()` that prints:

```text
Welcome to Python Programming
```

---

## Question 2 – Student Introduction

Create a function `student_info()` that prints:

* Name
* Age
* Course

Example output:

```text
Name: Rahul
Age: 21
Course: Python
```

---

## Question 3 – Display Numbers

Create a function `display_numbers()` that prints numbers from **1 to 10**.

---

## Question 4 – Display Even Numbers

Create a function `display_even_numbers()` that prints all even numbers from **1 to 20**.

---

## Question 5 – Simple Addition

Create a function `addition()`.

Inside the function, create two numbers and print their sum.

Example:

```text
First number: 10
Second number: 20
Sum: 30
```

---

## Question 6 – Calculate Rectangle Area

Create a function `rectangle_area()`.

Inside the function:

```python
length = 10
width = 5
```

Calculate and print the area of the rectangle.

---

## Question 7 – Calculate Circle Area

Create a function `circle_area()`.

Inside the function:

```python
radius = 7
pi = 3.14
```

Calculate and print the area of the circle.

Formula:

```text
Area = pi × radius × radius
```

---

## Question 8 – Check Even or Odd

Create a function `check_number()`.

Inside the function, store a number and check whether the number is **Even or Odd**.

Example:

```text
Number: 15
15 is Odd
```

---

## Question 9 – Multiplication Table

Create a function `multiplication_table()`.

Inside the function, store a number and print its multiplication table from **1 to 10**.

Example:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

## Question 10 – Simple Interest

Create a function `simple_interest()`.

Inside the function:

```python
principal = 10000
rate = 5
time = 2
```

Calculate and print the Simple Interest.

Formula:

```text
SI = (Principal × Rate × Time) / 100
```

---

# Part B – Functions With Parameters

## Question 11 – Greet Student

Create a function:

```python
greet_student(name)
```

The function should receive a student's name and print a greeting.

Example:

```python
greet_student("Rahul")
```

Output:

```text
Hello Rahul, Welcome to Python!
```

---

## Question 12 – Add Two Numbers

Create a function:

```python
add_numbers(a, b)
```

The function should receive two numbers and print their sum.

Example:

```python
add_numbers(10, 20)
```

Output:

```text
Sum: 30
```

---

## Question 13 – Calculate Square

Create a function:

```python
square(number)
```

The function should receive a number and print its square.

Example:

```python
square(5)
```

Output:

```text
Square: 25
```

---

## Question 14 – Check Even or Odd

Create a function:

```python
check_even_odd(number)
```

The function should receive a number and print whether it is even or odd.

Example:

```python
check_even_odd(12)
```

Output:

```text
12 is Even
```

---

## Question 15 – Calculate Rectangle Area

Create a function:

```python
rectangle_area(length, width)
```

The function should receive length and width and print the area.

Example:

```python
rectangle_area(10, 5)
```

Output:

```text
Area: 50
```

---

## Question 16 – Calculate Student Total

Create a function:

```python
calculate_total(mark1, mark2, mark3)
```

The function should receive three subject marks and print the total.

Example:

```python
calculate_total(70, 80, 90)
```

Output:

```text
Total: 240
```

---

## Question 17 – Calculate Average

Create a function:

```python
calculate_average(mark1, mark2, mark3)
```

The function should receive three subject marks and print the average.

Example:

```python
calculate_average(70, 80, 90)
```

Output:

```text
Average: 80.0
```

---

## Question 18 – Find Largest Number

Create a function:

```python
find_largest(a, b)
```

The function should receive two numbers and print the largest number.

Example:

```python
find_largest(25, 40)
```

Output:

```text
Largest: 40
```

---

## Question 19 – Calculate Salary

Create a function:

```python
calculate_salary(basic_salary, bonus)
```

The function should receive basic salary and bonus and print the total salary.

Example:

```python
calculate_salary(25000, 5000)
```

Output:

```text
Total Salary: 30000
```

---

## Question 20 – Student Result

Create a function:

```python
student_result(name, mark)
```

The function should receive the student's name and mark.

Rules:

```text
Mark >= 50 → Pass
Mark < 50  → Fail
```

Example:

```python
student_result("Rahul", 75)
```

Output:

```text
Rahul
Mark: 75
Result: Pass
```

---

# Function Structure

## Without Parameters

Students should follow this structure:

```python
def function_name():
    # logic
    print()

function_name()
```

## With Parameters

Students should follow this structure:

```python
def function_name(parameter1, parameter2):
    # logic
    print()

function_name(value1, value2)
```

## Important

For this assessment:

* Do **not** use `return`.
* Use `print()` to display the result.
* Do not use global variables unnecessarily.
* Focus on understanding how functions work.
