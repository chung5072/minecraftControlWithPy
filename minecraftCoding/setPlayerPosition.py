"""마인크래프트 월드에서 사용자의 위치를 이동하기"""
from mcpi.minecraft import Minecraft

minecraftPy = Minecraft.create()
minecraftPy.postToChat("hello, Minecraft!") # 파이썬과 마인크래프트가 잘 연결되는지 확인

"""
setPos(소수점), setTilePos(정수)로 사용자 위치를 변경하기
F3키를 이용해서 사용자의 위치를 알 수 있지만 getPos, getTilePos를 이용해서 위치를 알아내는 것도 좋다
F3으로 나오는 좌표계를 맹신해서는 안된다.
"""
playerPos = minecraftPy.player.getTilePos()
print("before: " + str(playerPos)) # 현 위치: (177, -2, -77)

minecraftPy.player.setTilePos(178,2,-90) # 해당 좌표로 이동하는 코드
"""
setTilePos()는 결과값이 없다.
해당 함수의 과정 중에서 이동이 일어났다.

playerPos.x = playerPos.x + 10
playerPos.y = playerPos.y + 10
playerPos.z = playerPos.z + 10

minecraftPy.player.setTilePos(playerPos)
print("after: " + playerPos)
"""