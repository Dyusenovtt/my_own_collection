#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Создает текстовый файл с заданным содержимым
version_added: "1.0.0"
description:
  - Модуль принимает путь к файлу и текст. Если файла нет или текст отличается, он перезаписывает файл.
options:
  path:
    description: Абсолютный путь к файлу.
    required: true
    type: str
  content:
    description: Содержимое файла.
    required: true
    type: str
author:
  - Ваш Имя Фамилия
'''

EXAMPLES = r'''
- name: Создать файл
  my_own_module:
    path: /tmp/test_ansible.txt
    content: "Привет, мир!"
'''

RETURN = r'''
path:
    description: Путь к созданному файлу
    type: str
    returned: always
'''

import os
from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    file_path = module.params['path']
    file_content = module.params['content']
    result['path'] = file_path

    # Проверка существования файла и его содержимого
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                current_content = f.read()
            if current_content == file_content:
                result['message'] = 'Файл существует, содержимое совпадает.'
                module.exit_json(**result)
        except Exception as e:
            module.fail_json(msg='Ошибка чтения файла: %s' % str(e), **result)

    # Режим проверки (Dry run)
    if module.check_mode:
        result['changed'] = True
        result['message'] = 'Файл будет создан или изменен.'
        module.exit_json(**result)

    # Запись в файл
    try:
        with open(file_path, 'w') as f:
            f.write(file_content)
        result['changed'] = True
        result['message'] = 'Файл успешно создан/обновлен.'
    except Exception as e:
        module.fail_json(msg='Ошибка записи файла: %s' % str(e), **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
