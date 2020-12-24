"""광산 만들기"""

"""
모양은 일자 계단식 하강, 터널 구간마다 2개의 횃불(torch)를 설치
"""

"""1. 모듈 불러오기"""
# 마인크래프트 서버 불러오기
from mcpi.minecraft import Minecraft

# 내가 만든 필수 함수 불러오기
from minecraftProj.minecraftPyModules import *

# 일정량의 시간을 비우기 위해
import time

"""2. 서버에 접속"""
minecraftPy = Minecraft.create() # 서버 접속

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

"""3. 플레이어의 위치를 확인하기"""
gotPlayerPos = essentialModule_selfMade.getMyPos() # 내 위치를 얻고, 출력하기

"""4. 블럭을 놓을 위치를 설정하기"""
# 블럭 변수 선언
# 플레이어의 위치에서 +1, -1, 0만큼 이동한 위치에서 시작
blockX = gotPlayerPos.x + 1
blockY = gotPlayerPos.y - 1
blockZ = gotPlayerPos.z + 0
"""
계단을 만들 때, y축(높이) + 1로 반복문을 돌리기 때문에,
처음 시작을 할 때, 1칸 내려간 상태에서 만든다.
"""

# 터널의 너비와 높이
TUNEL_SIZE = 5

"""5. 터널 만들기 시작"""
# 만들기 전에 잠시 쉬어주고
minecraftPy.postToChat("Please wait 3 seconds.")
time.sleep(3)

# 무한 반복문을 통해 만듬
while True:
    # 터널이니까 먼저 빈 공간을 뚫어준다. 아래로 내리기는 CTRL + ENTER
    # Z축 방향으로 6칸이 파임
    minecraftPy.setBlocks(blockX, blockY, blockZ,
                          blockX + TUNEL_SIZE, blockY + TUNEL_SIZE, blockZ + TUNEL_SIZE, blocks.AIR)

    # 터널의 중간아 토치를 설치한다.
    minecraftPy.setBlock(blockX, blockY, blockZ+TUNEL_SIZE / 2, blocks.TORCH) # 첫 번째 횃불
    minecraftPy.setBlock(blockX + TUNEL_SIZE / 2, blockY, blockZ + TUNEL_SIZE / 2, blocks.TORCH) # 두 번째 횃불

    # 터널의 구간을 만들어주기 위해서 터널 사이즈만큼 이동한 곳에서 1칸 내려주고 만들기 시작한다
    blockX = blockX + TUNEL_SIZE
    blockY = blockY - 1

    """터널 사이즈가 너무 커서 중간에 멈춤"""
    # 터널의 제한을 두기 위해서 변수 설정
    tunelLimit = blockY * -1 # -값에서 +값으로 변경
    breakPoint_tunel = tunelLimit % 1000 # 1000으로 나눔

    if breakPoint_tunel == 50: # 1000으로 나눈 값이 50이면 => -50000이면 멈춤
        break

minecraftPy.postToChat("Height limit is 256")

