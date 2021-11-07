#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import time
import threading
import tkinter as tk


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

  # StringVarを更新するように変更する
  def check_regno(self):
    """ for value in range(10):
      time.sleep(0.05)
      # StringVarを変更するとGUIスレッドでラベル文字列が更新される
      self.sv.set(str(value))
      # ラベルに表示されるだろう値を表示
      print(value) """
    self.regno_list.append("2626111222")
    self.sv_before.set(self.regno_list[-2])
    self.sv_new.set(self.regno_list[-1])
  
  def quit_gui(self):
    print("quit")
    self.root.destroy()


def main():
  gui = GUI()
  gui.start()

if __name__ == '__main__':
  main()
