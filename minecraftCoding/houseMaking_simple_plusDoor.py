"""마인크래프트 월드에서 문을 포함해서 집을 짓기"""

"""
문을 지을 때,
문의 방향, 문의 아래/위, 문이 열리는 방향도 제각각이라는 점을 알아둬야 한다.
문이 도저히 안달림
"""

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft #마인크래프트 서버와 파이썬 연동
from minecraftProj.minecraftPyModules import * # 블럭의 데이터를 가져오기
import time # 잠깐의 텀

minecraftPy = Minecraft.create() # 마인크래프트 서버와 연결을 생성
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

"""2. 블럭들을 쌓을 설정값? 정해주기"""
#블럭 데이터 설정
BRICK_BLOCK = blocks.BRICK_BLOCK # 금블럭
TORCH = blocks.TORCH # 토치
AIR = blocks.AIR # 공기 = 빈공간
DOOR_WOOD = blocks.DOOR_WOOD # 나무 문

# 블럭의 어느 크기 정도로 쌓을 것인지 설정
HEIGHT = 6 # 높이 = y 축
HORIZONTAL = 6 # 가로 = x 축
VERTICAL = 6 # 세로 = z 축

"""3. 플레이어의 위치를 가져오기"""
playerPos = minecraftPy.player.getTilePos()

"""4. 블럭을 놓을 위치를 설정하기"""
blockX = playerPos.x + 2 # 플레이어가 있는 위치에서 2만큼 이동한 곳에서 쌓기 시작
blockY = playerPos.y
blockZ = playerPos.z

"""5. 집 짓기"""
# 먼저 채워진 큐브를 쌓는다고 생각한다.
minecraftPy.setBlocks(blockX, blockY, blockZ, blockX+HORIZONTAL, blockY+HEIGHT, blockZ+VERTICAL, BRICK_BLOCK)
# 그 다음 집 내부의 빈 공간을 지정해준다.
minecraftPy.setBlocks(blockX+1, blockY, blockZ+1, blockX+HORIZONTAL-1, blockY+HEIGHT-1, blockZ+VERTICAL-1, AIR)
# 그 다음 집 앞의 문을 놓을 공간을 비워준다.
minecraftPy.setBlocks(blockX+3, blockY, blockZ+VERTICAL, blockX+3, blockY+1, blockZ+VERTICAL, AIR)
"""
blockX + 4를 하면 실제로 집을 짓기 시작하는 위치의 5칸을 이동한 곳에서 빈 공간이 생긴다.
"""
# 그 다음에 집 정 가운데에 횃불 달기a
minecraftPy.setBlock(int(blockX+HORIZONTAL/2), blockY, int(blockZ+VERTICAL/2), TORCH)
# 그 다음에 집에다가 문을 달기
minecraftPy.setBlock(blockX+3,blockY+1,blockZ+VERTICAL,DOOR_WOOD, 8)
minecraftPy.setBlock(blockX+3,blockY+0,blockZ+VERTICAL,DOOR_WOOD, 0)