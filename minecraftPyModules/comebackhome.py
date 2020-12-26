from mcpi.minecraft import Minecraft
from minecraftProj.minecraftPyModules import essentialModule_selfMade

minecraftPy = Minecraft.create() # 서버 접속

essentialModule_selfMade.connectSever() # 서버와 연결이 됐는지 확인

essentialModule_selfMade.comeBackHome()

