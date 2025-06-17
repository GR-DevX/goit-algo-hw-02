import queue
import time
import random
import uuid

# Створити чергу заявок
request_queue = queue.Queue()

def generate_request():
    """
    Генерує нову заявку з унікальним ID та додає її до черги.
    """
    request_id = uuid.uuid4()
    request_data = {"id": request_id, "data": f"Заявка з ID {request_id}"}
    request_queue.put(request_data)
    print(f"Нова заявка створена та додана до черги: ID {request_id}")

def process_request():
    """
    Обробляє заявку з черги.
    Якщо черга порожня, виводить відповідне повідомлення.
    """
    if not request_queue.empty():
        request_to_process = request_queue.get()
        print(f"Обробка заявки: {request_to_process['data']}...")
        # Імітація часу на обробку
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Заявка {request_to_process['id']} оброблена.")
        request_queue.task_done() # Повідомляємо черзі, що завдання виконано (для join())
    else:
        print("Черга пуста, немає заявок для обробки.")

# Головний цикл програми
if __name__ == "__main__":
    print("Симуляція роботи сервісного центру. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            # Випадково генеруємо або обробляємо заявки
            if random.random() < 0.8: # З ймовірністю 80% генеруємо нову заявку
                generate_request()
            
            if random.random() < 0.5 or not request_queue.empty(): # З ймовірністю 50% або якщо черга не пуста
                process_request()
            
            # Пауза для імітації реального часу
            time.sleep(random.uniform(0.3, 1))
            
            # Для демонстрації можна обмежити кількість ітерацій або додати умову виходу
            # Наприклад, якщо черга оброблена і певний час не було нових заявок

    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")
    finally:
        # Очікуємо, поки всі елементи в черзі будуть оброблені, якщо це потрібно
        # request_queue.join() # Це заблокує, якщо черга не пуста і task_done не викликався для всіх елементів
        print("Сервісний центр припиняє роботу.")
