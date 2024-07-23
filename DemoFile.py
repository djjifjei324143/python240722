#DemoFile.py

#파일 쓰기
f = open("Demo.txt", "Wt", encoding="utf-8")
f.write("첫 번째라인\n두번째라인\n세번째라인\n")
f.close()

#파일 읽기
f = open("Demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

f.close()