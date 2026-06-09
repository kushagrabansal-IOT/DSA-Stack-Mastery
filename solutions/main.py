# DSA-Stack-Mastery — Solutions
# Author: Kushagra Bansal — Project Lab India

def next_greater_element(nums):
    """Monotonic decreasing stack | O(n) T, O(n) S"""
    result = [-1] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            result[stack.pop()] = n
        stack.append(i)
    return result

def next_smaller_element(nums):
    """Monotonic increasing stack | O(n) T, O(n) S"""
    result = [-1] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] > n:
            result[stack.pop()] = n
        stack.append(i)
    return result

def valid_parentheses(s):
    """Match brackets with stack | O(n) T, O(n) S"""
    stack = []; pairs = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in '([{': stack.append(c)
        elif not stack or stack[-1] != pairs[c]: return False
        else: stack.pop()
    return not stack

def evaluate_postfix(expr):
    """Evaluate RPN expression | O(n) T, O(n) S"""
    stack = []
    ops = {'+':lambda a,b:a+b, '-':lambda a,b:a-b,
           '*':lambda a,b:a*b, '/':lambda a,b:int(a/b)}
    for token in expr.split():
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    return stack[0]

class MinStack:
    """O(1) push/pop/top/getMin | O(n) S"""
    def __init__(self):
        self.stack = []; self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        m = min(val, self.min_stack[-1]) if self.min_stack else val
        self.min_stack.append(m)
    def pop(self):
        self.stack.pop(); self.min_stack.pop()
    def top(self): return self.stack[-1]
    def getMin(self): return self.min_stack[-1]

def stock_span(prices):
    """Monotonic stack for span | O(n) T, O(n) S"""
    span = []; stack = []
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] <= p: stack.pop()
        span.append(i - stack[-1] if stack else i + 1)
        stack.append(i)
    return span

def largest_rectangle(heights):
    """Monotonic stack + extend | O(n) T, O(n) S"""
    stack = []; max_area = 0
    heights = heights + [0]
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    return max_area

def daily_temperatures(T):
    """Next warmer day via stack | O(n) T, O(n) S"""
    result = [0] * len(T); stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            j = stack.pop(); result[j] = i - j
        stack.append(i)
    return result

def remove_k_digits(num, k):
    """Greedy monotonic stack | O(n) T, O(n) S"""
    stack = []
    for d in num:
        while k and stack and stack[-1] > d:
            stack.pop(); k -= 1
        stack.append(d)
    if k: stack = stack[:-k]
    return ''.join(stack).lstrip('0') or '0'

if __name__ == "__main__":
    print("="*58)
    print("  DSA Stack Mastery — Project Lab India")
    print("="*58)
    print(f"  NGE([4,5,2,10]):              {next_greater_element([4,5,2,10])}")
    print(f"  Valid '()[]{{}}'              {valid_parentheses('()[]{{}')}")
    print(f"  Postfix '5 1 2 + 4 * + 3 -': {evaluate_postfix('5 1 2 + 4 * + 3 -')}")
    ms=MinStack(); [ms.push(x) for x in [5,3,7,2,8]]
    print(f"  MinStack getMin():            {ms.getMin()}")
    print(f"  StockSpan:                    {stock_span([100,80,60,70,60,75,85])}")
    print(f"  LargestRectangle [2,1,5,6]:   {largest_rectangle([2,1,5,6,2,3])}")
    print(f"  DailyTemps [73,74,75,71]:     {daily_temperatures([73,74,75,71,69,72,76,73])}")
    print("="*58)
