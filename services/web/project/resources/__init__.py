"""
Module for the function of checking the existence of a row in the database"
"""


def already_exist(entity, list_json: list) -> bool:
    """
    Checking for the existence row of such a entity
    :param entity: entity
    :param list_json: Entity data entered by the user
    :return: Status found or not
    """
    for obj in entity.query.all():
        row = entity.query.filter(obj.to_dict() == list_json).first()
        if row:
            return True
    return False
