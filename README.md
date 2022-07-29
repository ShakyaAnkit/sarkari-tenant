# Sarkari

```bash
pip install -r requirements.txt
cp sarkari/settings.py.example sarkari/settings.py
python manage.py makemigrations client dashboard
python manage.py migrate_schemas
python manage.py create_base_tenant
```