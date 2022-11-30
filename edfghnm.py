alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
phrase = 'Ha ocнoвe вceгo вышecкaзaннoгo, xoчy oтмeтить, чтo oсoбo пpиcтaльнoe внимaниe cтoит yдeлить нa aкцию "oдин плюc oдин"'
count = 0
for letter in alphabet:
    if letter in alphabet:
        count += 1
print(count)