# Python 虚拟环境备忘录

[TOC]

**venv**模块支持使用目录创建包隔离的“python包虚拟环境”。每个虚拟环境都有自己的python二进制文件，并且可以在目录中拥有独立的python软件包环境。

## **1、MacOS/类Unix**

### **（1）通过venv来创建一个虚拟环境**

```bash
python3 -m venv ~Coding/VirtualEnvironment
```

### **（2）激活和退出venv创建的虚拟环境**

**激活：source bin/activate**

```bash
source ~Coding/VirtualEnvironment/bin/activate
或
cd ~Coding/VirtualEnvironment
source bin/activate
```

**退出: deactivate**

```bash
cd ~Coding/VirtualEnvironment
deactivate
```

### **（3）通过which查看python二进制程序的具体位置**

```bash
%which python
#注意这个username是自己的用户名
/Users/username/Coding/VirtualEnvironment/bin/python
# 全局查看python效果
# %which python
# /usr/bin/python
```

### **（4）进入虚拟环境后pypi的包安装**

因为python虚拟环境的包和python全局环境的包环境是隔离的，如果在交互界面，使用pip安装包的时候，就需要进入虚拟环境后，激活虚拟环境，在用pip安装

```bash
cd ~Coding/VirtualEnvironment
source bin/activate
activate
pip install ping3
```

### **（5）MacOS/类Unix环境vscode虚拟环境便捷使用方法**

### **<1> 推荐vscode使用插件Project Manager把虚拟环境单独设置成一个项目**

```json
[
{
"name": "Project Python",
   #注意把username改为自己的用户名
"rootPath": "/Users/username/Coding/Python",
"paths": [],
"group": "",
"enabled": true
},
{
"name": "Project C",
"rootPath": "/Users/username/Coding/C",
"paths": [],
"group": "",
"enabled": true
},
{
"name": "Project Git",
"rootPath": "/Users/username/Coding/github",
"paths": [],
"group": "",
"enabled": true
},
{
"name": "Project PythonVenv",
"rootPath": "/Users/username/Coding/VirtualEnvironment",
"paths": [],
"group": "",
"enabled": true
}
]
```

### **<2>写vscode的代码片段时，应该添加专用的json header快捷字符**

```json
{
// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
// same ids are connected.
// Example:
// "Print to console": {
// "prefix": "log",
// "body": [
// "console.log('$1');",
// "$2"
// ],
// "description": "Log output to console"
// }
"utf file header": {
"prefix": "utf",
"body": [
"#! /usr/bin/env python3",
"# _*_ coding: utf-8 _*_"
],
"description": "utf file header"
},
"venv file header": {
"prefix": "venv",
"body": [
"#! ~/Coding/VirtualEnvironment/bin/python",
"# _*_ coding: utf-8 _*_"
],
"description": "venv file header"
}
}
```

### **<3> 写vscode的python脚本时，应该在代码开始的时候添加虚拟环境的环境变量**

输入代码片段python.json中的venv file header定义的字符快捷键，**venv**后自动显示文件全局变量

```python
#! ~/Coding/VirtualEnvironment/bin/python
# _*_ coding: utf-8 _*_
```

## **2、Windows**

### **（1）创建python虚拟环境**

如果已经配置好全局path和pathext变量

```bash
c:\>python -m venv c:\path\to\myenv
```

### **（2）激活和退出venv创建的虚拟环境**

**激活：source bin/activate**

```bash
cd c:\path\to\myenv
.\Scripts\activate
或
c:\path\to\myenv\Scripts\activate.bat
```

**退出: deactivate**

```bash
c:\path\to\myenv
deactivate
```

### **（3）windows的python虚拟环境中如何运行python**

```bash
...\myenv\Scripts\python.exe
```

### **（4）通过where查看python二进制程序的具体位置**

```bash
where python
```

## 3、网络工程师学习视频推荐

有很多使用Windows的同行，对类Unix和Python十分陌生，如果正苦于没有好的渠道入门，我推荐知乎站内的以下视频课程。该视频从GNU-Linux讲起、逐渐引入Python基础，值得一看。

[Python 深入浅出进阶课程](https://www.zhihu.com/education/video-course/1483114387217539072?section_id=1483114626753331201)