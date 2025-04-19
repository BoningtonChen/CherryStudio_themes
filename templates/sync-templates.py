import os
import requests
import argparse
from urllib.parse import urlparse

def download_github_folder(url, output_dir=None):
    """
    从GitHub文件夹URL下载所有文件到本地
    
    参数:
        url (str): GitHub文件夹URL (如: https://github.com/user/repo/tree/branch/path/to/folder)
        output_dir (str): 本地输出目录 (默认为脚本所在目录)
    """
    # 转换GitHub URL为API URL
    parsed = urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    
    if len(path_parts) < 5 or path_parts[2] != 'tree':
        print("错误: 无效的GitHub文件夹URL")
        return
    
    user = path_parts[0]
    repo = path_parts[1]
    branch = path_parts[3]
    folder_path = '/'.join(path_parts[4:])
    
    api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{folder_path}?ref={branch}"
    
    # 设置输出目录
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    else:
        output_dir = os.path.abspath(output_dir)
    
    # 创建输出目录(如果不存在)
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        contents = response.json()
        
        for item in contents:
            if item['type'] == 'file':
                file_url = item['download_url']
                file_path = os.path.join(output_dir, item['name'])
                
                print(f"下载: {item['name']}")
                file_response = requests.get(file_url)
                file_response.raise_for_status()
                
                with open(file_path, 'wb') as f:
                    f.write(file_response.content)
                    
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='从GitHub文件夹下载所有文件')
    parser.add_argument('url', help='GitHub文件夹URL')
    parser.add_argument('--output', '-o', help='输出目录(默认为脚本所在目录)')
    
    args = parser.parse_args()
    download_github_folder(args.url, args.output)