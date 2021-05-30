#%%
import numpy as np
import csv

times_dict = {'08:15':'0', '08:45':'1','09:15':'2','09:45':'3', '10:15':'4', '10:45':'5','11:15':'6','11:45':'7', '12:15':'8', '12:45':'9','13:15':'10','13:45':'11', '14:15':'12', '14:45':'13','15:15':'14','15:45':'15', '16:15':'16', '16:45':'17','17:15':'18','17:45':'19', '18:15':'20', '18:45':'21','19:15':'22','19:45':'23', '20:15':'24'}
day_dict = {'M': 0, 'T': 1, 'W': 2, 'H': 3, 'F': 4}

def make_2d_array():
    return np.zeros((5, len(times_dict))) # Each row represents a day, each time represents a timeslot
                                          # Ex. Accessing Tuesday's 3rd timeslot: arr[1][2] (0-based indexing)

class Course(object):
        # What is Course?
        # A COURSES_LIST will contain each course (likely for a specific subject).
    def __init__(self, title, course_no, section, times, room):
        self.title = title
        self.course_no = course_no
        self.section = section
        self.times = times        
        # 'times' dict will look like this: 
            # Ex. M 8:15-10:15
            #     W 8:15-9:45
            #     F 14:15-15:45
            # {0: [0,4], 2: [0,3], 4:[12,15]}
        self.room = room
    
    def __str__(self):
        return "Title: " + str(self.title) + "\n" + "Course #: " + str(self.course_no) + "\n" + "Section: " + str(self.section) + "\n" + "Times: " + str(self.times) + "\n" + "Room: " + str(self.room)

def csv_to_2d_arr():
    with open('output.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            data.append(row)
        return data

def convert_table(arr):
    new_table = []
    index_1 = 0
    index_2 = 0
    for row in range(len(arr)-2):
        if arr[row][0] != '':
            index_1 = row
            if arr[row+2][0] != '':
                index_2 = row + 2
            else:
                index_2 = row + 3
            new_table.append(arr[index_1:index_2])
    return new_table # Each row is a course

def string_to_time_list(string):
    time_list = []
    for time in string.split('-'):
        time_list.append(times_dict.get(time))
    return time_list 

def create_class_from_list(my_list): # Nested list
    section = my_list[0][0]
    course_no = my_list[0][1]
    title = my_list[0][2]
    room = my_list[0][5]
    times = {}
    for row in range(len(my_list)):
        days = my_list[row][3]
        for day in days:
            new_entry = {int(day_dict.get(day)): string_to_time_list(my_list[row][4])}
            times.update(new_entry)
    # return Course(title, course_no, section, times, room)
    print(Course(title, course_no, section, times, room))


def print_2d_arr(arr):
    for row in arr:
        print(row)


test = convert_table(csv_to_2d_arr())
print(test)
for row in test: # Each row is a course
    create_class_from_list(row)

####################

class Schedule(object):
    def __init__(self):
        self.timetable = make_2d_array()
    
    def add_course(self, COURSE_DATA):
        


# %%