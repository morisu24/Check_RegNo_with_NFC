# Check_RegNo_with_NFC

# 参考
https://qiita.com/Electro35/items/9a220c005f6b3a78131d

# 準備
## 1.libusbの導入
- [github](https://github.com/libusb/libusb/releases)からダウンロード
- 解凍後
  - 64ビット版Windowsの場合
    - `MS64\dll\libusb-1.0.dll` を `C:\Windows\System32` にコピー
    - `MS32\dll\libusb-1.0.dll` を `C:\Windows\SysWOW64` にコピー
  
  - 32ビット版Windowsの場合
    - `MS32\dll\libusb-1.0.dll` を `C:\Windows\System32` にコピー

## 2.Zadigのインストール
- [Zadigのサイト](https://zadig.akeo.ie/)からインストール
- RC-S380を刺してドライバが適用させるのを待つ
- Zadigを起動
- リストボックスからRC-S380を選択（見つからない場合は`Options -> List All Devices`）
- Driverの欄は`WinUSB`
- `Replace Driver`をクリック

## 3.nfcpyの導入
[nfcpy公式](https://nfcpy.readthedocs.io/en/latest/topics/get-started.html)
```python
$ pip install nfcpy
```
