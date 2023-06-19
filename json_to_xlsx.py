import csv
import json
import warnings
import openpyxl
warnings.simplefilter(action='ignore', category=FutureWarning)

output_file_name = "csvfile/ex6.xlsx"


with open('output/ex6.json', encoding='utf-8') as f:
  json_data = json.load(f)


datas = []
index=0
index_2=0

for i in range(len(json_data['images'][0]["fields"])):
  data = json_data['images'][0]["fields"][i]['inferText']
  print(data)
  if data == "구매":
    datas = datas
    index = 1
  elif data == "데이터":
    datas = datas
  elif data == "일용인부":
    datas = datas
    index = 2
  elif data == "인력":
    datas = datas
  elif data == "농자재":
    datas = datas
    index_2 = 3
  elif data == "구매량":
    datas = datas
  elif data == "(kg)":
    datas = datas
  elif data == "총":
    datas = datas
  elif data == "근무시간":
    datas.append("총 근무시간")
  elif data == "박스(개)":
    datas.append("구매량(kg)")
    datas.append("박스(개)")
  else:
    datas.append(data)
    print("done")


print(datas)
print(index)
print(index_2)




if index == 1:
  new_data = []
  if datas[0] == "날짜":
    for i in range(0, 8, 8):
      new_data.append(datas[i:i + 8])
    for i in range(8,len(datas),8):
      new_data.append(datas[i:i + 8])
  else:
    new_data.append(["날짜","품목","구매량(kg)","박스(개)","가격","이름","전화번호","주소"])
    for i in range(0,len(datas),8):
      new_data.append(datas[i:i + 8])

if index == 2:
  new_data = []
  if datas[0] =="연도":
    for i in range(0, 5, 5):
      new_data.append(datas[i:i + 5])
    for i in range(5, len(datas), 5):
      new_data.append(datas[i:i + 5])
  else:
    new_data.append(["연도","근무일수","총 근무시간","이름","연락처"])
    for i in range(0,len(datas),5):
      new_data.append(datas[i:i + 5])


if index_2 == 3:
  new_data = []
  if datas[0] == "날짜":
    b = 0
    for i in range(0, 4, 4):
      new_data.append(datas[i:i + 4])
    for i in range(4, len(datas)):
      if i % 4 == 3:
        a = i- b
        if datas[a] == "외상":
          new_data.append(datas[a-3:a+1])
        else:
          b = b + 1
          new_data.append(datas[a-3:a])
  else:
    new_data.append(["날짜", "품목", "개수", "비고"])
    b = 0
    for i in range(0, len(datas)):
      if i % 4 == 3:
        a = i - b
        if datas[a] == "외상":
          new_data.append(datas[a - 3:a + 1])
        else:
          b = b + 1
          new_data.append(datas[a - 3:a])


print(new_data)



wb = openpyxl.Workbook()
ws = wb.active

for i in range(len(new_data)):
    for j in range(len(new_data[i])):
        cell = ws.cell(row=i+1, column=j+1)
        cell.value = new_data[i][j]

wb.save(output_file_name)