# 【Python煮音乐】MID文件转WAV

## 运行环境：

[Win10系统](https://so.csdn.net/so/search?q=Win10系统&spm=1001.2101.3001.7020)，Python3.7

## 问题：

因为一些自娱自乐的需要，笔者遇到了一个需要将[MIDI](https://so.csdn.net/so/search?q=MIDI&spm=1001.2101.3001.7020)音乐标准格式转换为WAV音频的问题，在互联网的帮助下找到了 Python 库 [midi2audio](https://www.cnpython.com/pypi/midi2audio)，按照官方的引导使用如下方法进行优雅地转换：

```python
from midi2audio import FluidSynth
FluidSynth().midi_to_audio('input.mid', 'output.wav')
```

不过出现了以下问题：

```python
FileNotFoundError: [WinError 2] The system cannot find the file specified
```

## 不太痛苦地解决中：

查看报错源头，发现函数midi_to_audio()的定义如下：

```python
    def midi_to_audio(self, midi_file, audio_file):
        subprocess.call(['fluidsynth', '-ni', self.sound_font, midi_file, '-F', audio_file, '-r', str(self.sample_rate)])
```

这段程序调用了其实是调用了 fluidsynth 的命令，因此正确的解决方案应该是找到 fluidsynth.exe 可执行程序，并且将路径添加到系统变量 Path 中。这里也是找到了 [FluidSynth 官网](http://www.fluidsynth.org/)，并根据官网的提示找到了[下载链接](https://github.com/FluidSynth/fluidsynth/releases/tag/v2.2.4)。由于Github偶尔上不去，笔者分享了自己下载的文件，[网盘](https://pan.baidu.com/s/1MzUjRIWUS_6RsC7_g6GPew)提取码：1ki5 。下载到任意位置都行，然后把路径加到系统变量 Path 中。不过随后又出现了另外一个问题：

```vbnet
Parameter 'D:\/.fluidsynth/default_sound_font.sf2' not a SoundFont or MIDI file or error occurred identifying it.
```

也就是说，想要转换还需要 sound font 文件，根据笔者粗浅的理解，这个“声音字体”就是音色的数字实现，使用不同的 .sf2 文件就可以实现不同的音色了。因此去网上找了一些免费的文件，放到项目所在的文件夹下。同时在 FluidSynth() 函数中增加参数，问题解决。

```python
FluidSynth(sound_font="some_sound_font.sf2").midi_to_audio('input.mid', 'output.wav')
```

##  解决方案：

需要 fluidsynth.exe 和 default_sound_font.sf2