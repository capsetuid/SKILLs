"""The command surface, where destruction is witnessed and accounted for."""

from __future__ import annotations

import json

import pytest

from btm_setup_env.cli import main


@pytest.fixture
def provisioned(tmp_path):
    """A root a destroy will accept: a manifest plus one measurable file."""
    root = tmp_path / "denv"
    root.mkdir()
    (root / "manifest.json").write_text(
        json.dumps({"project": str(tmp_path), "spec": [], "host": "linux-64"}),
        encoding="utf-8",
    )
    (root / "payload").write_bytes(b"x" * 100)
    return root


def destroy(root, tmp_path, *flags):
    return main(["destroy", "--project", str(tmp_path), "--root", str(root), *flags])


class TestDestroy:
    def test_a_root_without_a_manifest_survives(self, tmp_path, capsys):
        root = tmp_path / "denv"
        root.mkdir()
        assert destroy(root, tmp_path) == 1
        assert "no manifest.json" in capsys.readouterr().err
        assert root.exists()

    def test_removal_reports_the_bytes_freed(self, provisioned, tmp_path, capsys):
        assert destroy(provisioned, tmp_path) == 0
        out = capsys.readouterr().out
        assert str(provisioned) in out and "bytes freed" in out
        assert not provisioned.exists()

    def test_json_reports_the_root_and_the_bytes(self, provisioned, tmp_path, capsys):
        assert destroy(provisioned, tmp_path, "--json") == 0
        document = json.loads(capsys.readouterr().out)
        assert document["removed"] == str(provisioned)
        assert document["bytes_freed"] >= 100
