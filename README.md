# Super30 Python While Loop Task

## Objective

The objective of this task is to understand condition-controlled iteration and learn when a `while` loop is more appropriate than a `for` loop.

## Concepts Covered

* `while` loop
* Initialization
* Loop condition
* Update
* Loop termination
* Modulus operator `%`
* Integer division `//`
* User input
* `break`
* Menu-driven programs
* Condition-controlled iteration

## Project Structure

```text
super30-python-while-loop-task/
│
├── 01_print_1_to_100.py
├── 02_print_100_to_1.py
├── 03_even_numbers.py
├── 04_sum_of_digits.py
├── 05_reverse_integer.py
├── 06_count_digits.py
├── 07_factorial.py
├── 08_sum_until_zero.py
├── 09_password_checker.py
├── 10_guessing_game.py
├── 11_menu_calculator.py
├── 12_atm_menu.py
└── README.md
```

## Questions and Approach

### Q1. Print 1 to 100

A `while` loop starts at 1 and continues while the number is less than or equal to 100.

### Q2. Print 100 to 1

The loop starts at 100 and decreases the number by 1 during every iteration.

### Q3. Even Numbers

The program checks each number using the modulus operator. A number is even when its remainder after division by 2 is zero.

### Q4. Sum of Digits

The `% 10` operation extracts the last digit, while `// 10` removes the last digit.

**Sample Input:**

```text
5832
```

**Sample Output:**

```text
18
```

### Q5. Reverse an Integer

The program extracts digits from right to left and constructs the reversed number.

**Sample Input:**

```text
12345
```

**Sample Output:**

```text
54321
```

### Q6. Count Digits

The program repeatedly divides the number by 10 until no digits remain. The number of iterations gives the number of digits.

**Sample:**

```text
Input: 5832
Output: 4
```

### Q7. Factorial

The factorial is calculated using a `while` loop.

**Sample Input:**

```text
5
```

**Sample Output:**

```text
120
```

### Q8. Sum Until Zero

The program repeatedly accepts numbers and adds them to a total. The loop terminates when the user enters `0`.

**Sample Run:**

```text
10
20
15
5
0

Sum: 50
```

This is a good example of why a `while` loop is useful when the number of iterations is unknown.

### Q9. Password Checker

The program repeatedly asks for a password until the correct password is entered.

A `while` loop is appropriate because the number of attempts is unknown.

### Q10. Guessing Game

A predefined secret number is used. The user continues guessing until the correct number is entered.

### Q11. Menu-Driven Calculator

The calculator provides:

```text
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
```

The menu continues until the user chooses Exit.

### Q12. ATM Menu

The ATM provides:

* Check Balance
* Deposit
* Withdraw
* Exit

The application continues running until the user explicitly selects Exit.

## While Loop Structure

The basic structure is:

```text
Initialization
      ↓
Condition
      ↓
Logic
      ↓
Update
      ↓
Condition again
```

For example:

```python
number = 1

while number <= 100:
    print(number)
    number = number + 1
```

## Why Use `while` Instead of `for`?

A `for` loop is generally useful when the number of iterations is known or when iterating over a sequence.

A `while` loop is useful when the number of iterations depends on a condition.

Examples from this task:

* Password checker: number of attempts is unknown.
* Guessing game: number of guesses is unknown.
* Sum until zero: number of inputs is unknown.
* Calculator: number of operations is unknown.
* ATM: number of transactions is unknown.

## Avoiding Infinite Loops

Every major `while` loop should have:

1. Initialization
2. Condition
3. Update or termination

For example:

```python
number = 1

while number <= 100:
    print(number)
    number = number + 1
```

The update ensures that the loop eventually reaches the termination condition.

## Video Demonstration

The YouTube video explains:

* Basic `while` loop
* Initialization
* Condition
* Update
* Digit manipulation
* Why `while` is preferable to `for`
* Password checker
* Guessing game
* Menu-driven calculator
* ATM menu
* Test cases

## Submission

**GitHub Repository:** `super30-python-while-loop-task`

**GitHub Repository Link:** Add the public GitHub repository link here.
