# IPv4 + IPv6 DDNS 工具

> 这是一个简单的python脚本，通过dynv6的DDNS服务为你的主机提供动态域名解析

## 项目简介

**功能与原理**

动态域名解析(DDNS工具)，支持IPv4和IPv6，其原理是定期获取你电脑的公网IP，并通过dynv6的DDNS服务A自动上传更新DNS解析记录。

程序支持将记录同步到多个不同密钥的多个地址，并且可以分开设置使用IPv4记录(A)还是IPv6记录(AAAA),当然，你也可以同时使用。

**程序特点**

▪️ 支持IPv6，没有公网IPv4也能用

▪️ 无需设置路由器上的DDNS

▪️ 不需要实名认证，只需要一个能用的邮箱

## 使用方法

**步骤1**

首先你要有dynv6账号，你可以去他们官网[dynv6.com](https://dynv6.com)注册一个。

注册完成后添加你要用于DDNS的域名并记住系统分发的密钥(token)。

> 中国大陆地区的同志注意一下，该网站不需要梯子，可以正常访问，但验证账号用的是谷歌验证，所以还是建议打开梯子，没有梯子的可以用游戏加速器替代。

**步骤2**

打开文件"更新列表.ini"，根据提示把你的域名和密钥按照要求填写进去。

如果没有，先运行一遍程序，首次运行会自动创建.

**步骤3**

填写完成后直接运行程序即可，你也可以把它添加进系统任务

如果程序没有提示错误，那多半成了。你可以再去dynv6上检查一下

如果有你的解析记录，那就可以使用了，当然，我还是建议你了解一下所有设置。

## 配置文件.ini，文件说明

##### 这个文件控制全局设置，它有下面这几个项，现在我们来了解一下它吧！**

1：启用IPv4，(默认值:True)，控制全局是否启用IPv4地址DDNS，强烈建议开启，因为下面还有一个选项可以更加细致地选择模式

2：启用IPv6，(默认值:True)，控制全局是否启用IPv6地址DDNS，强烈建议开启，因为下面还有一个选项可以更加细致地选择模式

3：自动获取，(默认值:True)，控制全局是否自动获取IPv4和IPv6地址，强烈建议开启，因为不自动获取你为啥还要DDNS？

4：更新时间，(默认值:600)，程序每次重新获取地址并更新的时间，单位秒，建议设置在600-1200

5：日志记录，(默认值:True)，正如它所说，是否开启日志记录

6：输出时间，(默认值:False)，是否在控制台输出的消息前面添加时间

## 更新列表.ini，文件说明

**这个文件用于记录你的解析地址和密钥，你可以添加多行记录，用于将IP地址同步到多个地址。并且每条记录都可以使用独立的密钥，并且可以独立控制使用IPv4记录还是IPv6记录。下面让我们来详细地看一下。**


### 格式：[域名,密钥, IPv4记录, IPv6记录, IPv6前缀, 更新项]

**格式非常重要，请严格按照格式来填写数据！！！**


### 参数详解

**域名：**用于解析的完整域名，如'ddns.example.cn'

**密钥：**一串随机字符，一般在password/Token后面'

**IPv4记录：**手动设置用于解析的IPv4地址，自动获取模式忽略

**IPv6记录：**手动设置用于解析的IPv6地址，自动获取模式忽略

**IPv6前缀：**自己百科，填不填无所谓，实测无影响，最好还是填一下

**更新项：**4-仅更新IPv4，6-仅更新IPv6，46或留空-更新IPv4+IPv6


### 填写示例

**示例1 (单个域名自动解析 IPv4+IPv6)**

◾ 域名是 ddns.example.cn，密钥是 3478teiu8rfj9ewut35ut34i0qwriegt90i，自动更新IPv4和IPv6记录

```cmd
[ddns.example.cn, 3478teiu8rfj9ewut35ut34i0qwriegt90i, , , , 46]
```



**示例2 (多个域名自动解析 IPv4/IPv6)**

◾ 域名1是 ddns1.example.cn，密钥是3478teiu8rfj9ewut35ut34i0qwriegt90i，自动更新IPv4和IPv6记录

◾ 域名2是 ddns2.example.cn，密钥是dcko490i39it90fi3it490rfo90rgoewrkg，仅自动更新IPv4记录

◾ 域名3是 ddns3.example.cn，密钥是saeijdh78w4r2ir0iefi299rw0rg9ief90a，仅自动更新IPv6记录

◾ 域名4是 ddns4.example.cn，密钥是ef783y4thjcdijru89wieu89rr33r02o33b，仅自动更新IPv6记录，IPv6前缀是 fe80:ab2:1919:810::/60

```cmd
[ddns1.example.cn, 3478teiu8rfj9ewut35ut34i0qwriegt90i, , , , 46]
[ddns2.example.cn, dcko490i39it90fi3it490rfo90rgoewrkg, , , , 4]
[ddns3.example.cn, saeijdh78w4r2ir0iefi299rw0rg9ief90a, , , , 6]
[ddns4.example.cn, ef783y4thjcdijru89wieu89rr33r02o33b, , , , 6]
```


**示例3（单个域名手动解析 IPv4+IPv6）**

域名是 ddns.example.cn，密钥是 3478teiu8rfj9ewut35ut34i0qwriegt90i，

IPv4地址192.168.1.1，IPv6地址fe80::1a2b3c:2233:1145:aabb，更新IPv4和IPv6记录

```cmd
[ddns.example.cn, 3478teiu8rfj9ewut35ut34i0qwriegt90i, 192.168.1.1, fe80::1a2b3c:2233:1145:aabb, , 46]
```


**示例4 (多个域名手动解析 IPv4/IPv6)**

◾ 域名1是 ddns1.example.cn，密钥是3478teiu8rfj9ewut35ut34i0qwriegt90i，

IPv4地址192.168.1.1，IPv6地址fe80::1a2b3c:2233:1145:aab1，更新IPv4和IPv6记录

◾ 域名2是 ddns2.example.cn，密钥是dcko490i39it90fi3it490rfo90rgoewrkg，

IPv4地址192.168.1.2，更新IPv4记录

◾ 域名3是 ddns3.example.cn，密钥是saeijdh78w4r2ir0iefi299rw0rg9ief90a，仅自动更新IPv6

IPv6地址fe80::1a2b3c:2233:1145:aab2，IPv6前缀是 fe80:ab2:1919:810::/60，更新IPv6记录

```cmd
[ddns1.example.cn, 3478teiu8rfj9ewut35ut34i0qwriegt90i, 192.168.1.1, fe80::1a2b3c:2233:1145:aab1, , 46]
[ddns2.example.cn, dcko490i39it90fi3it490rfo90rgoewrkg, 192.168.1.2, , , 4]
[ddns3.example.cn, saeijdh78w4r2ir0iefi299rw0rg9ief90a, , fe80::1a2b3c:2233:1145:aab2, fe80:ab2:1919:810::/60, 6]
```


### 注意事项

1：多条记录之间不能有空行

2：留空项的位置应当保留(如上面的例子)，不能删除

3：在任意行最前端添加符号 "#" 则注释掉该行


## 手动构建

程序只使用了python自带的5个库：os, re, time, datetime, requests

但如果你想手动构建的话得安装pyinstaller


打开cmd，输入pyinstaller安装命令

```cmd
pip install pyinstaller
```


安装完成后用pyinstaller打包成exe

来到你存放程序的目录，打开cmd，输入构建命令

```cmd
pyinstaller -F ddns.py
```


# 其它事项


个人主页：[Bilibili-豆豆zzydd](https://space.bilibili.com/543085311)

github用的还不是很习惯，如果我这个傻蛋迟迟没回，到B站私信找我(B站回复前只能发1条消息，说明清楚)

我认为README的教程已经很详细了，但如果你还是没看明白，我B站之后可能会教程，到时候可以去看下。
