def grade_hist(data_list, grade_list): #2d, 1d
    for i in data_list:
        for k in i:
            if 90 <= k <= 100:
                grade_list[0] += 1

            elif 80 <= k < 90:
                grade_list[1] += 1

            elif 70 <= k < 80:
                grade_list[2] += 1

            elif 60 <= k < 70:
                grade_list[3] += 1

            else:
                grade_list[4] += 1

def Mean_sorting(mean_list): #일차원 리스트
    list = mean_list[:]             #리스트 복제
    n = len(list)
    for i in range(n-1):
        for k in range(i+1, n):
            if list[i] < list[k]:   #정렬 알고리즘
                temp = list[i]
                list[i] = list[k]
                list[k] = temp
    return list                     #정렬된 리스트를 리턴함

def show_results(data_list, mean_list, grade_list):  #2차원 / 1차원 / 1차원
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    for i in range(len(data_list)):  # 행렬 출력
        print("%-10s"%data_list[i].name, end="") #학생 이름 표시
        for k in range(len(data_list[i].scores)): #학생 점수 표시
            print("%5i" % data_list[i].scores[k], end='')
        print() #한 명의 학생의 성적을 모두 표시하고 개행

    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡmeanㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    index_num = 0
    for i in mean_list:  # 평균 데이터 출력
        index_num += 1
        print("%-10.3f" % i, end="")
        if index_num % 5 == 0:      # 평균값 5개마다 개행하기 위함.
            print()

    sorted_mean_list = Mean_sorting(mean_list) # 평균값이 저장된 리스트를 정렬

    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡsorted meanㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    index_num = 0
    for i in sorted_mean_list:  # 평균 데이터 출력
        index_num += 1
        print("%-10.3f" % i, end="")
        if index_num % 5 == 0:  # 평균값 5개마다 개행하기 위함.
            print()
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")  # 히스토그램 출력
    print("Histogram of grades")
    print("A : %i" % grade_list[0])
    print("B : %i" % grade_list[1])
    print("C : %i" % grade_list[2])  # grade_list의 인덱스를 이용해 값을 출력.
    print("D : %i" % grade_list[3])
    print("F : %i" % grade_list[4])
    print("Sum of A,B,C,D,F : %i" % (sum(grade_list)))
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

    print("Max : %f (Name :" % (max(mean_list)), end=' ')  # 최댓값과 행번호 출력
    id = 0
    for i in mean_list:
        if i == max(mean_list):  # 최댓값이 중복될 경우를 위해 id 변수를 해당 값의 인덱스에 대응시킴
            print(data_list[id].name, end=' ')
        id += 1
    print(')')

    print("Min : %f (Name :" % (min(mean_list)), end=' ')  # 최솟값과 행번호 출력
    id = 0
    for i in mean_list:
        if i == min(mean_list):  # 최솟값이 중복될 경우를 위해 id 변수를 해당 값의 인덱스에 대응시킴
            print(data_list[id].name, end=' ')
        id += 1
    print(')')
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

def Myscores(name_list, name):
    index_list = []     # 입력한 것과 같은 이름을 가지는 학생이 name_list에서 가지는 인덱스 번호를 모아 둔 리스트를 만듦.
    index_num = 0       # 동명이인 등의 경우를 고려하여 index 메서드를 사용하지 않고 변수를 만듦.
    for cc in name_list:
        if name == cc:  # name_list 안의 이름과 입력한 name이 같은 경우, 해당 이름이 name_list에서 가지는 인덱스 번호를 index_list에 저장.
            index_list.append(index_num)
        index_num += 1

    return index_list
