# Basic FizzBuzz:

Create output following the pattern:
"1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16" for numbers from 1 to 100.


# Extended FizzBuzz

- pass divisor arguments: FizzBuzzExtended(16, {"fizz": 3, "buzz": 4})
- pass any number of divisor arguments: FizzBuzzExtended(17, {"fizz": 3, "buzz": 4, "foo": 8, "bar": 9})
- supplie a range of numbers to generate output: FizzBuzzExtended((2,4)) #-> "2,Fizz,4"
- handle exception for 0 and negative numbers