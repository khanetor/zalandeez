import requests
from .models import Article, Track, ArticleImage


def download_articles():
    pages = 9637
    base_url = 'https://api.zalando.com/articles?page=%s'

    for page in range(1, pages + 1):
        url = base_url % page
        response = requests.get(url)
        if response.status_code == 200:
            payload = response.json()
            content = payload.get('content')
            for article_json in content:
                name = article_json.get('name')
                shop_id = article_json.get('id')
                shop_url = article_json.get('shopUrl')
                article = Article(name=name, shop_id=shop_id, shop_url=shop_url)
                article.save()

                for image_json in article_json.get('media').get('images'):
                    image_url = image_json.get('mediumHdUrl')
                    image = ArticleImage(url=image_url)
                    article.images.add(image, bulk=False)
                article.save()


def get_tracks_for_articles():
    base_url = 'https://api.deezer.com/search/track?q=track:"%s"'

    for article in Article.objects.all():
        parts = article.name.split(' - ')
        token = None
        if len(parts) == 2:
            token = parts[0]
        elif len(parts) == 3:
            token = parts[1]

        if token is not None:
            url = base_url % token
            response = requests.get(url)

            if response.status_code == 200:
                payload = response.json()
                data = payload.get('data')[0:3]
                for track_json in data:
                    track_id = track_json.get('id')
                    track = Track(track_id=track_id)
                    article.tracks.add(track, bulk=False)
                article.save()
            else:
                continue
        else:
            continue
