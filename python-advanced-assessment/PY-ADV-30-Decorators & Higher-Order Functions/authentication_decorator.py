from functools import wraps

def authenticate(func):
    @wraps(func)
    def wrapper(username, is_logged_in):
        if is_logged_in:
            print(f"Authentication successful for {username}")
            return func(username, is_logged_in)
        else:
            print("Authentication failed. Please login first.")

    return wrapper

@authenticate
def view_profile(username, is_logged_in):
    print(f"Welcome to your profile, {username}!")

@authenticate
def view_dashboard(username, is_logged_in):
    print(f"Welcome to the dashboard, {username}!")

view_profile("Valli", True)

print()

view_dashboard("Valli", False)