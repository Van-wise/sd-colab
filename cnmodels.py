# -*- coding: utf-8 -*-
import os
import base64
import binascii
import subprocess
from urllib.parse import urlparse
from IPython.display import clear_output

sdw = binascii.a2b_uu("6<W1A8FQE+61I9F9U<VEO;BUW96)U:0``").decode('utf-8')
w = binascii.a2b_uu("(<V0M=V5B=6D`").decode('utf-8')
sai = binascii.a2b_uu("=<W1A8FQE+61I9F9U<VEO;BUS=&%B:6QI='DM86D`").decode('utf-8')
sd = binascii.a2b_uu("04W1A8FQE+61I9F9U<VEO;@``").decode('utf-8')
saa = sdw + "-assets"

webui_dir = '/root/main'
gwebui_dir = f'/content/drive/MyDrive/main'

def download(url, model_dir):
    filename = os.path.basename(urlparse(url).path)
    pth = os.path.abspath(os.path.join(model_dir, filename))
    if not os.path.exists(pth):
        print('Downloading: ' + os.path.basename(url))
        cmd = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d {model_dir} -o {filename} {url}"
        subprocess.run(cmd, shell=True, check=True)
    else:
        print(f"[1;32mThe model {filename} already exists[0m")

def cndown_colab():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-colab/main/cndown_colab.txt")
    mdldir = f"{webui_dir}/extensions/sd-webui-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt CN_models_v2.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()

def cndown_drive():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-colab/main/cndown_colab.txt")
    mdldir = f"{gwebui_dir}/extensions/sd-webui-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt CN_models_v2.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()