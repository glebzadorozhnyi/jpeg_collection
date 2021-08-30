import os, shutil
from tqdm import tqdm
from tqdm import tnrange, tqdm_notebook


directory_jpg = r'C:\Users\User\Desktop\Вика\jpeg отобрано'
directory_cr2_in = r'C:\Users\User\Desktop\Вика'
directory_cr2_out = directory_cr2_in + r'\на обработку'

os.chdir(directory_jpg)
list_files = os.listdir()
for i in range(len(list_files)):
    list_files[i] = list_files[i][0:-3] + 'CR2'
print(list_files)
os.chdir(directory_cr2_in)
os.mkdir(directory_cr2_out)
shutil.copy(list_files[0],directory_cr2_out)
with tqdm (total=len(list_files)) as pbar:
    for element in list_files:
        shutil.copy(element, directory_cr2_out)
        pbar.update(1)