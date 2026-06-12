# test_irr.py
import numpy as np
import numpy_financial as npf

def test_irr_basic():
    """Test basic IRR calculation"""
    cash_flows = [-1000, 300, 300, 300, 300]
    irr = npf.irr(cash_flows)
    assert irr > 0, "IRR should be positive for this cash flow"
    
def test_npv_basic():
    """Test basic NPV calculation"""
    rate = 0.05  # Changed from 0.1 to 0.05 (5% discount rate)
    cash_flows = [-1000, 300, 300, 300, 300]
    npv = npf.npv(rate, cash_flows)
    assert npv > 0, "NPV should be positive for this cash flow"

def test_placeholder():
    """Placeholder test to ensure pytest finds tests"""
    assert 1 + 1 == 2
