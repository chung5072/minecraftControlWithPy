"""마인크래프트 월드에서 getHeight을 활용하여 가장 높은 곳으로 텔레포트"""

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

"""3. 플레이어가 있는 좌표-x, z 에서 가장 높은 곳-y을 구하기"""
high_y = minecraftPy.getHeight(first_pos.x, first_pos.z) + 1 # 블럭 위로 텔레포트를 해야햐므로 + 1을 해줘야 한다.
print("Highest height is " + str(high_y))
minecraftPy.postToChat("Highest height is " + str(high_y)) # 가장 높은 좌표: -1

"""4. 가장 높은 곳의 좌표픞 구했으므로 해당 좌표로 이동"""
first_pos.y = high_y # 가장 높은 곳의 좌표를 첫번째 좌표로 지정

minecraftPy.postToChat("Please wait 5 seconds")
time.sleep(5)

minecraftPy.player.setTilePos(first_pos) # 변경된 첫 번째 좌표로 이동 (가장 높은 곳의 좌표)
second_pos = minecraftPy.player.getTilePos() # 변경된 좌표를 두 번째 좌표료 지정

print("Player\'s second pos is " + str(second_pos))
minecraftPy.postToChat("Player\'s second pos is " + str(second_pos)) # 변경된 좌표를 출력