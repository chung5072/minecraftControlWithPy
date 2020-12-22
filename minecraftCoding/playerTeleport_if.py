"""마인크래프트 월드에서 if문을 활용하여 무한 텔레포트_조건을 부여"""

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft
# 잠깐의 텀
import time

minecraftPy = Minecraft.create()
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

"""2. 플레이어의 위치를 확인"""
first_pos = minecraftPy.player.getTilePos()
print("Player\'s first pos is " + str(first_pos))
minecraftPy.postToChat("Player\'s first pos is " + str(first_pos)) # (178,2,-90)

"""3. while 문을 활용하여 플레이어의 위치를 이동"""
i = 0 # i의 초기값 설정
j = 0 # j의 초기값 설정
while True:
    j = j + 1 # 몇 번째 위치를 나타내기 위한 변수
    i = i + 10 # y축, 높이에다가 일정 길이를 더해주기 위한 변수
    minecraftPy.player.setTilePos(first_pos.x, (first_pos.y + i), first_pos.z)  # 초기값에서 y축으로 10을 더해줌

    moving_pos = minecraftPy.player.getTilePos()
    print(f"Player {j}\'s position is " + str(moving_pos))
    minecraftPy.postToChat(f"Player {j}\'s position is " + str(moving_pos))  # 더해준 상태의 위치를 출력

    time.sleep(0.3)

    if moving_pos.y > 100: # y축의 길이. 즉 높이가 100보다 높으면 멈춤, 나중에 설계도면에서 활용할 예정
        break

last_pos = minecraftPy.player.getTilePos()
print("Player\'s last pos is " + str(last_pos))
minecraftPy.postToChat("Player\'s last pos is " + str(last_pos)) # 마지막 위치값 출력