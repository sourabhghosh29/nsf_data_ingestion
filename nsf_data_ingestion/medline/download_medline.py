import os
import tarfile,sys
from shutil import copyfile
from shutil import rmtree
import sys
import tarfile
import shutil
import zipfile
from ftplib import FTP
from subprocess import call
import logging
import urllib
import calendar
import time

def download_pub_data(ftp_path):

   directory_path_data = '/home/ananth/data/'
   timestamp_file = 'time_stamp.txt'
   
   if os.path.exists(directory_path_data):
     if os.path.exists(directory_path_data+'time_stamp.txt'):
       f = open(directory_path_data+"time_stamp.txt", "r")
       old_time_stamp = int(f.read())
       current_time_stamp = calendar.timegm(time.gmtime())
       f.close()
       if current_time_stamp - old_time_stamp > 300:
         rmtree(directory_path_data)
         os.makedirs(directory_path_data)
     else:
       rmtree(directory_path_data)
   else:
     os.makedirs(directory_path_data)
   
   ftp = FTP('ftp.nlm.nih.gov')
   ftp.login(user='', passwd = '')
   ftp.cwd(ftp_path)
   files = ftp.nlst()

   for file in files:
    if file.endswith('.xml.gz'):
     localfile = open(directory_path_data+file, 'wb')
     ftp.retrbinary("RETR " + file ,localfile.write)
     logging.info('Downloading Pleae Wait.................')
   ftp.quit()
   localfile.close()
   if not os.path.exists(directory_path_data+'time_stamp.txt'):
     f = open(directory_path_data+"time_stamp.txt", "a")
     cur_time = calendar.timegm(time.gmtime())
     f.write(str(cur_time))
     f.close()


def persist(hdfs_path, directory_path_data):
 logging.info('Persisting data to HDFS')
 if not call(["hdfs","dfs", "-test", "-d", hdfs_path]):
   call(["hdfs","dfs", "-rm", "-r", "-f",  hdfs_path])
 
 call(["hdfs","dfs", "-mkdir", hdfs_path])
 call(["hdfs","dfs", "-put", directory_path_data, hdfs_path])
 logging.info('Files Persisted to - %s', hdfs_path)

