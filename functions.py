import json


def load_candidates():
    """загружает данные из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    """показывает всех кандидатов"""
    return load_candidates()


def get_by_pk(pk):
    """возвращает кандидата по pk"""
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return 'Not Found'


def get_by_skill(skill):
    """возвращает кандидатов по навыку"""
    result = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower():
            result.append(candidate)
    return result
