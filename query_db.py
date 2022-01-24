import sqlite3


def select_animals_list():
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    cursor.execute("""select animal_list.id, animal.name, animal_list.breed, animal_list.date, animal_list.color, animal_list.height
                    from animal_list
                    join animal on animal.code = animal_list.type_code""")

    data = cursor.fetchall()

    conn.close()
    return data


def select_animals_list_from_id(id):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    select = """select animal_list.type_code, animal_list.color, animal_list.height, animal_list.breed 
                    from animal_list
                    where animal_list.id = ?"""
    cursor.execute(select, (id,))

    data = cursor.fetchall()

    conn.close()
    return data


def select_type_animals():
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    cursor.execute("""select * from animal""")

    data = cursor.fetchall()

    conn.close()
    return data


def select_type_from_code(code):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    select = """select animal.name, animal.animal_family 
                    from animal
                    where animal.code = ?"""
    cursor.execute(select, (code,))

    data = cursor.fetchall()

    conn.close()
    return data


if __name__ == "__main__":
    select_type_animals()
