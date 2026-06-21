import pytest
import os
import json
from src.game.Player import Player

# Fixture para garantir que o arquivo de cartas exista de forma previsível antes dos testes
@pytest.fixture(autouse=True)
def setup_cards_json():
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", "cards.json")

    # Se o arquivo não existir por algum motivo no ambiente de CI, criamos um mock rápido
    if not os.path.exists(path):
        mock_cards = [
            {"id": i, "name": f"Carta {i}", "type": "DANO", "value": 2, "cost": 1, "return_mana": False}
            for i in range(1, 41)
        ]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(mock_cards, f)