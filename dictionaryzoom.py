student_scores={"brock" : "99", "bryan" : "94", "patrick" : "89", "cam" : "70", "ben" : "60"}
student_scores["sam"]="78"
student_scores["marie"]="92"
student_scores["ria"]="88"
print(student_scores)
num_students=len(student_scores)
print("number of students is:", num_students)

student_scores_values=list(map(int,(student_scores.values())))
print(student_scores_values)
sum=0
for i in student_scores_values:
	sum+=i
avg_score=[sum/len(student_scores)]
print(avg_score)


num_avg_students=0
for i in student_scores_values:
	if i >85:
		num_avg_students +=1
print("number of students that scored the average score:", num_avg_students)

myList=list(student_scores.values())
myList.sort()
print(myList[-1])

