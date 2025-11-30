import importlib.util
import sys
from pathlib import Path


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    repo_root = Path(__file__).resolve().parents[2]
    test_path = repo_root / 'tareas' / 'tests' / 'test_profinal_minimax.py'
    # Ensure repo root is on sys.path so 'tareas' can be imported as a namespace package
    sys.path.insert(0, str(repo_root))
    mod = load_module('test_minimax', str(test_path))

    # Run the pytest-style test function directly
    print('Running test_minimax_produces_valid_moves...')
    try:
        mod.test_minimax_produces_valid_moves()
    except AssertionError as e:
        print('TEST FAILED:', e)
        return 1
    print('TEST PASSED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
