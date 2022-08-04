from src.resizer.resize_imgs import resizer
folder_path = '/home/iamshri/PycharmProjects/oremedian-resizer/tests/testImages'


resizer((100, 100), folder_path,  'resizedImages', 100, n_f=True, view=True, out_format='jpg')
