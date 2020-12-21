"""마인크래프트 월드에서 채팅 치기"""
from mcpi.minecraft import Minecraft
"""
내부 Minecraft 클래스: class Minecraft
mcpi 내부의 minecraft에서 Minecraft의 내용을 불러온다.
"""

minecraftPy = Minecraft.create() # Minecraft 내부의 create()를 가져오겠다. 여기서 mc는 객체
"""
mcpi 파일 내부, minecraft.py 내부, class Minecraft:
@staticmethod
    def create
minecraftPy는 객체, Minecraft는 클래스
mcpi 라이브러리에서 Minecraft에 존재하는 create 함수로 생성한 객체를 minecraftPy에 담아서 사용합니다.   
minecraftPy는 라이브러리에서 구현하므로 그 내용을 확인하려면 mcpi라이브러리를 통쨰로 분석해야합니다. 
"""

minecraftPy.postToChat("/time set day") # 현재 시간을 아침으로 설정하겠다.
"""
mcpi 파일 내부, minecraft.py 내부, class Minecraft:
def postToChat(self, msg):
        '''Post a message to the game chat'''
        self.conn.send(b"chat.post", msg)
"""