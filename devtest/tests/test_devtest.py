"""
Unit and regression test for the devtest package.
"""

# Import package, test suite, and other packages as needed
import devtest
import pytest
import sys


def test_devtest_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "devtest" in sys.modules


def test_mdanalysis_logo_length(mdanalysis_logo_text):
    """Example test using a fixture defined in conftest.py"""
    logo_lines = mdanalysis_logo_text.split("\n")
    assert len(logo_lines) == 46, "Logo file does not have 46 lines!"


def test_mdanalysis_version():
    """Test that a develop version of MDAnalysis is installed"""
    import MDAnalysis as mda
    # test it end with dev0
    assert mda.__version__.endswith("dev0"), "MDAnalysis version is not a development version"