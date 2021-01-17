

import re

def test():
    print(f'urine')

def input_Output(keyWord,text,response,message):
    answer=re.search(keyWord,text)
    if answer is not None:
        await message.channel.send(response)
    else:
        return