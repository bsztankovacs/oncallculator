import json
import os


def get_hours(texts):
    def set_hours(hour_type):
        hours[hour_type] = get_user_input_for_number((texts.get(hour_type)))

    hours = {}
    for hour_types in texts.keys():
        set_hours(hour_types)
    return hours


def init():
    available_languages = []
    for language_files in os.listdir('i18n'):
        with open(f'i18n{os.sep}{language_files}', 'r') as language_file:
            available_languages.append(json.load(language_file))

    language_selection_text = f'Choose language / Valassz nyelvet:'
    for language in available_languages:
        language_selection_text += f'\n{available_languages.index(language) + 1}) {language.get("label")}'
    language_selection_text += '\n'

    while True:
        user_language_selection = input(language_selection_text)
        if user_language_selection.isnumeric() and 1 <= int(user_language_selection) <= len(available_languages):
            break
    print('*' * 8)
    return available_languages[int(user_language_selection) - 1]


def get_user_input_for_number(user_prompt):
    while True:
        user_input = input(user_prompt + '\n')
        if user_input.isnumeric() and 0 < int(user_input):
            break
    return int(user_input)


def get_user_salary():
    return get_user_input_for_number(selected_language['haviber']) / 174


def oncallculate(hours, hourly_pay_rate):
    plusz_berek = {}

    for hour_types in hours:
        if hour_types == 'keszenleti_orak':
            total_workhours = 0
            for worked_hours in hours:
                if worked_hours != 'keszenleti_orak':
                    total_workhours += hours[worked_hours]
            oncall_hours = hours['keszenleti_orak'] - total_workhours
            fizetes = oncall_hours * 0.2 * hourly_pay_rate
        elif hour_types == 'hetkoznap_ejszakai_rendkivuli_munkaidoben_dolgozott_orak':
            fizetes = hours[hour_types] * 1.65 * hourly_pay_rate
        elif hour_types == 'hetkoznap_rendkivuli_munkaidoben_dolgozott_orak':
            fizetes = hours[hour_types] * 1.5 * hourly_pay_rate
        elif hour_types == 'hetvegen_vagy_munkaszuneti_napon_ejszakai_rendkivuli_munkaidoben_dolgozott_orak':
            fizetes = hours[hour_types] * 2.15 * hourly_pay_rate
        elif hour_types == 'hetvegen_vagy_munkaszuneti_napon_rendkivuli_munkaidoben_dolgozott_orak':
            fizetes = hours[hour_types] * 2 * hourly_pay_rate

        plusz_berek[hour_types] = fizetes
    return plusz_berek


def display_pay(pays, texts):
    for fizetes in pays:
        print(f'{texts.get(fizetes)}: {pays[fizetes]:.2f} HUF')
    print(f'Total: {sum(pays.values()):.2f} HUF')


if __name__ == '__main__':
    selected_language = init()
    hours = get_hours(selected_language.get('kerdesek'))
    hour_pay_rate = get_user_salary()
    pay = oncallculate(hours, hour_pay_rate)
    display_pay(pay, selected_language.get('fizetes'))
