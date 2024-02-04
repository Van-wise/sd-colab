import re
import os
def replace_download_models(_version):
  with open(f"/content/{_version}/launch.py", "r") as f:
    code = f.read()

  # 使用正则表达式匹配第二个 download_models() 函数
  match = re.search(r"(?s)def download_models\(\):\n(.*?)\n\s+download_models\(\)", code)

  # 如果匹配成功，则将第二个 download_models() 函数替换为 #download_models()
  if match:
    code = code.replace(match.group(0), f"def download_models():\n{match.group(1)}\n#download_models()")

  # 将修改后的代码写入 launch.py 文件
  with open(f"/content/{_version}/launch.py", "w") as f:
    f.write(code)

models = []

class Data:
    def __init__(self, name, url, path):
        self.name = name
        self.url = url
        self.path = path

    def __str__(self):
        return f"Name: {self.name}, URL: {self.url}, Path: {self.path}"

def add_model(name, url, path):
    model = Data(name, url, path)
    models.append(model)

def add_juggernautxl(main_dir):
    add_model("juggernautXL_v8Rundiffusion.safetensors", "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/juggernautXL_v8Rundiffusion.safetensors", f"{main_dir}/models/checkpoints/") 
    add_model("sd_xl_offset_example-lora_1.0.safetensors", "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_offset_example-lora_1.0.safetensors", f"{main_dir}/models/loras/")

def add_realistic(main_dir):
    add_model("realisticStockPhoto_v20.safetensors", "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/realisticStockPhoto_v20.safetensors", f"{main_dir}/models/checkpoints/")
    add_model("SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors", "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors", f"{main_dir}/models/loras/")

def add_anime(main_dir):
    add_model("animaPencilXL_v100.safetensors", "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/animaPencilXL_v100.safetensors", f"{main_dir}/models/checkpoints/")
    add_model("DreamShaper_8_pruned.safetensors", "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/DreamShaper_8_pruned.safetensors", f"{main_dir}/models/checkpoints/")
    add_model("sd_xl_offset_example-lora_1.0.safetensors", "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_offset_example-lora_1.0.safetensors", f"{main_dir}/models/loras/")
    add_model("unaestheticXLv31.safetensors", "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/unaestheticXLv31.safetensors", f"{main_dir}/models/embeddings/")

def add_sai(main_dir):
    add_model("sd_xl_base_1.0_0.9vae.safetensors", "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0_0.9vae.safetensors", f"{main_dir}/models/checkpoints/")
    add_model("sd_xl_refiner_1.0_0.9vae.safetensors", "https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0_0.9vae.safetensors", f"{main_dir}/models/checkpoints/")
    add_model("sd_xl_offset_example-lora_1.0.safetensors", "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_offset_example-lora_1.0.safetensors", f"{main_dir}/models/loras/")

def add_controlnet(main_dir,cn,ip,face):
    add_model("fooocus_ip_negative.safetensors", "https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_ip_negative.safetensors", f"{main_dir}/models/controlnet/")
    if cn:
        add_model("control-lora-canny-rank128.safetensors", "https://huggingface.co/lllyasviel/misc/resolve/main/control-lora-canny-rank128.safetensors", f"{main_dir}/models/controlnet/")
        add_model("fooocus_xl_cpds_128.safetensors", "https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_xl_cpds_128.safetensors", f"{main_dir}/models/controlnet/")
    if ip:
        add_model("ip-adapter-plus_sdxl_vit-h.bin", "https://huggingface.co/lllyasviel/misc/resolve/main/ip-adapter-plus_sdxl_vit-h.bin", f"{main_dir}/models/controlnet/")
    if face:   
        add_model("ip-adapter-plus-face_sdxl_vit-h.bin", "https://huggingface.co/lllyasviel/misc/resolve/main/ip-adapter-plus-face_sdxl_vit-h.bin", f"{main_dir}/models/controlnet/")

def add_other(main_dir):
    add_model("sdxl_lcm_lora.safetensors", "https://huggingface.co/lllyasviel/misc/resolve/main/sdxl_lcm_lora.safetensors", f"{main_dir}/models/loras/")
    add_model("clip_vision_vit_h.safetensors", "https://huggingface.co/lllyasviel/misc/resolve/main/clip_vision_vit_h.safetensors", f"{main_dir}/models/clip_vision/")
    add_model("fooocus_upscaler_s409985e5.bin", "https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_upscaler_s409985e5.bin", f"{main_dir}/models/upscale_models/")
    add_model("pytorch_model.bin", "https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_expansion.bin", f"{main_dir}/models/prompt_expansion/fooocus_expansion/")

def add_vaeapp(main_dir):
    add_model("xlvaeapp.pth", "https://huggingface.co/lllyasviel/misc/resolve/main/xlvaeapp.pth", f"{main_dir}/models/vae_approx/")
    add_model("vaeapp_sd15.pth", "https://huggingface.co/lllyasviel/misc/resolve/main/vaeapp_sd15.pt", f"{main_dir}/models/vae_approx/")
    add_model("xl-to-v1_interposer-v3.1.safetensors", "https://huggingface.co/lllyasviel/misc/resolve/main/xl-to-v1_interposer-v3.1.safetensors", f"{main_dir}/models/vae_approx/")

import requests
from urllib.parse import unquote
import re

def get_models_name(link):
    response = requests.get(link, stream=True)
    if response.status_code == 200:
        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            file_name = unquote(content_disposition.split('filename=')[1])
        else:
            file_name = unquote(link.split("/")[-1])
        return re.sub(r'[";]','', file_name)
    else:
        return None  

def add_custom_ckpt(main_dir, links):
    if not links:  # 判断links是否为空值
      return  # 如果为空值，直接返回
    models_name = get_models_name(links)
    if models_name:
        add_model(models_name, links, f"{main_dir}/models/checkpoints/")

def add_custom_loras(main_dir,links):
    if not links:  # 判断links是否为空值
      return  # 如果为空值，直接返回
    models_name = get_models_name(links)
    if models_name:
        add_model(models_name, links, f"{main_dir}/models/loras/")

def add_custom_embeddings(main_dir,links):
    if not links:  # 判断links是否为空值
      return  # 如果为空值，直接返回
    models_name = get_models_name(links)
    if models_name:
        add_model(models_name, links, f"{main_dir}/models/embeddings/")

def add_inpaint(main_dir,_inpaint):
    add_model("fooocus_inpaint_head.pth", "https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/fooocus_inpaint_head.pth", f"{main_dir}/models/inpaint/")
    if _inpaint == "v1":
        add_model("inpaint.fooocus.patch", "https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/inpaint.fooocus.patch", f"{main_dir}/models/inpaint/")
    elif _inpaint == "v2.5":
        add_model("inpaint_v25.fooocus.patch", "https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/inpaint_v25.fooocus.patch", f"{main_dir}/models/inpaint/")
    else:
        add_model("inpaint_v26.fooocus.patch", "https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/inpaint_v26.fooocus.patch", f"{main_dir}/models/inpaint/")

def download_models(model):
    try:
        os.system(f"aria2c --console-log-level=error -q -c -x 16 -s 16 -k 1M -d {model.path} -o {model.name} {model.url}")
    except Exception as e:
        print(f"{model.name}", "文件下载错误：", e)

from concurrent import futures

def start_download_models(models):
    with futures.ThreadPoolExecutor() as executor:
        future_to_model = {}

        for model in models:
            future = executor.submit(download_models, model)
            future_to_model[future] = model

        for future in futures.as_completed(future_to_model):
            model = future_to_model[future]
            try:
                future.result()
                print(model.name, "下载成功!")
            except Exception as e:
                print(model.name, "文件下载错误：", e)

    print("所有模型下载完成...🎉")

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
#---
def set_default_ckpt(main_dir, ckpt_link):
    dm_path = f"{main_dir}/presets/default.json"

    if not ckpt_link:  # 判断links是否为空值
      return  # 如果为空值，直接返回
    models_name = get_models_name(ckpt_link)

    with open(dm_path, 'r') as file:
        file_content = file.read()
    new_content = file_content.replace('juggernautXL_v8Rundiffusion.safetensors', models_name)
    with open(dm_path, 'w') as file:
        file.write(new_content)

def set_default_loars(main_dir, loars_link):
    dm_path = f"{main_dir}/presets/default.json"

    if not loars_link:  # 判断links是否为空值
      return  # 如果为空值，直接返回
    models_name = get_models_name(loars_link)

    with open(dm_path, 'r') as file:
        file_content = file.read()
    new_content = file_content.replace('sd_xl_offset_example-lora_1.0.safetensors', models_name)
    with open(dm_path, 'w') as file:
        file.write(new_content)
#---
def fix_fooocus_expansion(main_dir):
    file_names = ["config.json",
                "merges.txt",
                "positive.txt",
                "special_tokens_map.json",
                "tokenizer.json",
                "tokenizer_config.json",
                "vocab.json"]

    expansion_dir = f"{main_dir}/models/prompt_expansion/fooocus_expansion"
    for file_name in file_names:
        url = "https://github.com/lllyasviel/Fooocus/raw/main/models/prompt_expansion/fooocus_expansion/" + file_name
        os.system(f"aria2c --console-log-level=error -q -c -x 16 -s 16 -k 1M -d {expansion_dir} -o {file_name} {url}")

def fix_fooocus_ripemd160(main_dir):
    tokendid_dir = f"{main_dir}/enhanced/token_did.py"
    with open(tokendid_dir, 'r') as file:
        file_content = file.read() 
    new_content = file_content.replace("ripemd160", "sha256")
    with open(tokendid_dir, 'w') as file:
        file.write(new_content)        
        
def fix_fooocus_clip(main_dir):
    clip_dir = f"{main_dir}/ldm_patched/modules/sd1_clip.py"
    with open(clip_dir, 'r') as file:
        file_content = file.read()
    new_content = file_content.replace("transformers", "transformers.models.clip")
    with open(clip_dir, 'w') as file:
        file.write(new_content)


#async_gradio_app.local_url = 'http://127.0.0.1:7865/'



