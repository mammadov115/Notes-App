

## 📌 **Project Description: Notes App with User Authentication (API Only)**

Bu layihə sadəcə **RESTful API** üzərində qurulmuş, Django framework-undan istifadə edən bir **Qeydlər Tətbiqidir (Notes App)**. Tətbiqin əsas məqsədi istifadəçilərə şəxsi qeydlərini yaratmaq, görüntüləmək, redaktə etmək və silmək imkanı verməkdir. Sistem istifadəçi qeydiyyatı və girişi ilə təmin olunmuşdur ki, hər istifadəçi yalnız öz qeydlərinə çıxış əldə edə bilsin.

#### 🔍 Əsas Funksionallıqlar:

* 🧑‍💼 **İstifadəçi qeydiyyatı (signup)**
* 🔐 **İstifadəçi girişi (login) və çıxışı (logout)**
* 🔑 **Token əsaslı autentifikasiya (JWT)**
* 📝 **Qeyd yaratmaq (Create note)**
* 📖 **Qeydləri görüntüləmək (List & Detail views)**
* 🛠 **Qeydi redaktə etmək (Update note)**
* ❌ **Qeydi silmək (Delete note)**
* 🔍 **Qeyd axtarışı və ya filtr (optional)**
* 📅 **Qeydin yaradılma və yenilənmə tarixləri**

---

## 🧰 Tech Stack (Texnologiyalar):

| Texnologiya               | Məqsəd                               |
| ------------------------- | ------------------------------------ |
| **Python**                | Proqramlaşdırma dili                 |
| **Django**                | Web framework                        |
| **Django REST Framework** | REST API-lərin yaradılması üçün      |
| **djoser / simplejwt**    | Token əsaslı autentifikasiya         |
| **PostgreSQL / SQLite**   | Verilənlər bazası (SQLite dev üçün)  |
| **Docker (optional)**     | Deployment və konteynerizasiya       |
| **Swagger / drf-yasg**    | API sənədləşməsi                     |
| **Poetry**                | Dependency management və virtual env |
| **Git + GitHub**          | Versiya nəzarəti                     |

---

## ✅ Task List (Tapşırıqlar siyahısı)

### 🔹 Layihənin başlanğıcı:

* [ ] Django layihəsinin yaradılması
* [ ] `poetry` və ya `pip` ilə virtual mühit qurulması
* [ ] `.gitignore`, `README.md`, `LICENSE` fayllarının əlavə olunması
* [ ] Git repo-nun yaradılması və ilk commit

### 🔹 İstifadəçi idarəsi:

* [ ] `users` app-in yaradılması
* [ ] `User` modeli (default istifadə oluna bilər)
* [ ] `djoser` və `JWT` inteqrasiyası (login/register/logout)
* [ ] İstifadəçinin profili API vasitəsilə əldə etmək

### 🔹 Qeyd (Note) modulu:

* [ ] `notes` app-in yaradılması
* [ ] `Note` modeli (`title`, `content`, `created_at`, `updated_at`, `user`)
* [ ] Serializer-lərin yazılması
* [ ] View-ların yazılması: `List`, `Create`, `Retrieve`, `Update`, `Delete`
* [ ] Yalnız login olan istifadəçilərin öz qeydlərinə çıxışına icazə verilməsi

### 🔹 API sənədləşməsi və test:

* [ ] `drf-yasg` və ya `Swagger` inteqrasiyası
* [ ] Postman collection (optional)
* [ ] Əsas view-lar üçün testlər yazılması (`pytest` və ya `unittest`)

### 🔹 Deployment və təkmilləşdirmə:

* [ ] Dockerfile və `docker-compose.yml` (optional)
* [ ] `.env` faylı ilə konfiqurasiya
* [ ] Admin panelin aktiv edilməsi və test üçün superuser yaradılması
* [ ] API rate limit (optional)



