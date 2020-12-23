"""마인크래프트 월드에서 블럭 데이터를 얻기"""
"""
사용하는 방법:
검을 들고 마우스 오른쪽 키를 누르면 사용할 수 있다.
"""

"""1. 마인크래프트 서버와 파이썬 연동"""
from mcpi.minecraft import Minecraft
# 잠깐의 텀
import time

minecraftPy = Minecraft.create()
minecraftPy.postToChat("hello, it\'s me!!") # 마인크래프트 서버와 파이썬 연동 성공

#블럭을 때리는 횟수에 조건을 걸어서 해당 조건이 발생하면 질문을 던짐.
blockCount = 0

"""2. 블럭의 좌표를 요청"""
while True: # 아래의 블럭 데이터를 무한 반복으로 얻기 위해서
    blockInf = minecraftPy.events.pollBlockHits()

    if len(blockInf) > 0:
        block = blockInf[0] # 블럭을 리스트로 받는데 가장 앞의 1개만 사용한다.
        """
        블럭을 때릴 때마다 실시간으로 처리하기 때문에 다른 번호를 사용할 일은 거의 없다.
        """
        blockID = minecraftPy.getBlock(block.pos.x, block.pos.y, block.pos.z) # block의 좌표: x, y, z

        # 얻은 블럭의 데이터를 출력
        minecraftPy.postToChat(f"x: {block.pos.x}, y: {block.pos.y}, z: {block.pos.z}")
        """
        minecraftPy.postToChat("x: %d, y: %d, z: %d"% (block.pos.x, block.pos.y, block.pos.z))
        각각 %d에 block.pos.x / y / z 값이 들어간다.
        """
        minecraftPy.postToChat("Block ID: " + str(blockID))
        minecraftPy.postToChat("face: " + str(block.face))
        # face 같은 경우는 계단 같은 특별한 경우만 face가 있다.
        blockInf = [] # 데이터가 있는 blockinf를 비워준다.

        """ 
        failed code
        if blockCount == 10:
            yesOrNo = input("블럭 데이터를 10번 구하셨습니다. 더 구하시겠습니까? ")

            if yesOrNo == "yes":
                blockCount = 0
            elif yesOrNo == "no":
                blockCount = 0
                break
        """
                            
