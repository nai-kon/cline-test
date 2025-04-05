import pytest
from src.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(6) == "Fizz"  # 追加
    assert fizzbuzz(10) == "Buzz"  # 追加
    assert fizzbuzz(12) == "Fizz"  # 追加
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(20) == "Buzz"  # 追加
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"  # 追加
    assert fizzbuzz(23) == "23"