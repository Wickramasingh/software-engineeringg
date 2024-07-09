import requests
import bs4

def test_telephone_inventor():
    response = requests.get("https://en.wikipedia.org/wiki/Telephone")
    assert response.status_code == 200
    assert "Alexander Graham Bell" in response.text


def test_inventor(invention, inventor):
    response = requests.get(f"https://en.wikipedia.org/wiki/{invention}")
    assert response.status_code == 200
    assert inventor in response.text
    print(f"Found {inventor} for {invention}.")


def test_telephone_inventor_page():
    from bs4 import BeautifulSoup
    response = requests.get("https://en.wikipedia.org/wiki/Telephone")
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    print(soup.title)
    # for img in soup.find_all('img'):
    #     print(img.get('src'))


if __name__ == "__main__":
    test_telephone_inventor()
    test_inventor("Telephone","Alexander Graham Bell")
    test_inventor("Transistor","Shockley")
    test_telephone_inventor_page()
    print("done.")
