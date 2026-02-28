"""OpenAPI JSON を Swagger UI の standalone HTML に変換してブラウザで開くスクリプト。"""

import json
import sys
import webbrowser
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
OPENAPI_PATH = REPO_ROOT / "shared" / "api" / "openapi.json"
OUTPUT_PATH = REPO_ROOT / "shared" / "api" / "openapi-viewer.html"

if not OPENAPI_PATH.exists():
    print(f"Error: {OPENAPI_PATH} not found. Run gen-openapi first.")
    sys.exit(1)

spec = json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))
spec_json = json.dumps(spec, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>{spec.get("info", {}).get("title", "API Docs")}</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({{ spec: {spec_json}, dom_id: "#swagger-ui" }})
  </script>
</body>
</html>"""

OUTPUT_PATH.write_text(html, encoding="utf-8")
print(f"\n💫 Generated: {OUTPUT_PATH}")

webbrowser.open(OUTPUT_PATH.as_uri())
print("🌐 Opened in browser")
