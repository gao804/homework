"""Start a fresh kernel for each notebook, execute all cells, and save outputs."""
from pathlib import Path
import os
import sys

import nbformat
from nbclient import NotebookClient


def main():
    prefix = Path(sys.prefix)
    if not (prefix / "conda-meta").is_dir() or prefix.name.lower() == "base":
        raise RuntimeError("Run this script in the homework conda environment.")
    if os.environ.get("CONDA_DEFAULT_ENV", "base") == "base":
        raise RuntimeError("Activate homework or use conda run -n homework.")
    root = Path(__file__).resolve().parents[1]
    notebooks = sorted(root.glob("*/*_*.ipynb"))
    if len(notebooks) != 4:
        raise RuntimeError(f"Expected 4 notebooks, found {len(notebooks)}")
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        NotebookClient(
            notebook,
            timeout=120,
            kernel_name="homework",
            resources={"metadata": {"path": str(path.parent)}},
            allow_errors=False,
        ).execute()
        cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
        assert [cell.execution_count for cell in cells] == list(range(1, len(cells) + 1))
        assert all(output.output_type != "error" for cell in cells for output in cell.outputs)
        nbformat.validate(notebook)
        nbformat.write(notebook, path)
        print(f"PASS {path.relative_to(root)}: {len(cells)} code cells, no uncaught errors")


if __name__ == "__main__":
    main()
