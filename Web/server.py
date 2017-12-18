from bottle import route, run, static_file

@route('/main/index.html')
def server_static(file_name):
    return static_file(file_name, root='./spine-ui-prototype/src')

if __name__ == "__main__":
    run()
