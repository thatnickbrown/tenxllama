# TenXLlama
Who needs a 10x programmer when you have a TenXLlama? Just tell the Llama what you want your program to do in plain English and it will spit out fully-functional code, ready to run.

## Requirements
- conda/miniconda CUDA environment with [Code Llama](https://github.com/facebookresearch/codellama) installed
- either an RTX 4090 or a lot of patience

## Example
Ask it to write a server, then run it:
```
$ torchrun tenxllama.py
  ...
TenXLlama will write any program you like.
What would you like the program to do?
➡️ listen for UDP packets on port 2222 and print their contents
What would you like to call your program?
➡️ llama_listens
Your program is complete. You can run it with ./llama_listens (assuming you have the required modules.)
$ ./llama_listens
han shot first
bring back firefly
```
Ask it to write a client, then use it...
```
$ torchrun tenxllama.py
  ...
TenXLlama will write any program you like.
What would you like the program to do?
➡️ send its command line argument via UDP to port 2222 on localhost and then exit
What would you like to call your program?
➡️ llama_speaks
Your program is complete. You can run it with ./llama_speaks (assuming you have the required modules.)
$ ./llama_speaks "han shot first"
$ ./llama_speaks "bring back firefly"
```

When studying AI in college this kind of thing would have seemed like sci-fi. It turns out 7 billion neural net parameters ought to be enough for anybody.