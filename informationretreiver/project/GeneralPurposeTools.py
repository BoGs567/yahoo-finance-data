import re
import certifi
import urllib3
from bs4 import BeautifulSoup
import datetime
import glob
import os
#-------------------------------------------------#

def GetDownloadsPath():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        from pathlib import Path
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        return path_to_download_folder

def RemoveHTMLTags(text, \
                   separator=''):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, separator, text)

def GetPageHTML(requestType, \
                infoPage, \
                parseType):
    page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request(requestType, info_page)
    soup = BeautifulSoup(page.data, 'html.parser')
    return soup

def StandardDateFromAmericanFormat(AmericanFormatedDate, \
                                   inputFormat = '%b %d, %Y', \
                                   outPutFormat = '%Y-%m-%d' ):
    return datetime.datetime.strptime(AmericanFormatedDate,inputFormat).strftime(outPutFormat)

def GetDownloadsFolderPath():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        from pathlib import Path
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        return path_to_download_folder

def RetreiveFilteredFolderFilesList(folderPath, \
                                    fileEnding = '*', \
                                    filterString = ''):
    files = glob.glob(GetDownloadsPath() + fileEnding)
    filteredFilesList = []
    for file_ in files:
        if filterString in file_:
            filteredFilesList.append(file_)
    return filteredFilesList 

def RetreiveLatestFilePathFromDownloadsDirectory():
    list_of_files = glob.glob(GetDownloadsPath() + '/*.csv')
    latest_downloaded_file_path = max(list_of_files, key=os.path.getctime)
    filePath = latest_downloaded_file_path

def RemoveFileWithPath(filePath):
    os.remove(filePath)

def ListRemoveFalsy(listInput):
    list_ = []
    for listItem in listInput:
        if listItem:
            list_.append(listItem)
    return list_

def ListRemoveUnsupportedDataTypes(listInput, behaviourFuncs):
    list_ = []
    for listItem in listInput:
        for key, func in behaviourFuncs.items():
            value, behaviorString = func(listItem)
            if behaviorString:
                print(value, behaviorString)
                list_.append(value)
                break
    return list_

#Rewrite this: should be able to find date format from date as string.
def DateFormatFromDateString(dateString):
    format = None
    if dateString.count('/') == 2:
        format = '%m/%d/%Y'
    return format

def CleanHeaders(headers):
    headers_ = []
    for header in headers:
        header = header.replace('*', '')
        subwords = header.split(' ')
        if all(subword.isalpha() for subword in subwords):
            headers_.append(header)
    return headers_
