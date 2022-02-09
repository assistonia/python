import random

word_sample=['python','programing','line','hangman'] # 여러 단어리스트 저장

answer=random.choice(word_sample) #랜덤으로 한개 선택

word_line='_ '*len(answer) #밑줄

conut1=len(answer) #가능한 시도횟수는 글자 수만큼


while True:
    print()
    print(word_line)

    letter=input('Input letter> ')
    input_word=answer.find(letter) #입력받은 글자가 있는지 확인

    if input_word ==-1:
        conut1-=1
        print("남은 시도 횟수:",format(conut1))

        if conut1==0:
            print('word={}'.format(answer))
            break
    else:
        for a in range(len(answer)):
            if answer[a]==letter:

                word_line=word_line[0:a*2]+answer[a]+word_line[a*2+1:] #내용에 있는 단어일경우 밑줄대신 넣어준다
        print('Correct')
    if answer == word_line.replace(' ',''):
        print()
        print(word_line)
        print('SUCCESS')
        print('word={}'.format(answer)) #정답일경우 답을 나오게 해줍니다.
        break

