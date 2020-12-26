"""건축 도면대로 건설하기"""

"""
참고 사이트: blog.naver.com/seungbo2000/90177908101
건축
가로: 29, 세로: 12, 대문 세로: 3, 높이: 6

고려해야할 상황
1. 1층의 구조, 복층의 구조, 지붕의 구조를 세분화
2. 복층을 for문으로 작성할 수 있도록 구분
->  1층
    for i in list(range()):
        복층
    지붕
"""

"""1. 모듈 불러오기"""
# 마인크래프트 서버 불러오기
from mcpi.minecraft import Minecraft

# 내가 만든 필수 함수 불러오기
from minecraftProj.minecraftPyModules import *

# 일정량의 시간을 비우기 위해
import time

"""2. 서버에 접속"""
mc = Minecraft.create() # 서버 접속

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

"""3. 사용자 위치 확인 및 좌표 변수 등록"""
gotPlayerPos = essentialModule_selfMade.getMyPos()

playerX = gotPlayerPos.x
playerY = gotPlayerPos.y
playerZ = gotPlayerPos.z

x = gotPlayerPos.x + 1
y = gotPlayerPos.y
z = gotPlayerPos.z + 1

essentialModule_selfMade.showDirection()

"""4. 집 재료"""
BRICK_BLOCK = blocks.BRICK_BLOCK
QUARTZ_BLOCK = blocks.QUARTZ_BLOCK
STONE_BRICK = blocks.STONE_BRICK
AIR = blocks.AIR
IRON_BLOCK = blocks.IRON_BLOCK
GLASS = blocks.GLASS
DOOR_IRON = blocks.DOOR_IRON
DOOR_WOOD = blocks.DOOR_WOOD
WOOD_PLANKS = blocks.WOOD_PLANKS

"""5. 건축 시작"""
"""5-0. 빈 공간 만들기_평소엔 비활성화"""
mc.setBlocks(x, y, z, x+17, y+1000, z+28, AIR)

"""5-0. 빌딩 공간_높이"""
HEIGHT = 0 # 일단 0

"""5-1. 1층 만들기"""
# 내가 있는 위치 땅 파기
mc.setBlock(playerX, playerY-1, playerZ, AIR)

## 1층 만들기
#1층 바닥만들기
mc.setBlocks(x,y-1,z, x+14,y-1,z+28, STONE_BRICK)
mc.setBlocks(x,y-1,z+12,x+17,y-1,z+16, IRON_BLOCK)

#1층 벽만들기
# 측면
mc.setBlocks(x,y,z, x+13, y+5, z, QUARTZ_BLOCK)
mc.setBlocks(x,y,z+12, x+17, y+5, z+12, QUARTZ_BLOCK)
mc.setBlocks(x,y,z+16, x+17, y+5, z+16, QUARTZ_BLOCK)
mc.setBlocks(x,y,z+28, x+13, y+5, z+28, QUARTZ_BLOCK)

# 앞면
mc.setBlocks(x+14,y,z, x+14, y+5, z+11, BRICK_BLOCK)
mc.setBlocks(x+14,y+3,z, x+14, y+3, z+11, QUARTZ_BLOCK)
mc.setBlocks(x+14,y,z+1, x+14, y+4, z+5, AIR)
mc.setBlocks(x+14,y,z+7, x+14, y+4, z+11, AIR)
mc.setBlocks(x+14,y,z+17, x+14, y+5, z+28, BRICK_BLOCK)
mc.setBlocks(x+14,y+3,z+17, x+14, y+3, z+28, QUARTZ_BLOCK)
mc.setBlocks(x+14,y,z+17, x+14, y+4, z+21, AIR)
mc.setBlocks(x+14,y,z+23, x+14, y+4, z+27, AIR)

#뒷면
mc.setBlocks(x,y,z+1, x, y+5, z+28, BRICK_BLOCK)

# 뒷면 유리창
mc.setBlocks(x, y + 3, z + 2, x, y + 3, z + 4, GLASS)
mc.setBlocks(x, y + 3, z + 24, x, y + 3, z + 26, GLASS)
mc.setBlocks(x, y + 3, z + 13, x, y + 3, z + 15, GLASS)

# 입구 만들기
mc.setBlocks(x+17,y,z+13, x+17,y+5,z+15, GLASS)
mc.setBlocks(x+17,y+3,z+13, x+17,y+3,z+15, QUARTZ_BLOCK)
mc.setBlocks(x+17,y,z+14,x+17,y+1,z+14, DOOR_IRON)

#천장 만들기
mc.setBlocks(x,y+5,z, x+14,y+5,z+28, QUARTZ_BLOCK)

# 문 만들기
mc.setBlocks(x+7,y,z+12, x+7, y+1, z+12, DOOR_WOOD)
mc.setBlocks(x+7,y,z+16, x+7, y+1, z+16, DOOR_WOOD)

h=0

# 복층 만들기
for i in range(3): #세 층을 얹음
    time.sleep(1)

    #바닥 만들기
    h = 5*i
    mc.setBlocks(x, y + h + 6, z, x + 17, y + h + 6, z + 28, QUARTZ_BLOCK)
    mc.setBlocks(x, y + h + 6, z, x + 15, y + h + 6, z, BRICK_BLOCK)
    mc.setBlocks(x, y + h + 6, z + 28, x + 15, y + h + 6, z + 28, BRICK_BLOCK)
    mc.setBlocks(x + 1, y + h + 6, z + 1, x + 13, y + h + 6, z + 11, WOOD_PLANKS)
    mc.setBlocks(x + 1, y + h + 6, z + 18, x + 13, y + h + 6, z + 27, WOOD_PLANKS)

    # 옆면 만들기
    mc.setBlocks(x, y + h + 7, z, x + 14, y + h + 10, z, QUARTZ_BLOCK)
    mc.setBlocks(x + 15, y + h + 7, z, x + 17, y + h + 10, z, BRICK_BLOCK)

    mc.setBlocks(x + 1, y + h + 7, z + 11, x + 17, y + h + 10, z + 11, QUARTZ_BLOCK)

    mc.setBlocks(x + 1, y + h + 7, z + 17, x + 17, y + h + 10, z + 17, QUARTZ_BLOCK)

    mc.setBlocks(x, y + h + 7, z + 28, x + 14, y + h + 10, z + 28, QUARTZ_BLOCK)
    mc.setBlocks(x + 15, y + h + 7, z + 28, x + 17, y + h + 10, z + 28, BRICK_BLOCK)

    # 앞면 만들기
    mc.setBlocks(x + 17, y + h + 7, z, x + 17, y + h + 10, z + 28, BRICK_BLOCK)
    mc.setBlocks(x + 17, y + h + 7, z + 12, x + 17, y + h + 10, z + 16, QUARTZ_BLOCK)

    # 뒷면 만들기
    mc.setBlocks(x, y + h + 6, z + 1, x, y + h + 10, z + 27, BRICK_BLOCK)

    # 앞면 유리창
    mc.setBlocks(x + 17, y + h + 8, z + 2, x + 17, y + h + 9, z + 4, GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 7, x + 17, y + h + 9, z + 9, GLASS)
    mc.setBlocks(x + 17, y + h + 7, z + 13, x + 17, y + h + 10, z + 15, GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 19, x + 17, y + h + 9, z + 21, GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 24, x + 17, y + h + 9, z + 26, GLASS)

    # 뒷면 유리창
    mc.setBlocks(x, y + h + 8, z + 2, x, y + h + 9, z + 4, GLASS)
    mc.setBlocks(x, y + h + 8, z + 24, x, y + h + 9, z + 26, GLASS)
    mc.setBlocks(x, y + h + 8, z + 13, x, y + h + 9, z + 15, GLASS)

    # 옆면 유리창
    mc.setBlocks(x + 3, y + h + 8, z, x + 5, y + h + 9, z, GLASS)
    mc.setBlocks(x + 9, y + h + 8, z, x + 11, y + h + 9, z, GLASS)

    mc.setBlocks(x + 3, y + h + 8, z + 28, x + 5, y + h + 9, z + 28, GLASS)
    mc.setBlocks(x + 9, y + h + 8, z + 28, x + 11, y + h + 9, z + 28, GLASS)

    # 문 만들기
    mc.setBlocks(x+7,y + h + 7, z+11 , x+7, y + h + 8 , z+11, DOOR_WOOD)
    mc.setBlocks(x+7,y + h + 7, z+17 , x+7, y + h + 8 , z+17, DOOR_WOOD)

## 지붕 설치

#지붕 바닥
h+=5
mc.setBlocks(x, y + h + 6, z, x + 17, y + h + 6, z + 28, QUARTZ_BLOCK)
mc.setBlocks(x, y + h + 6, z, x + 15, y + h + 6, z, BRICK_BLOCK)
mc.setBlocks(x, y + h + 6, z + 28, x + 15, y + h + 6, z + 28, BRICK_BLOCK)
mc.setBlocks(x + 1, y + h + 6, z + 1, x + 13, y + h + 6, z + 11, WOOD_PLANKS)
mc.setBlocks(x + 1, y + h + 6, z + 18, x + 13, y + h + 6, z + 27, WOOD_PLANKS)

mc.setBlocks(x, y + h + 7, z, x + 17, y + h + 8, z + 28, QUARTZ_BLOCK)
mc.setBlocks(x+1, y + h + 8, z+1, x + 16, y + h + 8, z + 27, AIR)

# 계단 설치
HighstH = mc.getHeight(x, z)
for i in range(HighstH):
    if(mc.getBlock(x+2,i+1,z+14) == 0):
        pass
    else:
        mc.setBlocks(x+2,i+1,z+14 ,x+6,i+1,z+14,AIR)
        for ii in range(10):
            if mc.getBlock(x+2+ii, i+1-ii, z+14) != AIR:
                break
            else:
                mc.setBlock(x+2+ii, i+1-ii, z+14, QUARTZ_BLOCK)
