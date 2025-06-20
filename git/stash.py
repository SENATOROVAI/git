# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
# ---

"""Шаг 3.

Git stash.
"""

# > 0.1 записать видео по stash
#
# https://youtu.be/D8i0bcnS_J4
#
# > Что делает команда git stash?
#
# Помещает все текущие файлы (и "проиндексированные" и нет) в stash
#
# > Как просмотреть список всех сохранённых изменений (стэшей)?
#
# `git stash list'
#
# > Какая команда применяется для использования верхнего стэша?
#
# `git stash pop'
#
# > Как применить конкретный стэш по его номеру?
#
# `git stash apply stash@{1}'
#
# > Чем отличается команда git stash apply от git stash pop?
#
# `git stash pop` применяет stash и удаляет из списка stash, `git stash apply` просто применяет
#
# > Что делает команда git stash drop?
#
# Удаляет stash
#
# > Как полностью очистить все сохранённые стэши?
#
# `git stash clear`
#
# > В каких случаях удобно использовать git stash?
#
# а) хочешь разделить изменения на несколько коммитов б) взять pull из 2 репо чтоб часть файлов не влияла на merge
#
# > Что произойдёт, если выполнить git stash pop, но в проекте есть конфликтующие изменения?
#
# Файлы из stash перепишут файлы где есть конфликт
#
# > Можно ли восстановить удалённый стэш после выполнения git stash drop?
#
# Нет
#
# > Что делает команда git stash save "NAME_STASH"
#
# сохраняет stash с названием
#
# > Что делает команда git stash apply "NUMBER_STASH"
#
# применяет stash с указанным номером
#
# > Что делает команда git stash pop "NUMBER_STASH"
#
# удаляет stash с указанным номером
#
# > Сохраните текущие изменения в стэш под названием "SENATOROV ver1", вставьте скриншот из терминала
#
# ![image.png](attachment:image.png)
#
# ![image-2.png](attachment:image-2.png)
#
# > Внесите любые изменения в ваш репозиторий и сохраните второй стэш под именем "SENATOROV ver2"
#
# ![image-3.png](attachment:image-3.png)
#
# > Восстановите ваш стэш "SENATOROV ver1", вставьте скриншот из терминала
#
# ![image-4.png](attachment:image-4.png)
#
# > Удалите все стеши из истории, вставьте скриншот из терминала
#
# ![image-5.png](attachment:image-5.png)
