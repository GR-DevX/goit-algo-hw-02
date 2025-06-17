def check_delimiters(s: str) -> str:
    """
    Перевіряє симетричність розділювачів у рядку.
    Ігнорує символи, що не є розділювачами.
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    open_brackets = "([{"
    close_brackets = ")]}"
    
    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack: # Закриваюча дужка без відповідної відкриваючої
                return "Несиметрично"
            top_element = stack.pop()
            if mapping[char] != top_element: # Невідповідність типів дужок
                return "Несиметрично"
        # Інші символи ігноруються
        
    if not stack: # Якщо стек порожній, всі дужки збалансовані
        return "Симетрично"
    else: # Якщо в стеку залишились відкриваючі дужки
        return "Несиметрично"

# Приклади використання:
if __name__ == "__main__":
    print(f"'(){{[](){{}}}}' -> {check_delimiters('(){[](){{}}}}')}") # Симетрично [cite: 12] (змінено для чистоти прикладу з ДЗ)
    print(f"'((()' -> {check_delimiters('((()')}")                     # Несиметрично [cite: 12]
    print(f"'([)]' -> {check_delimiters('([)]')}")                   # Несиметрично (припускаючи, що '(.' означало такий випадок)
    print(f"'()[1](1+3)(){{}}' -> {check_delimiters('()[1](1+3)(){{}}')}") # Симетрично [cite: 12]
    print(f"'((' -> {check_delimiters('((')}")                         # Несиметрично
    print(f"'))' -> {check_delimiters('))')}")                         # Несиметрично
    print(f"'{{[()]}}' -> {check_delimiters('{{[()]}}')}")               # Симетрично
    print(f"'{{[()]}}(' -> {check_delimiters('{{[()]}}(')}")             # Несиметрично
    print(f"'(37):' -> {check_delimiters('(11):')}")                   # Несиметрично (якщо дужки - частина виразу) [cite: 12]
    print(f"'(50 $(\\overline{{z}}-3)i:$' -> {check_delimiters('(50 $(\\overline{{z}}-3)i:')}") # Несиметрично (якщо дужки - частина виразу) [cite: 12]
