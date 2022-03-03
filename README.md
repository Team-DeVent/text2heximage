![head](./head.png)
# TextToHexImage

텍스트를 16진수로 변환하여 hex color 이미지로 표현하는 파이썬 패키지 입니다. 생성된 이미지를 텍스트로 변환할 수 있습니다.  

## Installation

```
pip3 install Text2HexImage
```

## Usage

```python
from text2heximage import core

control = core.T2i(200, 200, 40)

randomid = control.generatePrimaryId()
randomid_hex = control.createHex(randomid)

control.encrypt(randomid_hex, './')
hex_color = control.decrypt('result.png')
```

## Example


아래 그림은 예시 입니다.  
![ex_screenshot](./img/test.png)

