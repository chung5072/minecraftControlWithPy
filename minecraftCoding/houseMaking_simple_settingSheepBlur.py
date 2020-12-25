"""양털 색 값 구하기"""

"""
양털의 색을 구하기
핵심적인 부분
for blurCount in range(100):
    minecraftPy.setBlock(blockX + blurCount*2, blockY, blockZ, (35, blurCount))
    '''
    BLOCK을 놓을 곳에 아래의 코드를 넣으면 
    알록달록한 양털 워터 슬라이드가 만들어진다
    (35, colorCount)
    '''
"""

"""1. 모듈 불러오기"""
# 마인크래프트 서버 불러오기
from mcpi.minecraft import Minecraft

# 내가 만든 필수 함수 불러오기
from minecraftProj.minecraftPyModules import *

# 일정량의 시간을 비우기 위해
import time

# 건물을 쉽게 짓기 만드는 모듈 호출
from minecraftProj.minecraftCoding import psychicPower_makeBuilding_func as buildFunc

"""2. 서버에 접속"""
minecraftPy = Minecraft.create() # 서버 접속

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

"""3. 사용자의 위치 및 방향를 구하기"""
gotPlayerPos = essentialModule_selfMade.getMyPos() # 내 위치
essentialModule_selfMade.showDirection() # 내 위치를 중심으로 방향 구하기

blockX = gotPlayerPos.x-1
blockY = gotPlayerPos.y
blockZ = gotPlayerPos.z

"""4. 양털을 색 값을 구하기"""
for blurCount in range(16): # [0, 1, 2, ... 14, 15, 16]
    minecraftPy.setBlock(blockX - blurCount, blockY-1, blockZ, (35, blurCount)) # 35: 양털, blurCount: 색 지정
    minecraftPy.setBlock(blockX - blurCount, blockY, blockZ, (35, blurCount))

minecraftPy.setBlock(blockX-1, blockY-1, blockZ-2, (35, 0)) # white
minecraftPy.setBlock(blockX-2, blockY-1, blockZ-2, (35, 3)) # blue
minecraftPy.setBlock(blockX-3, blockY-1, blockZ-2, (35, 14)) # red
minecraftPy.setBlock(blockX-4, blockY-1, blockZ-2, (35, 15)) # dark

"""
BLOCK을 놓을 곳에 아래의 코드를 넣으면 
알록달록한 양털 워터 슬라이드가 만들어진다
(35, colorCount)
"""