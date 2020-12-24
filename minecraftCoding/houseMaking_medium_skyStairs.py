"""하늘로 올라가는 계단 만들기"""

"""
하늘로 올라가는 계단을 만들 때, 계단의 방향성도 생각을 해줘야 한다.
방향성으로는 0(동), 1(서), 2(남), 3(북)이 있다.

중간중간 아래와 같은 코드가 있을 것이다
blockX = blockX+1
blockZ = blockZ+1
blockX = blockX-1
blockZ = blockZ-1
이건 저번에 만들었던 setBlock()과 같은 원리이다.
x축으로 나아가고(x+1), z축으로 나아갔으면(z+1) 네모나게 만들기 위해서는
x축으로 되돌아오고(x-1), z축으로 되돌아와야(z-1) 하기 때문이다.
"""

"""1. 모듈 불러오기"""
# 마인크래프트 서버 불러오기
from mcpi.minecraft import Minecraft

# 내가 만든 필수 함수 불러오기
from minecraftProj.minecraftPyModules import *

# 일정량의 시간을 비우기 위해
import time

"""2. 서버에 접속"""
minecraftPy=Minecraft.create() # 서버 접속

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

"""3. 플레이어의 위치를 확인하기"""
gotPlayerPos = essentialModule_selfMade.getMyPos() # 내 위치를 얻고, 출력하기

"""4. 설치할 블럭의 위치를 생각하기"""
# 먼저 사용자의 좌표에 블럭의 변수를 대입하기
blockX = gotPlayerPos.x
blockY = gotPlayerPos.y
blockZ = gotPlayerPos.z

# 그 다음, 사용자의 위치에서 일정만큼 떨어진 곳에 계단 설치하기
blockX = blockX+1
blockY = blockY-1
"""
이 부분은 아래의 코드에서 
blockY = blockY+1
해당 부분으로 y축을 1칸 더해주고 시작을 하기 때문에
플레이어의 앞 1칸이 비어버리므로 1칸을 낮춘 상태에서 시작하는 것이다.
"""
time.sleep(3)
"""5. 올라가는 계단 설치하기"""
while blockY < 192: # 계단의 최대 높이를 설정 = 마인크래프트 내의 최고 건설 높이
    # 0 = 먼저 동쪽으로 계단 설치
    for eastStairs in list(range(10)): # 동쪽으로 계단 10개를 설치
        # 1칸씩 올라갈 수 있도록
        blockX = blockX+1 # 동쪽
        blockY = blockY+1
        minecraftPy.setBlock(blockX, blockY, blockZ, 53, 0)
    # 마지막으로 1칸 더 나아간 다음, 다른 방향으로 계단을 설치
    blockX = blockX+1
    minecraftPy.setBlock(blockX, blockY, blockZ, 53, 4) # 계단을 거꾸로 설치 - 평평한 땅을 위해서
    time.sleep(3)

    # 2 = 그 다음 남쪽으로 계단 설치
    for eastStairs in list(range(10)):  # 남쪽으로 계단 10개를 설치
        # 1칸씩 올라갈 수 있도록
        blockZ = blockZ + 1 # 남쪽
        blockY = blockY + 1
        minecraftPy.setBlock(blockX, blockY, blockZ, 53, 2)
    # 마지막으로 1칸 더 나아간 다음, 다른 방향으로 계단을 설치
    blockZ = blockZ + 1
    minecraftPy.setBlock(blockX, blockY, blockZ, 53, 4) # 계단을 거꾸로 설치 - 평평한 땅을 위해서
    time.sleep(3)

    # 1 = 그 다음 서쪽으로 계단 설치
    for eastStairs in list(range(10)):  # 서쪽으로 계단 10개를 설치
        # 1칸씩 올라갈 수 있도록
        blockX = blockX - 1 # 동쪽의 반대 = 서쪽
        blockY = blockY + 1
        minecraftPy.setBlock(blockX, blockY, blockZ, 53, 1)
    # 마지막으로 1칸 더 나아간 다음, 다른 방향으로 계단을 설치
    blockX = blockX - 1
    minecraftPy.setBlock(blockX, blockY, blockZ, 53, 4) # 계단을 거꾸로 설치 - 평평한 땅을 위해서
    time.sleep(3)

    # 3 = 마지막으로 북쪽으로 계단 설치
    for eastStairs in list(range(10)):  # 북쪽으로 계단 10개를 설치
        # 1칸씩 올라갈 수 있도록
        blockZ = blockZ - 1 # 남쪽의 반대 = 북쪽
        blockY = blockY + 1
        minecraftPy.setBlock(blockX, blockY, blockZ, 53, 3)
    # 마지막으로 1칸 더 나아간 다음, 다른 방향으로 계단을 설치
    blockZ = blockZ - 1
    minecraftPy.setBlock(blockX, blockY, blockZ, 53, 4) # 계단을 거꾸로 설치 - 평평한 땅을 위해서
    time.sleep(3)