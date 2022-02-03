# Github Study Project 2 (VS code)
Git과 VS Code 연동하기<br>

# ※ 사전 작업
  * git 다운로드
  * vs code 다운로드
  * vs code에서 파이썬, 깃허브 확장팩 다운로드
# 1. 파이썬 파일 생성
vs code를 열고 새 폴더를 생성 후 폴더 내 자신만의 파이썬 파일을 만든다.


![image](https://user-images.githubusercontent.com/79391012/148188921-dada2425-2372-4349-baaa-ec90fc2c33af.png)



# 2. 소스 제어 아이콘 클릭 -> Initialize Repository
왼쪽 탭에 있는 소스 제어 아이콘 클릭 후, Initialize Repository 버튼을 클릭한다.

![image](https://user-images.githubusercontent.com/79391012/148188974-fa2e98b7-889b-4778-bb41-b885241d0f22.png)


<br> 

# 3. 커밋 할 항목 로컬 저장소에 반영하기
1. git add . 와 같은 역할    
깃허브에 올리기 전 먼저 commit할 항목을 정하여 로컬 저장소에 반영해주어야 함<br>
commit할 항목을 정하는 방법은 아래 사진과 같이 + 버튼을 클릭하는 것으로,   
changes의 모든 항목에 대해 staging을 올릴 때 사용함.      
![image](https://user-images.githubusercontent.com/79391012/148189048-90baa7ed-8a47-4069-9155-bba709df7fc1.png)     
![image](https://user-images.githubusercontent.com/79391012/148189060-1eaf9618-435a-426b-9a8c-a1f63792f4b9.png)     
![image](https://user-images.githubusercontent.com/79391012/148189091-d991de15-0116-4130-92db-3c36aaaa0829.png)     
 


2. git commit -m "메시지 입력" 와 같은 역할   
staging 변경 사항들에 대해 체크 버튼을 누르고    
commit 시 남길 메시지를 입력 후, 로컬 저장소에 반영해준다. 
![image](https://user-images.githubusercontent.com/79391012/148189142-7f1bc825-f063-4798-aec3-06c2aa0e1d28.png)      




# 4. 원격 저장소 지정하기
우선, 터미널을 켜고 Git Bash로 지정해준다.    
![image](https://user-images.githubusercontent.com/79391012/148189246-983b77a5-07c0-4284-86a6-204e9b96b6d2.png)

Git_Study_2의 원격 저장소를 지정해준다.   
```swift
git remote add origin https://github.com/AISL-Study/Git_Study_2.git

```
![image](https://user-images.githubusercontent.com/79391012/148189281-9718574d-791b-4b5b-a24d-42bceb5463a1.png)


# 5. 원격 저장소 내용 로컬 저장소에 반영하기
```swift
git pull origin main --allow-unrelated-histories
```
![image](https://user-images.githubusercontent.com/79391012/148189313-821ede39-68ee-4c7d-b053-99486fc95c7d.png)


# 6. branch 생성하기
자신의 로컬 환경에서 코드를 추가하는 작업을 하기 위해 브랜치를 만들어준다.

```swift
git checkout -b 브랜치 이름
```
※ 브랜치 이름은 본인 영문 이름으로 할 것. (누가 코드를 추가했는지를 확인하기 위해서)    
![image](https://user-images.githubusercontent.com/79391012/148189352-27063777-be0c-4186-b3b2-b830db10769c.png)


# 6. git push를 통해 원격 저장소에 반영하기

```swift
git push origin 브랜치 이름
```
   > 원격 저장소에 내 브랜치로 수정한 내용을 push   
 
![image](https://user-images.githubusercontent.com/79391012/148189602-29695848-2a62-4dd0-b318-58a410a9b0bd.png)    
![image](https://user-images.githubusercontent.com/79391012/148189639-fcfeec67-6f38-49af-a1c6-a52e0856c698.png)

> 브랜치가 다음과 같이 새로 생성이 되면 성공!!

