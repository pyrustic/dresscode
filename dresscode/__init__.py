from dresscode.app import App
from dresscode.page import Page
from dresscode.page import error


class Component:
    def __init__(self, page, cid):
        self._page = page
        self._cid = cid
        self._parts = dict()

    @property
    def page(self):
        return self._page

    @property
    def cid(self):
        return self._cid

    @property
    def parts(self):
        return self._parts.copy()

    def build(self, **config):
        pass

    def read(self):
        pass

    def update(self, **config):
        pass
