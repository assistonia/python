
def recommandIDprogram(new_id):
    #1단계 대문자를 소문자로
    new_id=new_id.lower()
    answer=new_id
    #2단계 -_.을 제외한 특수문자 제거
    answer=''
    for correctword in new_id:  #문자열 for 문 new_id의 문자수 만큼 반복 한다
        if correctword.isalnum() or correctword in '-_.':
            answer+=correctword
    #3단계 .. 을 .으로 제거
    while '..' in answer:
        answer = answer.replace('..','.')
    #4단계 앞의 .과 끝의 .을 제거  //공백인경우를 체크안해주면 string index out of range 오류가남
    if answer!='':
        if answer[0]=='.':
            answer=answer[1:]
        else:
            answer
    if answer!='':
        if answer[-1]=='.':
            answer=answer[:-1]
        else:
            answer
    #5단계 빈칸인경우 a를 추가해줌
    if answer=='':
        answer='a'
    else:
        answer
    #6단계 16자이상인경우 15개를 제외한 나머지문자들을 제거한다 그리고 마지막이 .인경우 제거해준다
    if len(answer)>15:
        answer=answer[:15] #:15는 15개까지
    else:
        answer
    if answer[-1]=='.':
            answer=answer[:-1]
    else:
        answer
    #7단계 2자 이하인경우 3이 될때까지 늘려준다
    if len(answer)==1:
        answer+=answer[0]
        answer+=answer[0]
    elif len(answer)==2:
        answer+=answer[1]
    else:
        answer
    return answer


print("ID를 입력해주세요")
new_id=input()
print('RecommandID:',recommandIDprogram(new_id))
