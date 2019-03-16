class CardEmail:
    def __init__(self, title, desc, img, method_name):
        self.title = title.title()
        self.description = desc
        self.image_filename = f'/static/img/cards/{img}'
        self.method = method_name


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
    # emails + CardEmail(
    #     'Saudação',
    #     'Email de quando o cliente envia seu dados iniciais para o youcont! Enviado Pelo Wix',
    #     'teamwork.png',
    #     'greeting')

    # 2 Agradecimentos
    emails + CardEmail(
        '2º Agradecimento',
        'Adecer ao cliente por escolher a youcont',
        'winner.png',
        'welcome_to_your_cont'
    )

    # 3 Contract
    emails + CardEmail(
        '3º Contrato da prestação',
        'Envia cópia do contrato e solicita documentação',
        'dossier.png',
        'contact_for_contract_data'
    )
    #
    # # 4 Meteenging
    # emails + CardEmail(
    #     'Convite para Reunião',
    #     'Email padrão de solicitação dos dados do cliente',
    #     'dossier.png',
    #     'meeting_email'
    # )

    return emails
