from typing import Optional
import os
import fire
from llama import Llama

LLM_LOCATION = '../codellama/'

def main(
    ckpt_dir: Optional[str] = LLM_LOCATION+'CodeLlama-7b-Python/',
    tokenizer_path: Optional[str] = LLM_LOCATION+'CodeLlama-7b-Python/tokenizer.model',
    temperature: float = 0.2,
    top_p: float = 0.95,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    print("TenXLlama will write any program you like.")

    instructions = [
        [
            {
                "role": "user",
                "content": "Write an executable python3 program for linux that "+
                input("What would you like the program to do?\n➡️ "),
            },
        ],
    ]
    filename = input("What would you like to call your program?\n➡️ ")
    results = generator.chat_completion(
        instructions,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    with open(filename, 'w') as prog:
        prog.write(results[0]['generation']['content'].lstrip())
    os.chmod(filename, 0o700)

    print(f"Your program is complete. You can run it with ./{filename} (assuming you have the required modules.)")

if __name__ == "__main__":
    fire.Fire(main)
