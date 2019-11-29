from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=80, debug=True) #在这里直接开启debug
    app.debug = True


"""
1,首先，我们导入了 Flask 类。这个类的实例将会是我们的 WSGI 应用程序。
2,接下来，我们创建一个该类的实例，第一个参数是应用模块或者包的名称。 如果你使用单一的模块（如本例），你应该使用 __name__ ，
 因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 '__main__' 或实际的导入名）。这是必须的，这样Flask才知道到哪去找模板、静态文件等等。
 详情见 Flask的文档。
3,然后，我们使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。
4,这个函数的名字也在生成 URL 时被特定的函数采用，这个函数返回我们想要显示在用户浏览器中的信息。
最后我们用 run() 函数来让应用运行在本地服务器上。 其中 if __name__ =='__main__': 确保服务器只会在该脚本被 Python 
解释器直接执行的时候才会运行，而不是作为模块导入的时候。
欲关闭服务器，按 Ctrl+C。
"""