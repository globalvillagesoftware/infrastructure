"""
File system data loader for JSON objects

This handler reads JSON data from any file system location.
This handler works on both Linux and Windows.

.. only:: development_administrator
    
    Created on Jul. 6, 2020
    
    @author: Jonathan Gossage

"""

import json
from pathlib import Path
from typing import MutableMapping, Any, Optional

def handler(path: Optional[str] = '/etc/gvConfig',
            file: Optional[str] = 'pre.json') -> MutableMapping[str, Any]:
    """
    """
    _data: MutableMapping[str, Any] = {}
    _path: Optional[Path] = Path(Path(path) / file) if path and file else None
    
    if _path and _path.is_file():
        with _path as p:
            with p.open(mode='rt') as f:
                _data = json.load(f)
    return _data
