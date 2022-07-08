# Ukázka Django REST framework

### Instalace virtuálního prostředí
V ideálním případě si nainstalujeme viruální prostředí ve složce s projektem.
V Git Bash emulátoru za pomoci příkazu s umístěním v požadované složce:
```
$ python -m venv .venv        #.venv -> je název prostředí a "." skryje složku 
```
V Git Bash aktivujeme prostředí příkazem:
```
$ source .venv/scripts/activate
```

Násladně nainstalujeme potřebné knihovny:
```
$ pip install -r requirements.txt        # nainstaluje knihovny
```

### Spuštění Django REST frameworku v prohlížeči s nahranými daty
Přesuneme se do složky shop_project příkazem:
```
$ cd shop_project
```
Spustíme server příkazem:
```
$ python manage.py runserver
```
V prohlížeči otevřeme URL adresu:
http://127.0.0.1:8000/ImportAndDetail/

V prohlížeči nyní běží webové rozhraní s daty, která jsou uložena v souboru db.sqlite3. Data lze:

- GET - zobrazovat
- POST - přidávat
- PUT - upravovat
- DELETE - mazat

*Ve složce data je spolu s .jsony uložený skrypt _json_filter.py, který rozděluje původní test_data.json ze zadání.*


