#인당 좌석 예약 1개 제한 or 무제한으로 변경 -> 좌석 확인에서 모두 확인

def display_seat_info(seatinfo):
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ좌석 예약 현황ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('          ', end='')
    for s in range(20):
        print('%5i' %(s+1), end='')
    print()
    for i in range(5):
        print(i+1, '호차 :', end='  ')
        for t in range(20):
            print('%5s' %(seatinfo[i][t]), end='')
        print()
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

def display_menu():
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ기차 예약 시스템 메인 메뉴ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("현재 좌석 예약 현황 확인 (1)")
    print("좌석 예약하기 (2)")
    print("예약 취소하기 (3)")
    print("예약 확인하기 (4)")
    print("로그아웃 (88)")
    print("시스템 종료 (999)")
    selectf = int(input("괄호 옆의 숫자를 입력하여 이용하실 기능을 선택하세요 : "))
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    return selectf

def log_in_menu():
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ기차 예약 시스템 로그인 메뉴ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("로그인 (1)")
    print("회원가입 (2)")
    print("시스템 종료 (999)")
    selectf = int(input("괄호 옆의 숫자를 입력하여 이용하실 기능을 선택하세요 : "))
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    return selectf

def log_in(id_password, current_user):
    user_id = input("아이디를 입력하세요 : ")
    user_password = input("패스워드를 입력하세요 : ")
    correct_or_wrong = 0  #0 = wrong, 1 = correct
    for t in id_password:
        if user_id == t[1] and user_password == t[2]:
            correct_or_wrong = 1
            break
    if correct_or_wrong == 0:
        print('아이디 혹은 패스워드가 잘못되었습니다. 로그인 화면으로 돌아갑니다.')
        return 0
    else:
        print("정상적으로 로그인 되었습니다.")
        current_user[0] = user_id
        return 1


def register(id_password):
    id_is_duplicate = 1
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ회원가입ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    name = input("성함을 입력해 주세요 : ")
    id = input("ID를 입력해 주세요 : ")
    while id_is_duplicate == 1:
        for i in id_password:
            id_is_duplicate = 0
            if id == i[1]:
                id_is_duplicate = 1
                break
        if id_is_duplicate == 1:
            id = input("이미 사용되고 있는 ID입니다. 다른ID를 입력해 주세요 : ")

    password = input("패스워드를 입력해 주세요 : ")
    id_password.append([name,id,password])
    print("회원가입이 정상적으로 완료되었습니다.")
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

def make_reservation(seatinfo,guestinfo,currentid):
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ좌석 예약하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    while True:
        car = int(input("원하시는 차량의 번호를 입력해 주십시오.(1~5) : "))
        while car < 1 or car > 5:
            car = int(input("차량은 5호기 까지 있습니다. 다시 입력해 주십시오(1~5) : "))
        seat = int(input("원하시는 좌석의 번호를 입력해 주십시오.(1~20) : "))
        while seat < 1 or seat > 20:
            seat = int(input("좌석은 20번까지 있습니다. 다시 입력해 주십시오(1~20) : "))

        if seatinfo[car-1][seat-1] == 'O':
            seatinfo[car-1][seat-1] = 'X'
            print("차량과 좌석 선택이 완료되었습니다.")
            break
        else:
            print("선택하신 좌석은 이미 예약되어 있습니다.")
    name = input("예약자분의 이름을 입력해 주세요.")
    temp = [name, car, seat, currentid[0]]
    guestinfo.append(temp)
    print('예약이 완료되었습니다. 즐거운 여행 되시길 바랍니다.')
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

def canceling_reservation(seatinfo, guestinfo, current_userid):
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ예약 취소하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("예약 취소 과정을 진행합니다.")
    temp = []
    for reservation_info in guestinfo:
        if current_userid[0] == reservation_info[3]:
            reservation_info.append(guestinfo.index(reservation_info))  #reservation_info = [이름, 차량번호, 좌석번호, 아이디, guestinfo 안에 해당 데이터의 인덱스]
            temp.append(reservation_info)

    if len(temp) == 0: #temp 리스트에 원소가 없을경우
        print('죄송합니다, 예약된 기록이 존재하지 않습니다.')

    else:
        print("-예약내역-")

        num = 0 #몇번째 예약기록인지 표시하기 위한 변수
        for reservation_history in temp:
            num += 1
            print("%i. 예약자명 : %s / %i호차 %i번 좌석 "%(num, reservation_history[0], reservation_history[1], reservation_history[2]))

        print("어떤 예약을 취소하시겠습니까? (1~%i) : "%num)
        user_select = int(input('-> '))
        while user_select > num or user_select < 1:
            print("오류 : 정수 1~%i까지 입력할 수 있습니다. 다시 입력하세요" %num)
            user_select = int(input('-> '))

        current_selected_car = guestinfo[temp[user_select - 1][4]][1]
        current_selected_seat = guestinfo[temp[user_select - 1][4]][2]

        print(guestinfo[temp[user_select - 1][4]][1], '호차', guestinfo[temp[user_select - 1][4]][2], '번 좌석 예약취소')
        seatinfo[current_selected_car - 1][current_selected_seat - 1] = 'O'
        del(guestinfo[temp[user_select-1][4]])
        del(temp[user_select-1])
        for p in temp: # 2번 이상 취소를 할 때를 대비해 인덱스 값을 저장한 원소를 제거함.
            del(p[4])
        print('예약 취소 과정이 성공적으로 완료되었습니다. 이용해 주셔서 감사합니다.')
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

def guest_retrieval(guestinfo, current_userid):
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ예약내역 확인하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("예약자 검색 과정을 진행합니다.")
    temp = []
    for reservation_info in guestinfo:
        if current_userid[0] == reservation_info[3]:
            reservation_info.append(
                guestinfo.index(reservation_info))  # reservation_info = [이름, 차량번호, 좌석번호, 아이디, guestinfo 안에 해당 데이터의 인덱스]
            temp.append(reservation_info)

    if len(temp) == 0:  # temp 리스트에 원소가 없을경우
        print('죄송합니다, 예약된 기록이 존재하지 않습니다.')

    else:
        print("-예약내역-")

        num = 0  # 몇번째 예약기록인지 표시하기 위한 변수
        for reservation_history in temp:
            num += 1
            print("%i. 예약자명 : %s / %i호차 %i번 좌석 " % (
            num, reservation_history[0], reservation_history[1], reservation_history[2]))


#Main function

seat_info = []
guest_info = []
id_password = [['kim', 'id', 'pw']]#이름, 아이디, 패스워드
current_userid = ['']   #함수 실행과정에서 값이 변하도록 하기 위해 리스트를 선언
login_yes_no = 0 #0 = no = 로그인 되지 않은 상태, 1 = yes = 로그인 된 상태
terminator = 0 # terminator = 1 이면 프로그램 종료

for i in range(5):
    temp = []
    for t in range(20):
        temp.append('O')
    seat_info.append(temp)
#초기 데이터 생성부

while terminator == 0:
    if login_yes_no == 0:
        while 1:
            user_select = log_in_menu()
            while user_select > 999 or 999 > user_select > 2 or user_select < 1:
                print("오류 : 정수 1~2, 또는 999를 입력해 주세요.")
                user_select = log_in_menu()
            if user_select == 1:
                log_in_success = log_in(id_password, current_userid)
                if log_in_success == 1:
                    login_yes_no = 1
                    break
            elif user_select == 999:
                terminator = 1
                break
            else:
                register(id_password)
        #로그인 구역
    elif login_yes_no == 1:
        while 1: # 1=True
            selectf = display_menu()
            while selectf > 999 or 999 > selectf > 88 or 4 < selectf < 88 or selectf < 1:
                print("오류 : 정수 1~4, 88 또는 999를 입력해 주세요.")
                selectf = display_menu()
            if selectf == 1:
                display_seat_info(seat_info)

            elif selectf == 2:
                make_reservation(seat_info, guest_info, current_userid)

            elif selectf == 3:
                canceling_reservation(seat_info, guest_info, current_userid)

            elif selectf == 4:
                guest_retrieval(guest_info, current_userid)

            elif selectf == 88:
                login_yes_no = 0
                break

            elif selectf == 999:
                terminator = 1
                break
print('이용해 주셔서 감사합니다.')





# def canceling_reservation(seatinfo, guestinfo, current_userid):                 #####개선 후 삭제
#     print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ예약 취소하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#     print("예약 취소 과정을 진행합니다.")
#     index = 'none'
#     for i in guestinfo:
#         if current_userid == i[3]:
#             index = guestinfo.index(i)
#
#     temp = guestinfo[index]
#
#     if index == 'none':
#         print('죄송합니다, 예약된 기록이 존재하지 않습니다.')
#
#     else:
#         del(guestinfo[index])
#         print(temp[1],'호차', temp[2], '번 좌석 예약취소')
#         seatinfo[temp[1]-1][temp[2]-1] = 'O'
#         print('예약 취소 과정이 성공적으로 완료되었습니다. 이용해 주셔서 감사합니다.')
#     print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
