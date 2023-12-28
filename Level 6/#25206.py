#25206번 너의 평점은
score = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
total_grade = 0 #grade총합
total_result = 0 #학점*과목평점 총합
for i in range(20):
    x,y,z = input().split() #x는 과목명 y는 학점 z는 점수 input()괄호까먹지말기
    y = float(y) 
    if z is not 'P': #pass 계산 안해
        total_grade += y #grade 총합에 점수 넣고
        total_result += y * grade[score.index(z)] #학점*과목평점 더함
print('{:.6f}'.format(total_result / total_grade))

# 6자리 숫자 설정을 위해서는 '{:.6f}'.format!!
