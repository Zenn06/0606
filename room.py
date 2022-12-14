class st:
    def __init__(self,stone):
        self.stone = stone
        # print('connected.')

    def getWen(self):
        self.wen = int(self.stone) * 22000
        return self.wen
       
    def wenn_commas(self):
        # print('connected wenn_commas')
        self.wen_commas = ("{:,}").format(self.getWen())
        return self.wen_commas

    def blue_cal(self):
        self.blue_p = self.getWen() / 250
        return int(self.blue_p)

    def blue_p_commas(self):
        return ("{:,}").format(self.blue_cal())
    # def log(self):
    #     print(self.wen)
    # def st(self):
    #     x = input("จำนวนหิน : ")
    #     value = int(x) * 22000
        
    #     v = a(value)
    #     t = p(value)
    #     print(str(v) + " wen\n" + str(a(t)) + " Blue Potions")
    
# c = a.commas()
# a = st("1")
         # await message.channel.send(a.wenn_commas)