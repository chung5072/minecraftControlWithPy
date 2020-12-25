"""지나온 자리 얼음 장판 만들기"""

"""
지나온 자리가 얼음 장판이 되도록
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

"""3. 장판을 깔기 위해서 얼음 블록 설정"""
ICE = blocks.ICE

"""4. 지나온 자리 얼음 블록 깔기"""
# 조건을 설정하기 위해서 특정 시간을 잡아주기
# 조건은 일반 게임처럼 시작 시간 + 일정 시간
iceGroundStartTime = time.time()

# 무한 반복
while True:
    playerPos = minecraftPy.player.getTilePos() # 지속적으로 플레이어의 위치를 구한다

    # 플레이어의 위치를 블럭 좌표로 설정하기 위해서 변수어 대입한다.
    blockX = playerPos.x
    blockY = playerPos.y
    blockZ = playerPos.z

    minecraftPy.setBlock(blockX, blockY-1, blockZ, ICE) # 플레이어의 위치에서 1칸 아래(세로)에 블럭을 설치

    iceGroundEndTime = time.time() # 끝나는 시간을 구한다

    if iceGroundEndTime > iceGroundStartTime + 60: # 끝나는 시간이 시작시간 + 1분보다 많을 때 반복문이 끝난다.
        break

minecraftPy.postToChat("ICE Grounding Stop!")