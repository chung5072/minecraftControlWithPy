"""마인크래프트 월드에서 블럭을 특정 위치에 설치하기"""

"""이미 옆에 설치를 했으면 같은 곳에 설치를 해도 위에 쌓지는 않는다."""

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft #마인크래프트 서버와 파이썬 연동
from minecraftProj.minecraftPyModules import * # 블럭의 데이터를 가져오기
import time # 잠깐의 텀

minecraftPy = Minecraft.create()
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

"""2. 플레이어의 위치를 확인"""
first_pos = minecraftPy.player.getTilePos()
print("Player\'s first pos is " + str(first_pos))
minecraftPy.postToChat("Player\'s first pos is " + str(first_pos)) # (179,2,-90)

"""3. 플레이어의 위치에서 x축으로 +1만큼 이동한 곳에 블럭을 설치"""
first_pos.x = first_pos.x + 1 # 집 방향으로 바라보면 왼쪽에 설치가 된다.

minecraftPy.setBlock(first_pos, blocks.STONE)
