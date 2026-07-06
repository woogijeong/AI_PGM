class Television:
    serial_number = 0
    def __init__(self, channel, volume, on):  # 생성자, 변수 3개
        Television.serial_number += 1
        self.__channel = channel
        self.__volume = volume
        self.__on = on
        self.serial_number = Television.serial_number
        
    def set_channel(self, channel):  # 채널 설정
        self.__channel = channel         
    def get_channel(self):          # 채널 가져오기 
        return self.__channel
    def __str__(self): # 객체 출력
        return f"Television(channel={self.__channel}, volume={self.__volume}, on={self.__on} , Serial_num : {self.serial_number})"
    
    
    
tv1 = Television(1, 10, True)       # 객체 생성
tv2 = Television(1, 20 ,False)      # 객체 생성
tv3 = Television(3, 30 ,True)

# print(tv1)
# print(tv2) 
# print(tv3)

print(tv1.get_channel() == tv2.get_channel())  # 객체 끼리는 비교 인수를 정확히  