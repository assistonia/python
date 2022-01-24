global population

# 필요한 구명보트 개수 계산
def rescue_boat_amount(people, limit):
    global population

    # 최소와 최대 무게인 사람의 무게 합이 무게 제한 이하인 경우
    if (people[0] + people[population - 1]) <= limit:
        if population % 2 == 0:
            return population / 2

        else:
            return (population + 1) / 2
    # 최소와 최대 무게인 사람의 무게 합이 무게 제한 초과인 경우
    else:
        for i in range(population):
            if (people[0] + people[population - 1 - i]) <= limit:
                compensate = i # 무게 제한이 이하가 되는 대상까지 하향
                break
        
        if (population - compensate) % 2 == 0:
            return (population - compensate) / 2 + compensate

        else:
            return (population - compensate + 1) / 2 + compensate


people = []

# 인원 입력
print("인원을 입력하세요.")
population = int(input(">> "))


# 구명 보트 무게 제한 입력
print("구명보트의 무게 제한을 입력하세요.(40~240)")
WeightLimit = int(input(">> "))


# 조난자의 몸무게 입력
print(str(population) + "명의 몸무게를 입력하세요.")
print(">>")
for i in range(population):
    people.append(int(input()))

# 조난자의 몸무게 오름차순 정렬
for i in range(population):
        for j in range(population):
            if people[i] < people[j]:
                    temp = people[i]
                    people[i] = people[j]
                    people[j] = temp

print(int(rescue_boat_amount(people, WeightLimit)))