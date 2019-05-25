# -*- coding: utf-8 -*-
'''
Задание 18.3

В прошлых заданиях информация добавлялась в пустую БД.
В этом задании, разбирается ситуация, когда в БД уже есть информация.

Скопируйте скрипт add_data.py и попробуйте выполнить его повторно, на существующей БД.
Должна возникнуть ошибка.

При создании схемы БД, было явно указано, что поле MAC-адрес, должно быть уникальным.
Поэтому, при добавлении записи с таким же MAC-адресом, возникает ошибка.

Но, нужно каким-то образом обновлять БД, чтобы в ней хранилась актуальная информация.

Например, можно каждый раз, когда записывается информация,
предварительно просто удалять всё из таблицы dhcp.

Но, в принципе, старая информация тоже может пригодиться.

Поэтому, мы будем делать немного по-другому.
Создадим новое поле active, которое будет указывать является ли запись актуальной.

Поле active должно принимать такие значения:
* 0 - означает False. И используется для того, чтобы отметить запись как неактивную
* 1 - True. Используется чтобы указать, что запись активна

Каждый раз, когда информация из файлов с выводом DHCP snooping добавляется заново,
надо пометить все существующие записи (для данного коммутатора), как неактивные (active = 0).
Затем можно обновлять информацию и пометить новые записи, как активные (active = 1).


Таким образом, в БД останутся и старые записи, для MAC-адресов, которые сейчас не активны,
и появится обновленная информация для активных адресов.

Новая схема БД находится в файле dhcp_snooping_schema.sql

Измените скрипт add_data.py таким образом, чтобы выполнялись новые условия и заполнялось поле active.

Код в скрипте должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

> Для проверки корректности запроса SQL, можно выполнить его в командной строке, с помощью утилиты sqlite3.

Для проверки задания и работы нового поля, попробуйте удалить пару строк
из одного из файлов с выводом dhcp snooping.
И после этого проверить, что удаленные строки отображаются в таблице как неактивные.

'''
