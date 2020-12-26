"""해당 위치에 블럭이 있는지 확인 및 계단 설치하기"""

"""
참고 코드
# constructBuilding_second: 계단 설치
HighstH = mc.getHeight(x, z)
for i in range(HighstH):
    if(mc.getBlock(x+2,i+1,z+14) == 0):
        pass
    else:
        mc.setBlocks(x+2,i+1,z+14 ,x+6,i+1,z+14,AIR)
        for ii in range(10):
            if mc.getBlock(x+2+ii, i+1-ii, z+14) != AIR:
                break
            else:
                mc.setBlock(x+2+ii, i+1-ii, z+14, QUARTZ_BLOCK)
"""

"""1. 모듈 불러오기"""
# 마인크래프트 서버 불러오기
from mcpi.minecraft import Minecraft

# 내가 만든 필수 함수 불러오기
from minecraftProj.minecraftPyModules import *

# 일정량의 시간을 비우기 위해
import time

"""2. 서버에 접속"""
minecraftPy = Minecraft.create() # 서버 접속

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

"""3. 사용자 위치 확인 및 좌표 변수 등록"""
gotPlayerPos = essentialModule_selfMade.getMyPos()

playerX = gotPlayerPos.x
playerY = gotPlayerPos.y
playerZ = gotPlayerPos.z

blockX = gotPlayerPos.x + 1
blockY = gotPlayerPos.y
blockZ = gotPlayerPos.z + 1

"""4. 해당 위치의 좌표에 블럭이 있는지 확인"""
# 1. 직접 좌표를 입력해서
"""
if minecraftPy.getBlock(-994, -7, 1619) == 0:
    minecraftPy.postToChat("empty!")
else:
    minecraftPy.postToChat("something!")
"""
# 2. 내 위치의 얼만큼 이동해서 물체가 있는지 확인
"""
if minecraftPy.getBlock(blockX, blockY, blockZ) == 0:
    minecraftPy.postToChat("empty!")
else:
    minecraftPy.postToChat("something!")
"""
# 3. 플레이어가 특정 좌표를 입력하면 해당 좌표에 물체가 있는지 확인

somethingX = int(input("Input X Pos: "))
somethingY = int(input("Input Y Pos: "))
somethingZ = int(input("Input Z Pos: "))

if minecraftPy.getBlock(somethingX, somethingY, somethingZ) == 0:
    minecraftPy.postToChat("empty!")
else:
    minecraftPy.postToChat("something!")

