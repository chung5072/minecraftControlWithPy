"""하늘로 올라가는 계단 만들기_먼저 계단의 방향을 생각하기"""

"""
하늘로 올라가는 계단을 만들 때, 계단의 방향성도 생각을 해줘야 한다.
방향성으로는 0(동), 1(서), 2(남), 3(북)이 있다.
"""

from mcpi.minecraft import Minecraft
from minecraftProj.minecraftPyModules import *

"""1. 서버에 접속"""
minecraftPy=Minecraft.create() # 서버 접속

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

"""2. 플레이어의 위치를 확인하기"""
gotPlayerPos=essentialModule_selfMade.getMyPos() # 내 위치를 얻고, 출력하기

"""3. 나선 모양의 계단을 설치하기"""
# 사용자의 위치에 블럭의 좌표를 대입
blockX=gotPlayerPos.x+5
blockY=gotPlayerPos.y+5
blockZ=gotPlayerPos.z+5

# 방향: 0 = 내가 바라보는 방향 (아래 계단이 있는 곳 그니까 _- 이런 식.) / 동
blockX=blockX+2
minecraftPy.setBlock(blockX, blockY, blockZ, 53, 0)
# 방향: 1 = 내가 바라보는 방향의 반대 방향 / 서
blockX=blockX+2
minecraftPy.setBlock(blockX, blockY, blockZ, 53, 1)
# 방향: 2 = 내가 바라보는 방향에서 왼쪽을 향항 / 남
blockX=blockX+2
minecraftPy.setBlock(blockX, blockY, blockZ, 53, 2)
# 방향: 3 = 내가 바로보는 방향에서 오른쪽으로 향함 / 북
blockX=blockX+2
minecraftPy.setBlock(blockX, blockY, blockZ, 53, 3)

