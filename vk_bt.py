from urllib.request import urlretrieve
import vk_api,conf,math
import conf
def vk_pars (album_url='',prev_updt_tg=0):
    vk_session = vk_api.VkApi(token=conf.vkapi)
    vk = vk_session.get_api()
    album_id = album_url.split('/')[-1].split('_')[1]
    owner_id = album_url.split('/')[-1].split('_')[0].replace('album', '')
    ph=vk.photos.getAlbums(owner_id=owner_id, album_ids=album_id)['items']
    photos_count = ph[0]['size']
    photos_upd_vk=ph[0]['updated']

    base=[]
    if prev_updt_tg<photos_upd_vk:
        for j in range(math.ceil(photos_count / 1000)):
            p=(vk.photos.get(owner_id=owner_id,album_id=album_id, offset=j*1000, count=1000, rev=0)['items'])
            for i in range(len(p)):
                if int(p[i]['date'])>prev_updt_tg:
                    base.append([(p[i])['date'],(p[i])['text'],(p[i]['sizes'][(len((p[i])['sizes'])-1)])['url'],(p[i]['sizes'][(len((p[i])['sizes'])-2)])['url']])
    return base
