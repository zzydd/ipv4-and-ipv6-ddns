import os
import re
import time
import requests
import datetime
os.popen('title IPv4+IPv6动态域名解析工具')

#【获取时间】
def GetTime():
    Now = datetime.datetime.now()
    DateTime = Now.strftime("%Y.%m.%d-%H:%M:%S")
    return DateTime

#【日志模块】
def WriteLog(LogData):
    
    #格式化
    LogData = str(LogData)
    #获取时间
    DateTime = GetTime()
    DateTimeList = DateTime.split('-')

    #输出
    if OutputTime=='True':
        
        if LogData=='\n' or LogData=='':
            print('')
        else:        
            print('['+DateTime+'] - '+LogData)
    else:
        print(LogData)

    
    #创建目录
    LogPath = ('程序数据/日志/'+str(DateTimeList[0].replace('.','-')))
    try:
        os.makedirs(LogPath)
    except:
        pass
    
    #写入日志
    if Recording=='True':
        if LogData=='\n' or LogData=='':
            with open (LogPath+'/程序日志'+str(DateTimeList[0])+'.log','a') as file:
                file.write('\n')
        else:        
            with open (LogPath+'/程序日志'+str(DateTimeList[0])+'.log','a') as file:
                file.write('['+DateTime+'] - '+LogData+'\n')
    else:
        #日志记录未启用
        pass


#【获取公网IPv4】
def Get_IPv4():
    try:
        #发送请求
        Response = requests.get('https://myip.ipip.net') #发送请求
        ReturnText = Response.text #返回文本
        ReturnText = ReturnText.replace('\n','')

        #处理数据
        Format = (r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}') #IPv4地址格式
        Match = re.search(Format, ReturnText)
        if Match:
            IPv4 = Match.group()
        else:
            IPv4 = ('127.0.0.1')
    except Exception as ErrorMsg:
        IPv4 = ('127.0.0.1')
        ReturnText = ('Null')
        WriteLog('[IPv4获取程序]-[警告]-请求失败：'+str(ErrorMsg))

    #返回数据
    WriteLog('[IPv4获取程序]-当前IPv4属地：'+str(ReturnText))
    WriteLog('[IPv4获取程序]-返回IPv4地址：'+str(IPv4))
    return(IPv4)


#【获取公网IPv6】
def Get_IPv6():
    try:
        #执行命令
        ReturnText = os.popen('ipconfig /all').read()

        #处理数据
        Format = (r'(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})') #IPv6地址格式
        Match = re.search(Format, ReturnText)
        if Match:
            IPv6 = Match.group()
        else:
            IPv6 = ('None')
    except Exception as ErrorMsg:
        IPv6 = ('')
        WriteLog('[IPv6获取程序]-[警告]-获取失败：'+str(ErrorMsg))

    #返回数据
    WriteLog('[IPv6获取程序]-返回IPv6地址：'+str(IPv6))
    return(IPv6)



#【更新IPv4解析记录】
def UpdateDNS_IPv4(Domain, Token, Records):

    #发送请求
    try:
        WriteLog('[IPv4更新程序]-发起请求')
        URL = ('http://dynv6.com/api/update?hostname='+Domain+'&token='+Token+'&ipv4='+Records)#API接口地址
        Response = requests.get(URL) #发送请求
        RetuenCode = Response.status_code #返回代码
        ReturnText = Response.text #返回文本
    except Exception as ErrorMsg:
        WriteLog('[IPv4更新程序]-[警告]-请求失败：'+str(ErrorMsg))
        ReturnText = ('Null')
        RetuenCode = ('Null')
        pass

    #判断结果
    if RetuenCode==200:
        Result = ('更新成功！code:'+str(RetuenCode)+' ; '+str(ReturnText))
        
    elif RetuenCode==401:
        Result = ('更新失败！密钥无效！请检查密钥是否正确！code:'+str(RetuenCode)+' ; '+str(ReturnText))
        
    elif RetuenCode==404:
        Result = ('更新失败！地址不存在！请检查域名和密钥是否正确！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    elif RetuenCode==422:
        Result = ('更新失败！地址格式错误！请检查记录值是否正确！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    elif RetuenCode==403:
        Result = ('更新失败！网站拒绝访问！请检查权限！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    elif RetuenCode==503:
        Result = ('更新失败！无法访问网站！请稍后再试！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    else:
        Result = ('更新失败！未知错误！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    #返回结果
    WriteLog('[IPv4更新程序]-'+str(Result))
    return(Result)


#【更新IPv6解析记录】
def UpdateDNS_IPv6(Domain, Token, Records, Prefix):

    #发送请求
    try:
        WriteLog('[IPv6更新程序]-发起请求')
        URL = ('http://dynv6.com/api/update?hostname='+Domain+'&token='+Token+'&ipv6='+Records+'&ipv6prefix='+Prefix)#API接口地址
        Response = requests.get(URL) #发送请求
        RetuenCode = Response.status_code #返回代码
        ReturnText = Response.text #返回文本
    except Exception as ErrorMsg:
        WriteLog('[IPv6更新程序]-[警告]-请求失败：'+str(ErrorMsg))
        ReturnText = ('Null')
        RetuenCode = ('Null')
        pass

    #判断结果
    if RetuenCode==200:
        Result = ('更新成功！code:'+str(RetuenCode)+' ; '+str(ReturnText))
        
    elif RetuenCode==401:
        Result = ('更新失败！密钥无效！请检查密钥是否正确！code:'+str(RetuenCode)+' ; '+str(ReturnText))
        
    elif RetuenCode==404:
        Result = ('更新失败！地址不存在！请检查域名和密钥是否正确！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    elif RetuenCode==422:
        Result = ('更新失败！地址格式错误！请检查记录值是否正确！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    elif RetuenCode==403:
        Result = ('更新失败！网站拒绝访问！请检查权限！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    elif RetuenCode==503:
        Result = ('更新失败！无法访问网站！请稍后再试！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    else:
        Result = ('更新失败！未知错误！code:'+str(RetuenCode)+' ; '+str(ReturnText))

    #返回结果
    WriteLog('[IPv6更新程序]-'+str(Result))
    return(Result)


#【读取更新列表】
def Read_UpdateFile():
    
    #读取列表
    with open ('更新列表.ini','r',encoding='utf-8') as file:
        FileData = file.read()
    FileData = FileData.replace('[','')
    FileData = FileData.replace(']','')
    FileData = FileData.replace(' ','')
    UpdateList = FileData.split('\n')

    #删除注释和空元素
    UpdateList = [line for line in UpdateList if not line.startswith('#') and line.strip() != '']
        
    #返回列表
    return(UpdateList)
    




#【读取配置文件】

#创建文件夹
try:
    os.makedirs('程序数据')
except:
    pass

#检测文件
check = os.path.exists('配置文件.ini') #配置文件
if check==False:
    with open ('配置文件.ini','w',encoding='utf-8') as file:
        file.write('启用IPv4：True\n')
        file.write('启用IPv6：True\n')
        file.write('自动获取：True\n')
        file.write('更新时间：600\n')
        file.write('日志记录：True\n')
        file.write('输出时间：False\n')
else:
    pass

check = os.path.exists('更新列表.ini') #更新列表
if check==False:
    with open ('更新列表.ini','w',encoding='utf-8') as file:
        file.write("# 格式：[域名,密钥, IPv4记录, IPv6记录, IPv6前缀, 更新项]\n\n")
        file.write("# 域名：用于解析的完整域名，如'ddns.example.cn'\n")
        file.write("# 密钥：一串随机字符，一般在password/Token后面，共用密钥填相同'\n")
        file.write("# IPv4记录：手动设置用于解析的IPv4地址，自动获取模式忽略\n")
        file.write("# IPv6记录：手动设置用于解析的IPv6地址，自动获取模式忽略\n")
        file.write("# IPv6前缀：自己百科，填不填无所谓，实测无影响，最好还是填一下\n")
        file.write("# 更新项：4:仅更新IPv4，6:仅更新IPv6，46或留空:更新IPv4+IPv6\n\n")  
        file.write("[example.cn, 1a2b3c4d5e114514abcde, 192.168.1.1, fe80::1a2b3c:2233:1145:aabb, fe80:abc:1919:810::/60, 46]\n")
else:
    pass
        

#读取配置文件
with open ('配置文件.ini','r',encoding='utf-8') as file:
    FileData = file.read()
    
FileData = FileData.replace(' ','') 
SetList = FileData.split('\n')

EnableIPv4 = (SetList[0]).replace('启用IPv4：','')
EnableIPv6 = (SetList[1]).replace('启用IPv6：','')
EnableAuto = (SetList[2]).replace('自动获取：','')
UpdateTime = (SetList[3]).replace('更新时间：','')
UpdateTime = int(UpdateTime)

Recording = (SetList[4]).replace('日志记录：','')
OutputTime = (SetList[5]).replace('输出时间：','')

WriteLog('')
WriteLog('【程序准备就绪】')
print('')
WriteLog('[主程序]-配置文件：'+str(SetList))
WriteLog('')



#【主程序】

while True:

    WriteLog('[主程序]-开始运行')

    #【自动获取】
    if EnableAuto=='True':

        #【检测IP变化】

        WriteLog('[主程序]-正在检测IP变化')
        
        #IPv4检测
        if EnableIPv4=='True':

            #获取新IPv4地址
            IPv4 = Get_IPv4()
            WriteLog('[主程序]-当前IPv4地址：'+IPv4)

            #获取老IPv4地址
            try:
                with open('程序数据/IPv4.old.zzydd','r',encoding='utf-8') as file:
                    IPv4_old = file.read()
                WriteLog('[主程序]-上次IPv4地址：'+IPv4_old)
            except:
                IPv4_old = ('0.0.0.0')
                WriteLog('[主程序]-[警告]-未读取到IPv4历史记录')

            #变化判断
            if IPv4 != IPv4_old:
                IPv4_Change = True
                WriteLog('[主程序]-IPv4地址改变')
            else:
                IPv4_Change = False
                WriteLog('[主程序]-IPv4地址未改变')

            #更新文件记录
            with open('程序数据/IPv4.old.zzydd','w',encoding='utf-8') as file:
                file.write(IPv4)
        else:
            WriteLog('[主程序]-IPv4更新未启用')
            IPv4_Change = False
            pass


        #IPv6检测
        if EnableIPv6=='True':

            #获取新IPv6地址
            IPv6 = Get_IPv6()
            WriteLog('[主程序]-当前IPv6地址：'+IPv6)

            #获取老IPv6地址
            try:
                with open('程序数据/IPv6.old.zzydd','r',encoding='utf-8') as file:
                    IPv6_old = file.read()
                WriteLog('[主程序]-上次IPv6地址：'+IPv6_old)
            except:
                IPv6_old = ('::1')
                WriteLog('[主程序]-[警告]-未读取到IPv6历史记录')

            #变化判断
            if IPv6 != IPv6_old:
                IPv6_Change = True
                WriteLog('[主程序]-IPv6地址改变')
            else:
                IPv6_Change = False
                WriteLog('[主程序]-IPv6地址未改变')

            #更新文件记录
            with open('程序数据/IPv6.old.zzydd','w',encoding='utf-8') as file:
                file.write(IPv6)
        else:
            WriteLog('[主程序]-IPv6更新未启用')
            IPv6_Change = False
            pass
    

        #【判断变化】
        if IPv4_Change==True or IPv6_Change==True: #IP发生变化，运行更新程序

            #【更新记录】
            print('')
            WriteLog('[主程序]-地址改变，准备更新记录')

            #读取更新列表
            UpdateList = Read_UpdateFile()

            #遍历列表
            for UpdateListData in UpdateList:

                #读取数据
                WriteLog('[主程序]-读取更新列表：'+str(UpdateListData))
                DataList = UpdateListData.split(',') #数据列表
                Domain = DataList[0] #域名
                Token = DataList[1] #密钥
                IPv6_Prefix = DataList[4] #IPv6后缀
                Mode = DataList[5] #更新模式
                if Mode=='':
                    Mode=('46')

                #更新IPv4
                if EnableIPv4=='True' and (Mode=='4' or Mode=='46'):
                    WriteLog('[主程序]-正在更新IPv4地址')
                    UpdateDNS_IPv4(Domain, Token, IPv4)
                    time.sleep(0.5)
                    WriteLog('[主程序]-IPv4地址更新完成')
                else:
                    WriteLog('[主程序]-IPv4更新未启用')
                    pass

                #更新IPv6
                if EnableIPv4=='True' and (Mode=='6' or Mode=='46'):
                    WriteLog('[主程序]-正在更新IPv6地址')
                    UpdateDNS_IPv6(Domain, Token, IPv6, IPv6_Prefix)
                    time.sleep(0.5)
                    WriteLog('[主程序]-IPv6地址更新完成')
                else:
                    WriteLog('[主程序]-IPv6更新未启用')
                    pass
        else:
            WriteLog('[主程序]-地址均未改变，无需更新')
            pass



    #【手动设置】
    else:

        WriteLog('[主程序]-手动更新，正在读取更新列表')

        #读取更新列表
        UpdateList = Read_UpdateFile()
        
        #遍历列表
        for UpdateListData in UpdateList:

            WriteLog('[主程序]-更新列表：'+str(UpdateListData))

            #读取数据
            DataList = UpdateListData.split(',') #数据列表
            Domain = DataList[0] #域名
            Token = DataList[1] #密钥
            IPv4 = DataList[2]  #IPv4
            IPv6 = DataList[3]  #IPv6
            IPv6_Prefix = DataList[4] #IPv6后缀
            Mode = DataList[5] #更新模式
            if Mode=='':
                Mode=('46')

            #更新IPv4
            if EnableIPv4=='True' and (Mode=='4' or Mode=='46'):
                WriteLog('[主程序]-正在更新IPv4地址')
                UpdateDNS_IPv4(Domain, Token, IPv4)
                time.sleep(0.5)
                WriteLog('[主程序]-IPv4地址更新完成')
            else:
                WriteLog('[主程序]-IPv4更新未启用')
                pass

            #更新IPv6
            if EnableIPv4=='True' and (Mode=='6' or Mode=='46'):
                WriteLog('[主程序]-正在更新IPv6地址')
                UpdateDNS_IPv6(Domain, Token, IPv6, IPv6_Prefix)
                time.sleep(0.5)
                WriteLog('[主程序]-IPv6地址更新完成')
            else:
                WriteLog('[主程序]-IPv6更新未启用')
                pass


    #【检测延时】
    WriteLog('[主程序]-运行结束，程序挂起')
    WriteLog('')
    time.sleep(UpdateTime)


        
        


























