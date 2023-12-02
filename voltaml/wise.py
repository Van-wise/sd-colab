import os
def fix_clip(main_dir):
    file_path = f"{main_dir}/core/interrogation/clip.py"

    with open(file_path, 'r') as file:
        file_content = file.read()
    new_content = file_content.replace("https://huggingface.co/pharma/ci-preprocess/resolve/main/", "https://huggingface.co/pharmapsychotic/ci-preprocess/tree/main")
    with open(file_path, 'w') as file:
        file.write(new_content)


def fix_api(main_dir):
    file_path = f"{main_dir}/requirements/api.txt"

    with open(file_path, 'r') as file:
        file_content = file.readlines()

    for i in range(len(file_content)):
        if "pyngrok==6.0.0" in file_content[i]:
            file_content[i] = file_content[i].replace("pyngrok==6.0.0", "pyngrok==7.0.0")

    file_content.append("pycloudflared==0.2.0\n")

    with open(file_path, 'w') as file:
        file.writelines(file_content)

def fix_pytorch(main_dir):
    file_path = f"{main_dir}/requirements/pytorch.txt"

    with open(file_path, 'r') as file:
        file_content = file.read()

    # 替换 "boto3==1.26.153" 为 "boto3==1.28.63"
    new_content = file_content.replace("boto3==1.26.153", "boto3==1.28.63")

    # 添加一行 "urllib3==2.0.6"
    new_content += "\nurllib3==2.0.6\n"

    with open(file_path, 'w') as file:
        file.write(new_content)

def fix_colab(main_dir):
    fix_clip(main_dir)
    fix_api(main_dir)
    fix_pytorch(main_dir)

#---
import pandas as pd
import requests
from io import BytesIO
from google.colab import files, drive
from concurrent import futures

def checkmod_link(link):
  response = requests.get(link)
  if response.status_code == 200:
      content = response.content
      try:
          df = pd.read_excel(BytesIO(content))
          print("MOD读取成功!")
          return df
          #print(df.head())
      except Exception as e:
          print("无法正确读取文件,请检查文件格式是否为'.xlsx' :", str(e))
  else:
      print("无法获取文件,请检查链接是否正确!")

def checkmod_path(path):
  try:
    df = pd.read_excel(path)
    print("MOD读取成功!")
    return df
    #print(df.head())
  except Exception as e:
    print("无法正确读取文件,请检查文件格式是否为'.xlsx' :", str(e))

def checkmod_up():
    while True:
        try:
            uploaded = files.upload()
            if not uploaded:
                print("取消上传,使用默认MOD!")
                mod = 'https://github.com/Van-wise/sd-colab/raw/main/wise.xlsx'
                df = pd.read_excel(mod)
                break
            mod_file = os.path.join(os.getcwd(), list(uploaded.keys())[0])
            df = pd.read_excel(mod_file)
            print("MOD读取成功!")
            break  # Exit the loop if the file is successfully read

        except (ValueError, Exception) as e:
            os.remove(mod_file)
            print("无法正确读取文件，请检查文件格式是否为'.xlsx':", str(e))
            print("请重新上传文件。")
    return df

def download_mod(file_dLlink, save_dir, file_name, index):
    try:
        os.system(f"aria2c --console-log-level=error -q -c -x 16 -s 16 -k 1M {file_dLlink} -d {save_dir} -o {file_name}")
        print(f"第{index+1}行:{file_name}下载成功!")
    except Exception as e:
        print(f"第{index+1}行:{file_name}文件下载错误：", e)

from concurrent import futures

def start_mod(mod_link,mod_path,modelr_dir):
    if mod_link:
        df = checkmod_link(mod_link)
    elif mod_path:
        df = checkmod_path(mod_path)
    else:
        df = checkmod_up()
    df = df.fillna("")

    with futures.ThreadPoolExecutor() as executor:
        future_to_index = {}

        for index, row in df.iterrows():
            file_switch, file_name, file_type, file_dLlink = row[["开关", "名称", "类型", "下载地址"]]

            if any(value == "" for value in [file_switch, file_name, file_type, file_dLlink]):
                print(f"跳过,第{index+1}行,因为:|{'|'.join([key for key, value in row.items() if value == ''])}|的内容不能为空!")
                continue

            save_dir = os.path.join(modelr_dir, file_type)
            file_path = os.path.join(save_dir, file_name)

            if not os.path.exists(file_path) and file_switch == "on":
                future = executor.submit(download_mod, file_dLlink, save_dir, file_name, index)
                future_to_index[future] = index

        for future in futures.as_completed(future_to_index):
            index = future_to_index[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"第{index+1}行下载错误:", e)
    print("MOD运行完成...🎉")