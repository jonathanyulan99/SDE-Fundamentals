'''
❓ PROMPT
You open up your computer's downloads folder, looking for that cute video of Oliver barking at the doorbell you downloaded a few weeks ago. 
Of course, it's mixed in with all of the other silly otter videos and other stuff you just had to save. 
To make it easier to find, you click on the column to sort the view by date to see the most recent first, at the top.

For this problem, we're going to implement that file system sort by date. The files themselves are represented by objects:

{
  "filename": <string>,
  "size": <number>,
  "date": <string>}

and the date itself is in US format:

MM-DD-YYYY HH:MM:SS

Write a function that sorts an array of these file objects, with the most recent at the top.

Follow-up:

- What happens if a date like 2 Feb 2021 is compared with 12 Nov 2021 and the day and month don't have leading zeros: 2-2-2021? 
How can the code be modified to handle this?

- If the dates are tied down to the second, add a secondary sort by file name in descending order.

Example(s)
Input: sortFiles([
  {"filename": "otter.mpeg", "size": 512, "date": "01-16-2023 14:23:13"},
  {"filename": "oliver.mp4", "size": 1024, "date": "01-18-2023 12:46:57"},
])

Output: [
  {"filename": "oliver.mp4", "size": 1024, "date": "01-18-2023 12:46:57"},
  {"filename": "otter.mpeg", "size": 512, "date": "01-16-2023 14:23:13"},
]

🛠️ IMPLEMENT
function sortFiles(files) {
def sortFiles(files: list) -> list:

Plan: 
Input => {"key":"str",
            "filename":"otter.mpeg",
            "size":512,
            "date":""
            }
Input["date"]: "01-18-2023 12:46:57"
value = Input["date"]
    input = value.split() # 01-18-2023 12:46:57
    input[0] = 01-18-2023
    input[0].split() => 01 18 2023 
    month,day,year = input[0].split("-")
    input[1] = 12:46:57
    input[1].split() => 12 46 57
    hours,minutes,seconds = input[1].split(":")

Output => List
    1. Obtain the Input Object 
    2. Pre-process data on the Input["date"] key 
    3. Obtain date by splitting on the Input['date'] key
    4. first entry is automatically sorted 
        5. then take the second entry and compare it to the year 
            6. if same year compare it to the month, then day 
                7. if same day then compare it by hours 
                    8. if same day then most recent would be latest time 
                        9.latest time meaning that whatever hour is greater 
                            10. if same hour compare on minutes, seconds 
'''
def sortFiles(files:list)->list:
    result = list()
    if len(files) == 1:
        result.append(files[0])
        return result 
    
    # automatically pre-populate our list with the first file to compare too 
    result.append(files[0])
    
    for i in range(1,len(files)):
        date_time = files[i]['date']
        date_time = date_time.split() 
        date = date_time[0]
        time = date_time[1]
        month1,day1,year1 = date.split('-')
        month1, day1, year1 = map(int,[month1,day1,year1])
        hour1,minute1,second1 = time.split(':')
        hour1, minute1, second1 = map(int,[hour1,minute1,second1])
        for j in range(len(result)):
            result_date_time = result[j]['date']
            result_date_time = result_date_time.split() 
            result_date = result_date_time[0]
            result_time = result_date_time[1]
            month2,day2,year2 = result_date.split('-')
            month2, day2, year2 = map(int,[month2,day2,year2])
            hour2,minute2,second2 = result_time.split(':')
            hour2, minute2, second2 = map(int,[hour2,minute2,second2])
            if year2 > year1:
                result.append(files[i])
            elif year1 > year2:
                result.insert(j,files[i])
            else: 
                if month2 > month1: 
                    result.append(files[i])
                elif month1 > month2:
                    result.insert(j,files[i])
                else:
                    if day2 > day1:
                        result.append(files[i])
                    elif day1 > day2:
                        result.insert(j,files[i])
                    else:
                        if hour2 > hour1:
                            result.append(files[i])
                        elif hour1 > hour2:
                            result.insert(j,files[i])
                        else:
                            if minute2 > minute1:
                                result.append(files[i])
                            elif minute1 > minute2:
                                result.insert(j,files[i])
                            else:
                                if second2 > second1:
                                    result.append(files[i])
                                elif second1 > second2:
                                    result.insert(j,files[i])
                                    
    return result 
                        
    

print(sortFiles([{"filename": "otter.mpeg", "size": 512, "date": "01-16-2023 14:23:13"},{"filename": "oliver.mp4", "size": 1024, "date": "01-18-2023 12:46:57"}]))
# single file
files = [{"filename": "file1.txt", "size": 10, "date": "03-28-2023 12:00:00"}]
expected = files
print(sortFiles(files) == expected)

files = [
  {"filename": "otter.mpeg", "size": 512, "date": "01-16-2023 14:23:13"},
  {"filename": "oliver.mp4", "size": 1024, "date": "01-18-2023 12:46:57"},
]
expected = [
  {"filename": "oliver.mp4", "size": 1024, "date": "01-18-2023 12:46:57"},
  {"filename": "otter.mpeg", "size": 512, "date": "01-16-2023 14:23:13"},
]
print(sortFiles(files) == expected)

# files sorted descending
files = [
  {"filename": "file1.txt", "size": 10, "date": "03-28-2023 12:00:00"},
  {"filename": "file2.txt", "size": 20, "date": "03-27-2023 13:00:00"},
  {"filename": "file3.txt", "size": 30, "date": "03-26-2023 14:00:00"},
]
expected = [
  {"filename": "file1.txt", "size": 10, "date": "03-28-2023 12:00:00"},
  {"filename": "file2.txt", "size": 20, "date": "03-27-2023 13:00:00"},
  {"filename": "file3.txt", "size": 30, "date": "03-26-2023 14:00:00"},
]
print(sortFiles(files))

# # files sorted ascending
# files = [
#   {"filename": "file3.txt", "size": 30, "date": "03-26-2023 14:00:00"},
#   {"filename": "file2.txt", "size": 20, "date": "03-27-2023 13:00:00"},
#   {"filename": "file1.txt", "size": 10, "date": "03-28-2023 12:00:00"},
# ]
# expected = [
#   {"filename": "file1.txt", "size": 10, "date": "03-28-2023 12:00:00"},
#   {"filename": "file2.txt", "size": 20, "date": "03-27-2023 13:00:00"},
#   {"filename": "file3.txt", "size": 30, "date": "03-26-2023 14:00:00"},
# ]
# print(sortFiles(files) == expected)

# # same year/month but different day
# files = [
#   {"filename": "file2.txt", "size": 20, "date": "03-27-2023 05:00:00"},
#   {"filename": "file6.txt", "size": 10, "date": "03-28-2023 10:00:00"},
#   {"filename": "file4.txt", "size": 30, "date": "03-22-2023 14:00:00"},
#   {"filename": "file3.txt", "size": 30, "date": "03-26-2023 02:00:00"},
# ]
# expected = [
#   {"filename": "file6.txt", "size": 10, "date": "03-28-2023 10:00:00"},
#   {"filename": "file2.txt", "size": 20, "date": "03-27-2023 05:00:00"},
#   {"filename": "file3.txt", "size": 30, "date": "03-26-2023 02:00:00"},
#   {"filename": "file4.txt", "size": 30, "date": "03-22-2023 14:00:00"},
# ]
# print(sortFiles(files) == expected)

# # same year/day but different month
# files = [
#   {"filename": "file2.txt", "size": 20, "date": "06-15-2023 05:10:14"},
#   {"filename": "file6.txt", "size": 10, "date": "08-15-2023 12:47:13"},
#   {"filename": "file4.txt", "size": 30, "date": "03-15-2023 11:23:32"},
#   {"filename": "file3.txt", "size": 30, "date": "05-15-2023 18:54:08"},
# ]
# expected = [
#   {"filename": "file6.txt", "size": 10, "date": "08-15-2023 12:47:13"},
#   {"filename": "file2.txt", "size": 20, "date": "06-15-2023 05:10:14"},
#   {"filename": "file3.txt", "size": 30, "date": "05-15-2023 18:54:08"},
#   {"filename": "file4.txt", "size": 30, "date": "03-15-2023 11:23:32"},
# ]
# print(sortFiles(files) == expected)

# # earlier year but later date
# files = [
#   {"filename": "file6.txt", "size": 10, "date": "03-28-2019 10:00:00"},
#   {"filename": "file3.txt", "size": 30, "date": "01-16-2023 02:00:00"},
#   {"filename": "file1.txt", "size": 30, "date": "10-05-2022 06:00:00"},
# ]
# expected = [
#   {"filename": "file3.txt", "size": 30, "date": "01-16-2023 02:00:00"},
#   {"filename": "file1.txt", "size": 30, "date": "10-05-2022 06:00:00"},
#   {"filename": "file6.txt", "size": 10, "date": "03-28-2019 10:00:00"},
# ]
# print(sortFiles(files) == expected)
def sortFiles(files: list) -> list:
    def sortByDate(file):
        date, time = file["date"].split(" ")
        m, d, y = date.split("-")
        return f"{y}:{m}:{d} {time}"

    return sorted(files, key=sortByDate, reverse=True)

def sortFiles(files: list) -> list:
    def sortByDate(file):
        date, time = file["date"].split(" ")
        m, d, y = date.split("-")
        m = m.zfill(2)  # Add leading zero to month if necessary
        d = d.zfill(2)  # Add leading zero to day if necessary
        return f"{y}:{m}:{d} {time}"

    return sorted(files, key=lambda f: (sortByDate(f), f['filename']), reverse=True)