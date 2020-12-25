"""건물 만들기"""

"""
단숨에 건물 생산!
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

"""3. 건물 생산"""
while True:

    blockInf = minecraftPy.events.pollBlockHits()

    if len(blockInf) > 0:
        blockFirstIndex = blockInf[0]

        # 블럭 좌표를 다른 이름의 변수로 대입
        # 블럭의 좌표 변수를 변경, block 리스트에서 1번째 블럭을 불러오고 나서야 좌표가 지정됨.
        blockX = blockFirstIndex.pos.x
        blockY = blockFirstIndex.pos.y
        blockZ = blockFirstIndex.pos.z

        # 아래의 코드를 블럭 변수 선언 위에다가 두면 에러가 발생한다
        blockFirstIndexID = minecraftPy.getBlock(blockX, blockY, blockZ)
        """
        해당 코드를 변수 선언의 위에다가 작성을 하면
        없는 변수로 getBlock() 함수를 실행하기 때문에 
        어떻게 생각하면 당연히 에러가 발생할 수 밖에 없다.
        """

        # 블럭의 ID를 구하고 해당 블럭의 ID와 좌표를 출력
        minecraftPy.postToChat(f"Block\'s ID: {blockFirstIndexID}")
        minecraftPy.postToChat(f"{blockFirstIndexID} Block\'s position: {blockX}, {blockY}, {blockZ}")

        blockInf = [] # 블럭의 리스트를 초기화

        # 블럭의 데이터를 구하는 반복문을 끝내는 조건식
        if blockFirstIndexID == blocks.DOOR_WOOD:
            break
            """
            만일 해당 블럭의 ID 값이 DOOR_WOOD와 같다면
            무한 반복문을 깸.
            """

        # 다른 모듈의 buildEasyBuilding() 함수를 활용하여 건물을 지음.
        buildFunc.buildEasyBuilding(minecraftPy, blockX+1, blockY, blockZ+1)



