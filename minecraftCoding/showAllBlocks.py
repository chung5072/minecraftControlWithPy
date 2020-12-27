from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

pos = mc.player.getTilePos()
soil = 2 # 흙

# pos.x
pos.y = pos.y + 2
# pos.z

for blockCode in range(256):
    for blockState in range(16):
        mc.setBlock(pos.x, pos.y-1, pos.z + blockState, soil)  # x, y, z, blockCode, blockState > 인수
        mc.setBlock(pos.x, pos.y, pos.z + blockState, blockCode, blockState)  # x, y, z, blockCode, blockState > 인수
    pos.x = pos.x + 1
    time.sleep(0.1)
