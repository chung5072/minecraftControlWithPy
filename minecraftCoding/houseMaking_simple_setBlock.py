"""마인크래프트 월드에서 간단하기 집짓기_1번째"""

"""
설치하고자 하는 블럭을 1개 씩 설치
setBlock(블럭좌표_x, 블럭좌표_y, 블럭좌표_z, 설치할블럭)
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
blockX = player_pos.x + 1 # 플레이어에서 x 좌표로 1만큼 이동한 곳에서 블럭 쌓기 시작
blockY = player_pos.y
blockZ = player_pos.z

# 블럭의 어느 크기 정도로 쌓을 것인지 설정
HEIGHT = 5
HORIZONTAL = 5 # 가로
VERTICAL = 5 # 세로

# 설치할 블럭 종류를 설정
BRICK = blocks.BRICK_BLOCK # 45번

"""4_1. for ~ in ~문을 활용해서 가로 X 세로 블럭 쌓기"""
minecraftPy.postToChat("Wait 2 seconds, before setting blocks.")
time.sleep(2) # 잠시 멈춤

#가로로 쌓기, 시작: (0, 0)
for blockHorizontal in list(range(HORIZONTAL)): # [0, 1, 2, 3, 4, 5]
    minecraftPy.setBlock(blockX + blockHorizontal, blockY, blockZ, BRICK)
    """
    list(range())로 인해서
    x + 0 -> x + 1 -> x + 2 -> ... -> x + 5까지 쭉쭉 쌓는다
    range()로 작성해서 실행을 해도 list(range())와 같은 결과가 나타난다.
    그래도 list(range())로 작성하자
    """

#minecraftPy.postToChat("wait 2 seconds")
#time.sleep(2) # 잠시 멈춤

#세로로 쌓기, 시작: (5, 0)
for blockVertical in list(range(VERTICAL)):
    minecraftPy.setBlock(blockX + HORIZONTAL, blockY, blockZ + blockVertical, BRICK)
    """
    위에서 블럭을 가로로 5만큼 더해준 상태에서 세로를 쌓는 것이니까 blockX + HORIZONTAL로 시작하는 것이 맞다
    """
    
#minecraftPy.postToChat("wait 2 seconds")
#time.sleep(2) # 잠시 멈춤

#가로로 쌓기 - 거꾸로, 시작: (5, 5)
for blockHorizontal in list(range(HORIZONTAL)):
    minecraftPy.setBlock(blockX + HORIZONTAL - blockHorizontal, blockY, blockZ + VERTICAL, BRICK)
    """
    list(range())로 인해서
    x + 5 - 0 -> x + 5 - 1 -> x + 5 - 2 -> ... -> x + 5 - 5까지 쭉쭉 쌓는다
    """

#minecraftPy.postToChat("wait 2 seconds")
#time.sleep(2) # 잠시 멈춤

#세로로 쌓기 - 거꾸로, 시작: (5, 0)
for blockVertical in list(range(VERTICAL)):
    minecraftPy.setBlock(blockX, blockY, blockZ + VERTICAL - blockVertical, BRICK)
    """
    위에서 블럭을 세로로 5만큼 더해준 상태에서 세로로 쌓는 것이니까 blockZ + VERTICAL로 시작하는 것이 맞다
    """

minecraftPy.postToChat("Wait 5 seconds, before setting cube")
time.sleep(5)

"""4_2. for ~ in ~문을 활용해서 블럭 쌓기_최종 완성 본"""
for blockHeight in list(range(HEIGHT)): # 높이: 5번
    #minecraftPy.postToChat("Wait 2 seconds, before setting blocks.")
    #time.sleep(2)  # 잠시 멈춤

    # 가로로 쌓기, 시작: (0, 0)
    for blockHorizontal in list(range(HORIZONTAL)):  # [0, 1, 2, 3, 4, 5]
        minecraftPy.setBlock(blockX + blockHorizontal, blockY + blockHeight, blockZ, BRICK)
        """
        list(range())로 인해서
        x + 0 -> x + 1 -> x + 2 -> ... -> x + 5까지 쭉쭉 쌓는다
        range()로 작성해서 실행을 해도 list(range())와 같은 결과가 나타난다.
        """

    #minecraftPy.postToChat("wait 2 seconds")
    #time.sleep(2)  # 잠시 멈춤

    # 세로로 쌓기, 시작: (5, 0)
    for blockVertical in list(range(VERTICAL)):
        minecraftPy.setBlock(blockX + HORIZONTAL, blockY + blockHeight, blockZ + blockVertical, BRICK)
        """
        위에서 블럭을 가로로 5만큼 더해준 상태에서 세로를 쌓는 것이니까 blockX + HORIZONTAL로 시작하는 것이 맞다
        """

    #minecraftPy.postToChat("wait 2 seconds")
    #time.sleep(2)  # 잠시 멈춤

    # 가로로 쌓기 - 거꾸로, 시작: (5, 5)
    for blockHorizontal in list(range(HORIZONTAL)):
        minecraftPy.setBlock(blockX + HORIZONTAL - blockHorizontal, blockY + blockHeight, blockZ + VERTICAL, BRICK)
        """
        list(range())로 인해서
        x + 5 - 0 -> x + 5 - 1 -> x + 5 - 2 -> ... -> x + 5 - 5까지 쭉쭉 쌓는다
        """

    #minecraftPy.postToChat("wait 2 seconds")
    #time.sleep(2)  # 잠시 멈춤

    # 세로로 쌓기 - 거꾸로, 시작: (5, 0)
    for blockVertical in list(range(VERTICAL)):
        minecraftPy.setBlock(blockX, blockY + blockHeight, blockZ + VERTICAL - blockVertical, BRICK)
        """
        위에서 블럭을 세로로 5만큼 더해준 상태에서 세로로 쌓는 것이니까 blockZ + VERTICAL로 시작하는 것이 맞다
        """
