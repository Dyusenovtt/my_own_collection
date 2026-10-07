# my_own_collection

Коллекция Ansible `my_own_namespace.yandex_cloud_elk` с собственным модулем
и ролью для создания текстового файла на удалённом хосте.

## Состав

- **Модуль** `my_own_module` — создаёт файл по пути `path` с содержимым `content`. Идемпотентен, поддерживает `--check`.
- **Роль** `file_creator` — обёртка над модулем со значениями по умолчанию.
- **Плейбук** `site.yml` — пример использования роли.

## Установка

    ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

## Пример использования

    - hosts: localhost
      gather_facts: false
      roles:
        - role: my_own_namespace.yandex_cloud_elk.file_creator

## Домашнее задание

См. SOLUTION.md.
