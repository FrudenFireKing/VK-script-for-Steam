# VK-script-for-Steam
ENG - Script for monitoring Steam game download speed in the background  
RUS - Скрипт для мониторинга скорости загрузки игр в Steam в фоновом режиме


## Возможности
- Автоматическое определение пути установки Steam
- Определение текущей загружаемой игры
- Учет паузы загрузки
- Вывод скорости загрузки каждую минуту (5 минут)

## Как работает?
Скрипт анализирует логи Steam (`content_log.txt`), извлекая информацию о процессе загрузки. 

## Запуск
```bash
pip install -r requirements.txt
python steam_monitor.py
