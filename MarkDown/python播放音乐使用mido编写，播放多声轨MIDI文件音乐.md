# python播放音乐:使用mido编写，播放多声轨MIDI文件音乐

作者：隋顺意
微信：世界上的霸主
博客：Sui_da_xia

##### 欢迎转载，下载使用

### 前言：

人人都喜爱音乐，音乐丰富了我们的情感。在历史上，不乏有伟大的作曲家、钢琴家：巴赫、海顿、莫扎特、贝多芬、李斯特、勃拉姆斯……

我们可以在剧院里，音乐厅里听到美妙动听的音乐。当我看到钢琴家修长的手指在钢琴上飞快地舞动，奏出婉转的音乐，十分羡慕，相信你们也是一样。那怎样才能让电脑，手机播放出美妙的音乐呢？

今天，就让我，携您一起进入这美妙而又复杂的音乐世界吧。

### 安装：

从前有个库，名字叫mido. 其他不会做，就会发声音。

```python
pip install mido  
```

如果报错，试试用pip3。

### Mido使用：

使用mido库说来简单，但是特别的麻烦。它有许许多多的功能，这里仅介绍几种最常用的。贴个代码：

```python
1.import mido   #不用说  
2.	from mido import Message, MidiFile, MidiTrack    #懒得说  
3.	  
4.	mid = MidiFile()       #给自己的文件定的.mid后缀  
5.	track = MidiTrack()    #定义声部，一个MidoTrack()就是一个声部  
6.	
7.	track.append(Message('program_change',channel=0,program= X,time=0))         
8.	track.append(Message('note_on', note=XX, velocity=64, time=XX,channel=0))   
9.	track.append(Message('note_off', note=XX, velocity=64, time=XX,channel=0))  
```

mido的Message有可以放很多种不同的参数，每种参数都有不同的用途，接下来，我将会一一介绍以下参数：

#### program_change：

```python
1.	track.append(Message('program_change',channel=0,program= X,time=0))         
```

‘**program_change**’参数可以理解成是个起始，用于确定乐器的类型。其中,**channel和time不可改变**，只能是0，（不信的可以自己去试）。

Program用于确定乐器，*mido*有个专门的对应表，用数字命名，从0到16，17种不同的乐器。接下来，我会使用**2（钢琴）**作为参数

#### note_on：

```python
1.	track.append(Message('note_on', note=XX, velocity=64, time=XX,channel=0))   
```

‘**note_on**’ 参数是一个音的开端。用于确定音，与前个音之间的间隔，音量。

参数**note**代表“**音**”，和program一样，都是用数字命名，从21到108，**以半音作为最小单位**，它有张表格，记录了所有的对应。但，不见得每次都要查表。

为此，我花费两天时间，写了巨大的 函数“**num**”，把音转换成对应的数字。因为太长，这不放了，如有需要，请到我的github：

[https://github.com/duoduo666/mido-Barock/blob/master/translate(number%2Cnote)/note%20to%20number.py](https://github.com/duoduo666/mido-Barock/blob/master/translate(number,note)/note to number.py)

“**velocity** ”参数代表音量，具体换算分贝我没研究，有兴趣可以自己研究。建议使用**64**作为（官网是这样写的）

“**time**” 参数代表与**前个音间隔**时间，具体换算会在下面讲到

“**channel** ”参数很奇特，到现在，还没研究出有何用，就写0吧。

#### Note off:

```python
1.	track.append(Message('note_off', note=XX, velocity=64, time=XX,channel=0))  
```

“**note off**” 为一音结束，**音（note）须和note on 一样**，反之就报错。

“**velocity**” 是个很特别的参数，**可以和note on的不一样**。如：note on 音量是 64，这写 100，那会在发声时从64慢慢增加至100。但，建议不要再“**钢琴**”**频道**（2）**更改**，学过钢琴都知道，钢琴不能变音量的。

这里的“**time**”代表着这音持续多少。但，这里是个**时间单位**，而音乐节拍，如快板为120，是**速度单位**。这复杂了。而且，这的时间**不是一个基本单位**（如秒，微妙）time参数的1都不知是多少秒！这如何是好？先贴代码：

```python
1.	def beat(time):            #与mido的拍子互换  
2.	    time /= 60 * 1000  
3.	    time = 1/time  
4.	    return time  
```

这是个算式，请注意，**这是我自己做的运算，官网都没有写**。当**time = 1000**时，那播放120个音就是一分钟，**每分120拍**（音乐节拍就是用120表示）。晕…

**note off** 的 “**channel**”参数也没弄清，如有大佬明白，请到我的**github**

https://github.com/duoduo666/mido-Barock

的**issue**模块评论

### 集合函数

稍稍动动脑经，就可以很容易把刚刚说的三种参数放在一起

```python
1.	def yin(yin,pai,qian=0,liang=64,qi=2): #yin是音，pai是指时间（节拍），
2.	    if type(yin)== str:               #qian是是音前多少拍
3.	        yin = num(yin)                #liang是音量
4.	    track.append(Message('program_change',channel=0,program=qi,time=0))
5.	 	track.append(Message('note_on',note=yin,velocity=liang,time=qian,channel=0))
6.		track.append(Message('note_off',note=yin,velocity=liang,time=pai,channel=0))
```

但是，怎样才能**同时播放两个，至多个**呢？接下来，我们就要加声部。

还记得刚刚写过的一行代码

```python
1.	track = MidiTrack()
2.	mid.tracks.append(track)  
```

这就是增加一个声部，这个声部的名字为track。所以，我们就可以增加声部，并做个list，方便调用：

```python
1.	track = MidiTrack()  
2.	track2 = MidiTrack()  
3.	track3 = MidiTrack()  
4.	track4 = MidiTrack()  
5.	mid.tracks.append(track)  
6.	mid.tracks.append(track2)  
7.	mid.tracks.append(track3)  
8.	mid.tracks.append(track4)  
9.	tra = [track,track2,track3,track4] 
```

我这里先做四声部，有空的朋友可以多加几个（**除了巴赫写过首五部曲外，其他曲子，最多只有四声部**）再动动脑筋，让yin支持多声部：

```python
1.	def yin(yin,pai,qian=0,unit=track,liang=64,qi=2):
2.	 ·······
3.	 unit.append(Message('program_change',channel=0,program=qi,time=0))
4.	 unit.append(Message('note_on',note=yin,velocity=liang,time=qian,channel=0))
5.	 unit.append(Message('note_off',note=yin,velocity=liang,time=pai,channel=0))
```

##### 多音单声部函数

一首曲子，定不止一音，动动脑筋，得出：

```python
1.	 def myin(fu,pai,time,qian=None,yue=2):   #单声部  
2.	    pig = int(beat(time))                   
3.	    if qian == None:  
4.	        for i in range(len(pai):  
5.	            yin(fu[i],pai[i]*pig,qi=yue)  
6.	    else: 
7.	        for i in range(len(pai)):  
8.	            yin(fu[i],pai[i]*pig,qian[i],qi=yue)  
```

pig的beat刚在**note off 里的time参数**里专门讲过，这不再多说。

##### 多声部函数实现：

一首钢琴曲里，总会有好几个声部，何况我们后面讲的算法是巴洛克时期的曲子，当然要着重讲多声部啦。

在刚刚写的函数(myin)的基础上，我们稍稍改进一下：

```python
1.	def myin(fu,pai,time=120,bef=None,shenbu=track,yue=2):   #多声部版  
2.	    pig = int(beat(time))  
3.	    for i in range(len(pai)):  
4.	        if type(pai[i]) == list:  
5.	            for j in range(len(pai[i])):  
6.	                if bef == None:  
7.	                    yin(fu[i][j],pai[i][j]*pig,unit=tra[j],qi=yue)  
8.	                else:  
9.	                    yin(fu[i][j],pai[i][j]*pig,bef[i][j],unit=tra[j],qi=yue)
10.	        else:  
11.	            if bef == None:  
12.	                yin(fu[i],pai[i]*pig,unit=shenbu,qi=yue)  
13.	            else:
14.	                yin(fu[i],pai[i]*pig,bef[i],unit=shenbu,qi=yue)  
```

第四行if type(pai[i]) == list为了把多声部和单声部分开来，比如说输入：[64,[64,65,66]]那[64]就是单声部，[64,65,66]是多声部的。

至于bef，这其实没什么用，不想写的就不写吧。也麻烦

### 结语：

现在，您就可以实现播放音乐了，无论多复杂，多绕的音乐，您都可以动动脑筋实现。完整代码请去我的github。

https://github.com/duoduo666/mido-Barock

但完了么？文章是结束。但，你有没有想过，电脑，手机，可以播放音乐。但，它们可不可以通过计算，来“写”曲子呢？

为了弄清这些问题，我们需要了解许多令人发指的乐理，及计算令人发指的公式。你准备好了么？