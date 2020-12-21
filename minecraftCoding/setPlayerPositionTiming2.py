"""특정 횟수 이후에 플레이어를 이동시키는 함수"""
from mcpi.minecraft import Minecraft
import time

"""1. 마인크래프트 서버와 파이썬을 연결"""
minecraftPy = Minecraft.create()
minecraftPy.postToChat("hello, Minecraft!") # 마인크래프트 서버와 파이썬 연결, 여기에다가 한글을 쓰면 에러가 남

"""2. 플레이어가 몇 번동안 어느 정도의 거리를 이동하길 원하는 값을 입력 받음"""
wantToPosY = int(input("얼만큼 이동하길 원하세요? "))
wantToCount = int(input("몇 번 이동하길 원하세요?: "))
count = 0

"""3. 플레이어를 이동시킬 함수"""
def moveToY(count, y, moveCount):
    """y축으로 일정 거리를 일정 횟수만큼 이동시킬 함수"""
    """3-1. 먼저 플레이어의 위치를 출력"""
    nowPos = minecraftPy.player.getTilePos()
    print("Now's position is: " + str(nowPos))
    minecraftPy.postToChat("Now's position is")
    minecraftPy.postToChat(str(nowPos))

    """3-2. 특정 횟수만큼 특정 거리를 이동시킴"""
    while count < moveCount:
        nowPos.y = nowPos.y + y # y축으로 이동시킬 값을 더함
        print(str(nowPos))
        minecraftPy.postToChat(str(nowPos)) # 위치를 콘솔과 채팅창에 작성
        time.sleep(0.3) # 0.3초 대기
        minecraftPy.player.setTilePos(nowPos) # 이동!!
        count = count + 1

"""4. 출력하기 전 대기"""
minecraftPy.postToChat("wait 10 Seconds!!")
minecraftPy.postToChat("10!!")
time.sleep(5)
minecraftPy.postToChat("5!!")
time.sleep(1)
minecraftPy.postToChat("4!!")
time.sleep(1)
minecraftPy.postToChat("3!!")
time.sleep(1)
minecraftPy.postToChat("2!!")
time.sleep(1)
minecraftPy.postToChat("1!!")
time.sleep(1)
minecraftPy.postToChat("0!!")
minecraftPy.postToChat("Launch!!")

"""5. 함수 실행"""
moveToY(count, wantToPosY, wantToCount)

    
    
