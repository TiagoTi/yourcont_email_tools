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
        'Agradecer ao cliente por escolher a youcont',
        'winner.png',
        'welcome_to_your_cont'
    )

    # 3 Contract
    emails + CardEmail(
        '3º Contrato da contabilidade',
        'Enviar cópia do contrato e solicitar a documentação pessoal',
        'dossier.png',
        'contact_for_contract_data'
    )

    # 4 Meteenging
    emails + CardEmail(
        '4º Escolha opções para Convite de Reunião',
        'Horários da reunião',
        'question.png',
        'meeting_solicitation_email'
    )

    # 5 Envio do Linnk
    emails + CardEmail(
        '5º Envio de link do apper na data x e horario y',
        'Enviar somente link do apper mencionando a dada e horário escolhido',
        'video-conference.png',
        'call_email'
    )

    # 6 Rotina de documentos
    emails + CardEmail(
        '6º Documentação da empresa e destrato do antigo contador',
        'Documentação da empresa e destrato do antigo contador',
        'dossier.png',
        'routine_docs'
    )

    # 7 Rotina de documentos
    emails + CardEmail(
        '7º Rotina de trabalho',
        'Rotina de trabalho',
        'dossier.png',
        'routine_infos'
    )

    return emails
