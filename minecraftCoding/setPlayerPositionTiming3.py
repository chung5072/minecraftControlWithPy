"""마인크래프트 월드에서 사용자의 위치를 이동하기_특정 시간 이후 for~in~ 반복문을 통해서 위치 이동"""

from mcpi.minecraft import Minecraft
import time

"""1. 마인크래프트 서버와 파이썬 연동"""
minecraftPy = Minecraft.create()
minecraftPy.postToChat("connect success") # 마인크래프트 서버와 파이썬 연동.

"""2. 비교를 위해 현재 플레이어 위치를 출력"""
firstPlayerPos = minecraftPy.player.getTilePos() # 플레이어의 위치를 불러옴
print(str(firstPlayerPos)) 
minecraftPy.postToChat("first player's location is ~")
minecraftPy.postToChat(str(firstPlayerPos)) # 플레이어의 위치를 출력

"""3. 특정 시간 설정"""
time.sleep(5)
minecraftPy.postToChat("now, let's begin~")

"""4. for ~ in ~ 반복문을 통해 위치를 이동"""
for i in list(range(10)): # 리스트는 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    minecraftPy.player.setTilePos(firstPlayerPos.x, firstPlayerPos.y + (i * 5), firstPlayerPos.z)
    time.sleep(0.3)

lastPos = minecraftPy.player.getTilePos()
minecraftPy.postToChat("last pos is " + str(lastPos))
minecraftPy.postToChat("finished!!")