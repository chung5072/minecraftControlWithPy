"""워터슬라이드 만들기"""

"""
워터 슬라이드 단면도
벽돌: # 물: 0

#    #
##00##
 ####
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

# 동, 서, 남, 북 방향 확인하기
essentialModule_selfMade.showDirection()

"""4. 블럭을 놓을 위치를 설정하기"""
# 블럭 변수 선언
# 플레이어의 위치에서 +1, -1, 0만큼 이동한 위치에서 시작
blockX = gotPlayerPos.x
blockY = gotPlayerPos.y
blockZ = gotPlayerPos.z - 2

# 블럭 변수
DIRT = blocks.DIRT
AIR = blocks.AIR
ICE = blocks.ICE
WATER = blocks.WATER_FLOWING

"""5. 워터 슬라이드 설치하기"""
"""
먼저 단면도 생성
워터 슬라이드 단면도
벽돌: # 물: 0
#    #
##00##
 ####
"""
"""
변수의 이름이 같아야 한다
def waterslideSetBlocks(매개변수) -> blockX/Y/Z
함수 밖의 함수를 실행하기 위한 waterslideSetBlocks(매개변수) -> blockX/Y/Z
def 함수 내부의 블럭 좌표 변수 -> blockX/Y/Z
"""
def waterslideSetBlocks(blockX, blockY, blockZ, BLOCK):

    # 1. 꽉 찬 흙으로 된 블럭 설치, 크기: 3*6
    minecraftPy.setBlocks(blockX-3, blockY, blockZ,
                              blockX+3, blockY+2, blockZ, BLOCK)

    # 2. 단면도의 모양대로 빈 공간을
    minecraftPy.setBlock(blockX-3, blockY, blockZ, AIR)
    minecraftPy.setBlock(blockX+3, blockY, blockZ, AIR)
    minecraftPy.setBlocks(blockX-1, blockY+1, blockZ,
                              blockX+1, blockY+1, blockZ, AIR)
    minecraftPy.setBlocks(blockX-2, blockY+2, blockZ,
                              blockX+2, blockY+2, blockZ, AIR)

def waterslideSetBlocks_containWater(blockX, blockY, blockZ, BLOCK):
    for waterslideHeight in range(50): # 0, 1, 2, ... 50
        # waterSlideSize // 3 = 몫의 정수 부분 출력
        waterslideSetBlocks(blockX, blockY + waterslideHeight // 3, blockZ - waterslideHeight, BLOCK)

    minecraftPy.setBlocks(blockX-3, blockY+16, blockZ-50,
                          blockX+3, blockY+18, blockZ-50, BLOCK)
    minecraftPy.setBlock(blockX-3, blockY+16, blockZ-50, AIR)
    minecraftPy.setBlock(blockX+3, blockY+16, blockZ-50, AIR)

    minecraftPy.setBlocks(blockX - 2, blockY+18, blockZ-49,
                          blockX + 2, blockY+18, blockZ-49, WATER)
    minecraftPy.setBlocks(blockX - 1, blockY+17, blockZ-49,
                          blockX + 1, blockY+17, blockZ-49, WATER)

    minecraftPy.setBlocks(blockX-10, blockY, blockZ,
                          blockX+10, blockY-5, blockZ+26, BLOCK)

    minecraftPy.setBlocks(blockX - 9, blockY, blockZ+1,
                          blockX + 9, blockY - 4, blockZ + 25, WATER)

for colorCount in range(7):
    waterslideSetBlocks_containWater(blockX+7*colorCount, blockY, blockZ, ICE)

    """
    BLOCK을 놓을 곳에 아래의 코드를 넣으면 
    알록달록한 양털 워터 슬라이드가 만들어진다
    (35, colorCount)
    """


