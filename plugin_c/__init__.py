from .routers import router

class PluginC:
    @staticmethod
    def register(app):
        app.include_router(router)
