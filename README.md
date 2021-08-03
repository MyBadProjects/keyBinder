# keyBinder
This is a Python (3.9.4) module which binds a function to a key. It has been tested on Linux (requires console to be open but not focued) and works *perfectly* from my testing.

## How it works
This works by detecting keypresses using `keyboard`. The way it detects the keypress is by having a seperate thread which awaits keypresses, and on a press, calls the callback with the key (only). 

No keypresses should be delayed due to each one running on it's own thread, in theory.

## How to use
First of all `keyboard` installed as a module, do it now. Next you need to reference keyBinder by adding `import keyBinder` or `from keyBinder import Bind` into your script. Now to actually use it! It is pretty basic with some settings (toggles) and others. Here is the `__init__` of the class so you can farmiliarize yourself with the function.

```python
def __init__(self, key='q', callback=print, rappid_fire=False, print_data=True, close_on_error=True, end_on_press=False):
```

So to use this you would have to do `Bind('q', print)` to print the key (q) when pressed.
There is nothing else to the script as it is just a single class for simplisity!
