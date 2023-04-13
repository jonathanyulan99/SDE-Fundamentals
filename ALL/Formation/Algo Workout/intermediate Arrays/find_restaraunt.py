'''
❓ PROMPT
Ned and Mary want to choose a restaurant to bring their kids to for the evening, and they both have a list of their favorite places, 
represented by strings and sorted by preference. The place they each prefer the most is at the beginning of the list, and their least preferred at the end.

You need to help them find the optimal match to dine at based on their combined preferences score. 
They will often have to compromise, so their ideal option is a place they both have on their list, and it has the highest combined preference score.

To calculate the highest combined preference score, get the restaurant with the minimum index sum 
when adding the indices of the restaurant on both of their lists together. If multiple restaurants have the same highest score, output all of them.

Example(s)
Input:
nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Input:
nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: They both have "Shogun" on their preferred list and it has the highest preference score with an index sum of 1 (0+1). They both listed "KFC" but it has a lower preference score because the index sum is 3 (0+3). Likewise, "Burger King" has a preference score of 4 (2+2).

Input:
nedsChoices = ["Guppy House", "In-n-Out", "Dairy Queen"]
marysChoices = ["In-n-Out", "Guppy House", "Dairy Queen"]
Output: ["Guppy House", "In-n-Out"]
Explanation: They both have "Guppy House" and "In-n-Out" on their preferred list and both restaurants have the same highest total preference score with an index sum of 1 (0+1 and 1+0). They both listed "Dairy Queen" but the preference score is 4 (2+2).
 

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
function findCompatibleRestaurantsBetween(ned, mary) {
def findCompatibleRestaurantsBetween(ned: list[str], mary: list[str]) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''