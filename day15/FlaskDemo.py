# 引入Flask模块
from html import escape
from pickle import PUT

from flask import Flask, render_template
from flask import request
from flask import make_response

app = Flask(__name__) # 创建一个应用
# Flask通过修饰器(和Java的注解类似)来建立路由映射关系的，已经看到修饰器是app.rotue()
@app.route('/')
# 定义根目录处理器
def index():
    return '<h1>Hello World!</h1>'

@app.route('/hello')
def hello():
    return 'Hello!'



# 动态路由
"""
如访问 /user/bob 或者 /user/lily 都会映射到同一视图函数上
"""
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s! </h1>' % name


# 动态域名中动态的部分可以作为视图函数的参数，也支持多个动态参数，如访问 /user/bob/23
@app.route('/user/<name>/<age>')
def user(name, age):
    return "<h1> Hello, %s, you're %s years old" % (name, age)

# 还可以指定动态部分的数据类型，如
"""
支持的数据类型

类型	说明
string	(默认值) 任何不包含斜杠的文本
int	正整数
float	正浮点数
path	类似 string ，但可以包含斜杠
uuid	接受 UUID 字符串
"""
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


# 指定HTTP 方法
"""
HTTP 协议，支持多种 HTTP 方法，例如 HEAD、OPTIONS，以及常用的 GET、POST 等，
Flask自动处理了 HEAD 和 OPTIONS，路由默认接受的方法是 GET，如果要匹配其他请求方法，
可以在路由方法的 methods 参数来指定
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    print('GET')

def show_the_login_form():
    print('POST')



# 复合路由
"""
也可以将多个路由规则，用于一个视图函数, 如访问 /job/ 和访问 /work/ 效果是一样的

"""
# 访问 /job/ 和访问 /work/ 效果是一样的
@app.route('/job/')
@app.route('/work/')
def show_works():
    return 'This is works page'

#  /user/ 或者 /user/page/<pageindex> 时，都会有 show_users 视图函数来处理,
#  而且还为 /user/ 提供了默认值，即访问 /user/ 相当于访问 /user/page/1
@app.route('/users/', defaults={'page': 1})
@app.route('/users/page/<int:page>')
def show_users(page):
    pass



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) #在这里直接开启debug # 启动服务



# 路由
"""
路由是 Web 开发中一个很重要的概念，用来将不同的请求，映射到响应的处理方法上，
这个方法被称为视图函数。比如刚才的 Hello 应用，将根请求，映射到index处理方法上，
下面简单了解下Flask对路由的支持

Flask通过修饰器(和Java的注解类似)来建立路由映射关系的，已经看到修饰器是 app.rotue()
"""


# 请求和响应
"""
Web 应用，最重要的事情就是处理接收到的请求，并返回响应。Flask 框架也一样，它提供了请求对象 
request 和响应对象 response ，可以方便的在视图函数中使用。
"""

# 请求
"""
Flask 将客户端发送的 HTTP 请求封装成了 request 请求对象，并且使用上下文 (context) 
临时将 request 变为全局可访问的，于是在视图还是中，就可以直接使用了。

注意: request 并非真正的全局变量！试想，在多线程服务器中，多个线程同时处理不同客户端发送的
不同请求时，每个线程看到的 request 对象必然不同。Falsk 使用上下文让特定的变量在一个线程中
全局可访问，与此同时却不会干扰其他线程。
Flask 有两种上下文，分别为程序上下文和请求上下文，各自对应的全局变量如下表:
变量名	上下文类型	备注
current_app	程序上下文	表示当前运行的程序实例
g	        程序上下文	处理请求时用作临时存储对象，每次请求都会重新设值
request	    请求上下文	客户端发来的request请求对象
session	    请求上下文	请求携带的会话信息
"""

"""
request 对象提供了丰富的属性和方法，这里举个例子：
1,post: 通过使用 method 属性可以操作当前请求方法，通过使用 form 属性处理表单数据（在 POST 或者
        PUT 请求 中传输的数据）。
2,get: 如果要操作 URL （如 ?key=value ）中提交的参数可以使用 args 属性，如 :
        searchword = request.args.get('key', '')
"""


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def log_the_user_in(param):
    pass


def valid_login(param, param1):
    pass



# 请求钩子
"""
有时在处理请求之前或之后执行代码会很有用。例如，在请求开始时，可能需要创建数据库连接或者认证发起请求的用户。为了避免在每个视图函数中都使用重复的代码，Flask 提供了注册通用函数的功能，注册的函数可在请求被分发到视图函数之前或之后调用。 请求钩子使用修饰器实现。Flask 支持以下4种钩子:

before_first_request：注册一个函数，在处理第一个请求之前运行。
before_request：注册一个函数，在每次请求之前运行。
after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
teardown_request：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
"""
@app.before_first_request
def first_quest():
    print("run before first request")

# 响应
"""
响应是 Web 服务器对请求的一个回应，在 Flask 中，有多种形式的响应。视图函数的返回值会自动转换为一个响应对象。
如果返回值是一个字符串，那么会被 转换为一个包含作为响应体的字符串、一个 200 OK 出错代码 和一个 text/html 
类型的响应对象。 如果返回值是一个字典，那么会调用 jsonify() 来产生一个响应。 以下是转换的规则：

如果视图返回的是一个响应对象，那么就直接返回它。
如果返回的是一个字符串，那么根据这个字符串和缺省参数生成一个用于返回的 响应对象。
如果返回的是一个字典，那么调用 jsonify 创建一个响应对象。
如果返回的是一个元组，那么元组中的项目可以提供额外的信息。元组中必须至少 包含一个项目，且项目应当由 (response, status) 、 (response, headers) 或者 (response, status, headers) 组成。 status 的值会重载状态代码， headers 是一个由额外头部值组成的列表 或字典。
如果以上都不是，那么 Flask 会假定返回值是一个有效的 WSGI 应用并把它转换为 一个响应对象。
"""

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
"""
@app.errorhandler 修饰符，会将一个响应代码映射到一个视图函数上，这里是将404(找不到页面)码，
处理成一个个性的错误页面
另外，render_template 是 Flask 的模板函数，简单理解就是格式化一个动态的 html 字符串，
关于模板的详细用法，会在模板章节描述
"""


# 使用 make_response() 包裹返回表达式，获得响应对象，并对该对象 进行修改，然后再返回:
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp