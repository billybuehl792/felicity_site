#!python3
# pillow.py - make thumbnail version of picture
from PIL import Image
import os

def mk_cropped_thumbnail(img, size):
    fn, _ = os.path.splitext(img)                               # get fn
    filename = f'{fn}_thumbnail.png'                            # get filename
    i = Image.open(img)                                         # define i object
    resize = i.size[0]                                          # crop size = width

    if i.size[0] > i.size[1]:                                   # determine crop size
        resize = i.size[1]

    i_resize = i.resize(size, box=(0, 0, resize, resize))       # resize image to square
    i_resize.save(f'thumbnail/{filename}', quality=95)          # save thumbnail

    return filename

def mk_thumbnail(img, width, ext, dirname='thumbnail'):
    fn = os.path.basename(img)
    directory = os.path.dirname(img)

    # make directory if nonexistent
    thumb_dir = f'{directory}/{dirname}'
    if not (os.path.isdir(thumb_dir)):
        os.mkdir(thumb_dir)
        print(f'{thumb_dir} created!')

    thumbnail = f'{thumb_dir}/{os.path.splitext(fn)[0]}_{dirname}.{ext}'

    try:
        i = Image.open(img)                                         # define i object
        img_width = round(i.size[0] / (i.size[0] / width))
        img_height = round(i.size[1] / (i.size[0] / width))


        i_thumb = i.resize((img_width, img_height))
        i_thumb = i_thumb.convert('RGB')
        i_thumb.save(f'{thumbnail}', quality=95)

        return thumbnail
    except:
        print(f'{thumbnail} write failure!')


if __name__ == '__main__':
    img_dir = 'felicity_site/static/pictures/'

    for item in os.listdir(img_dir):
        img_file = img_dir + item
        # print(mk_thumbnail(img_file, 500, 'jpg'))
        print(mk_thumbnail(img_file, 1080, 'jpg', 'scaled'))
