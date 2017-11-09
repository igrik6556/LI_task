			-*- Описание -*-
	Задача:
Разработать проект реализации стены сообщений пользователей. Решение должно быть представлено в виде web-приложения, состоящего из 2 страниц:
• страницы входа;
• страницы просмотра/добавления/комментирования сообщений.
	Страница входа:
Если пользователь уже вошел в систему, при попадании на эту страницу, он должен быть автоматически перенаправлен на страницу сообщений.
Данная страница должна предоставлять возможность входа в систему только с помощью существующих социальных сетей (или сервисов, предоставляющих соответствующие API), например, Facebook. Для успешного выполнения задания, достаточно использования одного сервиса.
	Страница сообщений:
На эту страницу может попасть любой пользователь. При этом, пользователь, который не выполнил вход в систему, может просматривать все сообщения и не имеет возможности добавлять и комментировать сообщения. Вместо текстового поля для ввода текста сообщения должна быть
отображена надпись: “Для добавления и комментирования сообщений выполните вход” с ссылкой на страницу входа.
Сообщения могут быть двух видов:
• собственно, сообщение;
• комментарий какого-либо сообщения, либо другого комментария.
Таким образом, сообщения с комментариями могут иметь древовидную форму. Поэтому, на странице сообщений необходимо выполнить вывод сообщений и комментариев в виде дерева. При этом, сообщения должны быть отсортированы таким образом, чтобы свежие были вверху. А комментарии сообщений наоборот - свежие внизу.

			-*- Русский -*-
Для запуска необходим установленный Python 3 (3.4 или выше),
также нужны утилиты "pip" и "virtualenv".

Чтобы запустить проект, необходимо выполнить следующие шаги:

1. перейти в директорию, где вы хотите сохранить проект (cd ~/prj)
2. выполнить git clone https://github.com/igrik6556/LI_task.git
3. virtualenv li_task_env --no-site-packages
   a) cd li_task_env/bin/
   b) . activate
   c) cd ../../
4. cd LI_task
5. pip3 install -r requirements.txt
6. python3 manage.py runserver
7. открыть в браузере http://localhost:8000/
   Заметки: проект django идет со сформированной базой данных.
   Если вы хотите очистить базу данных. необходимо выполнить следующие шаги:
   	1. rm database.sqlite3
   	2. python3 manage.py migrate
   	Создастся новая база данных.

Есть созданный суперпользователь:
login = admin
pass  = 123

Чтобы запустить тесты, необходимо выполнить команду:
   python3 manage.py test comments



		-*- English -*-
You need to have Python 3 (3.4 or later) installed on your PC, 
also you need Python utilities "pip" and "virtualenv".

To launch the django app, you need:

1. cd to a directory of your choice (eg: cd ~/prj)
2. git clone https://github.com/igrik6556/LI_task.git
3. virtualenv li_task_env --no-site-packages
   a) cd li_task_env/bin/
   b) . activate
   c) cd ../../
4. cd LI_task
5. pip3 install -r requirements.txt
6. python3 manage.py runserver
7. open http://localhost:8000/ in your browser
   Notes: Django app comes with a preinstalled database.
   If you want clear the database, follow these steps:
   	1. rm database.sqlite3
   	2. python3 manage.py migrate
   	A new database will be created then.

There is created superuser:
login = admin
pass  = 123

To launch tests, please follow these instructions:
   python3 manage.py test comments


