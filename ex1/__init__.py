def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here

    elements = []
    for category_id in mapping['categoryIdsSorted']:
        id = 'category-' + category_id
        text = mapping['categories'][category_id]['name']
        items = [
                    {
                        'id': mapping['roles'][role_id]['id'],
                        'text': mapping['roles'][role_id]['name'],
                    }
                    for role_id in mapping['categories'][category_id]['roleIds']
                ]
        elements.append({'id': id, 'text': text, 'items': items})

    return {'categories': elements}
