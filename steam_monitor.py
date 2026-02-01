import time
from steam_utils import get_content_log_path, parse_download_info


INTERVAL = 60
TOTAL_MINUTES = 5


def read_log_tail(path, lines=200):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return "".join(f.readlines()[-lines:])


def main():
    log_path = get_content_log_path()
    print("Steam Download Monitoring запущен\n")
    
    prev_downloaded = None
    
    for minute in range(1, TOTAL_MINUTES + 1):
        log_text = read_log_tail(log_path)
        game, downloaded, status = parse_download_info(log_text)
        
        if prev_downloaded is not None:
            speed = max(downloaded - prev_downloaded, 0)
        else:
            speed = 0
            
        print(
            f"{minute} мин | {game} |"
            f"{speed:.2f} Мб/мин | {status}"
        )
        
        prev_downloaded = downloaded
        time.sleep(INTERVAL)
        
        
if __name__ == "__main__":
    main()