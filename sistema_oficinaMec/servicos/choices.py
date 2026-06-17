from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCA_OLEO_MOTOR = 'TOM', 'Trocar óleo do motor'
    TROCA_PASTILHA_FREIO = 'TPF', 'Troca das pastilhas de freio'
    TROCA_FILTRO_AR = 'TFA', 'Troca de filtro de AR'
    BALANCEAMENTO = 'B', 'Balanceamento'
    TROCA_LIQUIDO_ARREFECIMENTO = 'TLA', 'Troca do líquido de arrefecimento'