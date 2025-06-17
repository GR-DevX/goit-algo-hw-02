from collections import deque

def is_palindrome(input_string: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Нечутлива до регістру та пробілів.
    """
    # Нормалізація рядка: нижній регістр та видалення пробілів
    normalized_string = ''.join(input_string.lower().split())
    
    if not normalized_string: # Порожній рядок або рядок з одних пробілів вважається паліндромом
        return True
        
    char_deque = deque(normalized_string)
    
    while len(char_deque) > 1:
        first_char = char_deque.popleft()
        last_char = char_deque.pop()
        if first_char != last_char:
            return False
            
    return True

# Приклади використання:
if __name__ == "__main__":
    print(f"'Я иду с мечем судия' є паліндромом: {is_palindrome('Я иду с мечем судия')}")
    print(f"'Motorsport' є паліндромом: {is_palindrome('Motorsport')}")
    print(f"'Race car' є паліндромом: {is_palindrome('Race car')}")
    print(f"'MaD Am' є паліндромом: {is_palindrome('madam')}")
    print(f"' ' є паліндромом: {is_palindrome(' ')}") # Порожній після нормалізації
    print(f"'' є паліндромом: {is_palindrome('')}")   # Порожній рядок
    print(f"'R' є паліндромом: {is_palindrome('A')}")     # Рядок з одного символу
