"""마인크래프트 월드에서 사용자의 위치를 이동하기_일정 시간 이후에 움직이기"""

from mcpi.minecraft import Minecraft
import time

minecraftPy = Minecraft.create()

minecraftPy.postToChat("Start 10 seconds")
minecraftPy.postToChat("10")
minecraftPy.postToChat("5")
minecraftPy.postToChat("4")
minecraftPy.postToChat("3")
minecraftPy.postToChat("2")
minecraftPy.postToChat("1")
minecraftPy.postToChat("0")
minecraftPy.postToChat("Launch!")

beforePlayerPos = minecraftPy.player.getTilePos()
print("before: " + str(beforePlayerPos))

while(True):
    time.sleep(0.5)
    beforePlayerPos.y = beforePlayerPos.y + 10
    print(beforePlayerPos)
    minecraftPy.player.setTilePos(beforePlayerPos)
    if beforePlayerPos.y > 50:
        break