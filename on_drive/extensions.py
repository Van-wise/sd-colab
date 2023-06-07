import os
import base64
sdw = base64.b64decode(("c3RhYmxlLWRpZmZ1c2lvbi13ZWJ1aQ==").encode('ascii')).decode('ascii')
w = base64.b64decode(("c2Qtd2VidWk=").encode('ascii')).decode('ascii')
webui_dir = f'/content/{sdw}'
gwebui_dir = f'/content/drive/MyDrive/{sdw}'

# deforum-for-automatic1111-webui
os.system(f"rm -rf {gwebui_dir}/extensions/deforum-for-automatic1111-webui")
os.system(f"git clone https://github.com/deforum-art/deforum-for-automatic1111-webui {gwebui_dir}/extensions/deforum-for-automatic1111-webui")
os.system(f"git -C {gwebui_dir}/extensions/deforum-for-automatic1111-webui reset --hard && git -C {gwebui_dir}/extensions/deforum-for-automatic1111-webui pull")

# images-browser
os.system(f"rm -rf {gwebui_dir}/extensions/{sdw}-images-browser")
os.system(f"git clone https://github.com/camenduru/{sdw}-images-browser {gwebui_dir}/extensions/{sdw}-images-browser")
os.system(f"git -C {gwebui_dir}/extensions/{sdw}-images-browser reset --hard && git -C {gwebui_dir}/extensions/{sdw}-images-browser pull")

# {w}-additional-networks
os.system(f"rm -rf {gwebui_dir}/extensions/{w}-additional-networks")
os.system(f"git clone https://github.com/kohya-ss/{w}-additional-networks {gwebui_dir}/extensions/{w}-additional-networks")
os.system(f"git -C {gwebui_dir}/extensions/{w}-additional-networks reset --hard && git -C {gwebui_dir}/extensions/{w}-additional-networks pull")

# {w}-controlnet
os.system(f"rm -rf {gwebui_dir}/extensions/{w}-controlnet")
os.system(f"git clone https://github.com/Mikubill/{w}-controlnet {gwebui_dir}/extensions/{w}-controlnet")
os.system(f"git -C {gwebui_dir}/extensions/{w}-controlnet reset --hard && git -C {gwebui_dir}/extensions/{w}-controlnet pull")

# openpose-editor
os.system(f"rm -rf {gwebui_dir}/extensions/openpose-editor")
os.system(f"git clone https://github.com/fkunn1326/openpose-editor {gwebui_dir}/extensions/openpose-editor")
os.system(f"git -C {gwebui_dir}/extensions/openpose-editor reset --hard && git -C {gwebui_dir}/extensions/openpose-editor pull")

# {w}-tunnels
os.system(f"rm -rf {gwebui_dir}/extensions/{w}-tunnels")
os.system(f"git clone https://github.com/camenduru/{w}-tunnels {gwebui_dir}/extensions/{w}-tunnels")
os.system(f"git -C {gwebui_dir}/extensions/{w}-tunnels reset --hard && git -C {gwebui_dir}/extensions/{w}-tunnels pull")

# batchlinks-webui
os.system(f"rm -rf {gwebui_dir}/extensions/batchlinks-webui")
os.system(f"git clone https://github.com/etherealxx/batchlinks-webui {gwebui_dir}/extensions/batchlinks-webui")
os.system(f"git -C {gwebui_dir}/extensions/batchlinks-webui reset --hard && git -C {gwebui_dir}/extensions/batchlinks-webui pull")

# sdw-catppuccin
os.system(f"rm -rf {gwebui_dir}/extensions/{sdw}-catppuccin")
os.system(f"git clone https://github.com/camenduru/{sdw}-catppuccin {gwebui_dir}/extensions/{sdw}-catppuccin")
os.system(f"git -C {gwebui_dir}/extensions/{sdw}-catppuccin reset --hard && git -C {gwebui_dir}/extensions/{sdw}-catppuccin pull")

# sdw-wd14-tagger
os.system(f"rm -rf {gwebui_dir}/extensions/{sdw}-wd14-tagge")
os.system(f"git clone https://github.com/toriato/{sdw}-wd14-tagger {gwebui_dir}/extensions/{sdw}-wd14-tagge")
os.system(f"git -C {gwebui_dir}/extensions/{sdw}-wd14-tagge reset --hard && git -C {gwebui_dir}/extensions/{sdw}-wd14-tagge pull")

# {w}-prompt-all-in-one
os.system(f"rm -rf {gwebui_dir}/extensions/{w}-prompt-all-in-one")
os.system(f"git clone https://github.com/Physton/{w}-prompt-all-in-one {gwebui_dir}/extensions/{w}-prompt-all-in-one")
os.system(f"git -C {gwebui_dir}/extensions/{w}-prompt-all-in-one reset --hard && git -C {gwebui_dir}/extensions/{w}-prompt-all-in-one pull")

# sdw-localization-zh_CN
os.chdir(gwebui_dir)
os.system(f"rm -rf {gwebui_dir}/extensions/{sdw}-localization-zh_CN")
os.system(f"git clone https://github.com/dtlnor/{sdw}-localization-zh_CN {gwebui_dir}/extensions/{sdw}-localization-zh_CN")
os.system(f"git -C {gwebui_dir}/extensions/{sdw}-localization-zh_CN reset --hard && git -C {gwebui_dir}/extensions/{sdw}-localization-zh_CN pull")

#lycoris
os.chdir(gwebui_dir)
os.system(f"rm -rf {gwebui_dir}/extensions/a1111-{w}-lycoris")
os.system(f"git clone https://github.com/KohakuBlueleaf/a1111-{w}-lycoris {gwebui_dir}/extensions/a1111-{w}-lycoris")
os.system(f"git -C {gwebui_dir}/extensions/a1111-{w}-lycoris reset --hard && git -C {gwebui_dir}/extensions/a1111-{w}-lycoris pull")

# config.json
if not os.path.isfile(f"{gwebui_dir}/config.json"):
    os.system(f"wget -O {gwebui_dir}/config.json https://jihulab.com/vanwise/{w}-colab/-/raw/main/config.json")