"""마인크래프트 월드에서 간단하기 집짓기_2번째"""

"""
설치하고자 하는 블럭을 첫 좌표와 끝 좌표를 정해주면 전체 채운 블럭으로 설치
setBlocks(첫블럭_x, 첫블럭_y, 첫블럭_z, 끝블럭_x, 끝블럭_y, 끝블럭_z, 설치할블럭)

수를 5라고 설정을 해서 5개가 쌓일 줄 알았는데, 실제로는 6개가 쌓였다. 생각한 것보다 + 1개이다

처음과 끝의 변수를 같게 하면 한 위치만 설정을 해줄 수 있다.
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
"""
전에 여기서 에러가 발생했었는데
block.x = player_pos.x + 1
위에는 block 클래스?에는 x라는 변수가 없기 때문에 에러가 발생할 수 밖에 없다
변수처럼 인식할 수 있도록 설정을 해줘야 한다.
"""
# 플레이어의 x+1 좌표, y 좌표, z 좌표를 블럭 좌표에 매칭
blockX = player_pos.x + 1 # 플레이어에서 x 좌표로 1만큼 이동한 곳에서 블럭 쌓기 시작
blockY = player_pos.y
blockZ = player_pos.z

# 설치할 블럭 종류를 설정
BRICK = blocks.BRICK_BLOCK # 45번
AIR = blocks.AIR # 0번

# 블럭의 어느 크기 정도로 쌓을 것인지 설정
HEIGHT = 5
HORIZONTAL = 5 # 가로
VERTICAL = 5 # 세로

"""4_1. setBlocks() 함수를 활용해서 블럭을 한 번에 쌓기_꽉 찬 큐브"""
# minecraftPy.setBlocks(첫블럭_x, 첫블럭_y, 첫블럭_z, 끝블럭_x, 끝블럭_y, 끝블럭_z, 설치할블럭)
minecraftPy.setBlocks(blockX, blockY, blockZ, blockX + HORIZONTAL, blockY + HEIGHT, blockZ + VERTICAL, BRICK)

"""4_2. setBlocks() 함수를 활용해서 블럭을 한 번에 쌓기_문을 놓을 공간 및 내부 공간 비우기"""
minecraftPy.setBlocks(blockX, blockY, blockZ, blockX + HORIZONTAL, blockY + HEIGHT, blockZ + VERTICAL, BRICK)
minecraftPy.setBlocks(blockX+1, blockY, blockZ+1, blockX + HORIZONTAL-1, blockY + HEIGHT-1, blockZ + VERTICAL-1, AIR)
minecraftPy.setBlocks(blockX+2, blockY, blockZ+VERTICAL, blockX+3, blockY + HEIGHT-3, blockZ+VERTICAL, AIR)
"""
처음과 끝의 변수를 같게 하면 한 위치만 설정을 해줄 수 있다.
"""
