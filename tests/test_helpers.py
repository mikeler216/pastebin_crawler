import pytest

from pastebin_crawler.repository import RepositoryBase


def test_validate_not_flush_and_commit():
    with pytest.raises(ValueError):
        RepositoryBase._validate_not_flush_and_commit(commit=True, flush=True)
        RepositoryBase._validate_not_flush_and_commit(
            commit=False, flush=False
        )

    assert (
        RepositoryBase._validate_not_flush_and_commit(commit=True, flush=False)
        is None
    )
    assert (
        RepositoryBase._validate_not_flush_and_commit(commit=False, flush=True)
        is None
    )
