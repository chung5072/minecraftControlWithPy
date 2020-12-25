"""텔레포트할 수 있는 블럭 만들기"""

"""
사용자가 특정 위치에 도달했을 때,
특정 공간으로 이동시키기
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

"""3. 플레이어의 위치를 확인하기"""
gotPlayerPos = essentialModule_selfMade.getMyPos() # 내 위치를 얻고, 출력하기

#essentialModule_selfMade.showDirection() # 동서남북 방향 확인

"""4. 텔레포트를 시켜줄 블럭을 놓을 위치를 설정하기"""
# 블럭 변수 선언
# 플레이어의 위치에서 +1, -1, 0만큼 이동한 위치에서 시작
blockX = gotPlayerPos.x
blockY = gotPlayerPos.y
blockZ = gotPlayerPos.z - 3
print(f'print block pos: {blockX}, {blockY}, {blockZ}')

"""5. 텔레포트 시켜줄 블럭을 설치"""
minecraftPy.setBlock(blockX, blockY, blockZ, 35)

"""6. 플레이어가 특정 위치에 도달하면 특정 공간으로 이동하기"""

"""
여기다가 코드를 짜면 실행이 되지 않는다.
gotPlayerPos_2 = essentialModule_selfMade.getMyPos()  # 내 위치를 얻고, 출력하기
#print(gotPlayerPos_2)

playerPosX = gotPlayerPos_2.x
playerPosY = gotPlayerPos_2.y
playerPosZ = gotPlayerPos_2.z
"""

# (-552, 10, 712)로 이동하기
while True:

    gotPlayerPos_2 = essentialModule_selfMade.getMyPos()  # 내 위치를 얻고, 출력하기
    #print(gotPlayerPos_2)

    playerPosX = gotPlayerPos_2.x
    playerPosY = gotPlayerPos_2.y
    playerPosZ = gotPlayerPos_2.z

    if blockX == playerPosX and (blockY + 1) == playerPosY and playerPosZ == blockZ:
        minecraftPy.player.setTilePos(-552, 10, 712)
        break
