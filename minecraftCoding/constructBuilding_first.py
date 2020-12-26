"""건축 도면대로 건설하기"""

"""
참고 사이트: blog.naver.com/seungbo2000/90177908101
건축
가로: 29, 세로: 12, 대문 세로: 3, 높이: 6
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

"""3. 사용자 위치 확인 및 좌표 변수 등록"""
gotPlayerPos = essentialModule_selfMade.getMyPos()

buildX = gotPlayerPos.x
buildY = gotPlayerPos.y
buildZ = gotPlayerPos.z

"""4. 집 재료"""
BRICK_BLOCK = blocks.BRICK_BLOCK
QUARTZ_BLOCK = blocks.QUARTZ_BLOCK
STONE_BRICK = blocks.STONE_BRICK

"""5. 건축"""
minecraftPy.setBlocks(buildX, buildY - 1, buildZ,
                      buildX + 29, buildY - 1, buildZ + 12, STONE_BRICK)

minecraftPy.setBlocks(buildX, buildY, buildZ,
                      buildX, buildY + 6, buildZ + 12, QUARTZ_BLOCK)
minecraftPy.setBlocks(buildX+12, buildY, buildZ,
                      buildX+12, buildY + 6, buildZ + 15, QUARTZ_BLOCK)
minecraftPy.setBlocks(buildX+17, buildY, buildZ,
                      buildX+17, buildY + 6, buildZ + 15, QUARTZ_BLOCK)
minecraftPy.setBlocks(buildX+29, buildY, buildZ,
                      buildX+29, buildY + 6, buildZ + 12, QUARTZ_BLOCK)
