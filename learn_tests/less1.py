"""Изучаю тестирование pytest на python
https://www.youtube.com/watch?v=1HtEPEn4-LY&list=PLlKID9PnOE5hCuNW8L-qxC12U7WPWG6YS

"""
def division(a: int, b:int) -> float:
    """Делит делимое на делитель и возвращает результат.

    Args:
        a (int): Делимое
        b (int): Делитель
    
    Returns:
        _type_: результат деления 
    """
    result: float = a / b
    return result  


if __name__ == "__main__":
    print(division(10, 2))