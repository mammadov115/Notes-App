## 📄 **Layihənin Təsviri (Project Description)**

**Notes App with User Authentication** — istifadəçilərin qeyd (note) yaratması, oxuması, redaktə etməsi və silməsi üçün hazırlanmış sadə və təhlükəsiz bir RESTful API tətbiqidir. Hər bir istifadəçi qeydiyyatdan keçərək öz hesabı ilə sistemə daxil olur və yalnız öz qeydlərini idarə edə bilər. Bu sistem gələcəkdə frontend və mobil tətbiqlərlə asanlıqla inteqrasiya oluna biləcək şəkildə hazırlanır.

### 🎯 Əsas Funksionallıqlar:

* İstifadəçi qeydiyyatı (register)
* Sistəmə giriş və çıxış (login/logout)
* Token-based autentifikasiya
* Qeyd (note) yaratmaq
* Qeyd siyahısına baxmaq
* Qeyd detalları (detail view)
* Qeydi redaktə etmək
* Qeydi silmək
* Qeydlərin yalnız istifadəçiyə aid olması (authorization)
* Timestamps (yaradılma və dəyişmə vaxtı)

---

## 🧰 **Tech Stack**

### 💻 Backend:

* **Python 3.12+**
* **Django 5+**
* **Django REST Framework (DRF)**

### 🔐 Authentication:

* **DRF SimpleJWT** — Token-based authentication

### 🗄️ Database:

* **SQLite3** (development üçün)
* (Gələcəkdə PostgreSQL ilə əvəzlənə bilər)

### ✅ Testing:

* **Pytest + DRF test tools**

### 🛠️ Dev Tools:

* **Poetry** — Dependency management
* **Docker + Docker Compose** — İzolyasiya və deployment üçün
* **Pre-commit hooks** — Kod keyfiyyətini qorumaq üçün (black, isort, flake8)
* **.env** faylları ilə konfiqurasiya

---

## ✅ **Task List** (Sıralı və mərhələli)

### 📁 1. Layihənin başlanğıcı

* [+] Django layihəsini yarat (`django-admin startproject notes_api`)
* [+] Yeni app yarat: `notes` (`python manage.py startapp notes`)
* [+] Poetry ilə layihə başlat (`poetry init`) və dependency-ləri əlavə et:

  * `Django`, `djangorestframework`, `djangorestframework-simplejwt`, `python-dotenv`
* [+] `.env` faylı və `settings.py`-də konfiqurasiya
* [+] `rest_framework` və `notes` app-larını `INSTALLED_APPS`-ə əlavə et

---

### 👥 2. İstifadəçi Auth Sistemi

* [+] Custom User modeli yarat (əgər lazım olsa)
* [+] `users` adlı app yarat və qeydiyyat/login/logout üçün API-lər yaz
* [+] JWT autentifikasiya sistemi inteqrasiya et (`SimpleJWT`)
* [+] İstifadəçi qeydiyyatı API (`/api/register/`)
* [+] Token əldəetmə API (`/api/token/`)
* [+] Token yeniləmə API (`/api/token/refresh/`)
* [+] Logout üçün endpoint (token blacklist optional)

---

### 🗒️ 3. Notes CRUD Sistemi

* [+] `Note` modeli yarat:

  * title (CharField)
  * content (TextField)
  * owner (ForeignKey → User)
  * created\_at, updated\_at (DateTimeFields)
* [+] Note modelini admin panelə əlavə et
* [+] Serializer yaz: `NoteSerializer`
* [+] API views yaz:

  * List + Create — `/api/notes/`
  * Retrieve/Update/Delete — `/api/notes/<id>/`
* [+] Yalnız login olan istifadəçi üçün CRUD imkanları ver (authentication + permission)
* [+] Notes-lar yalnız sahibinə görünməlidir (queryset filtering)

---

### 🔒 4. Auth və Permissions

* [+] Custom permission yaz: `IsOwner`
* [+] View-larda permission əlavə et
* [+] Token olmadan endpoint-lərə girişin qarşısını al

---

### 🧪 5. Testlər

* [ ] İstifadəçi qeydiyyatı və login üçün testlər
* [ ] Token alma və doğrulama testləri
* [ ] CRUD əməliyyatları üçün testlər (auth və permission daxil olmaqla)

---

### 🐳 6. Dockerize Etmək

* [ ] `Dockerfile` və `docker-compose.yml` fayllarını yarat
* [ ] `.env` faylına əsasən environment dəyişkənləri konfiqurasiya et
* [ ] Django layihəsini konteynerdə işə sal

---

### 🧹 7. Kod Keyfiyyəti və Refaktor

* [ ] Pre-commit hooks əlavə et (black, isort, flake8)
* [ ] Kodun təmizlənməsi və sənədləşdirilməsi
* [ ] README faylına layihənin izahını yaz

---

### 📦 8. Deployment (əgər istənilirsə)

* [ ] Production üçün `PostgreSQL` dəstəyi əlavə et
* [ ] Environment dəyişkənləri üçün `.env.prod` faylı
* [ ] `gunicorn` və `nginx` ilə konfiqurasiya (gələcək mərhələdə)
