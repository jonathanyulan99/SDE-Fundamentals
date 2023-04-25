class LLNode:
    def __init__(self, value,next=None):
        self.value = value
        self.next = next

def mergeLinkedLists(n1, n2):
    # Merge lists first in-place.
    mergeListsInPlaceHelper(n1, n2, None)

    # If second list has greater value than second, return first list to start.
    # Otherwise return second list (first has lesser value).
    if n1.value < n2.value:
        return n1
    return n2

def mergeListsInPlaceHelper(n1, n2, n1Prev):
    # Handle null case for first node, and merge in second list pointer.
    if n1 is None:
        n1Prev.next = n2
        return
    # Handle null case for second node, no need for more work.
    if n2 is None:
        return
    
    # If second node is bigger, recursively merge again using node one's next pointer and current value as previous.
    if n1.value < n2.value:
        mergeListsInPlaceHelper(n1.next, n2, n1)
    # Otherwise, take previous pointer and set it to point at (next) node two.
    # Create a placeholder variable to keep track of node two's next pointer and reset it to node one.
    # From here, you can continue calling recursively to merge.
    else:
        if n1Prev is not None:
            n1Prev.next = n2
        newP2 = n2.next
        n2.next = n1
        mergeListsInPlaceHelper(n1, newP2, n2)

L1 = LLNode(1,LLNode(2,LLNode(3)))
LL1 = LLNode(1,LLNode(3,LLNode(5)))

mergeLinkedLists(L1,LL1)
while L1:
    print(L1.value,end='-->')
    L1= L1.next 
print("Done")