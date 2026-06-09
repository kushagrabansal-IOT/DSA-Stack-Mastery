# Stack — Learning Notes
# By Kushagra Bansal | Project Lab India

## When To Use Stack
- Next Greater/Smaller Element → Monotonic Stack
- Matching brackets/parentheses → Push/Pop pairs
- Undo operations → Stack of states
- Backtracking → Explicit stack replaces recursion
- Expression evaluation → Operator precedence

## Monotonic Stack Template
# For Next Greater Element (decreasing stack):
stack = []
for i, n in enumerate(nums):
    while stack and nums[stack[-1]] < n:    # condition varies
        result[stack.pop()] = n             # found answer
    stack.append(i)

## Min Stack — Two Stack Trick
push: min_stack.append(min(val, min_stack[-1] if min_stack else val))
pop: both stacks pop together
getMin: min_stack[-1]  ← always current minimum in O(1)

## Common Patterns
| Problem Type | Stack Type | Key |
|-------------|-----------|-----|
| NGE | Decreasing | pop when cur > stack top |
| NSE | Increasing | pop when cur < stack top |
| Histogram | Increasing | extend leftward |
| Daily Temps | Decreasing indices | pop when warmer found |
