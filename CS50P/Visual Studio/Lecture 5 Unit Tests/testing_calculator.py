from calculator import squre
def main():
    test_squre()
    
    
def test_squre():
    """Here if condition is not checked because 2+2=4"""
    if squre(2) != 4:
        print("2 squred was not 4")
        
    if squre(5) == 10:
        print("5 addition 5 is equal 10")
    if squre(6) != 36:
        print("6 squred was not 36")
    if squre(3) != 9:
        print("3 squred was not 9")
        
if __name__ == "__main__":
    main()
    