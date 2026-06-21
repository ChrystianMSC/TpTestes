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


def test_parse_stream_extracts_valid_payload():
    """Garante que uma stream de texto terminada com \\n extrai o objeto JSON corretamente."""
    buffer = '{"action":"SYNC_STATE","hp":10}\n'
    payloads, remaining_buffer = NetworkProtocol.parse_stream(buffer)

    assert len(payloads) == 1
    assert payloads[0]["action"] == "SYNC_STATE"
    assert payloads[0]["hp"] == 10
    assert remaining_buffer == ""


def test_parse_stream_leaves_incomplete_data_in_buffer():
    """Garante que dados parciais sem \\n continuam armazenados no buffer para a próxima leitura."""
    buffer = '{"action":"END_TURN"}\n{"action":"INCOMPLETE_PAYLOAD'
    payloads, remaining_buffer = NetworkProtocol.parse_stream(buffer)

    assert len(payloads) == 1
    assert payloads[0]["action"] == "END_TURN"
    assert remaining_buffer == '{"action":"INCOMPLETE_PAYLOAD'


def test_parse_stream_ignores_empty_lines():
    """Garante que quebras de linha puras e vazias no buffer são ignoradas sem quebrar o parser."""
    buffer = "\n\n"
    payloads, remaining_buffer = NetworkProtocol.parse_stream(buffer)

    assert len(payloads) == 0
    assert remaining_buffer == ""


def test_parse_stream_handles_multiple_payloads_at_once():
    """Garante que múltiplas mensagens acumuladas no buffer TCP são processadas juntas na mesma leitura."""
    buffer = '{"msg":1}\n{"msg":2}\n'
    payloads, remaining_buffer = NetworkProtocol.parse_stream(buffer)

    assert len(payloads) == 2
    assert payloads[0]["msg"] == 1
    assert payloads[1]["msg"] == 2
    assert remaining_buffer == ""


def test_parse_stream_handles_json_decode_error_gracefully():
    """Garante que strings corrompidas que não formam um JSON válido são ignoradas sem travar a thread de rede."""
    buffer = "TEXTO_INVALIDO_CORROMPIDO\n"
    payloads, remaining_buffer = NetworkProtocol.parse_stream(buffer)

    assert len(payloads) == 0
    assert remaining_buffer == ""