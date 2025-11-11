# Global University Success Factors — Scraping & API Analysis.


## О проекте

Этот проект сделан для гипотетического заказчика — частного инвестора, который хочет открыть уникальный университет-кампус. Мы собираем данные по 10k+ университетам и экономическим показателям стран, чтобы понять, какие внутренние характеристики вузов и внешние условия страны связаны с высоким рейтингом. Часть данных была собрана через **скрапинг сайта [Unipage](https://www.unipage.net/)**, а другая часть — через **API (TradingEconomics, WorldBank, Knoema)**.  
В итоге получилось более **10 000 университетов** и признаки по странам, что позволяет проанализировать связь между уровнем образования и экономическим развитием стран, и помогает понять, какие факторы помогают университету стать «успешным», чтобы инвестировать в открытие уникального кампуса.

---

## Что делает проект

### 1. Сбор данных об университетах  
- Используется `requests` и `BeautifulSoup`.  
- Сайт: [https://www.unipage.net/en/universities](https://www.unipage.net/en/universities)  
- Собираются данные:
  - название университета  
  - страна и город  
  - QS / THE / ARWU рейтинги  
  - стоимость обучения для разных степеней  
  - количество студентов, доля иностранных и женщин  
- Результат сохраняется в файл **`universities_data.csv`**  
  (всего — 10 001 строка).

---

### 2. Данные по странам через API  
Для анализа добавлены экономические показатели из открытых источников:

| Источник | Признак | Файл |
|----------|----------|------|
| **TradingEconomics API** | ВВП (gdp_total) | `gdp_total_with_code.csv` |
| **TradingEconomics API** | Безработица (unemployment_rate) | `unemployment_with_code.csv` |
| **Knoema API** | Индекс экономической свободы | `heritage_index_knoema.csv` |

---

### 3. Объединение данных  
После сбора все таблицы объединяются по **коду страны (ISO)**.  
Получается готовый датасет для дальнейшего анализа или визуализации.

---

---

## Признаки в данных

### Университеты
- `university_name` — название  
- `country`, `city` — локация  
- `qs_ranking_preview`, `the_ranking_preview`, `arwu_ranking_preview` — рейтинги  
- `bachelor_from`, `bachelor_to`, `master_from`, `master_to` — стоимость обучения  
- `total_students`, `international_students`, `female_students` — численные показатели  
- `establishment_year`, `acceptance_rate` — год основания, приём  
- `url` — ссылка на страницу университета  

### Страны
- `country_code` — ISO-код  
- `gdp_total_usd` — общий ВВП  
- `unemployment_rate` — уровень безработицы  
- `heritage_index` — индекс экономической свободы  
- `education_index` — уровень образования (при наличии данных)

---

## Используемые технологии
- **Python 3.12**  
- **Requests** — загрузка HTML  
- **BeautifulSoup4** — парсинг  
- **Pandas** — обработка и объединение  
- **CSV / JSON API** — хранение данных  
- **TradingEconomics / WorldBank / Knoema API** — источники данных

---

## Как запустить

```bash
# Клонировать проект
git clone https://github.com/ritaabgaryan/university-data.git
cd university-data

# Установить зависимости
pip install -r requirements.txt

# Запустить парсер университетов
python parser_universities.py

# Запустить загрузку данных по странам
python enrich_countries.py

# Объединить всё в один файл
python merge_datasets.py
