## Python | 读取 midi 文件

> 这个真的是费了好大好大好的的劲才弄出来。。。

# 格式

### 头区块 (Head Chunk)

```python
MThd + <区块字符长度> + <数据>
```

`头区块字符长度` 一般为 6

### 轨道区块 (Track Chunk)

```
Track Chunk = MTrk + <区块字符长度> + <MIDI 事件>
```

`区块字符长度` 是 4 byte 的无符号长整型

```
<MIDI 事件> = <时间戳> + （ <元 (Meta) 事件> | <普通事件> | <系统 (System) 事件>）
```

`时间戳` 为用 VLQ 表示的相对于上一个数据点的时间变化量 (delta time)

```
<元 (Meta) 事件> = \xFF + <类型> + <数据长度> + <数据>
```

`类型` 为 1 byte 的字节，对照表在下文
`数据长度` 为用 VLQ 表示的数据块的字符数

# 例子

比如下面这段 bwv806a.mid 的前 200 字节：

```
MThd\x00\x00\x00\x06\x00\x01\x00\x04\x00\xf0MTrk\x00\x00\x00G\x00\xff\x03\x08untitled\x00\xffT\x05`\x00\x03\x00\x00\x00\xffX\x04\x0c\x03\x0c\x08\x00\xffY\x02\x00\x00\x00\xffQ\x03\x06EO\x83\x97h\xffQ\x03\x07\xa1 \x82h\xffQ\x03\t\xa3\x1b\x82h\xffQ\x03\x0c\xe5\x0e\x00\xff/\x00MTrk\x00\x00\n\xd9\x00\xff!\x01\x00\x00\xff\x03\x1bEnglish Suite 1, 1. Prelude\x00\xc0\x00\x00\xb0\x07d\x00\n@\x90p\x90Qk\x81pLkxIk\x82hEk`Q\x00\x18PkHL\x00\x00E\x00\x00I\x00\x18P\x00\x18Nk`N\x00\x18Lk`L\x00\x18Nk`N\x00\x18
```

翻译后如下：

```
MThd
\x00\x00\x00\x06
\x00\x01    \x00\x04    \x00\xf0
0, 0, Header, 1, 4, 240
 
MTrk
\x00\x00\x00 G      # length of track
1, 0, Start_track
 
\x00    \xff    \x03    \x08    untitled
1, 0, Title_t, "untitled"              # Time0, METAEVENT, Type3, len8, data
 
\x00    \xff    T    \x05    `\x00\x03\x00\x00
1, 0, SMPTE_offset, 96, 0, 3, 0, 0
 
\x00    \xff    X    \x04    \x0c\x03\x0c\x08
1, 0, Time_signature, 12, 3, 12, 8
 
\x00    \xff    Y    \x02    \x00\x00
1, 0, Key_signature, 0, "major"
 
\x00    \xff    Q    \x03    \x06EO
1, 0, Tempo, 410959
 
\x83\x97 h    \xff    Q    \x03    \x07\xa1   # 注意这里结尾\xa1后还有一个空白字符 ' '
1, 52200, Tempo, 500000
 
\x82 h    \xff    Q    \x03    \ t \xa3
1, 52560, Tempo, 631579
 
\x1b\x82 h    \xff    Q    \x03    \x0c\xe5\x0e
1, 52920, Tempo, 845070
 
\x00    \xff    /    \x00
1, 52920, End_track
 
MTrk
\x00\x00 \n \xd9
2, 0, Start_track
 
\x00    \xff    !    \x01    \x00
2, 0, MIDI_port, 0
 
\x00    \xff    \x03    \x1b    English Suite 1, 1. Prelude
2, 0, Title_t, "English Suite 1, 1. Prelude"
 
\x00    \xc0    \x00
2, 0, Program_c, 0, 0
 
\x00    \xb0    \x07 d
2, 0, Control_c, 0, 7, 100
 
\x00    \n    @
2, 0, Control_c, 0, 10, 64
 
\x90 p    \x90    Q    k
2, 2160, Note_on_c, 0, 81, 107
 
\x81 p    LkxIk
2, 2400, Note_on_c, 0, 76, 107
 
\x82 h    Ek
2, 2520, Note_on_c, 0, 73, 107
.......
```

# 程序

```
from struct import unpack
import time
 
def read_vlq(f):
    result = ''
    buffer = unpack('B', f.read(1))[0]
    length = 1
    while buffer > 127:
        print(buffer)
        result += '{0:{fill}{n}b}'.format(buffer-128, fill='0', n=7)
        buffer = unpack('B', f.read(1))[0]
        length += 1
 
    result += '{0:{fill}{n}b}'.format(buffer, fill='0', n=7)
    return int(result, 2), length
 
 
def parse_event(evt, param):
    if 128 <= evt <= 143:
        print('Note Off event.')
    elif 144 <= evt <= 159:
        print('Note On event.', unpack('>BB', param))
    elif 176 <= evt <= 191:
        print('Control Change.')
    elif 192 <= evt <= 207:
        print('Program Change.')
 
with open('bwv806a.mid', 'rb') as f:
    print(f.read(200))
    # HEADER
    if f.read(4) != b'MThd':
        raise Exception('not a midi file!')
    print(f.read(4))
    header_info = f.read(6)
    print(unpack('>hhh', header_info))
 
    ''' ================================== '''
    while True:
        track_head = f.read(4)
        if track_head != b'MTrk':
            if track_head != b'':
                print(f.read(20))
                raise Exception('not a midi file!')
            else:
                break
        
        # length of track
        len_of_track = unpack('>L', f.read(4))[0]
        # print('len_of_track ', len_of_track)
 
        counter = 0
        t = 0
        last_event = None
        while True:
            delta_t, len_ = read_vlq(f)
            counter += len_
            t += delta_t
            # print('T ', t, end='')
            event_code = f.read(1)
            event_type = unpack('>B', event_code)[0]
            counter += 1
            # print(' event_type ', event_type, end='')
            if event_type == 255:
                meta_type = f.read(1)
                counter += 1
                # print(' - meta_type ', meta_type, end='')
                data_len, len_= read_vlq(f)
                counter += len_
                data = f.read(data_len)
                counter += data_len
                # print(' - ', data)
            elif event_type <= 127:
                parse_event(last_event, event_code+f.read(1))
                counter += 1
            else:
                if 128 <= event_type <= 143:
                    # print(' Note Off event.', end='')
                    parse_event(event_type, f.read(2))
                    counter += 2
                elif 144 <= event_type <= 159:
                    # print(' Note On event.', end='')
                    parse_event(event_type, f.read(2))
                    counter += 2
                elif 176 <= event_type <= 191:
                    # print(' Control Change.', end='')
                    parse_event(event_type, f.read(2))
                    counter += 2
                elif 192 <= event_type <= 207:
                    # print(' Program Change.', end='')
                    parse_event(event_type, f.read(1))
                    counter += 1
                last_event = event_type
 
 
            # print(counter)
            if counter == len_of_track:
                break
        
```

### 参考资料：

[Outline of the Standard MIDI File Structure (英文)](http://www.ccarh.org/courses/253/handout/smf/)，对 midi 文件的结构进行了解释
[The Midi File Format (英文)](http://midi.mathewvp.com/aboutMidi.htm)，另一篇比较好的说明文章
[Standard MIDI-File Format Spec. 1.1, updated (英文)](http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html)，详细说明了 VLQ 的一些信息
[MIDI Channel Voice Messages (英文)](https://www.csie.ntu.edu.tw/~r92092/ref/midi/midi_channel_voice.html)，midi_event 详解
[Python 3 struct 用法 (英文)](https://docs.python.org/3/library/struct.html)
[Variable-length_quantity (英文)](http://rosettacode.org/wiki/Variable-length_quantity#Python)，一种用 Python 来 parse VLQ 量的方法

转载于:https://www.jianshu.com/p/931be4f387bb