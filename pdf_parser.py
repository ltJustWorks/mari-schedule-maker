import tabula
import pandas as pd
import math
File_Path='./courses.pdf'
StartTime=dict.fromkeys(['M', 'T', 'W', 'H', 'F'])
EndTime=dict.fromkeys(['M', 'T', 'W', 'H', 'F'])

Empty={}
df=pd.DataFrame(Empty, columns=['Section', 'Course Number', 'Course Name/Teacher', 'Weekday', 'Time', 'Room'])
pages=['12-18', '75-77', '83-84', '88-96']
for page in pages:
    df1 = tabula.convert_into(File_Path, 'output.csv', pages=page, output_format='csv',java_options='-Dfile.encoding=UTF8')
    df1 = pd.read_csv('output.csv', header=None)
    df1.columns=['Section', 'Course Number', 'Course Name/Teacher', 'Weekday', 'Time', 'Room']
    df=df.append(df1)