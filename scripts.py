import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import (Schoolkid, Mark, Chastisement, Lesson,
                               Commendation)


COMMENDS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def get_student(schoolkid):
    try:
        student = Schoolkid.objects.get(full_name__contains=schoolkid)
        return student
    except ObjectDoesNotExist:
        return 'Такого ученика не существует'
    except MultipleObjectsReturned:
        return 'Найдено несолько учеников.'


def fix_marks(schoolkid):
    '''Исправляет плохие оценки в дневнике на 5.'''
    student = get_student(schoolkid)

    if isinstance(student, str):
        return student

    Mark.objects.filter(schoolkid=student, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    '''Удаляет из дневника все замечания.'''
    student = get_student(schoolkid)

    if isinstance(student, str):
        return student

    Chastisement.objects.filter(schoolkid=student).delete()


def create_commendation(schoolkid, lesson):
    '''Создает похвалу в дневнике.'''
    student = get_student(schoolkid)

    if isinstance(student, str):
        return student

    found_lesson = Lesson.objects.filter(
        year_of_study=student.year_of_study,
        group_letter=student.group_letter,
        subject__title__contains=lesson
    ).order_by('subject').first()

    if found_lesson:
        Commendation.objects.create(
            schoolkid=student,
            subject=found_lesson.subject,
            teacher=found_lesson.teacher,
            created=found_lesson.date,
            text=random.choice(COMMENDS)
        )

    else:
        return 'Урок не найден.'
