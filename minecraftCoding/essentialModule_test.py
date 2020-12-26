"""내가 생각했을 때 필요한 필.수 모듈_테스트"""

from mcpi.minecraft import Minecraft
from minecraftProj.minecraftPyModules import *

minecraftPy = Minecraft.create()

#essentialModule_selfMade.connectSever() # 서버와 잘 연결이 됐는지 확인

#essentialModule_selfMade.getMyPos() # 내 위치를 출력

essentialModule_selfMade.comeBackHome() # 집의 침대로 돌아가기

#essentialModule_selfMade.getBlockData() # 블럭의 데이터를 구하기

#essentialModule_selfMade.getHighestPos() # 가장 높은 곳으로 이동하기

#essentialModule_selfMade.removeNearBy() # 내 위치를 중심으로 주위로 가로*7, 세로*1, 높이*7 만큼 없에기

#essentialModule_selfMade.showDirection() # 내 위치를 중심으로 동, 서, 남, 북 보여주기

#essentialModule_selfMade.changeBlockToSomething() # 칼을 이용해서 우클릭한 블럭을 특정 블럭으로 변경하기

#essentialModule_selfMade.isThereSomething() # 플레이어가 특정 좌표를 입력해서 해당 좌표에 블럭이 있는지 확인