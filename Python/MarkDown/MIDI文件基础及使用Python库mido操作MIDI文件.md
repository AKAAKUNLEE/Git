## MIDI文件基础及使用Python库mido操作MIDI文件

技术标签： [歌声合成](https://codeleading.com/tag/歌声合成/) [python](https://codeleading.com/tag/python/)

#### 基础知识

MIDI文件头：4d 54 68 64 00 00 00 06 ff ff nn nn dd dd
4d 54 68 64：MThd
00 00 00 06：数据区长度六字节
ff ff：00 00-单音轨；00 01-多个同步音轨；00 10-多个不同步音轨
nn nn：音轨数目（含全局音轨和演奏音轨）
dd dd：最高位为标记位，0为采用ticks计时，后面的数据为一个4分音符的ticks；1为SMPTE格式计时，后面的数值则是定义每秒中SMTPE帧的数量及每个SMTPE帧的tick
Mido
**一、使用指导：**
通过pip命令安装：

```clike
pip install mido
```

推荐使用清华镜像源：

```clike
pip install mido -i https://pypi.tuna.tsinghua.edu.cn/simple
```

使用前`import mido`即可
**二、打开**
通过mid=mido.MidiFile(“绝对路径或同目录下文件名”)打开指定midi文件
每个音轨单独读取指令为`

```python
track_n=mido.MidiTrack(mid.tracks[n])
```

`(n从0开始) track.name可直接获取音轨名称，每个消息可按照下标单个读取 同时`MidiTrack（）`和`MidiFile（）`也可用作新音轨和新文件新建命令
**三、遍历读取**
示例代码：

```python
import mido
mid = mido.MidiFile(“test.mid”)
for i, track in enumerate(mid.tracks):#enumerate()：创建索引序列，索引初始为0
    print('Track {}: {}'.format(i, track.name))
    for msg in track:#每个音轨的消息遍历
        print(msg)
```

每个midi文件由多个音轨组成，mido称音轨为Track，其中Track 0 一般是全局音轨，其后跟随演奏音轨。
每个音轨包含若干条消息，消息可解释为相应音符，一般在全局音轨中放置元消息（mate massages）来指定mid文件的相关参数（速度/音轨数等）
mid.length=(以秒为单位的演奏总长度，float)
mid.type=(此midi文件类型)
is_mate可以返回判定是否是元消息

##### 消息相关：

```bash
Message(type,note=60,velocity=96,time=480)
```

消息设定代码（示例）

```bash
track.append(mido.Message(type,note=60,velocity=96,time=480))
```

type 这个参数确定信号的类型(str)。基本的为note_on作为音符开始，note_off作为音符终止。
note 这个参数确定音符的音高。60代表中央C，每增加12，音高升高一个八度。
velocity 这个参数确定音符的音量。0表示静音，127表示最大音量。
time 这个参数确定消息所在的时间。这个时间以tick为单位，而在mido的默认配置中，1拍中有480个tick。所以要想生成一个长度为1拍的音符，应该设置其time值为480，而不是1。
注：time用480*n来表示会比较省力
另注：time是指这条消息与上一条消息的时间差（结尾对结尾）
四、参数设置
**A音色**

```bash
track.append(mido.Message('program_change', program=1, time=0))
```

其中，program参数确定了这个音轨的音色。
另注：除了打击乐通道以外，音色的默认值为Piano 1。
**B曲速**

```bash
track.append(mido.MetaMessage('set_tempo', tempo=500000, time=0))
```

其中，tempo参数确定了乐曲的速度。
tempo 值的含义是每一拍为多少微秒。500000表示每一拍为0.5秒（1us=1e6s），即每分钟120拍。bpm和tempo的换算公式为

```clike
bpm=(6×10^7)/tempo
```

**C设置音轨名称**
音轨名称

```bash
track.append(mido.MetaMessage('track_name', name='Piano', time=0))
```

其中，name参数确定了音轨的名称。
五、文件保存

```python
mid.save(‘路径’)
```