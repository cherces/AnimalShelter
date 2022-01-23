import sqlite3, db


def select_animals_list():
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    cursor.execute("""select animal_list.id, animal.name, animal_list.breed, animal_list.date, animal_list.color, animal_list.height
                    from animal_list
                    join animal on animal.code = animal_list.type_code""")

    data = cursor.fetchall()

    return data


if __name__ == "__main__":
    select_animals_list()