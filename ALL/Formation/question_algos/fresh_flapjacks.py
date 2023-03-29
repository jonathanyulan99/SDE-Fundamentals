'''
❓ PROMPT
A restaurant has a dedicated cook making flapjacks (pancakes) in the mornings. 
First, they're removed from the griddle and added to a stack as they're ready. 
Then, servers remove them from the stack to serve customers. The manager wants to serve fresh flapjacks, 
meaning they never want the stack to be taller than 4. At the same time, they want the stack never to be 
empty so that no orders have to wait for pancakes.

Write a function that takes a series of numbers representing flapjacks being added and removed 
from the stack (positive for fresh off the grill, negative for an order being served). 
Return a tuple (or pair), where the first value is true or false to reflect if the manager's constraints
are always satisfied, and the second value is the max height of the stack.

Example(s)
goldilockFlapjacks([2, -1]) => [true, 2]
goldilockFlapjacks([-1, 2]) => [false, 1]
goldilockFlapjacks([2, -1, 3, -3, 2, -1]) => [true, 4]
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function goldilockFlapjacks(pancakes) {
def goldilockFlapjacks(pancakes: list[int]) -> list:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def goldilockFlapjacks(pancakes: list[int]) -> list:
    _max = 0
    _counter = 0
    _manager_condition = True

    for pancake in pancakes:
        _counter += pancake
        if _counter <= 0 or _counter > 4:
            _manager_condition = False
        if _counter > _max:
            _max = _counter

    return [_manager_condition, _max]


print(goldilockFlapjacks([2, -1, 3, -3, 2, -1]))
print(goldilockFlapjacks([2]) == [True, 2])
print(goldilockFlapjacks([-2]) == [False, 0])
print(goldilockFlapjacks([4]) == [True, 4])
print(goldilockFlapjacks([5]) == [False, 5])
print(goldilockFlapjacks([4, -2, 1, -2]) == [True, 4])
print(goldilockFlapjacks([2, -1, 1, -1, 1]) == [True, 2])
print(goldilockFlapjacks([4, -2, 1, -2, 4]) == [False, 5])
print(goldilockFlapjacks([4, -2, 1, -2, -4]) == [False, 4])
