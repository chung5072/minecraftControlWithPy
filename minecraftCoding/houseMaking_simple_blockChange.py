"""마인크래프트 월드에서 블럭을 건드려서 해당 블럭을 변경하기"""

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft #마인크래프트 서버와 파이썬 연동
from minecraftProj.minecraftPyModules import * # 블럭의 데이터를 가져오기
import time # 잠깐의 텀

minecraftPy = Minecraft.create() # 마인크래프트 서버와 연결을 생성
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

#블럭을 때리는 횟수에 조건을 걸어서 해당 조건이 발생하면 질문을 던짐.
blockCount = 0

"""2. 블럭들을 쌓을 설정값? 정해주기"""
#얼만큼 변경하고 싶은지
blockLimit = int(input("몇 번 변경하고 싶으세요? "))

#블럭 데이터 설정
GOLD = blocks.GOLD_BLOCK # 금블럭
TORCH = blocks.TORCH # 토치

# 횟수 제한
changeCount = 0

"""3. 블럭의 좌표를 요청 및 해당 블럭을 금 블럭으로 교체"""
while True: # 아래의 블럭 데이터를 무한 반복으로 얻기 위해서
    blockInf = minecraftPy.events.pollBlockHits() # 블럭을 때리면 해당 블럭을 리스트에 저장

    if len(blockInf) > 0:
        block = blockInf[0] # 블럭을 리스트로 받는데 가장 앞의 1개만 사용한다.
        """
        블럭을 때릴 때마다 실시간으로 처리하기 때문에 다른 번호를 사용할 일은 거의 없다.
        """

        # 블럭의 좌표 변수를 변경, block 리스트에서 1번째 블럭을 불러오고 나서야 좌표가 지정됨.
        blockX = block.pos.x  # x좌표
        blockY = block.pos.y  # y좌표
        blockZ = block.pos.z  # z좌표

        blockID = minecraftPy.getBlock(blockX, blockY, blockZ) # block의 좌표: x, y, z

        # 얻은 블럭의 좌표를 출력
        minecraftPy.postToChat(f"x: {blockX}, y: {blockY}, z: {blockZ}")
        """
        minecraftPy.postToChat("x: %d, y: %d, z: %d"% (block.pos.x, block.pos.y, block.pos.z))
        각각 %d에 block.pos.x / y / z 값이 들어간다.
        """
        minecraftPy.postToChat("Block ID: " + str(blockID))
        minecraftPy.postToChat("face: " + str(block.face))
        # face 같은 경우는 계단 같은 특별한 경우만 face가 있다. 블럭이 바라보는 방향

        minecraftPy.setBlock(blockX, blockY, blockZ, GOLD) # 해당 좌표에 있는 블럭을 원하는 블럭으로 변경
        blockInf = [] # 데이터가 있는 blockinf를 비워준다.

        blockCount = blockCount + 1 # 블럭 변경의 제한을 두기 위해서 갯수를 더해준다.
        minecraftPy.postToChat(f"count limit: {blockCount}")

        if blockCount == blockLimit:
            break

minecraftPy.postToChat("Change finished")