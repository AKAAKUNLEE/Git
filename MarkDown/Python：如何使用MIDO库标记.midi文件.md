# Python：如何使用MIDO库标记.midi文件

我有这些.midi[files](https://drive.google.com/drive/folders/1US5rL_T121thkRL0fjs1WeitnHORdSci?usp=sharing)，我想用每0.032秒的音高（midi数字）来标记它们。我想要的标签示例可以在[here](https://drive.google.com/file/d/1XW3kw-In0AE6x3ewgnK-pnCZpqkKYB-A/view?usp=sharing)中找到。在这个任务中，我使用pythonmido库，可以在[here](https://mido.readthedocs.io/en/latest/)中找到文档

据我所知，在处理.midi之前，我需要先迭代文件中所有可用的消息。我从这个[file](https://drive.google.com/file/d/1MTm9B_6rHvACk36pOHqEGGqsrRB0j_Wu/view?usp=sharing)中取一个例子，这是代码+结果

```
# Code to iterate .midi message
import mido
from mido import MidiFile
from mido import Message
mid_14 = MidiFile('00014 Twinkle, Twinkle, Little Star.mid', clip=True)
for i, track in enumerate(mid_14.tracks):
    print('Track {}: {}'.format(i, track.name))
    print("-"*100)
    for msg in track: #print message in tracks
        print(msg)
    print("="*100)
```

```
# Result
Track 0: untitled
----------------------------------------------------------------------------------------------------
<meta message track_name name='untitled' time=0>
<meta message time_signature numerator=4 denominator=4 clocks_per_click=24 notated_32nd_notes_per_beat=8 time=0>
<meta message key_signature key='C' time=0>
<meta message set_tempo tempo=500000 time=0>
<meta message sequencer_specific data=(5, 15, 28, 50, 48, 48, 49, 46, 49, 49, 46, 48, 57) time=0>
<meta message sequencer_specific data=(5, 15, 18, 0, 0, 127, 127, 0) time=0>
<meta message end_of_track time=0>
====================================================================================================
Track 1: MAJOR_TRACK
----------------------------------------------------------------------------------------------------
<meta message track_name name='MAJOR_TRACK' time=0>
program_change channel=0 program=0 time=0
<meta message sequencer_specific data=(5, 15, 9, 64, 72) time=0>
<meta message sequencer_specific data=(5, 15, 6, 71, 101, 110, 101, 114, 97, 108, 32, 77, 73, 68, 73) time=0>
note_on channel=0 note=60 velocity=110 time=0
note_on channel=0 note=60 velocity=0 time=480
note_on channel=0 note=60 velocity=110 time=0
note_on channel=0 note=60 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=69 velocity=110 time=0
note_on channel=0 note=69 velocity=0 time=480
note_on channel=0 note=69 velocity=110 time=0
note_on channel=0 note=69 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=960
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=62 velocity=110 time=0
note_on channel=0 note=62 velocity=0 time=480
note_on channel=0 note=62 velocity=110 time=0
note_on channel=0 note=62 velocity=0 time=480
note_on channel=0 note=60 velocity=110 time=0
note_on channel=0 note=60 velocity=0 time=960
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=62 velocity=110 time=0
note_on channel=0 note=62 velocity=0 time=960
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=62 velocity=110 time=0
note_on channel=0 note=62 velocity=0 time=960
note_on channel=0 note=60 velocity=110 time=0
note_on channel=0 note=60 velocity=0 time=480
note_on channel=0 note=60 velocity=110 time=0
note_on channel=0 note=60 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=480
note_on channel=0 note=69 velocity=110 time=0
note_on channel=0 note=69 velocity=0 time=480
note_on channel=0 note=69 velocity=110 time=0
note_on channel=0 note=69 velocity=0 time=480
note_on channel=0 note=67 velocity=110 time=0
note_on channel=0 note=67 velocity=0 time=960
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=65 velocity=110 time=0
note_on channel=0 note=65 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=64 velocity=110 time=0
note_on channel=0 note=64 velocity=0 time=480
note_on channel=0 note=62 velocity=110 time=0
note_on channel=0 note=62 velocity=0 time=480
note_on channel=0 note=62 velocity=110 time=0
note_on channel=0 note=62 velocity=0 time=480
note_on channel=0 note=60 velocity=110 time=0
note_on channel=0 note=60 velocity=0 time=960
<meta message end_of_track time=0>
====================================================================================================
```

我的问题是：我如何用可用的信息（节奏、速度）将它们分成0.032秒的块？我应该在开始标记它们之前从文件中收集更多信息吗