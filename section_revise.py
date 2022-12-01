"""
!/usr/bin/env python 3.9
-*- coding: utf-8 -*-
@File  : CCTVtrans.py
@Author: GinaChou
@Date  : 2022/12/01
"""
import os
import xml.etree.ElementTree as ET

###########修改XML ################
#通過Element物件的方法修改Element物件
#使用ElementTree，先將文件讀入，解析成樹
#根據路徑，定位到樹的每個節點，再對節點進行修改，最後直接將其輸出


def file_exist_or_not(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return

def read_xml(in_path):
    '''讀取並解析xml文件
       in_path: xml路徑
       return: ElementTree'''
    tree = ET.parse(in_path)
    return tree


def write_xml(tree, out_path):
    '''將xml文件寫出
       tree: xml樹
       out_path: 寫出路徑'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)

def change_one_xml(xml_path, xml_dw, update_content):
    # 打開xml文檔
    doc = ET.parse(xml_path)
    root = doc.getroot()
    # 查找修改路勁
    sub1 = root.find(xml_dw)
    # 修改標籤內容
    # sub1.text = update_content
    sub1.set("roadsection", update_content)
    # # 保存修改
    # doc.write(xml_path)

# https://blog.51cto.com/u_12386780/5479899


if __name__ == "__main__":
    # 1. 讀取xml文件
    path = os.getcwd()
    xml= "roadlevel_info_0000.xml"
    xml_file = os.path.join(path, xml)
    tree = read_xml(xml_file)
    root = tree.getroot()

    # 修改文件中的xpath定位
    xml_dw = './/Info[@routeid="nfb0001"]'

    # 想要修改成什麼內容
    update_content = "國道1號"

    # 查找修改路勁
    sub1 = root.find(xml_dw)
    # 修改標籤內容
    sub1.text = update_content
    write_xml(tree, "out.xml")
    # write_xml(tree, "road/out.xml")

    # # 保存修改
    # doc.write(xml_path)

    # # 2. 屬性修改
    # sub1 = root.find("sub1")  # 修改sub1的name属性
    # sub1.set("name", "New Name")roadsection


    # # 6. 輸出到結果文件
    # write_xml(tree, "venv/out.xml")

    print(f"TREE:{tree}")
