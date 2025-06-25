# db-hack

## Описание
Набор функций для работы с базой данных школьного дневника.

## Функция fix_marks
Функция позволяет исправить оценки пользователя (2 и 3) на пятерки

Пример использования:
```
user = Schoolkid.objects.get(full_name__contains="Фролов Иван")
fix_marks(user)
```

## Описание remove_chastisements
Функция позволяет удалить все замечания ученика.

Пример использования:
```
user = Schoolkid.objects.get(full_name__contains="Фролов Иван")
remove_chastisements(user)
```

## Описание create_commendation
Функция позволяет добавить похвалу для ученика.

Текст похвалы выбирается рандомно из списка.

Пример использования:
```
user = Schoolkid.objects.get(full_name__contains="Фролов Иван")
create_commendation(user, "Музыка")
```
Если уже есть похвала поданному предмету за сегодня, то будет соответсвующе уведомление.

