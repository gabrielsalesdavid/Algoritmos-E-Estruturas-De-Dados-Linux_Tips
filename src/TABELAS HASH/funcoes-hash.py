# ====================================== FUNÇÕES HASH ======================================

import hashlib
import json

payload_pix = {
    "transacao_id": "TX-998877",
    "valor": 1500.00,
    "pagador": "Carlos Silva",
    "recebedor": "LINUXTips"
}

payload_str = json.dumps(payload_pix, sort_keys = True)
hash_sha256 = hashlib.sha256(payload_str.encode()).hexdigest()

print("--- ASSINATURA SHA-256 DO PAYLOAD ---")
print("Payload: ", payload_str)
print("Hash: ", hash_sha256)