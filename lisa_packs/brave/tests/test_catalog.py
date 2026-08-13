from __future__ import annotations

import json

from sdk.content._catalog import build_tool_catalog_json, resolve_tool_roots

from lisa_packs.brave import get_content_root


def test_brave_pack_brave_search_tool_discovered() -> None:
    roots = resolve_tool_roots([get_content_root()])
    assert roots, "No tools/ directory found in brave provider pack"

    catalog = json.loads(build_tool_catalog_json(roots))

    assert "brave_search" in catalog
    tool = catalog["brave_search"]
    assert tool["tool_id"] == "brave_search"
    assert tool["module_path"].startswith("lisa_packs.brave.tools.")
