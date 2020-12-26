"""내가 생각했을 때 필요한 필수 모듈"""

"""
1. 연결이 됐는지 확인하는 함수
2. 내 위치를 확인하는 함수
3. 내 침대로 이동하는 함수
4. 지하로 내려갔을 경우, 해당 위치에서 가장 높은 위치로 이동하는 함수
5. 블럭의 ID값을 구하는 함수
6. 주위 블럭을 없에는 함수
7. 동서남북을 구하는 함수
8. 해당 블럭을 클릭하면 특정 블럭으로 바꾸는 함수
9. 특정 좌표를 입력해서 해당 좌표에 블럭이 있는지 확인하는 함수
"""

from mcpi.minecraft import Minecraft
from . import compare_inputAndBlocks
from . import blocks

minecraftPy = Minecraft.create()

"""1. 연결이 됐는지 확인하는 함수"""
def connectSever():
    minecraftPy.postToChat("hello, it\'s me!!")  # 마인크래프트 서버와 파이썬 연동 성공

"""2. 내 위치를 확인하는 함수"""
def getMyPos():
    playerPos = minecraftPy.player.getTilePos() # 플레이어의 현재 있는 위치를 정수로 구해줌

    minecraftPy.postToChat(f"Player\'s position is {playerPos}") # 정수로 구해준 값을 출력
    return playerPos # 정수로 구해준 값을 반환함 - 다른 함수에서 사용이 가능

"""3. 내 침대로 이동하는 함수"""
def comeBackHome():
    minecraftPy.player.setTilePos(-1000, -5, 1638) # 플레이어의 위치를 집에 있는 침대로 이동

"""4. 지하로 내려갔을 경우, 해당 위치에서 가장 높은 위치로 이동하는 함수"""
def getHighestPos():
    gotPlayerPos = getMyPos() # getMyPos()를 통해 구한 플레이어의 위치를 얻음

    # 플레이어의 좌표를 playerPosX, playerPosY, playerPosZ 좌표로 넣어줌
    playerPosX = gotPlayerPos.x
    playerPosY = gotPlayerPos.y
    playerPosZ = gotPlayerPos.z

    highestY = minecraftPy.getHeight(playerPosX, playerPosZ) + 1 # X와 Z 좌표를 이용해서 가장 높은 곳 + 1
    """
    여기서 가장 높은 곳 + 1을 해준 이유는 가장 높은 곳에서 1만큼 더 올라가야 블럭 위에 설 수 있기 때문에
    """

    playerPosY = highestY # 가장 높은 곳을 구함

    minecraftPy.player.setTilePos(playerPosX, playerPosY, playerPosZ) # 구한 위치로 플레이어를 이동

    newPlayerPos = getMyPos() # 새로 이동한 플레이어의 위치를 구함

    minecraftPy.postToChat(f"New playes\'s position is {newPlayerPos}") # 가장 높은 곳으로 이동한 좌표를 출력함

"""5. 블럭의 ID값을 구하는 함수"""
def getBlockData():
    blockCount = 0 # 블럭의 데이터를 구하는데 제한을 두기 위한 변수

    blockLimit = int(input("블럭 데이터를 몇 번 얻고 싶으세요? ")) # 몇 번만큼 블럭을 구하고 싶은지 사용자가 입력

    while True:  # 아래의 블럭 데이터를 무한 반복으로 얻기 위해서
        blockInf = minecraftPy.events.pollBlockHits()
        """
        여기다가 코드를 넣었더니 실패했다.
        blockCount = blockCount + 1
        print(f"blockcount: {blockCount}")
        """
        if len(blockInf) > 0:
            block = blockInf[0]  # 블럭을 리스트로 받는데 가장 앞의 1개만 사용한다.
            """
            블럭을 때릴 때마다 실시간으로 처리하기 때문에 다른 번호를 사용할 일은 거의 없다.
            """
            blockID = minecraftPy.getBlock(block.pos.x, block.pos.y, block.pos.z)  # block의 좌표: x, y, z

            # 얻은 블럭의 데이터를 출력
            minecraftPy.postToChat(f"x: {block.pos.x}, y: {block.pos.y}, z: {block.pos.z}")
            """
            minecraftPy.postToChat("x: %d, y: %d, z: %d"% (block.pos.x, block.pos.y, block.pos.z))
            각각 %d에 block.pos.x / y / z 값이 들어간다.
            """
            minecraftPy.postToChat("Block ID: " + str(blockID))
            minecraftPy.postToChat("face: " + str(block.face))
            # face 같은 경우는 계단 같은 특별한 경우만 face가 있다.
            blockInf = []  # 데이터가 있는 blockinf를 비워준다.

            blockCount = blockCount + 1  # 블럭 변경의 제한을 두기 위해서 갯수를 더해준다.
            minecraftPy.postToChat(f"count limit: {blockCount}")

            if blockCount == blockLimit: # 블럭 구하는데 제한이 다 되면 무한 반복을 멈춤
                break

"""6. 주위 블럭을 없에는 함수"""
def removeNearBy():
    gotplayerPos = getMyPos() # 플레이어의 현재 위치를 getMyPos()로 가져오고

    # 플레이어의 좌표를 기반으로 앞으로 놓을 블럭의 변수를 설정하고
    blockX = gotplayerPos.x
    blockY = gotplayerPos.y
    blockZ = gotplayerPos.z

    # 거리를 설정하여 해당 주변을 빈 공간으로 채운다. 현재 4*4
    minecraftPy.setBlocks(blockX-3, blockY, blockZ-3, blockX+3, blockY, blockZ+3, blocks.AIR)

"""7. 동서남북을 구하는 코드"""
def showDirection():
    gotplayerPos = getMyPos() # 플레이어의 현재 위치를 getMyPos()로 가져오고

    # 플레이어의 좌표를 기반으로 앞으로 놓을 블럭의 변수를 설정하고
    blockX = gotplayerPos.x
    blockY = gotplayerPos.y
    blockZ = gotplayerPos.z

    # east
    minecraftPy.setBlock(blockX + 1, blockY - 1, blockZ, (35, 3))
    minecraftPy.setBlock(blockX + 2, blockY - 1, blockZ, (35, 3))
    # west
    minecraftPy.setBlock(blockX - 1, blockY - 1, blockZ, (35, 0))
    minecraftPy.setBlock(blockX - 2, blockY - 1, blockZ, (35, 0))
    # south
    minecraftPy.setBlock(blockX, blockY - 1, blockZ + 1, (35, 14))
    minecraftPy.setBlock(blockX, blockY - 1, blockZ + 2, (35, 14))
    # north
    minecraftPy.setBlock(blockX, blockY - 1, blockZ - 1, (35, 15))
    minecraftPy.setBlock(blockX, blockY - 1, blockZ - 2, (35, 15))

    minecraftPy.postToChat("EAST == X + 1 == BLUE")
    minecraftPy.postToChat("WEST == X - 1 == WHITE")
    minecraftPy.postToChat("SOUTH == Z + 1 == RED")
    minecraftPy.postToChat("NORTH == Z - 1 == BLACK ")

"""8. 해당 블럭을 클릭하면 특정 블럭으로 바꾸는 함수"""
def changeBlockToSomething():
    userinput = input("Which block do you want to change? ")

    blockCode = compare_inputAndBlocks.compareInputAndBlocks(userinput)

    # 블럭을 때리는 횟수에 조건을 걸어서 해당 조건이 발생하면 질문을 던짐.
    blockCount = 0

    """2. 블럭들을 쌓을 설정값? 정해주기"""
    # 얼만큼 변경하고 싶은지
    blockLimit = int(input("What number would you like to change? "))

    """3. 블럭의 좌표를 요청 및 해당 블럭을 금 블럭으로 교체"""
    while True:  # 아래의 블럭 데이터를 무한 반복으로 얻기 위해서
        blockInf = minecraftPy.events.pollBlockHits()  # 블럭을 때리면 해당 블럭을 리스트에 저장

        if len(blockInf) > 0:
            block = blockInf[0]  # 블럭을 리스트로 받는데 가장 앞의 1개만 사용한다.
            """
            블럭을 때릴 때마다 실시간으로 처리하기 때문에 다른 번호를 사용할 일은 거의 없다.
            """

            # 블럭의 좌표 변수를 변경, block 리스트에서 1번째 블럭을 불러오고 나서야 좌표가 지정됨.
            blockX = block.pos.x  # x좌표
            blockY = block.pos.y  # y좌표
            blockZ = block.pos.z  # z좌표

            # 얻은 블럭의 좌표를 출력
            minecraftPy.postToChat(f"x: {blockX}, y: {blockY}, z: {blockZ}")
            """
            minecraftPy.postToChat("x: %d, y: %d, z: %d"% (block.pos.x, block.pos.y, block.pos.z))
            각각 %d에 block.pos.x / y / z 값이 들어간다.
            """

            minecraftPy.setBlock(blockX, blockY, blockZ, blockCode)  # 해당 좌표에 있는 블럭을 원하는 블럭으로 변경
            blockInf = []  # 데이터가 있는 blockinf를 비워준다.

            blockCount = blockCount + 1  # 블럭 변경의 제한을 두기 위해서 갯수를 더해준다.
            minecraftPy.postToChat(f"count limit: {blockCount}")

            if blockCount == blockLimit:
                break

    minecraftPy.postToChat("Change finished")

def isThereSomething():
    # 플레이어가 특정 좌표를 입력
    somethingX = int(input("Input X Pos: "))
    somethingY = int(input("Input Y Pos: "))
    somethingZ = int(input("Input Z Pos: "))

    if minecraftPy.getBlock(somethingX, somethingY, somethingZ) == 0: # 해당 좌표에 0(공기)이면
        minecraftPy.postToChat("empty!")
    else: # 해당 좌표에 0(공기)이 아니면
        minecraftPy.postToChat("something!")




