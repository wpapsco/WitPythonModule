Wit Python Module
=================

A python module for the wit.ai natural speech processing service.

Just copy the wit folder into your ```Python27/Lib``` folder.

You must also have the ```requests``` module installed.

Example
=======

```python
wit.key = 'XXXXYOURKEYHEREXXXX'
result = wit.query('hello wit!')
if result['outcome']['intent'] == 'greeting':
  print(result['outcome']['entities'])
  
result = wit.queryAudio('hello.wav') #only accepts .wav files in the current working directory
if result['outcome']['intent'] == 'greeting':
  print(result['msg_body']) #prints what was said in the audio file
  print(result['outcome']['intent']['entities'])
```
