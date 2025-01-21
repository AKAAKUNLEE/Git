# python创作音乐: 计算机创作，计算音乐

### 前言

上期留了尾，卖了关子。许多朋友感到不爽，气愤。这里**表示歉意**(๑*◡*๑)。我就接着上回，继续为您说。

（没看前篇的的朋友请点 [**这里**](https://blog.csdn.net/Sui_da_xia/article/details/104495111) 看上篇，否则看此文会有障碍）

如今，许多人尝试用计算机创作乐器，普遍方法是**随机生成一段音乐**，和现有曲子的**相似度**进行打分，一个分值范围内算通过。我也这么做？**不，这样做效率低下**，**随机生成几千首只有一首通过，计算速度也十分低下**（超级电脑不说），筛选出的曲子也**不一定好听**。

我用什么方法呢？今天，我们要了解许多令人发指的乐理，以及计算令人发指的乐理公式。准备好笔纸了么？今天，就让我，带您进入**美妙***复杂* **的音乐殿堂吧**！

### 乐理的代码（含拗口的句子）：

**友情提示**：*建议仔细阅读，多看几遍，看不懂不要紧，我学乐理时，是一头雾水。*

废话不多说，先来讲讲“**音程**”：

##### 音程及其算法：

看着玄乎，其实是最简单，**它表示两音之间的“距离”**，**其基本单位称为度**。在mido中，**以“半音”为基本单位**，接下来，我都采用**半音计数**。

> 1：**小二度**
> 2：**大二度**/减三度
> 3：**小三度**/增二度
> 4：**大三度**/减四度
> 5：**纯四度**/增三度
> 6：**增四度**/减五度
> 7：**纯五度**/减六度
> 8：**小六度**/增五度
> 9：**大六度**/减七度
> 10：**小七度**/增六度
> 11：**大七度**
> （**单位：半音**）

**除了四度和五度（八度不算）**，**度按减小大增来计算**，**没有基准**。但，**一般“大度”为最佳选择**。不信可以尝试下，是大三度好听，还是小三度好听。**除四度以外**，只有理论上的增减，不会说增三度，只说纯四度。因此，只需做11个函数就行了。比如说小二度：

```python
1.def sd_two(low=None,high=None):         #小二度  
2.    if type(low) == str:  
3.     ···#就是转换，前面的代码都写过  
4.    yin = []  
5.    if low and high == None:  
6.        high = low + 1  
7.    if high and low == None:  
8.        low = high - 1  
9.    yin.append(low)  
10.    yin.append(high)  
11.    return yin  
```

我花了**整天**肝枯燥的做简单计算 的代码，想看去我的Github：

[https://github.com/duoduo666/mido-Barock/blob/master/turn%20note/yin_cheng.py](https://github.com/duoduo666/mido-Barock/blob/master/turn note/yin_cheng.py)

记得给我star并关注哦

##### 三和弦：

三和弦有四类，**大三和弦，小三和弦，增三和弦，减三和弦**。七和弦较复杂，有兴趣读者可自己搜搜。

大三和弦结构是：**大三度+小三度**。小三和弦结构是：**小三度+大三度**。增三和弦结构是：**大三度+大三度**，减三和弦结构是：**小三度+小三度**。最舒服的和弦是大三和弦，最恶心的和弦是减三和弦。

因此，我们只要知道一个音，就可以求出其他的音。我在这贴大三和弦代码：

```python
1.	def b_three(geng=None,zhong=None,wu=None):  
2.	    yin = []  
3.	    if geng and zhong == None and wu == None:    #知道根音  
4.	        zhong = geng + 4  
5.	        wu = zhong + 3  
6.	         yin.append(geng)
7.	         yin.append(zhong)
8.	         yin.append(wu)
9.	         return yin
10.	    if zhong and geng == None and wu == None:      #知道中音  
11.	        geng = zhong - 4  
12.	        wu = zhong + 3  
13.	         ····#同上
14.	    if wu and geng == None and zhong == None:      #知道五音  
15.	        zhong = wu - 3  
16.	        geng = zhong - 4  
17.	        ····#同上
```

###### 转位

三和弦有四类，每类都有3种“形态”，称为“转位”，分别是：**第一转位（原位），第二转位（4转位），第三转位（46转位）**

**每次转位把最低音（根音）提八度（12半音）**。为大家理解，我画了**大三和弦转位图**
*单位：半音）。

![大三和弦转位图](https://img-blog.csdnimg.cn/2020022613060446.png)
**X代表根音（最低音），Y代表三音（中间音），Z代表五音（最高音）**。清楚多了吧，其余三个皆如此。

脑筋都不用动了，直接出转换代码。（转换位大4和弦）

```python
2.	yin = []  
3.	if geng and zhong and wu:                        #若是三个都有  
4.	    if zhong - geng == 4 and wu - zhong == 3:    #若是第一转为（三和弦）  
5.	        geng += 12  
6.	        yin.append(zhong)  
7.	        yin.append(wu)  
8.	        yin.append(geng)  
9.	        return yin  
10.	    if zhong - geng == 5 and wu - zhong == 4:    #若是第三转为（46和弦）  
11.	        wu -= 12  
12.	        yin.append(wu)  
13.	        yin.append(geng)  
14.	        yin.append(zhong)  
15.	        return yin  
16.	     if zhong - geng == 3 and wu - zhong == 5:  
17.	        return True  
```

但是，**种类太多**，**我花了10天**（*夸张 *） 完成，这不贴了，有兴趣的到我的GitHub

[https://github.com/duoduo666/mido-Barock/tree/master/turn%20note](https://github.com/duoduo666/mido-Barock/tree/master/turn note)

（记得要给star和关注哦）

#### 配上和弦（音程）：

哇！可以求和弦和、音程了！鼓掌👏。动动脑筋，在myin基础上，更改下，给曲子配上和弦：

```python
1.	def myin(fu,pai,time=120,du=None,chord=None,high=64,note="low",yue=2):  
2.	    #和声版  
3.	    pig = int(beat(time))    #int取整，time要求整数
4.	    for i in range(len(pai)):  
5.	        if type(pai[i]) == list:  
6.	            ···   #上篇文章有，看看
7.	        else:
8.	            if chord == None and du == None:
9.	                ···  #上篇文章有，看看
10.	            else:  
11.	                #和弦  
12.	                if chord == "dasan":            #大三和弦  
13.	                    if note == "low":  
14.	                        fu[i] = b_three(fu[i])  
15.	                    elif note == "zhong":  
16.	                        fu[i] = b_three(zhong=fu[i])  
17.	                    elif note == "wu":  
18.	                        fu[i] = b_three(wu=fu[i])  
19.	                ····· #此处省略一千行  
20.	
21.	                #音程（度）
22.	                if du == "xiaoer":                   #小二度  
23.	                    if note == "low":  
24.	                        fu[i] = sd_two(fu[i])  
25.	                    if note == "high":  
26.	                        fu[i] = sd_two(high=fu[i])  
27.	                ····#此处省略一千行  
28.	
29.	                #循环  
30.	                for x in range(len(fu[i])):  
31.	                    yin(fu[i][x],pai[i]*pig,liang=high,unit=tra[x],qi=yue)  
```

有太多的“音程”、“和弦”，这不可能全贴，看完整代码？去：

[https://github.com/duoduo666/mido-Barock/blob/master/play%20note/play%20note(basic).py](https://github.com/duoduo666/mido-Barock/blob/master/play note/play note(basic).py)

庆祝一下，我用这函数，给《玛丽有只小山羊》配了和弦和音程，只有你没想到，没有我做不出，去 [这里] (https://github.com/duoduo666/mido-Barock/tree/master/mary) 听听。

## 巴洛克曲子算法及实现：

巴洛克时期有许多不同的种类曲子，二部曲，三部曲，四部曲，宾格，赋格……数不过来，不同种类的曲子有不同形式。今天我们实现二部曲。二部曲有很多形式，单开式，双起式，加厚式……我们挑个简单的，“单开式”。

《巴赫二部创意曲》第一首就是讲这个。讲之前，要贴几段代码：

#### 倒影：

打个比方：[3,4,5]的倒影就是[3,2,1]。这形式在巴洛克时期全都是，实现函数：

```python
def dao(yin):                 #计算倒影
    a = yin[0] * 2
    daoyin = []
    for i in yin:
        b = a - i
        daoyin.append(b)
    return daoyin 
```

首音乘2，以此减接下来的数，得出数组（list)

倒影难道音高不变了？总要变吧。动动脑经，得出答案：

```python
def getdao(xuanlu,base):
    for i in range(len(xuanlu)):
        if type(xuanlu[i]) == str:
            xuanlu[i] = num(xuanlu[i])
    if type(base) == str:
        base = num(base)
    xuanlu = dao(xuanlu)
    high = base - xuanlu[0]
    for i in range(len(xuanlu)):
        xuanlu[i] += high
    return xuanlu
```

以base位基音，得出xuanlu倒影。

#### 分拆和弦、时间：

在巴洛克时期，总会把主题（主旋律）拆开来，分成个主题。但你不知道用户会输入怎样的节奏型。再动动脑筋，就可以把旋律按节拍的不同拆开。

```python
1.	def getlu(first,second,ind):  
2.	    s = 0  
3.	    c = 0  
4.	    for i in range(1,len(second)):  
5.	        if second[i] != second[s]:  
6.	            c += 1  
7.	            if c == ind:  
8.	                return first[s:i]  
9.	            else:  
10.	                s = i  
11.	    return first[s:]  
```

同理，分拆时间：

```python
1.	def gettime(paizi,ind):  
2.	    s = 0  
3.	    c = 0  
4.	    for i in range(1,len(paizi)):  
5.	        if paizi[i] != paizi[s]:  
6.	            c += 1  
7.	            if c == ind:  
8.	                return paizi[s:i]  
9.	            else:  
10.	                s = i  
11.	    return paizi[s:]  
```

这样你就可以获取任意一段的代码和时间了。

### 计算机计算乐曲实现：

有小白生气了，算法还不讲！别急，算法这不就来了？那最经典的BWV772举例：

![BWV772乐曲分析](https://img-blog.csdnimg.cn/20200226180249462.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1N1aV9kYV94aWE=,size_16,color_FFFFFF,t_70)
***此图版权为作者所有！严禁转载***
我们用**蓝色框匡主题，绿色框匡副题和配旋律。用黄色代表倒影**。我们用数学的语言总结下：（我画的）

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020022618063660.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1N1aV9kYV94aWE=,size_16,color_FFFFFF,t_70)***此图版权为作者所有！严禁转载***

有个特别的。所有的曲子都要“解决”，“解决”是较复杂，有兴趣的可以搜搜。这我自己做了个个性化 解决，大家可以拿来用。

```python
1.	    lastyin = [b_three(".do"),b_three(".mi"),b_three(".so"),b_three("do"),b_three("mi"),b_three("so"),'so','mi','do',"do","si"]  
2.	    lastpai = [xxxx,xxxx,xxxx,xxxx,xxxx,xxxx,0.5,0.5,1.5,5]  
3.	    myin(lastyin,lastpai,track=track4)  
4.	    myin(["do"],[10],high=120)  
```

***此解决方法，严禁抄袭，如有发现，必将追究法律责任！***

到这，**相信只要智商>100**，就可以写出来。但，许多的小白还是不会写。为了照顾小白，我原来想在这里贴，但是实在太长，放不下。请去 [**我的github的barok文件]**(https://github.com/duoduo666/mido-Barock/tree/master/barok) 哦

## 结语

我还会卖关子？不不不，不会了，不会让大家气愤了。

如今，您可以通过计算机计算出巴洛克时期的二部曲的开场事了，只要有个好旋律，就可以出个好曲子。但其他的种类呢？

这里打个小广告，可以买本《巴赫创意曲集》，一共30首曲子，每首曲子都很经典。可以自己挨个分析，写代码哦。

如果有问题，请到我的github的issue模块哦，只是我的Github.欢迎关注：

**https://github.com/duoduo666**