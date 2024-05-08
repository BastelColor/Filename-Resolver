import json
import os
from rich.progress import track

if input("実行してもよろしいですか？(Y/n)") != ("Y" or "y"):
    exit()

#read Catalog
with open("MediaPatch/MediaCatalog.json", "r") as json_file:
    MediaCatalog = json.load(json_file)

folder_path = "MediaPatch/"
files = os.listdir(folder_path)
for file_name in track(files, description="ファイル名変更中..."):
    file_path = os.path.join(folder_path, file_name)
    file_size = os.path.getsize(file_path)

    for key, value in MediaCatalog["Table"].items():
        try:
            if value["Bytes"] == file_size:
                new_file_name = value["FileName"]
                if file_name == new_file_name:
                    break
                os.rename(file_path, os.path.join(folder_path, new_file_name))
                break
        except FileExistsError:
            continue

print("ファイル名の変更が完了しました！")
os.system("Pause")