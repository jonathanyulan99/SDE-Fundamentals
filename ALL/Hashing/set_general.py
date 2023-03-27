# SETS: unordered, mutable, no duplicates
my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set, type(my_set))

my_set_2 = set([1, 2, 3, 4, 5])
my_set_3 = set("HELLO")
# NOTE THAT THIS IS UNORDERED
print(my_set_3)
# an empty set must be used with set()
# SETS ARE MUTABLE

my_set.add(6)
my_set.add(7)
my_set.remove(1)
# .remove raises a key error
# .discard doesn't raise a key error
try:
    my_set.remove(90)
except:
    print("ERROR")

my_set.discard(90)
# my_set.clear() clears our entire set
# my_set.pop() removes a random element in the set

for element in my_set:
    print(element)

if 1 in my_set:
    print("1 is in our set")

odds = {1, 3, 5}
evens = {2, 4, 6}
primes = {2, 3, 5, 7}

# combines two sets without duplication
union_odds_primes = odds.union(primes)
print(union_odds_primes)

# intersection will only find elements in both sets
intersection = odds.intersection(evens)
print(intersection)

# intersection of all the prime odd numbers
intersection_prime_odd = odds.intersection(primes)
print(intersection_prime_odd)

# takes odds that are in the first set but not in the second set
diff = odds.difference(evens)
print(diff)

# symmetrical difference returns a set from the original set, and
# the other set but not in both sets
symm_diff = evens.symmetric_difference(odds)
print(symm_diff)

# update one set with another set
evens.update(odds)
print(evens)
print(odds)

# intersection_update - updates the set that keeps only the elements in both sets
odds.intersection_update(evens)
print(odds)

# subset - all elements in first set are in the second set
print(odds.issubset(evens))

# superset - all elements in the first set have all the numbers in the second set
print(odds.issuperset(evens))

# disjoint - returns true if both sets have no same elements
print(odds.isdisjoint(evens))

frozen_set = frozenset([1, 2, 3, 4])
# cannot add forzen_set.remove() or .add() or any update methods() will not work!
