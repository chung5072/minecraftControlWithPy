"""해당 위치에 블럭이 있는지 확인 및 계단 설치하기"""

"""
참고 코드 - 강사님이 작성하신 계단 설치 코드
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

# 내가 만든 필수 함수 불러오기 - 블럭.py를 위해서 추가
from minecraftProj.minecraftPyModules import *

# 일정량의 시간을 비우기 위해
import time

"""2. 서버에 접속"""
minecraftPy = Minecraft.create() # 서버 접속 (minecraftPy = mc)

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

"""3. 사용자 위치 확인 및 좌표 변수 등록"""
gotPlayerPos = essentialModule_selfMade.getMyPos() # 내 위치 출력 (= minecraftPy.player.getTilePos() )

# 위치를 변수에 등록
playerX = gotPlayerPos.x
playerY = gotPlayerPos.y
playerZ = gotPlayerPos.z

"""4. 집 재료"""
QUARTZ_BLOCK = blocks.QUARTZ_BLOCK
AIR = blocks.AIR

"""5. 계단 설치"""
buildingVertical = 5 # 건물 깊이 혹은 너비
#buildingHeight = 5 # 건물 높이
buildingHeight = minecraftPy.getHeight(playerX, playerZ) # 해당 좌표에서 가장 높은 지붕을 구한다.

minecraftPy.postToChat(f"Building Height is {buildingHeight}.") # 해당 건물의 y좌표

# 사용자의 위치와 높이의 최대값 / 너비의 최대값까지의 리스트 생성
heightList = list(range(playerY, buildingHeight))
print(heightList)
verticalList = list(range(playerZ, playerZ + buildingVertical))
print(verticalList)

# 혹시 노트북의 성능으로 설치가 안되는지 불안하여 5초의 여유를 추가
minecraftPy.postToChat("please wait 5 seconds.")
time.sleep(5)

"""
별그리기에서 대각선으로 별을 찍는 코드를 참고하여
    *
   *
  *
 *
*
x의 좌표와 y의 좌표가 같을 때 블럭(QUARTZ_BLOCK)을 설치하고
x의 좌표외 y의 좌표가 다를 때는 빈 공간(AIR)를 설치하는 방향으로 설계
"""
for stairsHeight in heightList: # 현 사용자의 위치에서부터 가장 높은 곳까지의 리스트
    for stairsVertical in verticalList: # 현 사용자의 위치에서부터 건물의 너비 혹은 깊이만큼
        # 혹시 노트북의 성능으로 설치가 안되는지 불안하여 1초의 여유를 추가
        minecraftPy.postToChat("one second please.")
        time.sleep(1)
        if heightList.index(stairsHeight) == verticalList.index(stairsVertical): # 높이의 인덱스와 너비(?)의 인덱스가 같으면 설치
            # 설치가 되지 않아서 어느 좌표에 있는지 확인하기 위해서 코드를 추가
            minecraftPy.postToChat("Set QUARTZ_BLOCK.") # 블럭을 설치한다
            minecraftPy.postToChat(f"player\'s pos: x: {playerX}, y: {stairsHeight}, z: {stairsVertical}") # 설치되는 좌표
            # 실제로 블럭이 설치되는 코드
            minecraftPy.setBlock(playerX, stairsHeight, (playerZ + stairsVertical), QUARTZ_BLOCK)
        elif heightList.index(stairsHeight) != verticalList.index(stairsVertical): # 높이의 인덱스와 너비(?)의 인덱스가 안 같으면 빈 공간
            # 설치가 되지 않아서 어느 좌표에 있는지 확인하기 위해서 코드를 추가
            minecraftPy.postToChat("Empty space.")
            minecraftPy.postToChat(f"player\'s pos: x: {playerX}, y: {stairsHeight}, z: {stairsVertical}")
            # 실제로 블럭이 설치되는 코드
            minecraftPy.setBlock(playerX, stairsHeight, (playerZ + stairsVertical), AIR)
        else:
            minecraftPy.postToChat("This case is impossible.")