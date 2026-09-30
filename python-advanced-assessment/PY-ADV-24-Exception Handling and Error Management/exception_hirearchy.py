try:
    number = int("abc")
except ValueError:
    print("ValueError occurred")
except Exception:
    print("Some other error occurred")