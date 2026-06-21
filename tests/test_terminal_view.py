from unittest.mock import patch
from src.game.TerminalView import TerminalView


def test_clear_screen_calls_os_system():
    """Garante que o método de limpar a tela chama a função do sistema operacional correta."""
    with patch("os.system") as mock_system:
        TerminalView.clear_screen()
        # Verifica se o os.system foi chamado pelo menos uma vez
        mock_system.assert_called_once()
        # O argumento deve ser 'cls' no Windows ou 'clear' no Linux/Mac
        assert mock_system.call_args[0][0] in ['cls', 'clear']