import requests
import argparse

def main(api_url, access_token, comparison_parameter, max_objects):
    params = {}
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    all_objects = []

    while True:
        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            all_objects.extend(data["companies"])
            print(f"Собрано {len(all_objects)} объектов")

            if len(all_objects) >= max_objects:
                break

            if "cursor" in data:
                params["cursor"] = data['cursor']
            else:
                break
        else:
            print(f"Ошибка при запросе: {response.status_code}")
            break

    object_ids = set()
    duplicates = set()

    for obj in all_objects:
        obj_id = obj[comparison_parameter]
        if obj_id in object_ids:
            duplicates.add(obj_id)
        object_ids.add(obj_id)

    if duplicates:
        print(f"Найдены дубликаты: {duplicates}")
    else:
        print("Дубликатов не найдено.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скрипт для сравнения объектов на дубли по айдишникам.")
    parser.add_argument("--api_url", required=True, help="URL API ручки")
    parser.add_argument("--access_token", required=True, help="Ваш токен доступа")
    parser.add_argument("--comparison_parameter", required=True, type=str, help="Параметр сравнения")
    parser.add_argument("--max_objects", type=int, default=100, help="Максимальное количество объектов сравнения")


    args = parser.parse_args()
    main(args.api_url, args.access_token, args.comparison_parameter, args.max_objects)
