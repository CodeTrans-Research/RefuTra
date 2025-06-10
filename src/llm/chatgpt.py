import openai
import os
import json
OPENAI_API_KEY="???"
def ask(question):
    url="https://api.openai.com/v1"
    openai.api_key = OPENAI_API_KEY
    openai.api_base = url
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",messages=[{"role":"user","content":question}],stream=False
    )
    ans=res.choices[0].message.content
    return ans
def translate(fr,to,code):
    question=f"Translate the following {fr} code to {to}.Do not need to create main function:\n{code}"
    url="https://api.openai.com/v1"
    openai.api_key = OPENAI_API_KEY
    openai.api_base = url
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",messages=[{"role":"user","content":question}],stream=False
    )
    ans=res.choices[0].message.content
    return ans
def translateFiles(fr,to):
    frpath = f"dataset/{fr}2{to}/{fr}"   
    topath = f"result/translate/chatgpt/{fr}2{to}/{to}"
    cnt = 0
    extdic = {"java":".java","python":".py","c++":".cpp"}
    for _,_,fs in os.walk(frpath):
        for f in fs:
            filename,_ = os.path.splitext(f)
            '''if filename not in errnameset:
                continue'''
            
            code = open(os.path.join(frpath,f),"r").read()
            trcode = translate(fr,to,code)
            open(os.path.join(topath,filename+extdic[to]),"w").write(trcode)
            cnt += 1
            print(f"{cnt}:{f}")

if __name__ == "__main__":
    #translateFiles("java","python")
    #translateFiles("python","java")
    #translateFiles("java","cpp")
