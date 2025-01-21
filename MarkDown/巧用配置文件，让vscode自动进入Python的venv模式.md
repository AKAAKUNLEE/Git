# 巧用配置文件，让vscode自动进入Python的venv模式

[TOC]

## **一、Python venv**

很多朋友都喜欢使用Python的venv环境来隔离各个项目的Packages

但是，进入、退出venv环境，都要使用额外的命令达成

```bash
cd /root/python_venv_folder
source bin/activate
deactivate
```

是否有方法，可以规避额外命令呢？

这里，以网络工程师的视角，来回顾一下Python venv环境，安装、使用Nornir 的步骤。

操作系统环境： MacOS10.15

### **1、创建目录**

```bash
mkdir ~/Coding/Python_Nornir
```

### **2、使用Python创建venv环境**

```python
python -m venv ~/Coding/Python_Nornir
```

### **3、激活venv环境**

```bash
cd ~/Coding/Python_Nornir
source bin/activate
```

### **4、安装Nornir的venv环境**

```bash
pip install netmiko
pip install napalm
pip install nornir
pip install nornir_utils
pip install nornir_napalm
pip install nornir_netmiko
pip install nornir_scrapli
```

### **5、退出venv环境**

```bash
cd ~/Coding/Python_Nornir
deactivate
```

### **6、路径问题**

可以看到，以下路径

```bash
~/Coding/Python_Nornir
```

就成为Nornir venv环境的root目录了，所有Nornir的yaml配置文件路径，都起始于此。

**比如，要在这个目录中，新建3个目录，分别命名为nLab1、nLab2、nLab3，用以进行不同的nornir项目作业**

![img](https://pic4.zhimg.com/80/v2-0c9c471b851c1732747ec2d56dba0a23_720w.webp)

**那么，nLab[1-3]目录中的yaml文件，就要以此路径为起始路径。**

这里以nLab2目录中的config.yaml为例，进行说明：

由于Nornir venv环境的根目录是

```bash
~/Coding/Python_Nornir
```

那么nLab2的目录位置即为

```bash
~/Coding/Python_Nornir/nLab2
```

那么nLab2中的config.yaml文件中，指定hosts、groups、defaults文件的相对路径，就要从

```bash
~/Coding/Python_Nornir
```

开始，写作

```yaml
---
inventory:
plugin: SimpleInventory
options:
  host_file: "./nLab2/hosts.yaml"  # 相对路径必须加入venv起始路径
  group_file: "./nLab2/groups.yaml"
  defaults_file: "./nLab2/defaults.yaml"

runner:
plugin: threaded
options:
  num_workers: 100
```

### **7、手动开关venv环境**

如果觉得路径问题很麻烦，也可以把Nornir的所有yaml文件都放到

```bash
~/Coding/Python_Nornir
```

目录中。

开关Nornir的venv环境

```bash
cd ~/Coding/Python_Nornir
source bin/activate
deactivate
```

## **二、使用pyvenv.cfg简化venv的开关**

可以vscode的pyvenv.cfg文件来简化venv的开关。只需要在

```bash
~/Coding/Python_Nornir
```

中，创建vscode认可的pyvenv.cfg文件即可。

这样，vscode在运行相关Python程序的时候，就能自动开关venv环境了。

### **1、使用vscode打开Python的venv目录**

打开vscode，使用快捷键command + o打开

```bash
~/Coding/Python_Nornir
```

目录，在终端中运行以下命令

```bash
cd ~/Coding/Python_Nornir
source bin/activate
deactivate
```

通常，vscode就会在该目录下，自动创建一个pyvenv.cfg文件。

今后只要用vscode打开这个目录，直接运行Python程序，就会自动切换到venv模式下运行。省去了手动输入

```bash
source bin/activate
deactivate
```

的烦恼。

### **2、手动添加pyvenv.cfg文件**

当然，如果vscode没有自动生成pyvenv.cfg文件，也可以在该venv目录下，手动创建。

进入相关目录

```bash
cd ~/Coding/Python_Nornir
```

新建pyvenv.cfg文件

```bash
vim pyvenv.cfg
i
home = /Library/Frameworks/Python.framework/Versions/3.10/bin
include-system-site-packages = false
version = 3.10.4
:x
# home就是申明Python的可执行程序的环境变量，Windows同理

# include-system-site-packages用来说明是否调用Python系统环境中的第三方库，false表明只调用venv目录中的第三方库。

# version是Python的版本申明，根据实际情况修改。
```

### **3、实验效果**

操作系统： MacOS10.15.7

仿真软件： EVE-NG

Python venv目录：

```bash
~/Coding/Python_Nornir
```

目录结构

```bash
username@usernamedeMacBookPro1 Python_Nornir %ll
total 16
drwxr-xr-x  25 username staff  800  5 21 15:46 bin
drwxr-xr-x   2 username staff   64  5 21 15:43 include
drwxr-xr-x   3 username staff   96  5 21 15:43 lib
drwxr-xr-x   7 username staff  224  5 21 17:15 nLab1
drwxr-xr-x   8 username staff  256  5 21 17:12 nLab2
drwxr-xr-x   8 username staff  256  5 26 16:41 nLab3
-rw-r--r--   1 username staff  324  5 26 16:41 nornir.log
-rw-r--r--   1 username staff  115  5 26 16:27 pyvenv.cfg
```

实验拓扑

![img](https://pic2.zhimg.com/80/v2-0ad9744ed76989d0668ace2c559be421_720w.webp)

pyvenv.cfg

![img](https://pic4.zhimg.com/80/v2-613c52d8ba00e60bcb3e5a6d0102c287_720w.webp)

hosts.yaml

![img](https://pic4.zhimg.com/80/v2-7e058651b4c7c40f68c7c5c05bca0777_720w.webp)

groups.yaml

![img](https://pic2.zhimg.com/80/v2-a0f5dfd3da220c9beb6d4a19477e06f5_720w.webp)

defaults.yaml

![img](https://pic4.zhimg.com/80/v2-96756bbac3138d3f710530a6ad6ed1b3_720w.webp)

config.yaml

![img](https://pic1.zhimg.com/80/v2-45338429520c73cf10aff615ee071a48_720w.webp)

实验效果

![img](https://pic3.zhimg.com/80/v2-305a94b513e468d51de7cf5a27209992_720w.webp)

可以看到，当运行nLab2目录中的lab2.py程序时，vscode就会自动进入venv环境运行程序。