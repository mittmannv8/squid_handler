from application import create_app

app = create_app('settings.DevelopmentConfig')
app.run()
