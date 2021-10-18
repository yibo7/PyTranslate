import io
import os
import re
import traceback

from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QHeaderView, QAbstractItemView, \
    QTableWidget, QTableWidgetItem
import sys
from googletrans import Translator

from ui.tran_index import Ui_MainWindow


class IndexWindow(QMainWindow):

    def __init__(self):
        super(IndexWindow, self).__init__()
        self.ui = Ui_MainWindow()  # QUiLoader().load('index.ui') #Ui_MainWindow()
        self.ui.setupUi(self)
        tbColums = ['文件名称', '文件路径']
        # 设置列数
        self.ui.tb_datas.setColumnCount(len(tbColums))
        # 设置行数,一般会在读取到数据后再设置
        # self.ui.tb_datas.setRowCount(100)
        # 设置水平方向的表头标签与垂直方向上的表头标签，注意必须在初始化行列之后进行，否则，没有效果
        self.ui.tb_datas.setHorizontalHeaderLabels(tbColums)
        # 设置水平方向表格为自适应的伸缩模式
        # self.ui.tb_datas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tb_datas.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        # 禁止编辑
        self.ui.tb_datas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格整行选中
        self.ui.tb_datas.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 将行与列的高度设置为所显示的内容的宽度高度匹配
        QTableWidget.resizeColumnsToContents(self.ui.tb_datas)
        QTableWidget.resizeRowsToContents(self.ui.tb_datas)

        # 表格头的显示与隐藏
        # self.ui.tb_datas.verticalHeader().setVisible(False)
        # self.ui.tb_datas.horizontalHeader().setVisible(False)
    def save_file(self):
        txtHtml = self.ui.txt_rz.toPlainText()
        if self.current_sel_path != '':
            file = open(self.current_sel_path, mode='w', encoding="utf8")
            file.write(txtHtml)
            # 关闭打开的文件
            file.close()
        print("已保存:", self.current_sel_path)

    def tran_en(self):
        '''
        点击翻译后触发
        :return:
        '''
        # 设置Google翻译服务地址
        translator = Translator(service_urls=[
            'translate.google.cn'
        ])
        txtS = self.ui.txt_soure.toPlainText()
        # 提取字符串里的中文，返回数组
        pattern = "[\u4e00-\u9fa5]+"
        regex = re.compile(pattern)
        results = regex.findall(txtS)
        new_list = list(set(results))
        new_list.sort(key=lambda i: len(i), reverse=True)
        print(new_list)

        for kw in new_list:
            translation = translator.translate(kw, dest='en')  # dest='zh-CN'
            print(kw, ":", translation.text)
            txtS = txtS.replace(kw, translation.text)

        self.ui.txt_rz.setPlainText(txtS)

    def sel_folder(self):
        # file_path, _ = QFileDialog.getOpenFileName(self, "open file dialog", "", "Txt files(*.md)")
        file_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        self.ui.txt_folder_patch.setText(file_path)
        # file = open(file_path, mode='r', encoding="utf8")
        # data = file.read()
        # self.ui.txtSoure.setText(data)

    def seach_files(self):
        '''
        点击搜索文件时触发
        :return:
        '''
        self.ui.tb_datas.clearContents()  # 清空所有数据
        self.files.clear()
        sParentPath = self.ui.txt_folder_patch.text()
        self.scanFiles(sParentPath, ['.ftl'])
        if(len(self.files)) > 0:
            self.ui.tb_datas.setRowCount(len(self.files))
            itemIndex = 0
            for item in self.files:
                # self.testddd(item)
                fileName = os.path.basename(item)  # 带后缀的文件名
                self.ui.tb_datas.setItem(itemIndex, 0, QTableWidgetItem(fileName))
                self.ui.tb_datas.setItem(itemIndex, 1, QTableWidgetItem(item))
                itemIndex += 1

    def testddd(self, path):
        # file = open(path, mode='w', encoding="utf8")
        # file_content = file.read()  # data 是读取到的结果
        # 设置Google翻译服务地址
        translator = Translator(service_urls=[
            'translate.google.cn'
        ])
        with open(path, "r", encoding="utf-8") as fr:
            file_content = fr.read()  # data 是读取到的结果
            # 提取字符串里的中文，返回数组
            pattern = "[\u4e00-\u9fa5]+"
            regex = re.compile(pattern)
            results = regex.findall(file_content)
            new_list = list(set(results))
            new_list.sort(key=lambda i: len(i), reverse=True)
            print(new_list)

            for kw in new_list:
                translation = translator.translate(kw, dest='en')  # dest='zh-CN'
                print(kw, ":", translation.text)
                file_content = file_content.replace(kw, translation.text)

            with open(path, "w", encoding="utf-8") as fw:
                fw.write(file_content)
                print("已保存:", path)

    files = []
    current_sel_path = ''

    def scanFiles(self, path, fixs):
        '''
        扫描指定目录下的文件，可无限递归子目录
        :param path:指定目录
        :param fixs:指定只扫描的文件类型，数组类型, 比如 ['.txt', '.png']
        :return:
        '''
        parents = os.listdir(path)
        for parent in parents:
            child = os.path.join(path, parent)
            if os.path.isdir(child):
                self.scanFiles(child, fixs)
            else:
                if child[-4:] in fixs:
                    self.files.append(child)

    def openfile(self, row_index, col_index):
        '''
        双击列表控件时触发
        :param row_index: 双击双对应的索引
        :param col_index: 双击行对接的列表索引
        :return:
        '''
        self.current_sel_path = self.files[row_index]
        file = open(self.current_sel_path, mode='r', encoding="utf8")
        file_content = file.read()  # data 是读取到的结果
        # 赋值给源文本框
        self.ui.txt_soure.setPlainText(file_content)
        # 清空翻译结果的文本框
        self.ui.txt_rz.clear()
        file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('ui/logo.ico'))
    indexWin = IndexWindow()
    indexWin.show()

    sys.exit(app.exec())
