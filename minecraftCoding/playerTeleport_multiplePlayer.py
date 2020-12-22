"""마인크래프트 월드에서 entity.set/getPos을 활용하여 다른 사용자를 텔레포트"""

#minecraftPy.entity.setPos(id, x, y, z)
#minecraftPy.entity.getPos(id)
#minecraftPy.getPlayerEntityIds()

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft
# 잠깐의 텀
import time

minecraftPy = Minecraft.create()
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

"""2. 현재 내 서버에 들어와 있는 플레이어를 확인"""
playerIds = minecraftPy.getPlayerEntityIds()
print(playerIds)
minecraftPy.postToChat(playerIds) # 192

"""3. 알아낸 ID의 위치를 구하기"""
firstPlayerPos = minecraftPy.entity.getPos(playerIds)
print(firstPlayerPos)
minecraftPy.postToChat(firstPlayerPos)

"""4. 알아낸 ID의 위치를 특정 위치로 텔레포트하기"""
# 목적지는 179, -5, -68
minecraftPy.entity.setTilePos(playerIds, 179, -5, -68)
playerPos = minecraftPy.player.getTilePos()
print(playerPos)
minecraftPy.postToChat(playerPos)