import winreg
import os
import re


def get_steam_path():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Valve\Steam"
        )
        steam_path, _ = winreg.QueryValueEx(key, "SteamPath")
        return steam_path
    except FileNotFoundError:
        raise RuntimeError("Steam не найден в реестре")


def get_content_log_path():
    steam_path = get_steam_path()
    return os.path.join(steam_path, "logs", "content_log.txt")


def parse_download_info(log_text):
    game_match = re.searsch(r"Downloading\s+([^\n]+)", log_text)
    paused = "Paused" in log_text 
    
    size_match = re.findall(r"Downloaded\s+(\d+\.?\d*)\s+MB", log_text)
    
    game = game_match.group(1) if game_match else "Неизвестно"
    downloaded = float(size_match[-1]) if size_match else 0.0
    
    status = "Пауза" if paused else "Загрузка"
    
    return game, downloaded, status
