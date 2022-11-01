#要先讀檔
def readfile(file_name):
  txt = []
  with open(file_name, 'r') as f:
    for line in f:
      txt.append(line.strip())
  return txt


#轉換檔案
def convert(txt):
  new = []
  for line in txt:
    if line == 'Allen':
      person = 'Allen'
      continue
    elif line == 'Tom':
      person = 'Tom'
      continue
    new.append(person + ': ' + line)
  return (new)


#寫出檔案
def write_outfile(file_name, new):
  with open(file_name, 'w') as f:
    for line in new:
      f.write(line + '\n')


def main(file_name_1, file_name_2):
  txt = readfile(file_name_1)
  new = convert(txt)
  write_outfile(file_name_2, new)


main('input.txt', 'output.txt')
