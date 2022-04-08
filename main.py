import os
from PySide6.QtWidgets import QApplication, QMainWindow,  QHeaderView, QAbstractItemView, \
    QTableWidget, QTableWidgetItem
import sys
from XsCore import XsStrings, XsRegexUtils, XsDialogs
from XsCore.XsFso import FileUtils, XsFileList
from googletrans import Translator

from src.TranslateUtils import autoTran
from ui.tran_index import Ui_MainWindow


class IndexWindow(QMainWindow):
    files = []
    current_sel_path = ''
    isChange = False # 搜索到文件后是否同时翻译

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
        if txtHtml.strip() == '':
            XsDialogs.showInfo('没有可保存的内容！')
            return
        FileUtils.writeFile(self.current_sel_path, txtHtml)
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
        pattern = r"[\u4e00-\u9fa5]+"
        results = XsRegexUtils.FindStrToList(pattern, txtS)

        if results is None:
            XsDialogs.showInfo('没有得取到中文')
            return

        new_list = list(set(results))

        new_list.sort(key=lambda i: len(i), reverse=True)
        print(new_list)

        for kw in new_list:
            translation = translator.translate(kw, dest='en')  # dest='zh-CN'
            print(kw, ":", translation.text)
            txtS = txtS.replace(kw, translation.text)

        self.ui.txt_rz.setPlainText(txtS)

    def sel_folder(self):
        file_path = XsDialogs.askOpenFolder()  # QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        self.ui.txt_folder_patch.setText(file_path)

    currentItemCount = 0

    def __callBackFile(self, src):
        if src == '--end--':
            self.ui.btnSearchFiles.setEnabled(True)
            self.ui.btnSearchFiles.setText("搜索文件")
            return
        self.files.append(src)  # 方便读取，所以保存
        self.ui.tb_datas.setRowCount(self.currentItemCount + 1)
        fileName = os.path.basename(src)  # 带后缀的文件名
        # 往列表添加一行
        self.ui.tb_datas.setItem(self.currentItemCount, 0, QTableWidgetItem(fileName))
        self.ui.tb_datas.setItem(self.currentItemCount, 1, QTableWidgetItem(src))
        self.currentItemCount += 1
        if self.isChange :
            autoTran(src)

    def seach_files(self):
        '''
        点击搜索文件时触发
        :return:
        '''
        self.ui.tb_datas.clearContents()  # 清空所有数据
        self.files.clear()
        sParentPath = self.ui.txt_folder_patch.text().strip()
        if sParentPath == '':
            XsDialogs.showInfo('请选择一个正确的目录')
            return

        hz = self.ui.txtHz.text().strip()
        if hz == '':
            XsDialogs.showInfo("请输入至少一个文件后缀，多个用逗号分开")
            return

        self.isChange = self.ui.cbIsFy.isChecked()

        if self.isChange :
            isck = XsDialogs.askAskYesNo("您选择了翻译意味着搜索到文件的同时会覆盖成翻译后的文件，请确认你已经做好了原文件的备份了吗？")
            if isck is False:
                return

        self.ui.btnSearchFiles.setEnabled(False)
        self.ui.btnSearchFiles.setText("搜索中..")
        self.currentItemCount = 0
        xsFl = XsFileList(sParentPath, XsStrings.split(hz, ","))
        xsFl.getSubFilesAsync(self.__callBackFile)

    def openfile(self, row_index, col_index):
        '''
        双击列表控件时触发
        :param row_index: 双击双对应的索引
        :param col_index: 双击行对接的列表索引
        :return:
        '''
        self.current_sel_path = self.files[row_index]
        file_content = FileUtils.readFileAnyCode(self.current_sel_path)  # file.read()  # data 是读取到的结果
        # 赋值给源文本框
        self.ui.txt_soure.setPlainText(file_content)
        # 清空翻译结果的文本框
        self.ui.txt_rz.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('ui/logo.ico'))
    indexWin = IndexWindow()
    indexWin.show()

    sys.exit(app.exec())
