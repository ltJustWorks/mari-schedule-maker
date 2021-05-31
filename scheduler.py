#%%
import numpy as np
import csv
import string

times_dict = {'08:15':0, '08:45':1,'09:15':2,'09:45':3, '10:15':4, '10:45':5,'11:15':6,'11:45':7, '12:15':8, '12:45':9,'13:15':10,'13:45':11, '14:15':12, '14:45':13,'15:15':14,'15:45':15, '16:15':16, '16:45':17,'17:15':18,'17:45':19, '18:15':20, '18:45':21,'19:15':22,'19:45':23, '20:15':24}
day_dict = {'M': 0, 'T': 1, 'W': 2, 'H': 3, 'F': 4}

def make_2d_array():
    # Each row represents a day, each time represents a timeslot
    # Ex. Accessing Tuesday's 3rd timeslot: arr[1][2] (0-based indexing)
    return [[0] * 25 for i in range(5)]

class Course(object):
        # What is Course?
        # A COURSES_LIST will contain each course (likely for a specific subject).
    def __init__(self, title, course_no, section, times, room, teacher='N/A'):
        self.title = title
        self.course_no = course_no
        self.section = section
        self.times = times        
        self.teacher = teacher
        # 'times' dict will look like this: 
            # Ex. M 8:15-10:15
            #     W 8:15-9:45
            #     F 14:15-15:45
            # {0: [0,4], 2: [0,3], 4:[12,15]}
        self.room = room
        self.course_type = self.get_course_type()
    
    def get_course_type(self):
    
    def __str__(self):
        return "Title: " + str(self.title) + "\n" + "Course #: " + str(self.course_no) + "\n" + "Section: " + str(self.section) + "\n" + "Times: " + str(self.times) + "\n" + "Room: " + str(self.room) + "\n" + "Teacher: " + str(self.teacher) + "\n" + "Course type: " + self.course_type + "\n"

def csv_to_2d_arr(csv_name):
    with open(csv_name, 'r') as csv_file:
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
            if arr[row+1][0] != '':
                index_2 = row + 1
            elif arr[row+2][0] != '':
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
    room = my_list[0][5]
    title = ''
    teacher = ''
    times = {}
    for row in range(len(my_list)):
        lower_count = len([letter for letter in my_list[row][2] if letter in string.ascii_lowercase])
        if lower_count >= 2:
            teacher = my_list[row][2]
        else:
            title += " " + my_list[row][2]

        days = my_list[row][3]
        for day in days:
            new_entry = {int(day_dict.get(day)): string_to_time_list(my_list[row][4])}
            times.update(new_entry)
    return Course(title, course_no, section, times, room, teacher)


def print_2d_arr(arr):
    for row in arr:
        print(row)


####################

class Schedule(object):
    def __init__(self):
        self.timetable = make_2d_array()
        self.courses_taken = []
    
    def add_course(self, Course):
        for day in Course.times:
            index_0 = Course.times[day][0]
            index_1 = Course.times[day][1] 
            # self.timetable[day][index_0:index_1] = [Course] * (index_1 - index_0) 
            for slot in range(index_0, index_1):
                self.timetable[day][slot] = Course
        self.courses_taken.append(Course)


    def check_compatibility(self, Course):
        for day in Course.times:
            index_0 = Course.times[day][0]
            index_1 = Course.times[day][1]
            if self.timetable[day][index_0] != 0 or self.timetable[day][index_1] != 0:
                return False
            else:
                return True

#########################################

mySchedule = Schedule()

##########################################

# 6 subjects -> 6 lists

eng_index = ['603-103-MQ']
hum_index = ['345-LPH-MS']
com_index = ['ARH-LAA', 'ART-LAA', 'ART-LBA', 'CIN-LAA', 'FLM-LBA', 'GER-LAL', 'GER-LBL', 'ITA-LAA', 'MAT-LAM', 'MUS-LAA', 'PHI-LAA', 'PRO-LAM', 'SSS-LAQ', 'SSS-LBQ', 'STS-LBT', 'THE-LAA'] 
lin_index = ['201-NYC-05']
bio_index = ['101-LCU-05']
wav_index = ['203-NYC-05']

eng_courses = []
hum_courses = []
com_courses = []
lin_courses = []
bio_courses = []
wav_courses = []

FULL_COURSES_LIST = convert_table(csv_to_2d_arr('full_courses.csv'))

#with open('courses_list.txt', 'w') as wf:
#    for row in FULL_COURSES_LIST:
#        wf.write(str(row) + "\n")

CONV_COURSES_LIST = [create_class_from_list(row) for row in FULL_COURSES_LIST]
#with open('courses_list2.txt', 'w') as wf:
#    for Course in CONV_COURSES_LIST:
#        wf.write(str(Course))

#for Course in CONV_COURSES_LIST[282:]:
#    if not Course.course_no in com_index:
#        com_index.append(Course.course_no)

for Course in CONV_COURSES_LIST:
    if Course.course_no in eng_index:
        eng_courses.append(Course)
    if Course.course_no in hum_index:
        hum_courses.append(Course)
    if Course.course_no in com_index:
        com_courses.append(Course)
    if Course.course_no in lin_index:
        lin_courses.append(Course)
    elif Course.course_no in bio_index:
        bio_courses.append(Course)
    elif Course.course_no in wav_index:
        wav_courses.append(Course)

print_2d_arr(eng_courses)
print_2d_arr(hum_courses)
print_2d_arr(com_courses)
print_2d_arr(lin_courses)
print_2d_arr(bio_courses)
print_2d_arr(wav_courses)

# %%