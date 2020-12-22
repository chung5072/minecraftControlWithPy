"""마인크래프트 월드에서 사용자의 위치를 이동하기_함수"""

"""현재 위치를 파악한 뒤에 내 위치에서 입력한 값만큼 사각형으로 움직이는 함수 만들기"""
"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft
import time

minecraftPy = Minecraft.create()
minecraftPy.postToChat("hello, Minecraft!!") # 마인크래프트 서버와 파이썬 연동 성공

"""2. 사각형으로 이동하길 원하는 값 입력"""
wantToMove = int(input("how much do you want to move: "))

"""3. 이동시킬 함수 작성"""
def moveTo(distance):
    """플레이어를 특정 거리만큼 이동시키는 함수"""
    """3-1. 현재 플레이어의 위치를 구하기"""
    first_pos = minecraftPy.player.getTilePos()
    print(first_pos)
    minecraftPy.postToChat("first position is " + str(first_pos))

    minecraftPy.postToChat("now, let's begin~")

    """3-2. 플레이어를 이동"""
    time.sleep(0.5)
    minecraftPy.player.setTilePos(first_pos.x + distance, first_pos.y, first_pos.z)
    second_pos = minecraftPy.player.getTilePos()
    print(second_pos)
    minecraftPy.postToChat("Player's second position is " + str(second_pos))
    """
    이 부분에서 에러 발생: None이라고 나타남
    print(second_pos)
    minecraftPy.postToChat(second_pos)
    에러 해결 방법:
    minecraftPy.player.setTilePos()는 return 값이 없기 때문에
    minecraftPy.player.getTilePos()로 return 값을 받아서 
    print나 minecraftPy.postToChat()으로 출력을 해줘야 한다.
    """
    time.sleep(0.5)
    minecraftPy.player.setTilePos(second_pos.x - distance, second_pos.y, second_pos.z)
    third_pos = minecraftPy.player.getTilePos()
    minecraftPy.postToChat("Player's second position is " + str(third_pos))


minecraftPy.postToChat("before we start, please wait 5 seconds")
time.sleep(5)

moveTo(wantToMove)

minecraftPy.postToChat("we finiished")
last_pos = minecraftPy.player.getTilePos()
minecraftPy.postToChat("Player's second position is " + str(last_pos))