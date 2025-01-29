# Iseseisevtöö "Registreerimine ja autoriseerimine" https://moodle.edu.ee/mod/assign/view.php?id=1102881


# 1. Регистрация (проверка пароля)
def parool_kontroll(psword:any)->bool:
    """Parooli kontrollimine, kas see sisaldab: numbreid, suuri ja väikeseid tähti ning erimärke.
    :param any psword: Sisestatud parool
    :rtype: bool
    """
    if not any(char.isdigit() for char in psword):  # Проверяем наличие цифр
        return False
    if not any(char.isupper() for char in psword):  # Проверяем наличие заглавных букв
        return False
    if not any(char.islower() for char in psword):  # Проверяем наличие строчных букв
        return False
    spets_sumbolid=".,:;!_*-+()/#¤%&"   # Проверяем наличие хотя бы одного специального символа
    if not any(char in spets_sumbolid for char in psword):
        return False

    return True
