from typing import List

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("input_users, expected_users", [
    (
        [{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }],
        [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }]
    )
])
def test_restore_names(
        input_users: List[dict],
        expected_users: List[dict]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users
