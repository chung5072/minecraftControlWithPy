"""마인크래프트 월드에서 사용자의 위치를 이동하기_함수"""

"""현재 위치를 파악한 뒤에 내 위치에서 입력한 값만큼 움직이는 함수 만들기"""
from mcpi.minecraft import Minecraft

minecraftPy = Minecraft.create() # 파이썬과 마인크래프트 연동
minecraftPy.postToChat("hello, Minecraft!!") # 연동이 잘 되었는지 확인

"""1. 이동시키고 싶은 값을 입력받기"""
moveX = int(input("x 좌표의 값: "))
moveY = int(input("y 좌표의 값: "))
moveZ = int(input("z 좌표의 값: "))

def moveTo(x, y, z):
    """플레이어의 위치를 이동시키는 함수"""
    """2. 현재 위치를 파악하기"""
    beforePlayerPos = minecraftPy.player.getTilePos() # 현재 위치
    print("이동하기 전의 위치: " + str(beforePlayerPos))

    """3. 플레이어의 좌표에 해당 값을 대입"""
    beforePlayerPos.x = beforePlayerPos.x + x
    beforePlayerPos.y = beforePlayerPos.y + y
    beforePlayerPos.z = beforePlayerPos.z + z

    afterPlayerPos = beforePlayerPos # 이후에 이동하고자 하는 좌표를 표시
    print(afterPlayerPos) # 잘 더해졌는지 확인

    """4. 플레이어의 좌표에 대입하기"""
    minecraftPy.player.setTilePos(afterPlayerPos)

moveTo(moveX, moveY, moveZ)