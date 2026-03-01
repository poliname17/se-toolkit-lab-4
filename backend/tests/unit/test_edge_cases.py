"""Unit tests for edge cases and boundary values."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(
        id=id, learner_id=learner_id, item_id=item_id, kind="attempt"
    )


def test_filter_with_item_id_zero() -> None:
    interactions = [
        _make_log(1, 1, 0),
        _make_log(2, 2, 1),
        _make_log(3, 3, 0),
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 2
    assert all(i.item_id == 0 for i in result)