"""마인크래프트 월드에서 간단하기 집짓기_빈 공간으로 만들기"""

"""
먼저 생각할 것: 입력과 출력
1. 입력받을 것: 어느 정도의 빈 공간을 만들 것인지
2. 출력할 것: 실제 마인크래프트 세상에서 빈 공간이 생성되어야 함
추가. 함수 이름:
"""

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft #마인크래프트 서버와 파이썬 연동
from minecraftProj.minecraftPyModules import * # 블럭의 데이터를 가져오기
import time # 잠깐의 텀

minecraftPy = Minecraft.create() # 마인크래프트 서버와 연결을 생성
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

"""2. 플레이어의 위치를 확인"""
player_pos = minecraftPy.player.getTilePos() # 플레이어의 위치를 불러오기
print("Player\'s first pos is " + str(player_pos))
minecraftPy.postToChat("Player\'s first pos is " + str(player_pos)) # 불러온 값을 출력, 기본값: (179,2,-90)

"""3. 블럭들을 쌓을 설정값? 정해주기"""
# 플레이어의 x+1 좌표, y 좌표, z 좌표를 블럭 좌표에 매칭
blockX = player_pos.x # 플레이어에서 x 좌표로 1만큼 이동한 곳에서 블럭 쌓기 시작
blockY = player_pos.y
blockZ = player_pos.z

# 블럭의 어느 크기 정도로 비워둘 것인지 설정
HORIZONTAL = 100 # 가로
VERTICAL = 100 # 세로
HEIGHT = 100

# 설치할 블럭 종류를 설정
AIR = blocks.AIR # 빈 공간
STONE = blocks.STONE # 돌

"""4. setBlocks()를 활용해서 특정 범위만큼 특정 블럭의 공간으로 만들기"""
minecraftPy.setBlocks(blockX+1, blockY+1, blockZ+2, blockX+12, blockY+30, blockZ+12, blocks.AIR)