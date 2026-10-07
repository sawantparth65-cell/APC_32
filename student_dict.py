student_marks={
    "Parth":85,
    "Arya":95,
    "Om":80,
    "Aditya":78,
    "Sid":75,
    "Shubham":70,
    "Siddhesh":65
}
topper=max(student_marks,key=student_marks.get)
top_score=student_marks[topper]
class_average=sum(student_marks.values())
print("Student marks dictionary:",student_marks)
print("Topper:",topper,"with",top_score,"marks")
print("Class Average:",class_average)

