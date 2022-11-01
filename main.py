#要先讀檔
txt = []
with open('input.txt', 'r') as f:
  for line in f:
    txt.append(line.strip())

print(txt)

#轉換檔案
new = []
for line in txt:
  if line == 'Allen':
    person = 'Allen'
    continue
  elif line == 'Tom':
    person = 'Tom'
    continue
  new.append(person + ': ' + line)

print(new)

#寫出檔案
with open('output.txt', 'w') as f:
  for line in new:
    f.write(line + '\n')
