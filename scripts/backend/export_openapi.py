"""FastAPI の OpenAPI スキーマを shared/api/openapi.json に出力するスクリプト。"""

import json
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root / "backend"))

from app.main import app  # noqa: E402

output_path = repo_root / "shared" / "api" / "openapi.json"
output_path.parent.mkdir(parents=True, exist_ok=True)

schema = app.openapi()
output_path.write_text(json.dumps(schema, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"\n💫 Generated: {output_path}")
