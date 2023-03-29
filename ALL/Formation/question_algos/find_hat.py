'''
❓ PROMPT
Oliver the Dog is missing his favorite hat and is asking his friends at the dog park if they've seen it.
Each dog either has seen it or suggests a list of other dogs to ask. Return the name of the dog who has seen the hat.
Oliver starts out by asking his best friend. This function will take two parameters. The first is a map of dogs to a list of their friends.
The second is Oliver's best friend, who Oliver will ask first.

One of the most common uses of a queue is to keep a list of "work to be done". Just like doing housework, often new things get added to the to-do
list while doing some other task. New jobs get added to the end of the queue, and when one is complete, the next one is taken from the top of the list.

As a follow-up, how would you handle it when there's circular knowledge? For example, Jono's suggestion is to ask Angus, and Angus' suggestion is to ask
Jono. These 'cycles' aren't restricted to pairs of dogs, they can be of any size.

Example(s)
dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], // Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Carter'],
  'Snoopy': ['Pepper'],
  'Fido': []
}
findHat(dogs, 'Loki') == 'Ivy'


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
function findHat(dogs, bestFriend) {
def findHat(dogs: dict, bestFriend: str) -> str:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
from collections import deque


def findHat(dogs: dict, bestFriend: str) -> str:
    queue = deque([bestFriend])
    seen_friends = []

    while queue:
        friend = queue.pop()
        seen_friends.append(friend)
        friends_or_hat = dogs.get(friend)

        for friend_or_hat in friends_or_hat:
            if seen_friends.count(friend_or_hat) > 0:
                continue
            if friend_or_hat == 'HAT':
                return friend
            else:
                queue.appendleft(friend_or_hat)

    return "Couldn't find the hat"


dogs = {
    'Carter': ['Fido', 'Ivy'],
    'Ivy': ["HAT"],  # Ivy has seen the hat
    'Loki': ['Snoopy'],
    'Pepper': ['Carter'],
    'Snoopy': ['Pepper'],
    'Fido': []
}
print(findHat(dogs, 'Loki') == "Ivy")
print(findHat(dogs, 'Snoopy') == "Ivy")
print(findHat(dogs, 'Ivy') == "Ivy")
print(findHat(dogs, 'Fido') == "Couldn't find the hat")

dogs = {
    'Ariel': ['Bork'],
    'Bork': ['Cassie'],
    'Cassie': ['Drex'],
    'Drex': ['Zoe'],
    'Zoe': ["HAT"],
}
print(findHat(dogs, "Ariel") == "Zoe")
print(findHat(dogs, "Bork") == "Zoe")
print(findHat(dogs, "Cassie") == "Zoe")
print(findHat(dogs, "Drex") == "Zoe")
print(findHat(dogs, "Zoe") == "Zoe")

dogs = {
    'Zoe': ['Jono'],
    'Jono': ['Angus'],  # dead-end, circular knowledge
    'Angus': ['Jono'],  # dead-end, circular knowledge
    'Paavo': ['Zoe', 'Oliver'],
    'Oliver': ["HAT"],
}
print(findHat(dogs, "Paavo") == "Oliver")
print(findHat(dogs, "Oliver") == "Oliver")
print(findHat(dogs, "Zoe") == "Couldn't find the hat")
print(findHat(dogs, "Angus") == "Couldn't find the hat")
print(findHat(dogs, "Jono") == "Couldn't find the hat")

dogs = {
    'Zoe': ['Jono'],  # circular knowledge
    'Jono': ['Angus'],  # circular knowledge
    'Angus': ['Paavo'],  # circular knowledge
    'Paavo': ['Zoe', 'Oliver', 'Angus'],  # can lead to circular knowledge
    'Oliver': ["HAT"],
}

print(findHat(dogs, "Paavo") == "Oliver")
print(findHat(dogs, "Oliver") == "Oliver")
print(findHat(dogs, "Zoe") == "Oliver")
print(findHat(dogs, "Angus") == "Oliver")
print(findHat(dogs, "Jono") == "Oliver")
'''
queue.appendleft('Carter')
for friend_or_hat in friends_or_hat: ['Carter']
friends_or_hat = dogs.get('Pepper')
friend = deque.pop() #'Pepper'
else queue.appendleft('Pepper')
for friend_or_hat in friends_or hat: ['Pepper']
friends_or_hat = dogs.get('Snoopy') #['Pepper']
friend = deque.pop() # 'Loki'
while--->
else condition queue.appendleft(friend_or_hat) #'Snoopy'
for friend in friends_or hat: ['Snoopy']
dogs.get('Loki') # ['Snoopy']
friend = deque.pop() # 'Loki'
while -->
queue = deque([Loki])
findHat(dogs,bestFriend)
'''
