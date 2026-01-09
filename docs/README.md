forum-app
Run Django using runserver command on sqlite (without docker)
python manage.py migrate --settings=config.settings_sqlite python manage.py runserver --settings=config.settings_sqlite

You can see the Routes
python manage.py show_urls
✅ Postman URLs for categories/ Action Method URL Description Create Category POST http://localhost:8000/categories/ Create a new category (requires add_category permission) List Categories GET http://localhost:8000/categories/ List all categories (requires view_category permission) Update a category PATCH http://localhost:8000/categories/<category_id>/ { "name": "Updated Name" } Delete a category DELETE http://localhost:8000/categories/<category_id>/
