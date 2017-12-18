from bottle import route, run, static_file

@route('/main/<filepath:path>', method="get")
def server_static(filepath):
    return static_file(filepath, root='/home/tema/dev/Web/spine-ui-prototype')

if __name__ == "__main__":
    run()
