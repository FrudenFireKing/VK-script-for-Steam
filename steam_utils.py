import os
import re
import winreg
import psutil


def get_steam_path():
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Valve\Steam"
    )
    steam_path, _ = winreg.QueryValueEx(key, "SteamPath")
    return steam_path


def get_content_log_path():
    steam_path = get_steam_path()
    log_path = os.path.join(steam_path, "logs", "content_log.txt")
    if not os.path.exists(log_path):
        raise RuntimeError("content_log.txt not found")
    return log_path


def parse_download_info(log_text):
    patterns = [
        r"Downloading\s+(.+)",
        r"Starting download of\s+(.+)",
        r"AppID\s+\d+\s+\((.+)\)"
    ]

    for pattern in patterns:
        match = re.search(pattern, log_text)
        if match:
            return match.group(1).strip()

    chunk_match = re.search(r"chunks for depot\s+(\d+)", log_text)
    if chunk_match:
        return f"Depot {chunk_match.group(1)}"

    return "Неизвестная игра"


def get_total_net_mb():
    net = psutil.net_io_counters()
    return net.bytes_recv / (1024 * 1024)