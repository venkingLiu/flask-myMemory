# -*- coding: utf-8 -*-
__author__ = 'venking'
import MySQLdb

class BlobDataTestor:
    def __init__(self):
        self.conn=MySQLdb.connect(host='localhost',user='root',passwd='liuwj',db='0')


    def __def__(self):
        try:
            self.conn.close()
        except:
            pass


    def closedb(self):
        self.conn.close()


    def setup(self):
        cursor = self.conn.cursor()
        cursor.execute( """
            CREATE TABLE IF NOT EXISTS `Dem_Picture` (
            `ID` int(11) NOT NULL auto_increment,
            `PicData` mediumblob,
            PRIMARY KEY (`ID`)
            ) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;
            """)
        cursor.commit()



    def teardown(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute( "Drop Table Dem_Picture" )
        except:
            pass
        # self.conn.commit()

    def testRWBlobData(self):
    # 读取源图片数据
        f = open( "C:\\11.jpg" , "rb" )
        b = f.read()
        f.close()

    # 将图片数据写入表
        cursor = self.conn.cursor()
        cursor.execute( "INSERT INTO Dem_Picture (PicData) VALUES (%s)", (MySQLdb.Binary(b)))
    # self.conn.commit()

    # 读取表内图片数据，并写入硬盘文件
        cursor.execute( "SELECT PicData FROM Dem_Picture ORDER BY ID DESC limit 1" )
        d = cursor.fetchone()[0]
        cursor.close()

        f = open( "C:\\22.jpg" , "wb" )
        f.write(d)
        f.close()

# 下面一句的作用是：运行本程序文件时执行什么操作
if __name__ == "__main__":

    test = BlobDataTestor()

    try:
        test.setup()
        test.testRWBlobData()
        test.teardown()
    finally:
        test.closedb()