"""
Solution for Data Storage Using Lists
Problem ID: F083
"""

def create_user_list():
    """
    Creates an empty list to store users.
    Returns empty list.
    """
    # TODO: Implement your solution here
    pass

def add_user(users_list, name, email, age):
    """
    Adds a user to the users list with auto-generated ID.
    Returns updated list with new user.
    """
    # TODO: Implement your solution here
    pass

def get_users_by_age(users_list, min_age):
    """
    Filters users by minimum age.
    Returns list of users with age >= min_age.
    """
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    users = create_user_list()
    print(f"Lista inicial: {users}")
    
    users = add_user(users, "Ana García", "ana@email.com", 28)
    users = add_user(users, "Bob Smith", "bob@email.com", 22)
    print(f"Después de añadir usuarios: {users}")
    
    filtered = get_users_by_age(users, 25)
    print(f"Usuarios con edad >= 25: {filtered}")
    
if __name__ == "__main__":
    result = main()
    print(f"Resultado final: {result}")
