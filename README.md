### Парсер, нужный каждому программисту
+ Чтобы ни одна новинка PEP не осталась вами не замеченой
+ Чтобы весь PEP был у вас под рукой
# Представляем асинхронный парсер SCRAPY_PARSER_PEP!
------------
#### Что входит в набор:
+ быстрый парсинг
+ результаты выводятся в файл (csv)
---
#### В работе применяются библиотеки:
+ scrapy
---
#### Установка и запуск:
+ клонируем репозиторий:

  git clone git@github.com:sabina-045/scrapy_parser_pep.git

+ устанавливаем зависимости:

  pip install -r requirements.txt

+ запускаем паука из корневой директории и
  после окончания его работы заглядываем в папку results:

  scrapy crawl pep

+ запуск shell:

  scrapy shell "https://peps.python.org/"

-------
Проект создан Гаджиевой С. при поддержке команды Яндекс Практикум
