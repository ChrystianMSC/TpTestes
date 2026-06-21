import pytest
from unittest.mock import MagicMock, patch
import time
from src.game.GameController import GameController
from src.network.NetworkEngine import NetworkEngine

@pytest.fixture
def mock_network():
    """Cria um mock para o motor de rede P2P."""
    return MagicMock(spec=NetworkEngine)

@pytest.fixture
def game_controller(mock_network):
    """Instancia o GameController usando o mock de rede e um nome padrão."""
    # Desativamos o time.sleep para os testes rodarem instantaneamente
    with patch("time.sleep"):
        controller = GameController(mock_network, "Chrystian")
        return controller