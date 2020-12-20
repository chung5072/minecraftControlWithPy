"""마인크래프트 서버와 파이썬이 서로 연동되는지 확인_채팅으로"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("mcpi: hello, minecraft")