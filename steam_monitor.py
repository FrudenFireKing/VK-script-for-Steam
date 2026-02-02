# steam_monitor.py
import time

from steam_utils import (
    get_content_log_path,
    parse_download_info,
    get_total_net_mb
)

INTERVAL = 60
TOTAL_MINUTES = 5
LOW_SPEED_THRESHOLD = 1.0
PAUSE_MINUTES = 2


def read_log_tail(path, lines=300):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return "".join(f.readlines()[-lines:])


def main():
    log_path = get_content_log_path()

    prev_net = None
    low_speed_counter = 0

    for minute in range(1, TOTAL_MINUTES + 1):
        try:
            log_text = read_log_tail(log_path)
            game = parse_download_info(log_text)
        except Exception:
            game = "Неизвестная игра"

        current_net = get_total_net_mb()

        if prev_net is not None:
            speed = max(current_net - prev_net, 0)
        else:
            speed = 0.0

        if speed < LOW_SPEED_THRESHOLD:
            low_speed_counter += 1
        else:
            low_speed_counter = 0

        if low_speed_counter >= PAUSE_MINUTES:
            status = "Пауза"
        else:
            status = "Загрузка"

        print(
            f"{minute} min | {game} | {speed:.2f} MB/min | {status}"
        )

        prev_net = current_net
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()