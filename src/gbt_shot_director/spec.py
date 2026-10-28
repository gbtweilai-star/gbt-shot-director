"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "shot_director",
 "domain": "creation",
 "desc": "**镜头导演**（主人令 2026-10-16：把 **Seedance 2.0 Skill OS** 蒸进来）：蒸自 **Emily2040/seedance-2.0**（**MIT** · v6.7.0）的思想—— 视频模型 = **一个从没见过你的剧组**（不能提问 · 按字面渲染 · 只做第一个动作 · 跳剪忘光位站位 · 不告诉它就不移镜）。**十大坑 → 十修法**：字面但不死板（**感觉的一个普通词 + 一个物理锚**）· **一镜一动作** · 道具写手 · **每镜锁定句**（光/人/站位）· 位置与地理每镜重述 · **镜头表先于散文** · 提交前合规预筛（分类器拒的是词不是意图）。不代付生成费。op=plan/shot_table/rules/punctuation/moderation/evidence/check/route（**全只读·零作用域·不出网**）。",
 "handler": "shot_director",
 "safe": false,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "plan",
  "shot_table",
  "rules",
  "punctuation",
  "moderation",
  "evidence",
  "check",
  "route"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
