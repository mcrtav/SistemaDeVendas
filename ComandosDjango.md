Desenvolvendo uma loja em python django 3.2
https://www.youtube.com/playlist?list=PL2Dw5PtrD32xhnKAUpMh8UqyprhQ_c3Wm


# Ambiente virtual
py -m venv venv

# Ativar o ambiente virtual
venv\Scripts\activate

# gitignore
venv/
venv/include/
venv/Lib/
venv/Script/
venv/pyvenv.cfg
include/
Lib/
Script/
pyvenv.cfg
db.sqlite3

# Desativar ambiente virtual
deactivate

# instalar dependencias django e pillow
py -m pip install django pillow

# criar projeto
django-admin startproject lojaproject .

# criar aplicativo
django-admin startapp lojaapp

# fazer a migração
python manage.py migrate

# Criar Superuser
python manage.py createsuperuser
Username: admin
Email: admin@admin.com
password: admin123
Password (again): admin123

# github # github # github # github # github # github # github # github # github # github # github # github
echo "# SistemaDeVendas" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mcrtav/SistemaDeVendas.git
git push -u origin main
# remover remote
git remote remove origin
# para saber quantos commit tem
git log --oneline --graph --all --decorate

# no setting.py colocar NO TEMPLATES:
tEMPLATES  -> 'DIRS': [BASE_DIR / 'templates'],

# Criar no final da setting.py
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static_cdn"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Colcoar na url do projeto 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Rodar o Servidor
python manage.py runserver



(aplicativo)models.py ── import ──► (aplicativo)serializer.py
              │                                   | 
            import                              import      
              │                                   │
              └──────► (aplicativo)views.py ◄─────┘
                                     |  
                                   import 
                                     |
                                     ▼ 
                       (aplicativo)urls.py 
                                     |  
                                   include 
                                     |
                                     ▼ 
                           (projeto)urls.py




  (aplicativo)apps.py ─── INSTALLED_APP ─── ► (projeto)settings.py 



  # fazer migração
  python manage.py makemigrations
  python manage.py migrate


  # Criar super Usuario
   python manage.py createsuperuser    

   # rodar o servidor de desenvolvimento
   python manage.py runserver