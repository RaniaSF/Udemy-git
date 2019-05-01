print('"Choose one : student_names, student_score,student_count"')
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

grade_no=str(input('Enter Class Name : '))

def student_names(grade_no):
    if grade_no=="grade_one":
        print('student names: ',grade_one.keys())
        grade_one_k_list=list(grade_one.keys())
    elif grade_no=="grade_two":
       print('student names: ',grade_two.keys())
       grade_two_k_list=list(grade_two.keys())
    elif grade_no=="grade_three":
       print('student names: ',grade_three.keys())
       grade_three_k_list=list(grade_three.keys())
       

def student_score(grade_no,student_name):
    if grade_no=="grade_one":
        for x in grade_one:
            print('total of student scores: ',sum(grade_one[x]))
    elif grade_no=="grade_two":
        for x in grade_two:
            print('total of student scores: ',sum(grade_two[x]))
    elif grade_no=="grade_three":
        for x in grade_three:
            print('total of student scores: ',sum(grade_three[x]))

def student_score(student_name,grade_no):
    if grade_no=="grade_one":
        print('number of students: ',len(grade_one_k_list))
    elif grade_no=="grade_two":
         print('number of students: ',len(grade_two_k_list))
    elif grade_no=="grade_three":
         print('number of students: ',len(grade_three_k_list))

    else:
         exit
