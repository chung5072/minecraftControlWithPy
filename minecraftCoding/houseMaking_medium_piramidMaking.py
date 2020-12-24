"""피라미드 만들기"""

"""
정사각형의 피라미드를 만드는데, 가장 밑의 크기는 50 * 50
for 문을 활용해서 만듦
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

"""4. 블럭을 놓을 위치를 설정하기"""
# 블럭 변수 선언
# 플레이어의 위치에서 +1, -1, 0만큼 이동한 위치에서 시작
blockX = gotPlayerPos.x + 1
blockY = gotPlayerPos.y - 1
blockZ = gotPlayerPos.z + 1
"""
계단을 만들 때, y축(높이) + 1로 반복문을 돌리기 때문에,
처음 시작을 할 때, 1칸 내려간 상태에서 만든다.
"""

# 피라미드 크기 설정
PIRAMIDS_SIZE = 100

"""5. 피라미드 만들기"""
"""
높이의 절반만큼 
즉, 50만큼 쌓을 예정
piramids = [0, 1, 2, 3, ... 98, 99, 100]
"""
for piramids in list(range(int(PIRAMIDS_SIZE / 2))):
    minecraftPy.setBlocks(blockX+piramids, blockY-1, blockZ+piramids,
                          blockX + PIRAMIDS_SIZE - piramids, blockY + piramids, blockZ + PIRAMIDS_SIZE - piramids,
                          blocks.SANDSTONE)
    time.sleep(2)