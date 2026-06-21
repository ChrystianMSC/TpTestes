import pytest
import json
from src.network.NetworkProtocol import NetworkProtocol

def test_serialize_converts_dict_to_bytes_with_newline():
    """Garante que a serialização transforma dicionários em bytes válidos terminados em \\n."""
    payload = {"action": "END_TURN"}
    result = NetworkProtocol.serialize(payload)

    assert isinstance(result, bytes)
    assert result.endswith(b"\n")

    # Decodifica de volta para verificar a integridade do JSON
    decoded = json.loads(result.decode('utf-8').strip())
    assert decoded["action"] == "END_TURN"