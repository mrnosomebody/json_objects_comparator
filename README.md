### Команда для запуска
```python main.py --api_url <url> --comparison_parameter id --access_token <token>```

- `--api_url, required=True, help="URL API ручки"`
- `--access_token, required=True, help="Ваш токен доступа"`
- `--comparison_parameter, required=True, type=str, help="Параметр сравнения"`
- `--max_objects, type=int, default=100, help="Максимальное количество объектов сравнения"`
