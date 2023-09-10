import tkinter as tk
import numpy as np
import pandas as pd
import random as rand
from prettytable import PrettyTable
#Input & display 
subject_list = np.array([], dtype=str)
credit_list = np.array([], dtype=int)
def add_subject():
    global subject_list, credit_list
    subject = subject_entry.get()
    credit = int(credit_entry.get())
    if len(subject_list) <= 6 and sum(credit_list) + credit <= 20:
        subject_list = np.append(subject_list, subject)
        credit_list = np.append(credit_list, credit)
        subject_entry.delete(0, tk.END)
        credit_entry.delete(0, tk.END)
        info_label.config(text="")
        update_table()
    else:
        info_label.config(text="Maximum 6 subjects or credits exceed 20!")
def update_table():
    table.clear_rows()
    for subject, credit in zip(subject_list, credit_list):
        table.add_row([subject, credit])
    table_label.config(text=table.get_string())
root = tk.Tk()
root.title("Subject and Credit Input")
subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()
credit_label = tk.Label(root, text="Credit:")
credit_label.pack()
credit_entry = tk.Entry(root)
credit_entry.pack()
info_label = tk.Label(root, text="")
info_label.pack()
add_button = tk.Button(root, text="Add Subject", command=add_subject)
add_button.pack()
table = PrettyTable()
table.field_names = ["Subject", "Credit"]
table_label = tk.Label(root, text=table.get_string())
table_label.pack()
root.mainloop()
print("Subjects:", subject_list)
print("Credits:", credit_list)
print(list(zip(subject_list, credit_list)))
#table = PrettyTable()
#table.field_names = ["Subjects", "Credits"]
#for subject_list, credit_list in zip(subject_list, credit_list):
#    table.add_row([subject_list, credit_list])
#print(table)

#This is lecture assignment
final=[]
for i in range(0, len(subject_list)):
  final.append([subject_list[i], credit_list[i]])
list_lec1=['free', "free", "Lunch", "free", "free"]
list_lec2=[]
list_lec3=[]
list_lec4=[]
list_lec5=[]
list_lec6=[]
count=0
while count<=20:
  count+=1
  x=rand.randint(0, len(final)-1)
  if final[x][1]>0:
    if len(list_lec2)<5:
        if len(list_lec2)==2:
            list_lec2.append("Lunch")
        else:
            list_lec2.append(final[x][0])
            print(list_lec2)
            continue
    if len(list_lec3)<5:
        if len(list_lec3)==2:
            list_lec3.append("Lunch")
        else:
            list_lec3.append(final[x][0])
            continue
    if len(list_lec4)<5:
        if len(list_lec4)==2:
            list_lec4.append("Lunch")
        else:
            list_lec4.append(final[x][0])
            continue
    if len(list_lec5)<5:
        if len(list_lec5)==2:
            list_lec5.append("Lunch")
        else:
            list_lec5.append(final[x][0])
            continue
    if len(list_lec6)<5:
        if len(list_lec6)==2:
            list_lec6.append("Lunch")
        else:
            list_lec6.append(final[x][0])
            continue
batch1 = pd.DataFrame({
    'Monday': list_lec1,
    'Tuesday': list_lec2,
    'Wednesday': list_lec3,
    'Thursday': list_lec4,
    'Friday': list_lec5,
    'Saturday': list_lec6})

#Time table creation

print("Timetable For Batch1", "\n")
print(batch1, "\n")

list_fac = ["null", "null", "Lunch", "null", "null"]
batch1 = pd.DataFrame({
    'Monday': list_fac,
    'Tuesday': list_fac,
    'Wednesday': list_fac,
    'Thursday': list_fac,
    'Friday': list_fac,
    'Saturday': list_fac
})


a = pd.DataFrame({
    'Monday': list_fac,
    'Tuesday': list_fac,
    'Wednesday': list_fac,
    'Thursday': list_fac,
    'Friday': list_fac,
    'Saturday': list_fac
})
b = pd.DataFrame({
    'Monday': list_fac,
    'Tuesday': list_fac,
    'Wednesday': list_fac,
    'Thursday': list_fac,
    'Friday': list_fac,
    'Saturday': list_fac
})
c = pd.DataFrame({
    'Monday': list_fac,
    'Tuesday': list_fac,
    'Wednesday': list_fac,
    'Thursday': list_fac,
    'Friday': list_fac,
    'Saturday': list_fac
})
d = pd.DataFrame({
    'Monday': list_fac,
    'Tuesday': list_fac,
    'Wednesday': list_fac,
    'Thursday': list_fac,
    'Friday': list_fac,
    'Saturday': list_fac
})
e = pd.DataFrame({
    'Monday': list_fac,
    'Tuesday': list_fac,
    'Wednesday': list_fac,
    'Thursday': list_fac,
    'Friday': list_fac,
    'Saturday': list_fac
})
f = pd.DataFrame({
    'Monday': list_fac,
    'Tuesday': list_fac,
    'Wednesday': list_fac,
    'Thursday': list_fac,
    'Friday': list_fac,
    'Saturday': list_fac
})

for i in range(len(batch1)):
    for j in range(len(batch1.columns)):
        if batch1.iloc[i, j] in ["a"]:
            a.iloc[i, j] = "batch1"
            
for i in range(len(batch1)):
    for j in range(len(batch1.columns)):
        if batch1.iloc[i, j] in ["b"]:
            b.iloc[i, j] = "batch1"
for i in range(len(batch1)):
    for j in range(len(batch1.columns)):
        if batch1.iloc[i, j] in ["c"]:
            c.iloc[i, j] = "batch1"
for i in range(len(batch1)):
    for j in range(len(batch1.columns)):
        if batch1.iloc[i, j] in ["d"]:
            d.iloc[i, j] = "batch1"
for i in range(len(batch1)):
    for j in range(len(batch1.columns)):
        if batch1.iloc[i, j] in ["e"]:
            e.iloc[i, j] = "batch1"
for i in range(len(batch1)):
    for j in range(len(batch1.columns)):
        if batch1.iloc[i, j] in ["f"]:
            f.iloc[i, j] = "batch1"



print("Timetable For Teacher a")
print(a, "\n")
print("Timetable For Teacher b")
print(b, "\n")
print("Timetable For Teacher c")
print(c, "\n")
print("Timetable For Teacher d")
print(d, "\n")
print("Timetable For Teacher e")
print(e, "\n")
print("Timetable For Teacher f")
print(f, "\n")
