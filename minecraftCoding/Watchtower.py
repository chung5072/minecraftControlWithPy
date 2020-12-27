from mcpi.minecraft import Minecraft
import time
from minecraftProj.minecraftCoding import blocks

def buildWatchTower(mc,x,y,z) :

    y-=1
    
    time.sleep(3)

    #초기화
    mc.setBlocks(x-2, y, z-2, x+7, y+40, z+7, blocks.AIR)

    # 벽면
    mc.setBlocks(x-1, y, z-1, x-1, y+40, z+7, blocks.STONE)
    mc.setBlocks(x+7, y, z-1, x+7, y+40, z+7, blocks.STONE)
    mc.setBlocks(x-1, y, z-1, x+7, y+40, z-1, blocks.STONE)
    mc.setBlocks(x-1, y, z+7, x+7, y+40, z+7, blocks.STONE)
    #바닥
    mc.setBlocks(x, y, z, x+6, y, z+6, blocks.WOOD_PLANKS)
    #탑꼭대기
    mc.setBlocks(x-6, y+40, z+12, x+12, y+45, z-6, blocks.STONE)
    mc.setBlocks(x-6, y+42, z+12, x+12, y+42, z-6, blocks.GLASS)
    mc.setBlocks(x-5, y+41, z+11, x+11, y+44, z-5, blocks.AIR)
    # 문
    mc.setBlock(x+3, y+1, z-1, blocks.DOOR_WOOD, 1, 0)
    mc.setBlock(x+3, y+2, z-1, blocks.DOOR_WOOD, 8, 0)

    for i in range(2): # 높이 20 * 2
        for face in [0,2,1,3]:
            #0,2,1,3 동남서북
            for j in list(range(5)):
                """
                5칸을 올라갈때마다 방향에 따라서 계단의 방향을 설치
                1칸 1칸마다 높이를 1씩 올리기
                5칸에 도달했을 때, 블럭을 하나 큐브 블럭을 하나 설치해서 
                다음 계단과 연결고리를 만들어줌
                
                0(동), 1(서), 2(남), 3(북)
                """
                if face == 0:
                    x += 1
                elif face == 2 :
                    z += 1
                elif face == 1:
                    x -= 1
                elif face == 3:
                    z -= 1
                y += 1
                mc.setBlock(x,y,z,53,face)
            if face == 0:
                x += 1
            elif face == 2 :
                z += 1
            elif face == 1:
                x -= 1
            elif face == 3:
                z -= 1
            mc.setBlock(x,y,z,blocks.WOOD_PLANKS)
            mc.setBlock(x,y+1,z,blocks.TORCH)
            time.sleep(0.5)
            
    # 계단을 올라갈 수 있도록 계단과 꼭대기에 빈 공간을 줌
    mc.setBlocks(x,y,z+2,x,y,z+4,blocks.AIR)

