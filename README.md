# hanifx 🔐

**Version:** 9.0.0  
**Author:** Hanif  
**Email:** sajim4653@gmail.com  

## 🔥 About

`hanifx` is a full-fire, handcrafted Python encoding module built with pure logic — no external encryption libraries!  
It includes:

- Base64, XOR, Caesar, ROT13 encoders
- Time-based encoding with expiry
- Device-locked encoding (cannot be decoded on another system)
- One-way irreversible LifeLock encoding
- Smart input detector (file/string)
- File writer to SDCard
- CLI tool support
- Ready for PyPI upload 🚀

---

## ✅ Installation

```bash
pip install hanifx

~ installation

# pip install hanifx 

# pkg install git 

# git clone https://github.com/hanifx-540/hanifx-v9.git

# cd hanifx-v9

# python hanifx_v9.py

# python3 hanifx_v9.py



#----------------#
      USE():
from hanifx.enc.chain_layer import encode_pipeline, decode_pipeline

text = "Hello Hanif"
layers = ["base64", "xor", "caesar"]

encoded = encode_pipeline(text, layers)
print("Encoded:", encoded)

decoded = decode_pipeline(encoded, layers)
print("Decoded:", decoded)



MIT License

Copyright (c) 2025 Hanif

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
