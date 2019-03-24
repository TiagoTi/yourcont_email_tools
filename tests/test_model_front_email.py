from models.front_emails import CardEmail, ListOfCards


def test_card():
    titulo = "titulo do card 1"
    descricao = "Meu primeiro card"
    url_image = "imagem.png"
    url_link = "card1"
    card = CardEmail(titulo, descricao, url_image, url_link)

    assert card.title == "Titulo Do Card 1"
    assert card.description == descricao
    assert card.image_filename == '/static/img/cards/imagem.png'
    assert card.method == "card1"


def test_cards():
    descricao = "Desc Card"
    url_image = "imagem.png"
    method_name = "card"

    c1 = CardEmail("titulo do card 1", descricao, url_image, method_name)
    c2 = CardEmail("titulo do card 2", descricao, url_image, method_name)
    c3 = CardEmail("titulo do card 3", descricao, url_image, method_name)

    lst_card = ListOfCards([c1, c2])
    assert len(lst_card) == 2

    lst_card + c3
    assert len(lst_card) == 3

    for card in lst_card:
        assert str(type(card)) == "<class 'models.front_emails.CardEmail'>"

#     # fim de testes
