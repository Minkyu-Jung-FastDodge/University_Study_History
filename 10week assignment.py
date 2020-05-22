import random
import mymodule

class Student:

    def __init__(self, name):
        self.name = name
        self.scores = []
        self.mean = 0
        self.grade = ''

    def __str__(self):
        score_output = ''
        for v in self.scores:
            score_output += str(v) + '  '
        message = "Name : " + self.name + "\n" + "Scores : " + score_output + '\n' + "Mean : " + str(self.mean) + '\n' + "Grade : " + self.grade + "\n"
        return message

    def input_score(self, M):
        for i in range(M):
            self.scores.append(random.randint(60, 100))

    def CalculateMean(self):
        num = 0
        for n in self.scores:
            num += 1
        self.mean = sum(self.scores)/num

    def Grade(self):
        if 90 <= self.mean:
            self.grade = 'A'

        elif 80 <= self.mean < 90:
            self.grade = 'B'

        elif 70 <= self.mean < 80:
            self.grade = 'C'

        elif 60 <= self.mean < 70:
            self.grade = 'D'

        else:
            self.grade = 'F'

Hanyang = []
N = int(input("How many students? : "))
M = int(input("How many subjects? : "))
for i in range(N):                  #학생 인스턴스 초기화
    print("%d 번째 "%(i+1), end="")
    student = Student(input("학생의 이름은 무엇입니까? : "))
    student.input_score(M)
    student.CalculateMean()
    student.Grade()
    Hanyang.append(student)

score_2d_list = []                  #학생 수를 행 갯수, 과목 수를 열 갯수로 하는 2차원 리스트 생성, NxM 행렬
for student_object in Hanyang:
    score_2d_list.append(student_object.scores)

mean_list = []                      #학생별 평균을 저장할 리스트 변수
for student_object in Hanyang:
    mean_list.append(student_object.mean)

grade_list_subject = [0,0,0,0,0]    #히스토그램, ABCDF를 각 '과목별'로 판정함. [A,B,C,D,F]
mymodule.grade_hist(score_2d_list, grade_list_subject)

mymodule.show_results(Hanyang, mean_list, grade_list_subject)   #각종 결과들을 표시해줌

name_list = []                                          #학생의 이름을 저장하는 리스트 변수
for student_object in Hanyang:
    name_list.append(student_object.name)

while 1:
    print()
    print("데이터를 조회하고 싶은 학생의 이름을 입력하세요 :", end="")
    index_num_list = mymodule.Myscores(name_list, input(""))
    print() #입력한 것과 같은 이름을 가지는 학생이 Hanyang 리스트에서 가지는 인덱스 번호를 모아 둔 리스트를 만듦.
    if index_num_list == []:    #리스트가 비어있으면 입력한 이름과 일치하는 학생이 없음
        print("해당 학생이 존재하지 않습니다")
    else:
        for i in index_num_list:     #index_num 안의 인덱스 번호를 이용해 적절한 학생 인스턴스를 Hanyang 리스트에서 출력.
            print(Hanyang[i])

    terminator = input("프로그램을 끝내시겠습니까? (y 입력 시 종료, 이외 아무 키 입력시 종료하지 않음.) :")
    if terminator == 'y':
        print("종료합니다.")
        break



# 학생들 성적 가져와서 2차원 리스트 구성    ->      이거 가지고 히스토그램 1차원 리스트도 구성
# 학생들 평균 싹 가져와서 1차원 리스트 구성



#[[과목1 점수, 과목2 점수, ...], [과목1 점수, 과목2 점수, ...], ...]
#           과목1     과목2     과목3     과목4      .....
#학생1       점수       점수      점수      점수      ....
#학생2       점수       점수      점수      점수      ....
#학생3       점수       점수      점수      점수      ....
# .           .         .         .         .
# .           .         .         .         .
# .           .         .         .         .