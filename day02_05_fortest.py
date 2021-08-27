marks = [90, 25, 67, 45, 80]

for index,mark in enumerate(marks): 
    
    if marks >= 60: 
        print("%d번 학생은 합격입니다." % index)
    else: 
        print("%d번 학생은 불합격입니다." % index)

for i in range(1,11,2):
    print(i)