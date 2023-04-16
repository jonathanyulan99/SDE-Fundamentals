'''
❓ PROMPT
Most commercial software utilize logs to track what happens in the system and when.
These logs often record everything including user actions (what features were used) as well as important thing that may happen deep in the back end.
By looking at charts of how many events happen over the course of each hour teams can monitor the health of their products and systems. 
 
You are given an array of [timestamp, country] pairs representing the log for a particular event. 
Each timestamp represents the number of seconds since January 1, 1970, at 00:00:00 GMT. 
Your task is to write a function that takes this array of pairs and returns a map of country to a time sorted list of hourly event counts. 
Each hourly event count is a pair: the hour (timestamp rounded down to the nearest hour) and the event count in that hour.

Write a function count_events(events: List[List[int, str]]) -> Dict[str, List[Tuple[int, int]]] that takes the following parameter:

events: a list of [timestamp, country] pairs, where timestamp is an integer representing the number of seconds since January 1, 1970, at 00:00:00 GMT 
and country is a string representing the country code.
The function should return a dictionary that maps each country to a list of (hour, count) pairs, where hour is the timestamp rounded down to the nearest
hour, and count is the number of events that occurred in that hour. The list should be sorted in ascending order of hour.

Example(s)
Input:

events = [
    [1615369200, 'US'],  # March 9, 2021 11:00:00 PM GMT
    [1615372800, 'US'],  # March 10, 2021 12:00:00 AM GMT
    [1615376400, 'US'],  # March 10, 2021 1:00:00 AM GMT
    [1615380000, 'US'],  # March 10, 2021 2:00:00 AM GMT
    [1615383600, 'US'],  # March 10, 2021 3:00:00 AM GMT
    [1615387200, 'US'],  # March 10, 2021 4:00:00 AM GMT
    [1615390800, 'US'],  # March 10, 2021 5:00:00 AM GMT
    [1615394400, 'US'],  # March 10, 2021 6:00:00 AM GMT
    [1615398000, 'US'],  # March 10, 2021 7:00:00 AM GMT
]

Output:

{
    'US': [
        (1615369200, 1),
        (1615372800, 1),
        (1615376400, 1),
        (1615380000, 1),
        (1615383600, 1),
        (1615387200, 1),
        (1615390800, 1),
        (1615394400, 1),
        (1615398000, 1),
    ],
}
 
You are given an array of [timestamp, country] pairs representing the log for a particular event. 
Each timestamp represents the number of seconds since January 1, 1970, at 00:00:00 GMT. 
Your task is to write a function that takes this array of pairs and returns a map of country to a time sorted list of hourly event counts. 
Each hourly event count is a pair: the hour (timestamp rounded down to the nearest hour) and the event count in that hour.

Write a function count_events(events: List[List[int, str]]) -> Dict[str, List[Tuple[int, int]]] that takes the following parameter:

events: a list of [timestamp, country] pairs, where timestamp is an integer representing the number of seconds since January 1, 1970, at 00:00:00 GMT 
and country is a string representing the country code.
The function should return a dictionary that maps each country to a list of (hour, count) pairs, where hour is the timestamp rounded down to the nearest
hour, and count is the number of events that occurred in that hour. The list should be sorted in ascending order of hour.
 

🛠️ IMPLEMENT
def count_events(events: List[List[int, str]]) -> Dict[str, List[Tuple[int, int]]]

make a dictionary to return as a result
then we can create a dictionary based on our list[1] value 

events[0] => [1615369200, 'US']
events[0][0] => [1615369200]
events[0][1] => ['US']

'''
event = [
    [1615369200, 'US'],  # March 9, 2021 11:00:00 PM GMT
    [1615372800, 'US'],  # March 10, 2021 12:00:00 AM GMT
    [1615376400, 'US'],  # March 10, 2021 1:00:00 AM GMT
    [1615380000, 'US'],  # March 10, 2021 2:00:00 AM GMT
    [1615383600, 'US'],  # March 10, 2021 3:00:00 AM GMT
    [1615387200, 'US'],  # March 10, 2021 4:00:00 AM GMT
    [1615390800, 'US'],  # March 10, 2021 5:00:00 AM GMT
    [1615394400, 'US'],  # March 10, 2021 6:00:00 AM GMT
    [1615398000, 'UK'],  # March 10, 2021 7:00:00 AM GMT
]

def count_events(events: list[list[int, str]]) -> dict[str, list[tuple[int, int]]]:
        result = {} 
        final = {} 
        for element in events: 
            country = element[1]
            time = element[0]
            result_value = result.get(country,'X')
            # if 'X' not in our result yet 
            # add it 
            if result_value == 'X':
                result[country] = [time]
            else:
                result[country].append(time)
            final[country] = [] 
                
        country_keys = list(result.keys()) 
        for country in country_keys: 
            values = result[country]
            for value in values:
                count = values.count(value)
                if value not in list(final.values()):
                    final[country].append(tuple((value,count)))
        
        return final 

from collections import defaultdict

def count_events(events):
    # default dictionary is the same as a dictionary except there is no key raised error 
    # the defaultdict(value) being passed ensures that a list is outputted if there was to raise an issue where a key-error would exist or is missing 
    counts = dict() 
    # counts = defaultdict(list)
    for event in events:
        country, timestamp = event[1], event[0]
        hour = (timestamp // 3600) * 3600
        key_value = counts.get(country,'X')
        if key_value != 'X':
            counts[country].append(hour)
        else:
            counts[country] = [hour]
        # counts[country].append(hour)
        
    for country in counts:
        counts[country].sort()
        hourly_counts = []
        # get our very first value in our list for our first key in our dictionary 
        hour = counts[country][0]
        count = 0
        for i in range(0,len(counts[country])):
            if counts[country][i] != hour:
                hourly_counts.append((hour, count))
                count = 1
                hour = counts[country][i]
            else:
                count += 1

        hourly_counts.append((hour, count))

        counts[country] = hourly_counts

    return counts
            

def test_count_events_single_event():
    events = [
        [1615399200, 'US'],  # March 10, 2021 7:00:00 AM GMT
    ]

    expected_output = {
        'US': [
            (1615399200, 1),
        ],
    }

    return(count_events(events) == expected_output)


def test_count_events_multiple_events_same_country():
    events = [
        [1615399200, 'US'],  # March 10, 2021 7:00:00 AM GMT
        [1615402800, 'US'],  # March 10, 2021 8:00:00 AM GMT
        [1615406400, 'US'],  # March 10, 2021 9:00:00 AM GMT
        [1615410000, 'US'],  # March 10, 2021 10:00:00 AM GMT
        [1615413600, 'US'],  # March 10, 2021 11:00:00 AM GMT
        [1615417200, 'US'],  # March 10, 2021 12:00:00 PM GMT
        [1615420800, 'US'],  # March 10, 2021 1:00:00 PM GMT
        [1615424400, 'US'],  # March 10, 2021 2:00:00 PM GMT
        [1615428000, 'US'],  # March 10, 2021 3:00:00 PM GMT
    ]

    expected_output = {
        'US': [
            (1615399200, 1),
            (1615402800, 1),
            (1615406400, 1),
            (1615410000, 1),
            (1615413600, 1),
            (1615417200, 1),
            (1615420800, 1),
            (1615424400, 1),
            (1615428000, 1),
        ],
    }

    return(count_events(events) == expected_output)


def test_count_events_multiple_events_multiple_countries():
    events = [
        [1615399200, 'US'],  # March 10, 2021 7:00:00 AM GMT
        [1615399200, 'UK'],  # March 10, 2021 7:00:00 AM GMT
    ]

    expected_output = {
        'US': [
            (1615399200, 1),
        ],
        'UK': [
            (1615399200, 1),
        ],
    }

    return(count_events(events) == expected_output)


def test_count_events_multiple_events_same_hour():
    events = [
        [1615399200, 'US'],  # March 10, 2021 7:00:00 AM GMT
        [1615399200, 'UK'],  # March 10, 2021 7:00:00 AM GMT
        [1615402800, 'UK'],  # March 10, 2021 8:00:00 AM GMT
        [1615402800, 'US'],  # March 10, 2021 8:00:00 AM GMT
        [1615402800, 'US'],  # March 10, 2021 8:00:00 AM GMT
        [1615406400, 'US'],  # March 10, 2021 9:00:00 AM GMT
        [1615406400, 'US'],  # March 10, 2021 9:00:00 AM GMT
        [1615410000, 'UK'],  # March 10, 2021 10:00:00 AM GMT
        [1615413600, 'US'],  # March 10, 2021 11:00:00 AM GMT
    ]

    expected_output = {
        'US': [
            (1615399200, 2),
            (1615402800, 3),
            (1615406400, 2),
            (1615410000, 1),
            (1615413600, 1),
        ],
    }

    return(count_events(events) == expected_output)

events = [
        [1615399200, 'US'],  # March 10, 2021 7:00:00 AM GMT
        [1615399200, 'US'],  # March 10, 2021 7:00:00 AM GMT
        [1615402800, 'US'],  # March 10, 2021 8:00:00 AM GMT
        [1615402800, 'US'],  # March 10, 2021 8:00:00 AM GMT
        [1615402800, 'US'],  # March 10, 2021 8:00:00 AM GMT
        [1615406400, 'US'],  # March 10, 2021 9:00:00 AM GMT
        [1615406400, 'US'],  # March 10, 2021 9:00:00 AM GMT
        [1615410000, 'US'],  # March 10, 2021 10:00:00 AM GMT
        [1615413600, 'US'],  # March 10, 2021 11:00:00 AM GMT
    ]

print(count_events(events))

def test_count_events_empty_input():
    events = []

    expected_output = {}

    assert count_events(events) == expected_output
            
            