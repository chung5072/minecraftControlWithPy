"""마인크래프트 월드에서 사용자의 위치를 가져오기"""
from mcpi.minecraft import Minecraft

minecraftPy = Minecraft.create()

intPos = minecraftPy.player.getTilePos() # 위치 조회, 정수형

minecraftPy.postToChat(f"x: {intPos.x}") # 얘는 매개변수가 1개여야 한다. 문자형, 실수형 조합이 안된다.
minecraftPy.postToChat(f"y: {intPos.y}")
minecraftPy.postToChat(f"z: {intPos.z}")

# 179, -2, -68

floatPos = minecraftPy.player.getPos() # 위치 조회, 실수형

minecraftPy.postToChat(f"x: {floatPos.x}")
minecraftPy.postToChat(f"y: {floatPos.y}")
minecraftPy.postToChat(f"z: {floatPos.z}")

# 여기서부터는 파이참 내부 콘솔에서 결과를 보여줌
print(f"x: {intPos.x}")
print(f"y: {intPos.y}")
print(f"z: {intPos.z}")

print(f"x: {floatPos.x}")
print(f"y: {floatPos.y}")
print(f"z: {floatPos.z}")

"""
F3을 눌러서 위치를 확인할 수 있지만, F3으로 나오는 결과와 파이썬에서 나오는 즉, mcpi의 값과 정확하게 같지 않다
F3을 맹신해서 하면 안되고 위치를 알고 싶으면 getTilePos나 getPos로 위치를 확인해보도록 하자. 
"""