#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_shot_director info
PYTHONPATH=src python -m gbt_shot_director check --payload '{}'
PYTHONPATH=src python -m gbt_shot_director run   --payload '{}'
