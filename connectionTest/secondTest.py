"""마인크래프트 서버와 파이썬이 서로 연동되는지 확인_블럭 만들기"""
from mcpi.minecraft import Minecraft # 마인크래프트 서버와 연동
"""
마인크래프트 서버가 열려있지 않으면 코드를 실행할 수 없음.
에러: 
ConnectionRefusedError: [WinError 10061] 대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다
"""

from minecraftProj.minecraftPyModules import * # minecraftPyModules의 __init__.py 내부의 모듈을 이용

mc = Minecraft.create() # Minecraft 클래스의 객체 mc
pos = mc.player.getTilePos() # 플레이어의 위치를 불러옴

mc.setBlocks(pos.x, pos.y, pos.z, pos.x+5, pos.y+2, pos.z, blocks.GRASS) # 해당 위치에 블럭을 생성
mc.setBlock(pos.x, pos.y, pos.z, blocks.AIR)
mc.setBlock(pos.x+5, pos.y, pos.z, blocks.AIR)
mc.setBlocks(pos.x+1, pos.y+2, pos.z, pos.x+4, pos.y+2, pos.z, blocks.AIR)
mc.setBlocks(pos.x+2, pos.y+2, pos.z, pos.x+3, pos.y+2, pos.z, blocks.AIR)