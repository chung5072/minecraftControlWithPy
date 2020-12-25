"""마인크래프트 월드에서 문을 포함해서 집을 짓기"""

"""
문을 지을 때,
문의 방향, 문의 아래/위, 문이 열리는 방향도 제각각이라는 점을 알아둬야 한다.
그리고 문을 위에서 아래로 지어야 문이 제대로 지어진다.
"""

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft #마인크래프트 서버와 파이썬 연동
from minecraftProj.minecraftPyModules import * # 블럭의 데이터를 가져오기
import time # 잠깐의 텀

minecraftPy = Minecraft.create() # 마인크래프트 서버와 연결을 생성
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

"""2. 블럭들을 쌓을 설정값? 정해주기"""
DOOR_WOOD = blocks.DOOR_WOOD # 나무 문

"""3. 플레이어의 위치를 가져오기"""
playerPos = minecraftPy.player.getTilePos()

"""4. 블럭을 놓을 위치를 설정하기"""
blockX = playerPos.x + 2 # 플레이어가 있는 위치에서 2만큼 이동한 곳에서 쌓기 시작
blockY = playerPos.y
blockZ = playerPos.z

time.sleep(2)
minecraftPy.setBlock(blockX,blockY+3,blockZ,DOOR_WOOD, 8, 1)
minecraftPy.setBlock(blockX,blockY+2,blockZ,DOOR_WOOD, 0, 1)