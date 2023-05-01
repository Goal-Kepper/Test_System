import subprocess


def check(need: list, got: list, mode: str) -> bool:
    """

    Функция, сравнивающая два подаваемых на вход списка - need и got.
    Существует несколько специальных режимов:

    - All In Order (AIO) - режим, при котором нужно получить точный конкретный вывод - реализован как сравнение списков;

    - All Without Order (AWO) - режим, при котором нужно получить все результаты, но порядок не важен - реализован как сравнение множеств на списках;

    - One From List - режим, при котором нужно вывести m вариантов из n возможных (причем n > m) - проверка на вхождение элементов списка во множество;

    """

    if mode == 'AIO':
        return need == got

    if mode == 'AWO':
        return set(need) == set(got)

    if mode == 'OFL':
        for g in got:
            if g not in need:
                return False
        return True


def get_tests(name: str, tests: list, mode: str):
    for test in tests:

        fin = open(test + '.in', 'r')
        fout = open(test + '.out', 'r')

        p = subprocess.Popen(['python', name], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        p.text_mode = True
        output, _ = p.communicate(''.join(fin.readlines()).encode())

        need = [''.join(fout.readlines()).encode()]
        got = [output.strip()]

        need = [line.decode().split() for line in need]
        got = [line.decode().split() for line in got]

        assert check(need, got, 'AIO'), f'Test {test} failed! Need: {str(*need)}, got: {str(*got)}'


get_tests("main.py", ['1'], 'AIO')
