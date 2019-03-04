class CardEmail:
    def __init__(self, title, desc, img, path):
        self.title = title.title()
        self.description = desc
        self.image_filename = f'/static/img/cards/{img}'
        self.path_link = f'/{path}'


class ListOfCards:
    def __init__(self, cards):
        self._cards = cards

    def __getitem__(self, item):
        return self._cards[item]

    def __len__(self):
        return len(self._cards)

    def __add__(self, card):
        self._cards.append(card)


def cards_email():
    emails = ListOfCards([])

    # 1 Welcome
    emails + CardEmail(
        'welcome to your cont',
        'Email de quando o cliente entra para youcont',
        'winner.png',
        'welcome_to_your_cont_wiki'
    )

    # 2 Agradecimentos
    emails + CardEmail(
        'adecimento ao cliente',
        'Adecer ao cliente por escolher a youcont',
        'teamwork.png',
        'welcome_to_your_cont'
    )

    # 3 Contrato
    emails + CardEmail(
        'Solicitação de Dados',
        'Email padrão de solicitação dos dados do cliente',
        'winner.png',
        'contact_for_contract_data'
    )

    return emails
