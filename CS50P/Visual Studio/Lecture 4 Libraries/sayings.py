"""Custom Library"""
def main():
    hello("WorLD")
    goodbye("World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"GoodBye, {name}")
    
if __name__ == "__main__":
    main()