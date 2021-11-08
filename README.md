# Check RegNo with NFC
学生証をNFCリーダーで読み取り学籍番号を確認する。


## 準備
### 1. Zadigのインストール
[Zadig](https://zadig.akeo.ie/)

- [Zadig](https://zadig.akeo.ie/)をダウンロード
- RC-S380を接続してドライバが適用されるのを待つ
- Zadigを起動
- `Options -> List All Devices`を選択
- リストから利用するNFCデバイスを選択（今回はRC-S380）
- Driverの欄は`WinUSB`
- `Replace Driver`をクリック


### 2. libusbの導入
[libsub](https://libusb.info/)

- [libusb](https://github.com/libusb/libusb/releases)(`Downloads -> Latest Windows Binaries`)からダウンロード
- 7Zipで解凍
- 64ビット版Windowsの場合
  - `MS64\dll\libusb-1.0.dll` を `C:\Windows\System32` にコピー
  - `MS32\dll\libusb-1.0.dll` を `C:\Windows\SysWOW64` にコピー
- 32ビット版Windowsの場合
  - `MS32\dll\libusb-1.0.dll` を `C:\Windows\System32` にコピー


### 3. nfcpyの導入
[nfcpy](https://nfcpy.readthedocs.io/en/latest/topics/get-started.html)
```python
$ pip install -U nfcpy
```
## 参考
- [nfcpy: Getting started](https://nfcpy.readthedocs.io/en/latest/topics/get-started.html)
- [Python3でnfcpy](https://qiita.com/Electro35/items/9a220c005f6b3a78131d)
- [nfcpyを使って学生証から学籍番号を読み取る](https://aizu-vr.hatenablog.com/entry/2019/08/02/nfcpy%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E5%AD%A6%E7%94%9F%E8%A8%BC%E3%81%8B%E3%82%89%E5%AD%A6%E7%B1%8D%E7%95%AA%E5%8F%B7%E3%82%92%E8%AA%AD%E3%81%BF%E5%8F%96%E3%82%8B)
