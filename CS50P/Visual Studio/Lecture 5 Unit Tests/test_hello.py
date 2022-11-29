from hello import hello

def test_default():
    assert hello("Jabed") == "hello, Jabed"
    
    
def test_argument():
    for name in ["Jabed", "Renu", "Kona", "Tanha", "Ayaan"]:
        assert hello() == "hello, world"