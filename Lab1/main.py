# Exercise 1.2
flavors = ["vanilla", "chocolate", "strawberry", "pistacchio"]
sauces = ["caramel", "butterscotch", "chocolate"]
for flavor in flavors:
    for sauce in sauces:
        print(flavor + " ice cream sundae with " + sauce + " sauce")

# Exercise 1.3:
def triangle():
    value = 1
    row = 1
    while row <= 10:
        column = 1
        while column <= row:
            if column != row:
                print(value, ' ', sep = '', end = '')
            else:
                print(value)
            value = value + 1
            column = 1

# Exercise 1.4:
## Question 1:
def cube(n):
    return n * n * n

def factorial(n):
    if(n < 0):
        print('Please enter a non integer.')
        return
    if(n == 0):
        return 1

    return n * factorial(n - 1)

def count_pattern(pattern, list):
    count = 0
    i = 0

    for j in range(len(list)):
        if list[j] == pattern[i]:
            i += 1
            if i == len(pattern):
                count += 1
                i = 0
        else:
            if i > 0:
                if list[j] == pattern[0]:
                    i = 1
                else:
                    i = 0

    return count

def multiplication_table(n):
    for i in range(1, n):
        print(f"{n} * {i} = {n * i}")

def simple_calculator():
    while(True):
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        choice = input("Enter the operation you want to perform: \n1. +\n2. -\n3. *\n4. /\nYour choice: ")

        match(choice):
            case 1:
                print(f"{num1} + {num2} = {num1 + num2}")
                break
            case 2:
                print(f"{num1} - {num2} = {num1 - num2}")
                break
            case 3:
                print(f"{num1} * {num2} = {num1 * num2}")
                break
            case 4:
                print(f"{num1} / {num2} = {num1 / num2}")
                break
            case _:
                print("Invalid input please try again\n");
                break

        exit = input("Do you want to exit? Y/n")
        if (exit == 'y' or exit == 'Y'):
            return;

def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    sorted = " ".join(words)
    print(f"The sorted sentence is: {sorted}")

# Question 2:
class RomanNumeral:
    def __init__(self, integer):
        self.integer = integer
        self.roman = ""
        self.nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        self.symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    def convert_to_roman(self):
        i = 12
        number = self.integer
        while number:
            div = number // self.nums[i]
            number %= self.nums[i]
            while div:
                self.roman += self.symbols[i]
                div -= 1
            i -= 1

    def display(self):
        print(f"The integer is {self.integer} and roman numeral is {self.roman}")

# Question 3:
class FindPair:
    def __init__(self, nums):
        self.nums = nums

    def find_pair(self, target):
        for i in range(0, len(self.nums) - 1):
            for j in range(i, len(self.nums)):
                if self.nums[i] + self.nums[j] == target:
                    return i + 1, j + 1                        # Assuming returning indices start from 1
        return -1, -1

# Qustion 4:
class FindTriplets:
    def __init__(self, nums):
        self.nums = nums

    def find_triplets(self):
        self.nums = self.nums.sort()
        triplets = []
        i = 0
        while i < len(self.nums - 2):
            j = i + 1
            k = len(self.nums) - 1
            while j < k:
                if self.nums[i] + self.nums[j] + self.nums[k] < 0:
                    j += 1
                elif self.nums[i] + self.nums[j] + self.nums[k] > 0:
                    k -= 1
                else:
                    triplets.append([self.nums[i], self.nums[j], self.nums[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and self.nums[j] == self.nums[j - 1]:
                        j += 1
                    while j < k and self.nums[k] == self.nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(self.nums) - 2 and self.nums[i] == self.nums[i - 1]:
                i += 1
        return triplets

# Question 5:
class ReverseStringByWord:
    def reverse_string(self, string):
        words = string.split()
        words.reverse()
        reversed = "".join(words)
        print(f"Reversed String: {reversed}")

# Question 6:
class CountCharacters:
    def count_characters(self, string):
        count = 0
        for character in string:
            count += 1
        print(f"The number of characters in string are {count}")

# Question 7 and 8:
class Matrices:
    def add_matrices(self):
        size = input("Enter the size of matrices you want to add: ")
        size = int(size)
        matrix1 = []
        matrix2 = []

        print("Enter elements of first matrix row-wise:")
        for i in  range(0, size):
            row = list(map(int, input().split()))
            matrix1.append(row)

        print("Enter elements of second matrix row-wise:")
        for i in  range(0, size):
            row = list(map(int, input().split()))
            matrix2.append(row)

        result = []
        for i in range(size):
                result.append([0] * size)

        for i in range(0, size):
            for j in range(0, size):
                result[i][j] = matrix1[i][j] + matrix2[i][j]

        print("Added Matrix: ")
        for i in range(0, size):
            for j in range(0, size):
                print(result[i][j], end=' ')
            print()

    def multiply_matrices(self):
        rows1 = int(input("Enter the number of rows for first matrix: "))
        cols1 = int(input("Enter the number of columns for first matrix: "))
        rows2 = int(input("Enter the number of rows for second matrix: "))
        cols2 = int(input("Enter the number of columns for second matrix: "))

        if cols1 != rows2:
            print("Matrix multiplication not possible. Columns of first matrix must equal rows of second matrix.")
            return

        matrix1 = []
        matrix2 = []

        print("Enter elements of first matrix row-wise:")
        for i in range(rows1):
            row = list(map(int, input().split()))
            matrix1.append(row)

        print("Enter elements of second matrix row-wise:")
        for i in range(rows2):
            row = list(map(int, input().split()))
            matrix2.append(row)

        result = []
        for i in range(rows1):
            result.append([0] * cols2)

        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        print("Multiplied Matrix: ")
        for i in range(rows1):
            for j in range(cols2):
                print(result[i][j], end=' ')
            print()

# Question 9:
def calculator(num1, num2, operator = '+', output_format = "-f"):
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Please provide a valid operator<+, -, *, />")
        return -1
    if output_format != "-f" and output_format != "-i":
        print("Please provide valid output format <-i, -f>")
        return -1

    match operator:
        case '+':
            res = num1 + num2
            if(output_format == "-i"):
                print(f"{num1} + {num2} = {round(res)}")
            else:
                print(f"{num1} + {num2} = {res}")
        case '-':
            res = num1 - num2
            if(output_format == "-i"):
                print(f"{num1} - {num2} = {round(res)}")
            else:
                print(f"{num1} - {num2} = {res}")
        case '*':
            res = num1 * num2
            if(output_format == "-i"):
                print(f"{num1} * {num2} = {round(res)}")
            else:
                print(f"{num1} * {num2} = {res}")
        case '/':
            if(num2 == 0):
                print("Cannot divide by zero")
                return -1
            res = num1 / num2
            if(output_format == "-i"):
                print(f"{num1} / {num2} = {round(res)}")
            else:
                print(f"{num1} / {num2} = {res}")


# Question 10:
class Numbers:
    MULTIPLIER = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self, a):
        return a * self.MULTIPLIER

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, new_values):
        if isinstance(new_values, tuple) and len(new_values) == 2:
            self.x, self.y = new_values
        else:
            raise ValueError("Expected a tuple of two numbers.")

    @value.deleter
    def value(self):
        del self.x
        del self.y
