import datetime
import random

from django.core.exceptions import MultipleObjectsReturned

from datacenter.models import Subject, Commendation, Lesson, Mark, Schoolkid, Chastisement

phrases = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]


def fix_marks(schoolkid: Schoolkid) -> None:
    """
    Функция испровляет оценки пользователя.

    :param schoolkid - объект с информацией об ученике
    """
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid: Schoolkid) -> None:
    """
    Функция удаляет все замечания ученика

    :param schoolkid - объект с информацией об ученике
    """
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid: Schoolkid, subject_title: str) -> None:
    """
    Функция создает похвалу указанному ученику, по указанному предмету.
    Если похвала уже есть, выведется соответсвтующее сообющение.

    :param schoolkid - объект с информацией об ученике
    :param subject_title - название  предмета по которому нужно добавить похвалу например 'Математика'
    """
    subject = Subject.objects.filter(title=subject_title, year_of_study=6)
    if subject:
        lesson = Lesson.objects.filter(group_letter=schoolkid.group_letter, subject=subject[0])
        if not lesson:
            print("Указанного урока не существует")
    else:
        print("Указанный предмет не существует")
    if subject and lesson:
        now = datetime.datetime.now()
        if Commendation.objects.filter(schoolkid=schoolkid, subject=subject[0], created=now).order_by('-created'):
            print(f"По указанному предмету({subject_title}) уже есть похвала")
        else:
            Commendation.objects.create(text=random.choice(phrases), schoolkid=schoolkid, subject=subject[0],
                                    teacher=lesson[0].teacher, created=now)


if __name__ == "__main__":
    try:
        user = Schoolkid.objects.get(full_name__contains="Нестерова Анна Владиславовна")
        #create_commendation(user, "Музыка")
        #remove_chastisements(user)
    except Schoolkid.DoesNotExist:
        print("Пользователь не найден")

    except MultipleObjectsReturned:
        print("Найдено более 1 записи")


