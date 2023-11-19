import os
import re
import shutil
import random

def add(directory,string):
    for folders,subFolders,files in os.walk(directory):
        for file in files:
            fileWithExt = os.path.splitext(file)
            shutil.move(folders + "\\" + file, folders + "\\" + fileWithExt[0] + string + fileWithExt[1])
            
def replace(word,new_word,directory):
    listOfTitles = []
    count=0
    for folders,subFolders,files in os.walk(directory):
        for file in files:
            listOfTitles.append(file)
    if word == ".":
        print("this is a dot and you are stupid")
        return 0
    else:
        subRegex = re.compile(word)
        for folders,subFolders,files in os.walk(directory):
            for file in files:
                count+=1
                rn = random.randint(0,1000000000)
                fileWithExt = os.path.splitext(file)
                if subRegex.sub(new_word,fileWithExt[0])+fileWithExt[1] == file or subRegex.sub(new_word,fileWithExt[0]) == "":
                    pass
                else:
                    if subRegex.sub(new_word,fileWithExt[0])+fileWithExt[1] in listOfTitles:
                        if subRegex.sub(new_word,fileWithExt[0]) +"Copy "+"("+str(count)+str(rn)+")"+ fileWithExt[1] in listOfTitles:
                            break
                        else:
                            shutil.move(folders + "\\" + file, folders + "\\" + subRegex.sub(new_word,fileWithExt[0]) +"Copy "+"("+str(count)+str(rn)+")"+ fileWithExt[1])
                    else:
                        shutil.move(folders + "\\" + file, folders + "\\" + subRegex.sub(new_word,fileWithExt[0]) + fileWithExt[1])