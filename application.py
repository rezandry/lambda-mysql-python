from app.Main import Main


def handler(event, context):
    data = Main.run(event, context)
    return data