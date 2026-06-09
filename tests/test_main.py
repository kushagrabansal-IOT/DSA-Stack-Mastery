import sys; sys.path.insert(0,'..')
from solutions.main import *

def test_nge():
    assert next_greater_element([4,5,2,10]) == [5,10,10,-1]
    assert next_greater_element([1,2,3,4]) == [2,3,4,-1]
    assert next_greater_element([4,3,2,1]) == [-1,-1,-1,-1]

def test_valid_parens():
    assert valid_parentheses("()[]{}") == True
    assert valid_parentheses("(]") == False
    assert valid_parentheses("{[]}") == True
    assert valid_parentheses("") == True

def test_postfix():
    assert evaluate_postfix("5 1 2 + 4 * + 3 -") == 14
    assert evaluate_postfix("3 4 +") == 7

def test_min_stack():
    ms = MinStack()
    ms.push(5); ms.push(3); ms.push(7); ms.push(2)
    assert ms.getMin() == 2
    ms.pop()
    assert ms.getMin() == 3

def test_stock_span():
    assert stock_span([100,80,60,70,60,75,85]) == [1,1,1,2,1,4,6]

def test_histogram():
    assert largest_rectangle([2,1,5,6,2,3]) == 10
    assert largest_rectangle([2,4]) == 4

def test_daily_temps():
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
