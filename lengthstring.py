def length(str):
    count=0
    if str !="":
        for char in str:
            count+=1
    return count
print(length("hello world"))