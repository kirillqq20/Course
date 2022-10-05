import json
def decode_text():
    with open('text.txt', 'rt') as file:
        data = file.read()
        dict = json.load(open('dict.json', 'rt'))
        content = ''
        for key in data:
            if key in dict:
                content += dict[key]
            else:
                content += key
        return content  



def decode_bin():
    with open('0008.bin', 'rb') as file:
        data = file.read()
        dict = json.load(open('0008.json', 'rt'))
        new_dict={}
        for i in dict:
          new_dict[int(i)]=dict[i]
        content = ''
        for key in data:
            if key in new_dict:
                content += new_dict[key]
            else:
                content += chr(key)
        return content