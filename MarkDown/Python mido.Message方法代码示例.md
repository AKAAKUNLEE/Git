# [Python mido.Message方法代码示例](https://vimsky.com/examples/detail/python-method-mido.Message.html)

本文整理汇总了Python中**mido.Message\**方法\****的典型用法代码示例。如果您正苦于以下问题：Python mido.Message方法的具体用法？Python mido.Message怎么用？Python mido.Message使用的例子？那么恭喜您, 这里精选的方法代码示例或许可以为您提供帮助。您也可以进一步了解该方法所在**类**[`mido`](https://vimsky.com/examples/detail/python-module-mido.html)的用法示例。
在下文中一共展示了**mido.Message方法**的15个代码示例，这些例子默认根据受欢迎程度排序。您可以为喜欢或者感觉有用的代码点赞，您的评价将有助于系统推荐出更棒的Python代码示例。

## 示例1: __str__

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def __str__(self):
    """Returns a regex pattern for matching against a mido.Message string."""
    if self._msg is not None:
      regex_pattern = '^' + mido.messages.format_as_string(
          self._msg, include_time=False) + r' time=\d+.\d+$'
    else:
      # Generate regex pattern.
      parts = ['.*' if self._type is None else self._type]
      for name in mido.messages.SPEC_BY_TYPE[self._inferred_types[0]][
          'value_names']:
        if name in self._kwargs:
          parts.append('%s=%d' % (name, self._kwargs[name]))
        else:
          parts.append(r'%s=\d+' % name)
      regex_pattern = '^' + ' '.join(parts) + r' time=\d+.\d+$'
    return regex_pattern 
```

开发者ID:magenta，项目名称:magenta，代码行数:18，代码来源:[midi_hub.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Fmagenta%2Fmagenta)



## 示例2: update

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def update(self,
             qpm,
             start_time,
             stop_time=None,
             program=_DEFAULT_METRONOME_PROGRAM,
             signals=None,
             duration=_DEFAULT_METRONOME_TICK_DURATION,
             channel=None):
    """Updates Metronome options."""
    # Locking is not required since variables are independent and assignment is
    # atomic.
    self._channel = _DEFAULT_METRONOME_CHANNEL if channel is None else channel

    # Set the program number for the channels.
    self._outport.send(
        mido.Message(
            type='program_change', program=program, channel=self._channel))
    self._period = 60. / qpm
    self._start_time = start_time
    self._stop_time = stop_time
    if signals is None:
      self._messages = _DEFAULT_METRONOME_MESSAGES
    else:
      self._messages = [s.to_message() if s else None for s in signals]
    self._duration = duration 
```

开发者ID:magenta，项目名称:magenta，代码行数:27，代码来源:[midi_hub.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Fmagenta%2Fmagenta)



## 示例3: stop

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def stop(self, block=True):
    """Signals for the playback to stop and ends all open notes.

    Args:
      block: If true, blocks until thread terminates.
    """
    with self._lock:
      if not self._stop_signal.is_set():
        self._stop_signal.set()
        self._allow_updates = False

        # Replace message queue with immediate end of open notes.
        self._message_queue.clear()
        for note in self._open_notes:
          self._message_queue.append(
              mido.Message(type='note_off', note=note, time=time.time()))
        self._update_cv.notify()
    if block:
      self.join() 
```

开发者ID:magenta，项目名称:magenta，代码行数:21，代码来源:[midi_hub.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Fmagenta%2Fmagenta)



## 示例4：testMidiSignal_ValidityChecks

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def testMidiSignal_ValidityChecks(self):
    # Unsupported type.
    with self.assertRaises(midi_hub.MidiHubError):
      midi_hub.MidiSignal(type='sysex')
    with self.assertRaises(midi_hub.MidiHubError):
      midi_hub.MidiSignal(msg=mido.Message(type='sysex'))

    # Invalid arguments.
    with self.assertRaises(midi_hub.MidiHubError):
      midi_hub.MidiSignal()
    with self.assertRaises(midi_hub.MidiHubError):
      midi_hub.MidiSignal(type='note_on', value=1)
    with self.assertRaises(midi_hub.MidiHubError):
      midi_hub.MidiSignal(type='control', note=1)
    with self.assertRaises(midi_hub.MidiHubError):
      midi_hub.MidiSignal(msg=mido.Message(type='control_change'), value=1)

    # Non-inferrale type.
    with self.assertRaises(midi_hub.MidiHubError):
      midi_hub.MidiSignal(note=1, value=1) 
```

开发者ID:magenta，项目名称:magenta，代码行数:22，代码来源:[midi_hub_test.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Fmagenta%2Fmagenta)



## 示例5: SetNoteOn

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def SetNoteOn(note, velocity):
    global previous_note
    if monophonic and previous_note != None:
        SetNoteOff(previous_note, 0)
    # construct the MIDI message
    if midichannel is None:
        msg = mido.Message('note_on', note=note, velocity=velocity)
    else:
        msg = mido.Message('note_on', note=note, velocity=velocity, channel=midichannel)
    # send the MIDI message
    previous_note = note
    outputport.send(msg)
    # schedule a timer to switch it off after the specified duration
    if duration_note != None:
        t = threading.Timer(duration_note, SetNoteOff, args=[note, 0])
        t.start() 
```

开发者ID:eegsynth，项目名称:eegsynth，代码行数:18，代码来源:[outputmidi.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Feegsynth%2Feegsynth)



## 示例6: SetNoteOff

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def SetNoteOff(note, velocity):
    global previous_note
    if monophonic and previous_note != note:
        # do not switch off notes other than the previous one
        return
    # construct the MIDI message
    if midichannel is None:
        msg = mido.Message('note_off', note=note, velocity=velocity)
    else:
        msg = mido.Message('note_off', note=note, velocity=velocity, channel=midichannel)
    # send the MIDI message
    previous_note = None
    outputport.send(msg)


# send the MIDI message, different messages have slightly different parameters 
```

开发者ID:eegsynth，项目名称:eegsynth，代码行数:18，代码来源:[outputmidi.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Feegsynth%2Feegsynth)



## 示例7: run

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def run(self):
        global monitor, scale, offset
        pubsub = r.pubsub()
        pubsub.subscribe('VOLCAKEYS_UNBLOCK')  # this message unblocks the redis listen command
        pubsub.subscribe(self.redischannel)    # this message contains the note
        while self.running:
            for item in pubsub.listen():
                if not self.running or not item['type'] == 'message':
                    break
                if item['channel'] == self.redischannel:
                    monitor.trace(item)
                    # map the Redis values to MIDI values
                    val = EEGsynth.rescale(float(item['data']), slope=scale, offset=offset)
                    val = EEGsynth.limit(val, 0, 127)
                    val = int(val)
                    monitor.update(item['channel'], val)
                    msg = mido.Message('note_on', note=self.note, velocity=val, channel=midichannel)
                    with lock:
                        outputport.send(msg) 
```

开发者ID:eegsynth，项目名称:eegsynth，代码行数:21，代码来源:[volcakeys.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Feegsynth%2Feegsynth)



## 示例8: run

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def run(self):
        pubsub = r.pubsub()
        pubsub.subscribe('VOLCABEATS_UNBLOCK') # this message unblocks the redis listen command
        pubsub.subscribe(self.redischannel)    # this message contains the note
        while self.running:
            for item in pubsub.listen():
                if not self.running or not item['type'] == 'message':
                    break
                if item['channel'] == self.redischannel:
                    monitor.trace(item)
                    # map the Redis values to MIDI values
                    val = EEGsynth.rescale(float(item['data']), slope=scale, offset=offset)
                    val = EEGsynth.limit(val, 0, 127)
                    val = int(val)
                    monitor.update(item['channel'], val)
                    msg = mido.Message('note_on', note=self.note, velocity=val, channel=midichannel)
                    with lock:
                        outputport.send(msg) 
```

开发者ID:eegsynth，项目名称:eegsynth，代码行数:20，代码来源:[volcabeats.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Feegsynth%2Feegsynth)



## 示例9: add_notes

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def add_notes(track, notes, sec_per_tick):
    times_in_ticks = [n.position_in_sec / sec_per_tick for n in notes]
    for ix, note in enumerate(notes):
        time_delta_in_ticks = int(
            times_in_ticks[ix] - (times_in_ticks[ix-1] if ix > 0 else 0))
        track.append(
            Message(
                'note_on',
                note=note.value,
                velocity=note.velocity,
                time=max(time_delta_in_ticks - note.duration, 0)
            )
        )
        track.append(
            Message(
                'note_off',
                note=note.value,
                velocity=note.velocity,
                time=note.duration
            )
        ) 
```

开发者ID:aniawsz，项目名称:rtmonoaudio2midi，代码行数:23，代码来源:[midi.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Faniawsz%2Frtmonoaudio2midi)



## 示例10: save

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def save(self, filename):
        for message in self.messages_to_save:            
            try:
                time_delay = message[1] - previous_message_time                
            except:
                time_delay = 0
            previous_message_time = message[1]

            if(message[0] == "note"):
                self.track.append(Message(message[2], note=int(message[3]), velocity=int(message[4]), time=int(time_delay*40000)))
            else:                
                self.track.append(Message(message[2], channel=int(message[3]), control=int(message[4]),  value=int(message[5]), time=int(time_delay*40000)))
            self.last_note_time = message[1]

        self.messages_to_save = []    
        self.isrecording = False
        self.mid.save('Songs/'+filename+'.mid')        
        menu.render_message("File saved", filename+".mid", 1500) 
```

开发者ID:onlaj，项目名称:Piano-LED-Visualizer，代码行数:20，代码来源:[visualizer.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Fonlaj%2FPiano-LED-Visualizer)



## 示例11: set_button_color

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def set_button_color(self, button_name, color='white', animation=ANIMATION_DEFAULT):
        """Sets the color of the button with given name.
        'color' must be a valid RGB or BW color name present in the color palette. See push2_python.constants.DEFAULT_COLOR_PALETTE for default color names.
        If the button only acceps BW colors, the color name will be matched against the BW palette, otherwise it will be matched against RGB palette.
        'animation' must be a valid animation name from those defined in push2_python.contants.ANIMATION_*. Note that to configure an animation, both the 'start' and 'end'
        colors of the animation need to be defined. The 'start' color is defined by setting a color with 'push2_python.contants.ANIMATION_STATIC' (the default).
        The second color is set setting a color with whatever ANIMATION_* type is desired.
        See https://github.com/Ableton/push-interface/blob/master/doc/AbletonPush2MIDIDisplayInterface.asc#setting-led-colors
        """
        button_n = self.button_name_to_button_n(button_name)
        if button_n is not None:
            button = self.button_map[button_n]
            if button['Color']:
                color_idx = self.push.get_rgb_color(color)
            else:
                color_idx = self.push.get_bw_color(color)
            msg = mido.Message(MIDO_CONTROLCHANGE, control=button_n, value=color_idx, channel=animation)
            self.push.send_midi_to_push(msg) 
```

开发者ID:ffont，项目名称:push2-python，代码行数:20，代码来源:[buttons.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Fffont%2Fpush2-python)



## 示例12: volChanged

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def volChanged(self, source_name, volume):
        self.log.info("Volume "+source_name+" changed to val: "+str(volume))
        results = self.mappingdb.getmany(self.mappingdb.find('input_type == "fader" and bidirectional == 1'))
        if not results:
            self.log.info("no fader results")
            return
        for result in results:


            j=result["action"]%"0"
            k=json.loads(j)["source"]
            self.log.info(k)
            if k == source_name:
                val = int(map_scale(volume, result["scale_low"], result["scale_high"], 0, 127))
                self.log.info(val)

                msgNoC = result.get("out_msgNoC", result["msgNoC"])
                self.log.info(msgNoC)
                portobject = self.getPortObject(result)
                if portobject and portobject._port_out:
                    self.block=True
                    portobject._port_out.send(mido.Message('control_change', channel=0, control=int(result["msgNoC"]), value=val)) 
```

开发者ID:lebaston100，项目名称:MIDItoOBS，代码行数:24，代码来源:[main.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Flebaston100%2FMIDItoOBS)



## 示例13: sceneChanged

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def sceneChanged(self, event_type, scene_name):
        self.log.debug("Scene changed, event: %s, name: %s" % (event_type, scene_name))
        # only buttons can change the scene, so we can limit our search to those
        results = self.mappingdb.getmany(self.mappingdb.find('input_type == "button" and bidirectional == 1'))
        if not results:
            return
        for result in results:
            j = json.loads(result["action"])
            if j["request-type"] != event_type:
                continue
            msgNoC = result.get("out_msgNoC", result["msgNoC"])
            channel = result.get("out_channel", 0)
            portobject = self.getPortObject(result)
            if portobject and portobject._port_out:
                if result["msg_type"] == "control_change":
                    value = 127 if j["scene-name"] == scene_name else 0
                    portobject._port_out.send(mido.Message(type="control_change", channel=channel, control=msgNoC, value=value))
                elif result["msg_type"] == "note_on":
                    velocity = 1 if j["scene-name"] == scene_name else 0
                    portobject._port_out.send(mido.Message(type="note_on", channel=channel, note=msgNoC, velocity=velocity)) 
```

开发者ID:lebaston100，项目名称:MIDItoOBS，代码行数:22，代码来源:[main.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Flebaston100%2FMIDItoOBS)



## 示例14: on_midi

▲ 点赞 6 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def on_midi(self, message):
        if message.type == "clock":
            return

        log.debug("MIDI received: {}".format(message))

        if message.type == "sysex":
            addr = '/sysex'
            arg = ('s', message_to_oscsysexpayload(message))
        else:
            addr = '/midi'
            arg = ('m', message_to_oscmidipayload(message))

        osc = liblo.Message(addr, arg)
        log.debug("Sending OSC {}, {} to: {}:{} UDP: {} URL: {}".format(
            addr,
            arg,
            self.target.get_hostname(),
            self.target.get_port(),
            self.target.get_protocol() == liblo.UDP,
            self.target.get_url()))
        liblo.send(self.target, osc) 
```

开发者ID:velolala，项目名称:touchosc2midi，代码行数:24，代码来源:[touchosc2midi.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2Fvelolala%2Ftouchosc2midi)



## 示例15: dict_msg_to_str

▲ 点赞 5 ▼

```
# 需要导入模块: import mido [as 别名]
# 或者: from mido import Message [as 别名]
def dict_msg_to_str(dict_message):
    msg_type = dict_message.pop('type')
    message = mido.Message(msg_type, **dict_message)

    return mido.format_as_string(message, include_time=False) 
```

开发者ID:FrancescoCeruti，项目名称:linux-show-player，代码行数:7，代码来源:[midi_utils.py](https://vimsky.com/link.php?source=https%3A%2F%2Fgithub.com%2FFrancescoCeruti%2Flinux-show-player)





注：[本文](https://vimsky.com/examples/detail/python-method-mido.Message.html)中的**mido.Message方法**示例由[纯净天空](https://vimsky.com/)整理自Github/MSDocs等开源代码及文档管理平台，相关代码片段筛选自各路编程大神贡献的开源项目，源码版权归原作者所有，传播和使用请参考对应项目的**License**；未经允许，请勿转载。