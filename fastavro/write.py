try:
    from . import _write
except ImportError:
    from . import _write_py as _write
from . import json_write

# Private API

# Public API
writer = _write.writer
Writer = _write.Writer
json_writer = json_write.json_writer
schemaless_writer = _write.schemaless_writer
LOGICAL_WRITERS = _write.LOGICAL_WRITERS

__all__ = [
    'writer', 'Writer', 'schemaless_writer', 'LOGICAL_WRITERS',
]
