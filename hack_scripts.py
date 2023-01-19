from datacenter.models import (
    Chastisement, Schoolkid, Mark, Lesson, Commendation, Subject)
from sys import exit
import random

PRAISE = ["Молодец!",
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

def get_schoolkid_info(child_full_name):
    try:
        child_info = Schoolkid.objects.get(full_name__contains=child_full_name)
    except Schoolkid.MultipleObjectsReturned:
        exit('ОШИБКА: Найдено несколько учеников')
    except Schoolkid.DoesNotExist:
        exit('ОШИБКА: имя не найдено.')
    return child_info


def get_lesson(lesson,kid):
    lessons_info = Lesson.objects.filter(
        group_letter=kid.group_letter,
        year_of_study=kid.year_of_study,
        subject__title=lesson).order_by('-date').first()
    if lessons_info is None:
        exit("ОШИБКА: Неверно введено название предмета")
    return lessons_info


def change_bad_marks(schoolkid):
    kid = get_schoolkid_info(schoolkid)
    all_bad_marks = Mark.objects.filter(
        schoolkid=kid, points__in=[1, 2, 3])
    all_bad_marks.update(points = 5)



def remove_chastisements(schoolkid):
    all_bad_marks = Chastisement.objects.filter(schoolkid=get_schoolkid_info(schoolkid))
    all_bad_marks.delete()



def create_commendation(schoolkid,subject):

    kid = get_schoolkid_info(schoolkid)
    lesson = get_lesson(subject,kid)

    Commendation.objects.create(
        teacher=lesson.teacher,
        subject=lesson.subject,
        created=lesson.date,
        schoolkid=kid,
        text=random.choice(PRAISE))
