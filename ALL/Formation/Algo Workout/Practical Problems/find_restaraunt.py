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
Explanation: They both have "Shogun" on their preferred list and it has the highest preference score with an index sum of 1 (0+1).
They both listed "KFC" but it has a lower preference score because the index sum is 3 (0+3). Likewise, "Burger King" has a preference score of 4 (2+2).

Input:
nedsChoices = ["Guppy House", "In-n-Out", "Dairy Queen"]
marysChoices = ["In-n-Out", "Guppy House", "Dairy Queen"]
Output: ["Guppy House", "In-n-Out"]
Explanation: They both have "Guppy House" and "In-n-Out" on their preferred list and both restaurants have the same highest total preference score with an index 
sum of 1 (0+1 and 1+0). They both listed "Dairy Queen" but the preference score is 4 (2+2).

🛠️ IMPLEMENT
function findCompatibleRestaurantsBetween(ned, mary) {
def findCompatibleRestaurantsBetween(ned: list[str], mary: list[str]) -> list[str]:
 
P: 
- Result is a list : Result = []
- Dictionary as container to be populated against nedsChoices : neds_dictionary_choices = {restarunt_one: index , restaurant_two:index} 
- iterate through marysChoices and if its in there then add the index that we are at to update the value at neds_dictionary_choices 
- iterate through the dictionary values and have a temp variable called smallest_index 
- smallest_index is instatiated to the value of inf 
- anything smaller 
- if it is smaller we also want to pop off the list if we find a new minimum, and only add to the result if we find a tie 
- return our result 
'''
def findCompatibleRestaurantsBetween(ned: list[str], mary: list[str]) -> list[str]:
    # instantiate our result 
    result = []
    # instantiate our dictionary 
    restaraunt_dictionary = {} 
    
    # # use a set to make sure the restaraunts are in both list 
    # ned_set = set(ned)
    # mary_set = set(mary)
    
    #restaraunt_set = ned_set.intersection(mary_set)
    restaraunt_set = set(ned).intersection(set(mary))
    
    # iterate through our list, we need our indices, starting at index 0 
    for index,restaraunt in enumerate(ned):
        if restaraunt in restaraunt_set:
            restaraunt_dictionary[restaraunt] = index 
    
    # iterate through our mary's choices check to see if there is a crossover
    for index,restaraunt in enumerate(mary):
        if restaraunt in restaraunt_set:
            restaraunt_dictionary[restaraunt] += index 
            
    
    # get the smallest_index in our combination of list
    smallest_index = sorted(restaraunt_dictionary.items(),key=lambda x: x[1])[0][1]
    
    for key,value in restaraunt_dictionary.items():
        # if the value_index is smallest_index 
        if value <= smallest_index:
            result.append(key)
    
    return result 
        

nedsChoices = ["Guppy House", "In-n-Out", "Dairy Queen"]
marysChoices = ["In-n-Out", "Guppy House", "Dairy Queen"]
print(findCompatibleRestaurantsBetween(nedsChoices,marysChoices))
nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["KFC", "Shogun", "Burger King"]
print(findCompatibleRestaurantsBetween(nedsChoices,marysChoices))
nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findCompatibleRestaurantsBetween(nedsChoices,marysChoices))
nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices)
== ["Shogun"])

nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["KFC", "Shogun", "Burger King"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices)
== ["Shogun"])

nedsChoices = ["Guppy House", "In-n-Out", "Dairy Queen"]
marysChoices = ["In-n-Out", "Guppy House", "Dairy Queen"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices).sort()
== ["Guppy House", "In-n-Out"].sort())

nedsChoices = ["Olive Garden", "Outback Steakhouse", "Red Lobster"]
marysChoices = ["Olive Garden", "Outback Steakhouse", "Red Lobster"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices)
== ["Olive Garden"])

nedsChoices = ["Hometown Buffet", "Olive Garden", "Red Lobster"]
marysChoices = ["Panda Express", "Denny's", "Red Lobster"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices)
== ["Red Lobster"])

nedsChoices = ["Costco Food Court"]
marysChoices = ["Costco Food Court"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices)
== ["Costco Food Court"])

nedsChoices = ["Costco Food Court", "Saigon Deli", "Med Mix"]
marysChoices = ["Med Mix", "Saigon Deli", "Costco Food Court"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices).sort()
== ["Saigon Deli", "Costco Food Court", "Med Mix"].sort())

nedsChoices = ["Costco Food Court"]
marysChoices = ["Med Mix", "Saigon Deli", "Costco Food Court"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices)
== ["Costco Food Court"])
nedsChoices = ["Costco Food Court","Saigon Deli","Med Mix"]
marysChoices = ["Med Mix", "Saigon Deli", "Costco Food Court"]
print(findCompatibleRestaurantsBetween(nedsChoices,marysChoices))

def findCompatibleRestaurantsBetween(ned: list[str], mary: list[str]) -> list[str]:
    res = []
    nedPrefs = dict()
    minIndexSum = float('INF')

    for i in range(len(ned)):
        nedPrefs[ned[i]] = i

    for j in range(len(mary)):
        maryPref = mary[j]

        if maryPref in nedPrefs:
            prefSum = j + nedPrefs[maryPref]

        if prefSum < minIndexSum:
            res = [maryPref]
            minIndexSum = prefSum
        elif prefSum == minIndexSum:
            res.append(maryPref)

    return res

nedsChoices = ["Costco Food Court","Saigon Deli","Med Mix"]
marysChoices = ["Med Mix", "Saigon Deli", "Costco Food Court"]
print(findCompatibleRestaurantsBetween(nedsChoices, marysChoices))