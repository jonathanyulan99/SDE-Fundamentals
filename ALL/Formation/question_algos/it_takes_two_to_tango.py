'''
It takes two to Tango!

A dance studio is holding a Tango lesson tonight involving 2 half-hour sessions.
The studio is creating a plan to pair dancers in the second session with a different partner from the first session. 
Given a list of Tango pairs for each session, determine if the studio will pair up any partners twice.

This problem aims to familiarize you with storing and retrieving information from data structures to create a minimal algorithm.
In this instance, the Engineering Method is valuable because it helps you arrive at a more optimal algorithm than brute force.

As a follow-up, how would you write an algorithm to detect repeated pairs in 3 sessions, in any number of sessions? 
How would you write an O(N) time algorithm to determine how often the matcher created each pair? 
Again, it should count pairs in reversed order as the same pair.
 

EXAMPLE(S)
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Charles"], ["Baxter", "Davis"], ["Alice", "Daniels"]]
hasRepeatTangoPartner(session1, session2) == False

session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Daniels"], ["Alice", "Charles"], ["Baxter", "Davis"]]
hasRepeatTangoPartner(session1, session2) == True

Jack and Daniels have been partnered up on both sessions.
 

FUNCTION SIGNATURE
def hasRepeatTangoPartner(firstSession: list[str], secondSession: list[str]) -> bool:
'''


def hasRepeatTangoPartner(firstSession: list[str], secondSession: list[str]) -> bool:
    dancer_pair_frequency = {}

    for index in range(len(firstSession)):
        pair = list(sorted(firstSession[index]))
        count = dancer_pair_frequency.get(pair[0], 0)+1
        dancer_pair_frequency[pair[0]] = pair

    for index in range(len(secondSession)):
        pair = list(sorted(secondSession[index]))
        count = dancer_pair_frequency.get(pair[0], -1)
        if count == pair:
            return True

    return False


session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Charles"], ["Baxter", "Davis"], ["Alice", "Daniels"]]
print(hasRepeatTangoPartner(session1, session2) == False)

session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Daniels"], ["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == True)

# swapped ordering shouldn't affect the correctness
session1 = [["Alice", "Baxter"]]
session2 = [["Baxter", "Alice"]]
print(hasRepeatTangoPartner(session1, session2) == True)

# disjoint list
session1 = [["Alice", "Baxter"]]
session2 = [["Charles", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == False)

# partner mixing
session1 = [["Alice", "Baxter"], ["Charles", "Davis"]]
session2 = [["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == False)

# more partner mixing
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Charles"], ["Baxter", "Davis"], ["Alice", "Daniels"]]
print(hasRepeatTangoPartner(session1, session2) == False)

# 1 overlap
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Daniels"], ["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == True)

# overlap with flipped partners
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Daniels", "Jack"], ["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == True)

# no overlap
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jono", "Paavo"], ["Zoe", "Angus"], ["Oliver", "Pixel"]]
print(hasRepeatTangoPartner(session1, session2) == False)
