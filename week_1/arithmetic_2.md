Следующая задача: вводится число N, необходимо отрезать от него K последних цифр. Например, при N = 123456 и K = 3 ответ должен быть 123.

Для решения этой задачи нужно понять, что происходит при целочисленном делении на 10 (основание системы счисления). Если мы разделим число на 10, то будет отброшена последняя цифра, независимо от того, какой она была. Если разделим число на 100 - будет отброшено две последние цифры. Исходя из этого получается решение задачи: необходимо просто разделить число N на 10 в степени K:

```python
n = int(input())
k = int(input())
print(n // 10**k)
```