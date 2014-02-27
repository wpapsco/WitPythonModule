WitPythonModule
===============

A python module for the wit.ai natural speech processing service.

Just copy the wit folder into your ```Python27/Lib``` folder.

Example
=======

```python
wit.key = XXXXYOURKEYHEREXXXX
result = wit.query('hello wit!')
if result['outcome']['intent'] == 'greeting':
  print(result['outcome']['entities'])
```
