#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import time
import csv
import datetime
import threading
import binascii
import nfc
import tkinter as tk

# 学生証のサービスコード
service_code = 0x010B


class GUI(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.value = 0
    self.quit_flag = False
  
  def start(self):
    self.root = tk.Tk()
    self.root.title(u"Check RegNo.")
    self.root.geometry("400x150")

    self.regno_list = [[0,""], [0,""]]

    # StringVarをフィールドに定義する
    self.sv_before = tk.StringVar()
    self.sv_before.set(self.regno_list[-2][1])

    self.sv_new = tk.StringVar()
    self.sv_new.set(self.regno_list[-1][1])

    # ラベルの表示 データはStringVarをバインドする
    self.label_before = tk.Label(self.root, textvariable=self.sv_before, fg="#c5c5c5", font=("Arial", "30", "bold"))
    self.label_before.pack()

    self.label_new = tk.Label(self.root, textvariable=self.sv_new, font=("Arial", "40", "bold"))
    self.label_new.pack()

    # ボタンの表示
    self.button = tk.Button(self.root, text='Save & Quit', command=self.quit_gui)
    self.button.pack()
    self.check_regno_callback()
    self.root.mainloop()

  # 別スレッドで実行するコールバック
  def check_regno_callback(self):
    th = threading.Thread(target=self.check_regno, args=(), daemon=True)
    th.start()

  def on_connect_nfc(self, tag):
    # nfcタグ読み取り  
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
      try:
        sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,service_code & 0x3f)
        bc = nfc.tag.tt3.BlockCode(0,service=0)
        data = tag.read_without_encryption([sc],[bc])
        sid = data[2:12]
        regno = sid.decode()
        
        print(regno)
        if(regno not in [r[1] for r in self.regno_list[2:]]):
          now = datetime.datetime.now()
          self.regno_list.append([now,regno])
          self.sv_before.set(self.regno_list[-2][1])
          self.sv_new.set(self.regno_list[-1][1])
          
      except Exception as e:
        print ("error: %s" % e)
    else:
      print ("error: tag isn't Type3Tag")

  # 
  def check_regno(self):
    clf = nfc.ContactlessFrontend('usb')
    while not(self.quit_flag):
      clf.connect(rdwr={'on-connect': self.on_connect_nfc})
      time.sleep(2)  # 読み取り間隔
    
  
  def quit_gui(self):
    self.quit_flag = True
    self.root.destroy()


def save_csv(regno_list):
  now = datetime.datetime.now()
  filename = '../output/log_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'
  # str_regno = '\n'.join(regno_list[2:])
  with open(filename, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    #f.write(str_regno)
    regno_list = sorted(regno_list[2:], key=lambda x: x[1])
    print(regno_list)
    writer.writerows(regno_list)
  print ("saved csv")

def main():
  gui = GUI()
  gui.start()
  save_csv(gui.regno_list)
  sys.exit()
  

if __name__ == '__main__':
  main()
