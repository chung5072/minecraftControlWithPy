from mcpi.minecraft import Minecraft
import time
from minecraftProj.minecraftCoding import blocks

"""
땅의 높이를 구하는 함수 - mc.getHeight(x, z)에서 발전된 형태
기존 getHeight는 공기, 나무, 버섯 등등 모든 블럭을 포함해서 데이터를 구했는데
나무 위 등등 그런 곳에 성벽이 세워지면 이상하므로 해당 데이터는 제외하고
온전한 땅의 데이터를 구한다.

코드를 실행하면 n번째 높이: 숫자, 숫자
숫자 > 이 값이 블럭의 데이터이다.
숫자
숫자
숫자
...
"""
def highestLand(x,z, mc):
    treelist = [0,17,18] #air, tree, mushroom > 그냥 blocks를 호출하면 따로 데이터의 숫자를 쓸 필요가 없다.
    h = mc.getHeight(x,z)
    while(True):
        data = mc.getBlock(x,h-1,z)
        if data not in treelist:
            print(data)
            return h
        h-=1 # 높이를 계속 빼가면서 땅의 데이터를 계속 찾는다.
    
def buildGreateWall(mc,x,y,z) :
    BRICK_BLOCK = 45
    AIR = 0
    length = 100

    mc.postToChat("Start 2 sec later")
    time.sleep(2)
    Hoz = 6
    Ver = 6
    He  = 6

    #GLASS     = 20 > 그냥 blocks를 호출하면 따로 데이터의 숫자를 쓸 필요가 없다.
    #TORCH     = 50
    #DOOR_WOOD = 64

    # 땅에 대한 x 정보를 가져옴
    landListHigh = []
    landListLow = []

    mc.postToChat("Start gathering information of lands")

    for i in range(length):
        # z 좌표 +0~+5에 대해 검사하여 최대의 값을 저장
        """
        높은 부분과 낮은 부분을 구함
        높은 부분을 기준으로 성벽을 쌓고
        낮은 부분은 빈 공간을 없에주기 위해서 구해야함.
        맨 아래부터 맨 윗까지 꽉 찬 성벽을 쌓기 위해서 필요하다.
        """
        zHeight = []

        for j in range(5):
            zHeight.append(highestLand(x+i,z+j,mc)) # highestLand에 대한 데이터를 zHeight 리스트에 저장

        h = max(zHeight) # 높이에 대한 데이터들을 저장한 리스트에 가장 높은 값과 가장 낮은 값을 구함
        l = min(zHeight)
        landListHigh.append(h)
        landListLow.append(l)
        print("%d번째 높이 : %d, %d" %(i,h,l))

    mc.postToChat("Start Building Wall")

    # 지금까지 구한 땅에 대한 정보를 바탕으로 흙 세팅
    for i in range(length):
        mc.setBlocks(x + i,   landListLow[i], z,     x + i, landListHigh[i] + 6, z + 4, 1)
        mc.setBlocks(x + i,landListHigh[i]+6, z + 1, x + i, landListHigh[i] + 6, z + 3, 0)
        time.sleep(0.2)
    
