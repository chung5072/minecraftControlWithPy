from mcpi.minecraft import Minecraft
import time
from minecraftProj.minecraftCoding import the_great_Wall as gw

mc = Minecraft.create()

while(True):
    """블럭의 데이터를 얻는 코드"""
    blockInf = mc.events.pollBlockHits()

    if len(blockInf) > 0:
        block = blockInf[0]
        bID = mc.getBlock(block.pos)

        mc.postToChat(f"x: {block.pos.x}, y: {block.pos.y}, z:{block.pos.z}")
        mc.postToChat(f"Block ID: {bID}")
        mc.postToChat(f"face: {block.face}")
        blockInf = []

        """만리장성을 쌓는 함수"""
        gw.buildGreateWall(mc, block.pos.x+2, block.pos.y, block.pos.z)