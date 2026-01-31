# combo
generate a wordlist with info that you have

# How to use it
For example, if your victime have a dog, the name of that dog is steeve, you want to generate a wordlist with every possibility of the name steeve like sTeEVe STEEVE STeeVE etc.
```python
python combo.py -s steeve -o out.txt
```

if now you want to add every possible number you have to add the option -c
```python
python combo.py -s steeve -c 100 -o out.txt 
```
Will generate every combination of steeve + every combination of number. You will see something like steeve steeve0 steeve00 StEevE099...
Every possible combination will be generated for your wordlist.

Enjoy for your ctf.
