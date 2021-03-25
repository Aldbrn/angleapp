# angleapp
釣果を投稿、検索できるアプリケーションです。

## 使用技術
- Python 3.9.1
- Django 3.1.6
- postgresql
- gunicorn 20.0.4
- whitenoise 5.2.0
- heroku
- cloudinary
- Docker/Docker Compose
- Google Maps API
  - Geocoding API
  - Maps JavaScript API
  
## 機能一覧
- サインアップ機能
- ログイン、ログアウト機能
- 投稿機能
- 投稿編集機能
- 投稿削除機能
- 魚種検索機能
- 地名検索機能
- Google Mapsエリア表示機能
- ページネーション機能

## Usage
```
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py runserver 0:8000
```
