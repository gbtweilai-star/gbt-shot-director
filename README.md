# shot_director

**One capability bit from GBT V8, packaged standalone.** No. 55 of 341,
`creation` domain (Creation).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> **镜头导演**（主人令 2026-10-16：把 **Seedance 2.0 Skill OS** 蒸进来）：蒸自 **Emily2040/seedance-2.0**（**MIT** · v6.7.0）的思想—— 视频模型 = **一个从没见过你的剧组**（不能提问 · 按字面渲染 · 只做第一个动作 · 跳剪忘光位站位 · 不告诉它就不移镜）。**十大坑 → 十修法**：字面但不死板（**感觉的一个普通词 + 一个物理锚**）· **一镜一动作** · 道具写手 · **每镜锁定句**（光/人/站位）· 位置与地理每镜重述 · **镜头表先于散文** · 提交前合规预筛（分类器拒的是词不是意图）。不代付生成费。op=plan/shot_table/rules/punctuation/moderation/evidence/check/route（**全只读·零作用域·不出网**）。

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-shot-director.git
cd gbt-shot-director
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_shot_director info                  # capability card
python -m gbt_shot_director spec --json           # machine-readable contract
python -m gbt_shot_director check --payload '{}'
python -m gbt_shot_director run   --payload '{}'
```

Real `info` output from this machine:

```text
shot_director  (creation)  v1.0.0
----------------------------------------
**镜头导演**（主人令 2026-10-16：把 **Seedance 2.0 Skill OS** 蒸进来）：蒸自 **Emily2040/seedance-2.0**（**MIT** · v6.7.0）的思想—— 视频模型 = **一个从没见过你的剧组**（不能提问 · 按字面渲染 · 只做第一个动作 · 跳剪忘光位站位 · 不告诉它就不移镜）。**十大坑 → 十修法**：字面但不死板（**感觉的一个普通词 + 一个物理锚**）· **一镜一动作** · 道具写手 · **每镜锁定句**（光/人/站位）· 位置与地理每镜重述 · **镜头表先于散文** · 提交前合规预筛（分类器拒的是词不是意图）。不代付生成费。op=plan/shot_table/rules/punctuation/moderation/evidence/check/route（**全只读·零作用域·不出网**）。

gated      : True   <- needs explicit consent
external   : False
multi-op   : True
params     : (none)
values     : plan, shot_table, rules, punctuation, moderation, evidence, check, route
```

Wire a real implementation:

```python
from gbt_shot_director import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（8 个）**：`plan`、`shot_table`、`rules`、`punctuation`、`moderation`、`evidence`、`check`、`route`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Gated: this bit is marked `safe: false` in the registry — it can change state that no inverse action restores.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.11s
```

## Provenance

| field | value |
|---|---|
| capability | `shot_director` |
| domain | `creation` |
| handler | `shot_director` |
| safe | `False` (gated = `True`) |
| external | `False` |
| atlas page | [creation/shot_director](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/creation/shot_director.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
