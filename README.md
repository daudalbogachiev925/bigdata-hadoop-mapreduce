# Big Data: Hadoop MapReduce

Практическая работа по обработке больших данных с использованием Hadoop MapReduce.

## Задача
Анализ логов веб-сервера: подсчёт количества запросов по IP-адресам.

## Стек
- Python 3
- Hadoop Streaming
- HDFS

## Файлы
- `mapper.py` — маппер
- `reducer.py` — редьюсер
- `logs.txt` — пример входных данных

## Запуск
```bash
hadoop jar hadoop-streaming.jar \
  -input /logs \
  -output /output \
  -mapper mapper.py \
  -reducer reducer.py
