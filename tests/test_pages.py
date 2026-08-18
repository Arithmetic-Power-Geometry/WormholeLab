import importlib
import sys
import types


def test_all_page_modules_import_and_expose_render(monkeypatch):
    if "streamlit" not in sys.modules:
        monkeypatch.setitem(sys.modules, "streamlit", types.ModuleType("streamlit"))
    modules=["home","spacetime","ssp","light_ray","shadow_ring","orbit","ringdown","wif","osct","residual","mmwt","falsification","repro","blind"]
    for name in modules:
        m=importlib.import_module(f"pages.{name}")
        assert callable(getattr(m,"render",None))
