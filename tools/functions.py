import base64


def bytes_a_base64(datos_bytes) -> str:
    return base64.b64encode(datos_bytes).decode('utf-8')


def base64_a_bytes(datos_base64: bytes) -> bytes:
    return base64.b64decode(datos_base64)