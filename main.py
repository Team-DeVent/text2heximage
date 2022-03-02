# TextToImage 
# DipokalHHJ
# 지금까지 커밋이 깔리지 않아 잔디가 뒤숭숭..ㅠㅠ

from text2heximage import core

def main():
  CRH = core.T2i(200, 200, 40)
  pid_org = CRH.generatePrimaryId()
  pid_hex = CRH.createHex(pid_org)

  CRH.encrypt(pid_hex, './')

  hex_color = CRH.decrypt('result.png')
  # hex_data = CRH.createRgbtoHex(rgb_color)

  print(pid_org)
  print(''.join(hex_color))
  # print(hex_data)
     
if __name__ == "__main__":
  main()
