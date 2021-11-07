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
  
  def start(self):
    self.root = tk.Tk()
    self.root.title(u"Check RegNo.")
    self.root.geometry("400x150")

    self.regno_list = ["2720111222","2516111222"]

    # StringVarをフィールドに定義する
    self.sv_before = tk.StringVar()
    self.sv_before.set(self.regno_list[-2])

    self.sv_new = tk.StringVar()
    self.sv_new.set(self.regno_list[-1])

    # ラベルの表示 データはStringVarをバインドする
    self.label_before = tk.Label(self.root, textvariable=self.sv_before, fg="#c5c5c5", font=("Arial", "30", "bold"))
    self.label_before.pack()

    self.label_new = tk.Label(self.root, textvariable=self.sv_new, font=("Arial", "30", "bold"))
    self.label_new.pack()

    # ボタンの表示
    self.button = tk.Button(self.root, text='Click to Quit', command=self.quit_gui)
    self.button.pack()
    self.check_regno_callback()
    self.root.mainloop()

  # 別スレッドで実行するコールバック
  def check_regno_callback(self):
    th = threading.Thread(target=self.check_regno, args=())
    th.start()

  def on_connect_nfc(self, tag):
    # タグのIDなどを出力する
    # print tag
    
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
      try:
          sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,service_code & 0x3f)
          bc = nfc.tag.tt3.BlockCode(0,service=0)
          data = tag.read_without_encryption([sc],[bc])
          sid = data[2:12]
          regno = sid.decode()
          # print (sid)
          self.sv_before.set(self.regno_list[-2])
          self.sv_new.set(self.regno_list[-1])
          
      except Exception as e:
        print ("error: %s" % e)
    else:
      print ("error: tag isn't Type3Tag")

  # 
  def check_regno(self):
    self.regno_list.append("2626111222")
    clf = nfc.ContactlessFrontend('usb')
    while True:
      clf.connect(rdwr={'on-connect': self.on_connect_nfc})
      time.sleep(1)
    
  
  def quit_gui(self):
    print("quit")
    self.root.destroy()


def save_csv(regno_list):
  now = datetime.datetime.now()
  filename = '../output/log_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'
  str_regno = '\n'.join(regno_list)
  with open(filename, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    f.write(str_regno)
    

def main():
  gui = GUI()
  gui.start()
  save_csv(gui.regno_list)
  

if __name__ == '__main__':
  main()
