'''
Declaration of views and routes.
'''
from flask import render_template, request
from app import app

config = {
    "bg_color": "#dcdcdc"
}

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    lipsum = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu accumsan quam. Integer vel mauris lacus. Vestibulum arcu augue, hendrerit ac enim at, rhoncus mattis lorem. Suspendisse sit amet ex a dui ornare efficitur. In faucibus justo eget magna pretium viverra. Etiam ac condimentum lectus. Proin rhoncus fringilla eros, ac auctor sapien.

Nullam id elit ipsum. Maecenas sollicitudin tincidunt leo id euismod. Nullam scelerisque vel dui ut sollicitudin. Praesent sit amet mi tortor. Morbi elementum ex ac odio dignissim eleifend. Vivamus at ipsum at neque tempor vehicula. Nullam nec ante et neque efficitur pharetra. In hac habitasse platea dictumst. Integer ut diam vitae dolor pellentesque fringilla id at augue. Nulla nec fermentum orci. Fusce quis scelerisque orci, quis suscipit lorem. Nullam vitae urna dui. Fusce pulvinar, felis vitae faucibus facilisis, felis augue viverra dui, ac sagittis nibh velit eget arcu. Sed tristique hendrerit scelerisque.

Etiam vitae magna risus. Cras placerat dictum mauris, ut dapibus nisi consequat dapibus. Morbi iaculis ligula arcu, et commodo purus tempus fringilla. Duis pulvinar nisl sit amet arcu finibus, ut dictum mauris congue. Mauris at ornare quam. Nullam nisi lacus, venenatis viverra velit at, dapibus iaculis risus. Pellentesque nec quam nec elit feugiat placerat. In et odio dignissim, sagittis dui a, interdum lectus. Nulla facilisi. Integer at consectetur erat. Sed luctus iaculis mauris. Fusce mollis interdum lectus, ac bibendum metus pellentesque vel. Suspendisse ipsum purus, aliquam vel est venenatis, volutpat pharetra dui. Donec maximus, arcu at lobortis laoreet, magna odio pharetra quam, at dapibus nibh mauris quis orci. Suspendisse felis tortor, accumsan sit amet mauris quis, mollis cursus augue.

Donec sodales metus eu metus pellentesque, sit amet congue urna vestibulum. Donec efficitur, mauris et pellentesque gravida, erat velit aliquam nunc, eget consequat erat enim eu dui. Integer condimentum metus in laoreet interdum. Morbi congue libero arcu, et feugiat erat iaculis sed. Suspendisse eu nulla urna. Etiam varius lacus vitae elit tincidunt, ut efficitur ante dignissim. Aliquam fringilla maximus tortor ac finibus. Donec et lorem ipsum. Donec pulvinar luctus posuere. Mauris eu egestas eros. Aenean viverra dignissim risus, fringilla porttitor ante.

Integer non erat a lectus bibendum varius. Curabitur semper quam ante, non pulvinar mauris semper id. Curabitur condimentum eros scelerisque velit posuere, finibus porttitor ante feugiat. Donec hendrerit iaculis lacinia. Quisque vitae tristique metus, id ornare massa. Praesent velit nunc, viverra pulvinar aliquet sit amet, sodales non elit. Duis lobortis euismod libero ac euismod. Donec at lacus mollis magna congue auctor vitae nec sem. Vivamus in bibendum diam. In hac habitasse platea dictumst. Mauris nec lacus ut felis rhoncus sagittis a non orci. Morbi ultrices volutpat blandit. '''
    test = [
        {"name": "Entry #1", "description": "ja;ldskjflakdj;flakjdf", "tags": ["tag1", "tag2"], "formats": ["csv", "xlsx", "REST API"], "last_updated": "Sep 19, 10:10"},
        {"name": "Entry #2", "description": lipsum, "tags": ["tag1", "tag2"], "formats": ["csv", "xlsx", "REST API"], "last_updated": "Sep 19, 10:10"},
        {"name": "Entry #3", "description": lipsum, "tags": ["tag2", "tag3"], "formats": ["csv", "xlsx", "REST API"], "last_updated": "Sep 19, 10:10"}
    ]
    return render_template('index.html', recent=test, config=config)