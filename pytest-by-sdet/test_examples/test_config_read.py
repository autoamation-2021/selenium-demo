import os

config_path = os.path.join(os.path.abspath(os.curdir), 'configurations', 'config.ini')
print("Config Path:", config_path)
print("File Exists:", os.path.exists(config_path))