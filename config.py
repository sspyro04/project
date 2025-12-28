import json, pathlib

CFG_PATH = pathlib.Path("config.json")

DEFAULTS = {
    "threshold": 1.0,
}

def get_cfg():
    return DEFAULTS | load_cfg()

def load_cfg():
    if CFG_PATH.exists():
        return json.loads(CFG_PATH.read_text(encoding="utf-8"))
    return {}

def save_cfg(d):
    CFG_PATH.write_text(json.dumps(d, indent=2), encoding="utf-8")

def export_cfg_bytes(d):
    return json.dumps(d, indent=2).encode()
