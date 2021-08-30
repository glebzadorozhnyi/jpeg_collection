import os
import re
import shutil
from tqdm import tqdm


def get_stars_jpeg(jpeg_directory, file_extension='CR2'):
    os.chdir(jpeg_directory)
    list_files = os.listdir()

    jpeg_stars_list = list()
    pattern = r'xmp:Rating.{0,2}[\d]'

    with tqdm(total=len(list_files), desc='Поиск фото с рейтингом') as pbar:
        for photo in list_files:
            path_name = jpeg_directory + '\\' + photo
            with open(path_name, "rb") as photo_file:
                img_as_text = str(photo_file.read())
                xmp_tekst = re.search(pattern, img_as_text)
                if xmp_tekst is None:
                    rating = 0
                else:
                    rating = int(xmp_tekst.group()[-1:])
            if rating > 0:
                jpeg_stars_list.append(photo[0:-3] + file_extension)  # сразу меняем расширение
            pbar.update(1)
    print()
    print('Отобрано {} фото'.format(len(jpeg_stars_list)))
    print()
    return jpeg_stars_list


def copy_selected_cr2(path_in, path_out, list_files):
    os.chdir(path_in)
    try:
        os.mkdir(path_out)
    except FileExistsError:
        pass
    with tqdm(total=len(list_files), desc='Копируем отобранные cr2') as pbar2:
        for photo in list_files:
            shutil.copy(photo, path_out)
            pbar2.update(1)


# Задаём папку

path = r'C:\Users\User\Desktop\02_Питер с Катей'

jpeg_path = path + r'\jpeg'  # папка с jpeg
cr2_path = path  # папка с cr2
cr2_selected_path = path + r'\на обработку'  # куда копируем отобранные cr2

# main
stars_jpeg = get_stars_jpeg(jpeg_path)  # получаем список фото с рейтингом
copy_selected_cr2(cr2_path, cr2_selected_path, stars_jpeg)
