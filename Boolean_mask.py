import pandas as pd
marks = pd.Series([78,87,76,99,54], index = ['A','B','C','D','E'])
print(marks)
 
mask = marks >= 60
print(mask)

filtered_marks = marks[mask]
print(filtered_marks)

print(marks[(marks >= 60) & (marks < 70)])

marks[marks < 70] = 70
print(marks)