"""건물 만들기_해당 파일을 불러와서 다른 파일에서 함수로 실행"""

"""
단숨에 건물 생산!
"""

"""1. 모듈 불러오기"""
# 마인크래프트 서버 불러오기
from mcpi.minecraft import Minecraft

# 내가 만든 필수 함수 불러오기
from minecraftProj.minecraftPyModules import *

# 일정량의 시간을 비우기 위해
import time

"""2. 건물을 만드는 함수"""
# 블럭 설정
BRICK_BLOCK = blocks.BRICK_BLOCK
AIR = blocks.AIR
GLASS = blocks.GLASS
TORCH = blocks.TORCH
DOOR_WOOD = blocks.DOOR_WOOD
BRICK_STAIRS = blocks.BRICK_STAIRS

# 함수_매개변수로 minecraftPy와 건축물을 지을 좌표값.
def buildEasyBuilding(minecraftPy, buildingBlockX, buildingBlockY, buildingBlockZ):
    minecraftPy.postToChat("Making Building 1 later seconds")
    time.sleep(1)

    # 건물 크기
    HORIZONTAL = 6
    VERTICAL = 6
    HEIGHT = 6

    # 건물의 큰 뼈대_벽돌, 유리
    minecraftPy.setBlocks(buildingBlockX, buildingBlockY, buildingBlockZ,
                          buildingBlockX + HORIZONTAL, buildingBlockY + HEIGHT, buildingBlockZ + VERTICAL,
                          BRICK_BLOCK) 
    minecraftPy.setBlocks(buildingBlockX, buildingBlockY + 2, buildingBlockZ,
                          buildingBlockX + HORIZONTAL, buildingBlockY + 4, buildingBlockZ + VERTICAL,
                          GLASS)
    
    # 건물 내부에 들어갈 수 있도록 빈 공간
    minecraftPy.setBlocks(buildingBlockX + 1, buildingBlockY+1, buildingBlockZ + 1,
                          buildingBlockX + HORIZONTAL - 1, buildingBlockY + HEIGHT - 1, buildingBlockZ + VERTICAL - 1,
                          AIR)
    
    # X축, Z축으로 정 가운데에 횃불을 설치
    minecraftPy.setBlock(int(buildingBlockX + HORIZONTAL / 2), buildingBlockY, int(buildingBlockZ + VERTICAL / 2), TORCH)

    # 입구에 문 설치
    # 문을 설치할 때, 위에서 아래로 지어야 문이 생성된다.
    minecraftPy.setBlock(buildingBlockX + 1, buildingBlockY + 2, buildingBlockZ, DOOR_WOOD, 8) # 윗 부분, y+1, 8
    minecraftPy.setBlock(buildingBlockX + 1, buildingBlockY + 1, buildingBlockZ, DOOR_WOOD, 0) # 아랫 부분, y, 0

    # 계단 설치
    minecraftPy.setBlock(buildingBlockX + 1, buildingBlockY, buildingBlockZ - 1, BRICK_STAIRS, 2) # 남쪽, 2
    minecraftPy.setBlock(buildingBlockX + 1, buildingBlockY - 1, buildingBlockZ - 2, BRICK_STAIRS, 2) # 남쪽, 2
    minecraftPy.setBlock(buildingBlockX + 1, buildingBlockY - 1, buildingBlockZ - 1, BRICK_BLOCK) # 계단 사이에 벽돌